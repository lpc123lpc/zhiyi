from database.static.createTable import *
from spider import *

today = ""


'''
description:get infection information
name:"world"(世界)/国家姓名/地区姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域的感染信息
'''


def getInfMessage(name, time):
    InfMessage.infmessage = None
    return InfMessage.infmessage


'''
description:get infection information
param:name:"world"(世界)/国家姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域所包含的国家/地区的感染信息
'''


def getInfMessageInclude(name, time):
    InfMessage.infmessages = []
    return InfMessage.infmessages


'''
description:get infection information
name:"world"(世界)/国家姓名/地区姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域的接种信息
'''


def getVacMessage(name, time):
    VacMessage.vacmessage = None
    return VacMessage.vacmessage


'''
description:get infection information
name:"world"(世界)/国家姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域所包含的国家/地区的接种信息
'''


def getVacMessageInclude(name, time):
    VacMessage.vacmessages = []
    return VacMessage.vacmessages


'''
description:save infection information
对接爬虫
'''


def saveInfMessage(messages):
    return None


'''
description:save vaccination information
对接爬虫
'''


def saveVacMessage(messages):
    for i in messages:
        message = messages[i]
        total = Area.query.filter_by(childArea=message.areaName)
        rate = float(message.totalNum/total)
        x = NowVacMessage(time=message.time,
                          areaName=message.areaName,
                          totalNum=message.totalNum,
                          addNum=message.addNum,
                          vacRate=rate)
        db.session.add(x)


'''
description:save advice
对接前端
'''


def saveAdvice(message, time):
    return None

'''
每日更新中国疫情信息
'''
def updateChinaInf():
    data = getJsonData(nowDomesticDataUrl)
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

    print("ok")
    #print(len(province))



'''
每日更新全国疫情信息
'''
def updateGlobalInf():
    globalInf = getJsonData(nowGlobalDataUrl)
    x = NowInfMessage(time=today,
                      areaName="global",
                      currentNum=globalInf['nowConfirm'],
                      totalNum=globalInf['confirm'],
                      addNum=globalInf['confirmAdd'],
                      cured=globalInf['heal'],
                      totalDead=globalInf['dead'],
                      addDead=globalInf['deadAdd'],
                      infRate=round(float(0), 5)
                      )
    add(x)
    foreignInf = getJsonData(nowForeignCouDataUrl)
    for message in foreignInf:
        add(changeType(message, "NowInfMessage"))

#得到Json文件
def getJson():
    data = getJsonData(nowDomesticDataUrl)
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
        #total = Area.query(Area.number).filter_by(childArea=name)
        confirm = area['total']['nowConfirm']
        #rate = round(float(total/confirm), 5)
        x = ChinaInfMessage(time=today,
                            areaName=name,
                            currentNum=confirm,
                            totalNum=area['total']['confirm'],
                            addNum=area['today']['confirm'],
                            cured=area['total']['heal'],
                            totalDead=area['total']['dead'],
                            addDead=0,
                            infRate=round(float(0), 5))
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
                          addDead=area['deadCompare'],
                          infRate=round(float(0), 5))
        return x

#test()
#clearTable("ChinaInfMessages")
#updateChinaInf()
#updateGlobalInf()