from database.static.table import *
from spider.spider import *

'''
description:get infection information
name:"global"(世界)/国家姓名/地区姓名
return:返回该区域的实时感染信息
'''


def getNowInfMessage(name):
    message = db.session.query(NowInfMessage).filter(NowInfMessage.areaName == name).first()
    return message if message != [] else None


'''
description:get infection information
param:name:"global"(世界)/国家姓名
return:返回该区域所包含的国家/地区的实时感染信息（下一级）
'''


def getNowInfMessageInclude(name):
    messages = db.session.query(NowInfMessage) \
        .filter(Area.parentArea == name) \
        .filter(Area.childArea == NowInfMessage.areaName).all()
    if name == "吉林":
        for message in messages:
            if message.areaName == "吉林市":
                message.areaName = "吉林"
    return messages if messages != [] else None


'''
description:get infection information
param:name:"global"(世界)/国家姓名
return:返回该区域的历史感染信息
'''


def getHisInfMessage(name):
    isChina = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == name).first()
    messages = None
    if isChina is None:
        messages = db.session.query(InfMessage) \
            .filter(InfMessage.areaName == name) \
            .order_by(InfMessage.time.desc()).limit(180).all()
        if messages is not None:
            messages.reverse()
    else:
        messages = db.session.query(ChinaInfMessage) \
            .filter(ChinaInfMessage.areaName == name) \
            .order_by(ChinaInfMessage.time.desc()).limit(180).all()
        if messages is not None:
            messages.reverse()
    return messages if messages != [] else None


'''
description:get infection information
param:name:"global"(世界)/国家姓名
return:返回该区域所包含的国家/地区的历史感染信息（下一级）
'''


def getHisInfMessageInclude(name):
    areas = db.session.query(Area).filter(Area.parentArea == name).all()
    messages = []
    if areas is None:
        return None
    else:
        a = areas[0]
        isChina = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == a.childArea).first()
        print(isChina)
        if isChina is None:
            for area in areas:
                message = db.session.query(InfMessage) \
                    .filter(InfMessage.areaName == area.childArea) \
                    .order_by(InfMessage.time.desc()).limit(180).all()
                if message is not None:
                    message.reverse()
                    messages.append(message)
        else:
            for area in areas:
                message = db.session.query(ChinaInfMessage) \
                    .filter(ChinaInfMessage.areaName == area.childArea) \
                    .order_by(ChinaInfMessage.time.desc()).limit(180).all()
                if area == "吉林市":
                    for m in message:
                        m.areaName = "吉林"
                if message is not None:
                    message.reverse()
                    messages.append(message)
        return messages if messages != [] else None


'''
description:get infection information
name:"global"(世界)/国家姓名/地区姓名
return:返回该区域的实时接种信息
'''


def getNowVacMessage(name):
    message = db.session.query(NowVacMessage).filter(NowVacMessage.areaName == name).first()
    return message if message != [] else None


'''
description:get infection information
name:"world"(世界)/国家姓名
return:返回该区域所包含的国家/地区的实时接种信息（下一级）
'''


def getNowVacMessageInclude(name):
    message = db.session.query(NowVacMessage) \
        .filter(Area.parentArea == name) \
        .filter(Area.childArea == NowVacMessage.areaName).all()
    return message if message != [] else None


'''
description:get infection information
name:"global"(世界)/国家姓名/地区姓名
return:返回该区域的历史接种信息
'''


def getHisVacMessage(name):
    message = db.session.query(VacMessage) \
        .filter(VacMessage.areaName == name) \
        .order_by(VacMessage.time.desc()).limit(180).all()
    if message is not None:
        message.reverse()
    return message if message != [] else None


'''
description:get infection information
name:"world"(世界)/国家姓名
return:返回该区域所包含的国家/地区的历史接种信息（下一级）
'''


def getHisVacMessageInclude(name):
    messages = []
    areas = db.session.query(Area).filter(Area.parentArea == name).all()
    if areas is None:
        return None
    else:
        for area in areas:
            message = getHisVacMessage(area.childArea)
            if message is not None:
                messages.append(message)
        if len(messages) == 0:
            return None
        else:
            return messages if messages != [] else None


'''
description:save advice
message:建议内容
对接前端
'''


def saveAdvice(message, t):
    advice = Advice(text=message, time=t)
    add(advice)


'''
每日更新中国疫情信息
'''


def updateChinaInf():
    data = Spider.getData(4)
    today = data['lastUpdateTime'][:10]  # XXXX-XX-XX
    china = data['areaTree'][0]
    addMessage(china, "ChinaInfMessage", today)
    provinces = china['children']
    for province in provinces:
        addMessage(province, "ChinaInfMessage", today)
        cities = province['children']
        for city in cities:
            if errorName(city['name']) == 1:
                if city['name'] == "吉林":
                    city['name'] += '市'
                addMessage(city, "ChinaInfMessage", today)
    print("update china ok")


'''
每日更新全球疫情信息
'''


def updateGlobalInf():
    globalInf = Spider.getData(1)
    today = globalInf['lastUpdateTime'][:10]
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
    foreignInf = Spider.getData(3)
    for message in foreignInf:
        addMessage(message, "NowInfMessage", today)

    print('global ok')


