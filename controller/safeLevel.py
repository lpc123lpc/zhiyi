from flask import jsonify
from database.static import dao, travelAdvice
import json
import datetime
import joblib
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def getInfo(region):
    with open("area.json", 'r', encoding='gbk') as f:
        allInfo = json.load(f)
    return allInfo[region]


def getRegion(region):
    places = region.split("  ")
    return places[len(places) - 1]


def modify(a):
    if a >= 0:
        return a
    else:
        return 0


def safeLevel(oriRegion, time):
    print(oriRegion)
    # str1 = ""
    region = getRegion(oriRegion)
    print(region)
    addList = travelAdvice.getIfAddInf(region)
    mid = []
    high = []
    if addList is None:
        str1 = "    抱歉，该地区的收据暂未收录。"
    elif len(addList) == 0:
        policyIndex = travelAdvice.getPolicyIndex(region)
        if policyIndex is None:
            str1 = "    该地区十四天内无新增病例，目前疫情态势稳定，出行前请了解目的地的相关政策，并做好防护。"
        else:
            str1 = "    该地区的政策严格性指数为：" + str(policyIndex) + "，且十四天内无新增病例。目前疫情态势稳定，出行前请了解目的地的相关政策，并做好防护。"
    else:
        policyIndex = travelAdvice.getPolicyIndex(region)
        if policyIndex is None:
            str1 = "    该地区十四天内有新增病例，新增病例数为："
        else:
            str1 = "    该地区的政策严格性指数为:" + str(policyIndex) + "，且十四天内有新增病例，新增病例数为："
        for i in addList:
            str1 = str1 + str(i) + "例 "
        str1 = str1 + "。"
        info = getInfo(region)
        path = "saved_model/" + str(info['num']) + ".pkl"
        num = datetime.datetime.strptime(time, '%Y-%m-%d') - datetime.datetime.strptime(info['begindate'], '%Y-%m-%d')
        predictnum = np.array([[num.days - 1, num.days]])
        # model = KNeighborsRegressor(weights='distance')
        model = joblib.load(path)
        ans = model.predict(predictnum)
        infMsg = dao.getNowInfMessage(region)
        rate = (abs((ans - modify(getattr(infMsg, "totalNum")))) + modify(getattr(infMsg, "addNum"))) / info['population']
        if rate >= 0.0001:
            str1 = str1 + "该地区目前的风险等级为高，"
        else:
            str1 = str1 + "该地区目前的风险等级为中，"
        str1 = str1 + "目前有一定风险，建议您如非必要不要前往。出行前请了解目的地的相关政策，并做好防护。"
        places = oriRegion.split("  ")
        # risks = []
        if len(places) == 1:
            risks = travelAdvice.getRiskArea()
        elif len(places) == 2:
            risks = travelAdvice.getRiskArea(places[1])
        else:
            risks = travelAdvice.getRiskArea(places[1], places[2])
        if len(risks) != 0:
            for i in risks:
                if getattr(i, "level") == 1:
                    mid.append(getattr(i, "childArea") + getattr(i, "abstract"))
                else:
                    high.append(getattr(i, "childArea") + getattr(i, "abstract"))
    return jsonify({
        "str1": str1,
        "mid": mid,
        "high": high
    })
