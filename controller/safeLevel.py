from flask import jsonify
from database.static import dao, travelAdvice
import json
import datetime
import joblib
from sklearn.neighbors import KNeighborsRegressor


def getInfo(region):
    with open("../controller/area.json", 'r', encoding='gbk') as f:
        allInfo = json.load(f)
    return allInfo[region]


def getRegion(region):
    places = region.splite(str="  ")
    return places[len(places) - 1]


def modify(a):
    if a >= 0:
        return a
    else:
        return 0


def safeLevel(oriRegion, time):
    str1, str2, str3, str4 = "", "", "", ""
    region = getRegion(oriRegion)
    addList = travelAdvice.getIfAddInf(region)
    mid = []
    high = []
    if addList is None:
        str1 = "抱歉，该地区的收据暂未收录。"
    elif len(addList) == 0:
        str1 = "该地区十四天内无新增病例。"
        str2 = "该地区目前疫情态势稳定，出行前请了解目的地的相关政策，并做好防护。"
    else:
        str1 = "该地区十四天内有新增病例。"
        str2 = "该地区近十四天的新增病例数为："
        for i in addList:
            str2 = str2 + str(i) + "例 "
        info = getInfo(region)
        path = "../saved_model/" + str(info['num']) + ".pkl"
        num = datetime.datetime.strptime(time, '%Y-%m-%d') - datetime.datetime.strptime(info['begindate'], '%Y-%m-%d')
        predictnum = [[num.days]]
        model = KNeighborsRegressor(weights='distance')
        joblib.load(path, model)
        ans = model.predict(predictnum)
        infMsg = dao.getNowInfMessage(region)
        rate = (ans + modify(getattr(infMsg, "addNum"))) / info['population']
        if rate >= 0.001:
            str3 = "该地区目前的风险等级为高"
        else:
            str3 = "该地区目前的风险等级为中"
        str4 = "该地区目前有一定风险，建议您如非必要不要前往。出行前请了解目的地的相关政策，并做好防护。"
        places = oriRegion.splite(str="  ")
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
                    mid.append({"area": getattr(i, "childArea"), "abstract": getattr(i, "abstract")})
                else:
                    high.append({"area": getattr(i, "childArea"), "abstract": getattr(i, "abstract")})
    return jsonify({
        "str1": str1,
        "str2": str2,
        "str3": str3,
        "str4": str4,
        "mid": mid,
        "high": high
    })


if __name__ == '__main__':
    getInfo("1")
    num = datetime.datetime.today() - datetime.datetime.strptime("2021-06-01", '%Y-%m-%d')
    a = num.days
    print(num)