def updateForeignProvinceInf():
    y, t, uy, ut = Spider.getData(7)
    worldMappingPath = './world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        globalProvinces = Spider.getCSVDictReader(y)
        for province in globalProvinces:
            countryName = province['Country_Region']
            if countryName in worldMapping:
                countryName = worldMapping[province['Country_Region']]['cn']
            provinceName = province['Province_State']
            cityName = province['Admin2']
            if countryName != 'US' and cityName == '' and provinceName != 'Unknown':
                Last_Update = province['Last_Update']
                t = Last_Update[:10]

                x = NowInfMessage(time=t,
                                  areaName=provinceName,
                                  currentNum=-1 if province['Active'] == '' else int(province['Active']),
                                  totalNum=-1 if province['Confirmed'] == '' else int(province['Confirmed']),
                                  addNum=-1,
                                  cured=-1 if province['Recovered'] == '' else int(province['Recovered']),
                                  totalDead=-1 if province['Deaths'] == '' else int(province['Deaths']),
                                  addDead=-1)
                add(x)
                y = InfMessage(time=t,
                               areaName=provinceName,
                               currentNum=-1 if province['Active'] == '' else int(province['Active']),
                               totalNum=int(province['Confirmed']),
                               addNum=-1,
                               cured=int(province['Recovered']),
                               totalDead=int(province['Deaths']),
                               addDead=-1)
                add(y)

    usProvinces = Spider.getCSVDictReader(uy)
    print(uy)
    for province in usProvinces:
        t = province['Last_Update'][:10]
        x = NowInfMessage(time=t,
                          areaName=province['Province_State'],
                          currentNum=-1 if province['Active'] == '' else int(province['Active'].split('.')[0]),
                          totalNum=-1 if province['Confirmed'] == '' else int(province['Confirmed'].split('.')[0]),
                          addNum=-1,
                          cured=-1 if province['Recovered'] == '' else int(province['Recovered'].split('.')[0]),
                          totalDead=-1 if province['Deaths'] == '' else int(province['Deaths'].split('.')[0]),
                          addDead=-1)
        add(x)
        y = InfMessage(time=t,
                       areaName=province['Province_State'],
                       currentNum=-1 if province['Active'] == '' else int(province['Active'].split('.')[0]),
                       totalNum=-1 if province['Confirmed'] == '' else int(province['Confirmed'].split('.')[0]),
                       addNum=-1,
                       cured=-1 if province['Recovered'] == '' else int(province['Recovered'].split('.')[0]),
                       totalDead=-1 if province['Deaths'] == '' else int(province['Deaths'].split('.')[0]),
                       addDead=-1)
        add(y)


def updateInf():
    clearTable('nowInfMessages')
    updateChinaInf()
    updateGlobalInf()
    updateForeignProvinceInf()


'''
更新疫苗接种信息
'''


def updateVac():
    vacMessage = Spider.getData(0)
    lastName = ""
    i = 0
    worldMappingPath = './world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        v1 = None
        for v in vacMessage:
            if v['location'] in worldMapping:
                name = worldMapping[v['location']]['cn']
            else:
                name = 'global' if v['location'] == 'World' else v['location']
            if name != lastName and i != 0:
                totalNum = -1 if v1['total_vaccinations'] == '' else int(v1['total_vaccinations'])
                addNum = -1 if v1['daily_vaccinations_raw'] == '' else int(v1['daily_vaccinations_raw'])
                vacRate = -1 if v1['total_vaccinations_per_hundred'] == '' else float(v1['total_vaccinations_per_hundred'])
                NowVacMessage.query.filter_by(areaName=lastName) \
                    .update({'time': v1['date'], 'totalNum': totalNum, 'addNum': addNum, 'vacRate': vacRate})
                db.session.commit()
            lastName = name
            v1 = v
            i += 1
        totalNum = -1 if v['total_vaccinations'] == '' else int(v['total_vaccinations'])
        addNum = -1 if v['daily_vaccinations_raw'] == '' else int(v['daily_vaccinations_raw'])
        vacRate = -1 if v['total_vaccinations_per_hundred'] == '' else float(v['total_vaccinations_per_hundred'])
        NowVacMessage.query.filter_by(areaName=name) \
            .update({'time': v['date'], 'totalNum': totalNum, 'addNum': addNum, 'vacRate': vacRate})
        db.session.commit()


# 清除表单
def clearTable(name):
    db.reflect(app=app)
    db.get_engine().execute(f"truncate table {name}")


# 插入数据
def add(x):
    db.session.merge(x)
    db.session.commit()


# 判断去除一些奇怪的地区名
def errorName(name):
    if name == "地区待确认" or name[:2] == "境外" or name[:2] == "外地":
        return 0
    else:
        return 1


# 换数据格式使其与数据库表单相对照
def addMessage(area, toType, today):
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
        add(x)
        y = NowInfMessage(time=x.time,
                          areaName=x.areaName,
                          currentNum=x.currentNum,
                          totalNum=x.totalNum,
                          addNum=x.addNum,
                          cured=x.cured,
                          totalDead=x.totalDead,
                          addDead=x.addDead)
        add(y)
    elif toType == "NowInfMessage":
        name = area['name']
        if name == '日本本土':
            name = '日本'
        print(area['confirmAdd'])
        x = NowInfMessage(time=today,
                          areaName=name,
                          currentNum=area['nowConfirm'],
                          totalNum=area['confirm'],
                          addNum=area['confirmAdd'],
                          cured=area['heal'],
                          totalDead=area['dead'],
                          addDead=area['deadCompare'])
        add(x)
