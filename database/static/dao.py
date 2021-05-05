from database.static.table import *
from spider.spider import *


'''
description:get infection information
name:"global"(世界)/国家姓名/地区姓名
return:返回该区域的实时感染信息
'''
def getNowInfMessage(name):
    message = db.session.query(NowInfMessage).filter_by(NowInfMessage.areaName == name).first()
    return message


'''
description:get infection information
param:name:"global"(世界)/国家姓名
return:返回该区域所包含的国家/地区的实时感染信息（下一级）
'''
def getNowInfMessageInclude(name):
    messages = db.session.query(NowInfMessage)\
        .filter_by(Area.parentArea == name)\
        .filter_by(Area.childArea == NowInfMessage.areaName).all()
    return messages


'''
description:get infection information
param:name:"global"(世界)/国家姓名
return:返回该区域的历史感染信息
'''
def getHisInfMessage(name):
    isChina = db.session.query(ChinaInfMessage.time).filter_by(ChinaInfMessage.areaName == name).first()
    messages = None
    if isChina is None:
        messages = db.session.query(InfMessage) \
            .filter_by(InfMessage.areaName == name) \
            .order_by(InfMessage.time.desc()).limit(180).all()
        if messages is not None:
            messages.reverse()
    else:
        messages = db.session.query(InfMessage) \
            .filter_by(InfMessage.areaName == name) \
            .order_by(InfMessage.time.desc()).limit(180).all()
        if messages is not None:
            messages.reverse()
    return messages


'''
description:get infection information
param:name:"global"(世界)/国家姓名
return:返回该区域所包含的国家/地区的历史感染信息（下一级）
'''
def getHisInfMessageInclude(name):
    areas = db.session.query(Area.childArea).filter_by(Area.parentArea == name).all()
    messages = []
    if areas is None:
        return None
    else:
        isChina = db.session.query(ChinaInfMessage.time).filter_by(ChinaInfMessage.areaName == areas[0]).first()
        if isChina is None:
            for area in areas:
                message = db.session.query(InfMessage)\
                    .filter_by(InfMessage.areaName == area)\
                    .order_by(InfMessage.time.desc()).limit(180).all()
                if message is not None:
                    message.reverse()
                    messages.append(message)
        else:
            for area in areas:
                message = db.session.query(ChinaInfMessage)\
                    .filter_by(ChinaInfMessage.areaName == area)\
                    .order_by(ChinaInfMessage.time.desc()).limit(180).all()
                if message is not None:
                    message.reverse()
                    messages.append(message)
        return messages


'''
description:get infection information
name:"global"(世界)/国家姓名/地区姓名
return:返回该区域的实时接种信息
'''
def getNowVacMessage(name):
    message = db.session.query(NowVacMessage).filter_by(NowVacMessage.areaName == name).first()
    return message


'''
description:get infection information
name:"world"(世界)/国家姓名
return:返回该区域所包含的国家/地区的实时接种信息（下一级）
'''
def getNowVacMessageInclude(name):
    message = db.session.query(NowVacMessage)\
        .filter_by(Area.parentArea == name)\
        .filter_by(Area.childArea == NowVacMessage.areaName).all()
    return message


'''
description:get infection information
name:"global"(世界)/国家姓名/地区姓名
return:返回该区域的历史接种信息
'''
def getHisVacMessage(name):
    message = db.session.query(VacMessage)\
        .filter_by(VacMessage.areaName == name)\
        .order_by(VacMessage.time.desc()).limit(180).all()
    if message is not None:
        message.reverse()
    return message


'''
description:get infection information
name:"world"(世界)/国家姓名
return:返回该区域所包含的国家/地区的历史接种信息（下一级）
'''
def getHisVacMessageInclude(name):
    messages = []
    areas = db.session.query(Area.childArea).filter_by(Area.parentArea == name).all()
    if areas is None:
        return None
    else:
        for area in areas:
            message = getHisVacMessage(area)
            if message is not None:
                messages.append(message)
        if len(messages) == 0:
            return None
        else:
            return messages


'''
description:save advice
message:建议内容
对接前端
'''
def saveAdvice(message):
    advice = Advice(text=message)
    add(advice)
    return None

'''
每日更新中国疫情信息
'''
def updateChinaInf():
    clearTable('chinaInfMessages')
    data = getJsonData(nowDomesticCovidDataUrl)
    global today
    today = data['lastUpdateTime'][:10]     #XXXX-XX-XX
    errorAreaName = "地区待确认"
    china = data['areaTree'][0]
    add(changeType(china, "ChinaInfMessage"))
    provinces = china['children']
    for province in provinces:
        add(changeType(province, "ChinaInfMessage"))
        cities = province['children']
        for city in cities:
            if errorName(city['name']) == 1:
                add(changeType(city, "ChinaInfMessage"))

    #print("ok")
    #print(len(province))



'''
每日更新全球疫情信息
'''
def updateGlobalInf():
    clearTable('nowInfMessages')
    globalInf = getJsonData(nowGlobalCovidDataUrl)
    x = NowInfMessage(time=today,
                      areaName="global",
                      currentNum=globalInf['nowConfirm'],
                      totalNum=globalInf['confirm'],
                      addNum=globalInf['confirmAdd'],
                      cured=globalInf['heal'],
                      totalDead=globalInf['dead'],
                      addDead=globalInf['deadAdd']
                      )
    add(x)
    foreignInf = getJsonData(nowForeignCovidDataUrl)
    for message in foreignInf:
        add(changeType(message, "NowInfMessage"))

#得到Json文件
def getJson():
    data = getJsonData(nowDomesticCovidDataUrl)
    saveToJsonFile(data, "china.json")

#清除表单
def clearTable(name):
    db.reflect(app=app)
    db.get_engine().execute(f"truncate table {name}")

#插入数据
def add(x):
    db.session.add(x)
    db.session.commit()

#判断去除一些奇怪的地区名
def errorName(name):
    if name == "地区待确认" or name[:2] == "境外" or name[:2] == "外地":
        return 0
    else:
        return 1

#换数据格式使其与数据库表单相对照
def changeType(area, toType):
    if toType == "ChinaInfMessage":
        name = area['name']
        confirm = area['total']['nowConfirm']
        x = ChinaInfMessage(time=today,
                            areaName=name,
                            currentNum=confirm,
                            totalNum=area['total']['confirm'],
                            addNum=area['today']['confirm'],
                            cured=area['total']['heal'],
                            totalDead=area['total']['dead'],
                            addDead=0)
        return x
    elif toType == "NowInfMessage":
        name = area['name']
        x = NowInfMessage(time=today,
                          areaName=area['name'],
                          currentNum=area['nowConfirm'],
                          totalNum=area['confirm'],
                          addNum=area['confirmAdd'],
                          cured=area['heal'],
                          totalDead=area['dead'],
                          addDead=area['deadCompare'])
        return x

