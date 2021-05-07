from database.static.table import *
from spider.spider import *
from database.static.dao import *

def getArea():
    clearTable('areas')
    chinaData = Spider.getData(4)
    chinaData = chinaData['areaTree'][0]
    name = chinaData['name']
    provinces = chinaData['children']
    for province in provinces:
        pArea = Area(parentArea=name, childArea=province['name'])
        add(pArea)
        cities = province['children']
        for city in cities:
            if errorName(city['name']) == 1:
                if city['name'] == "吉林":
                    city['name'] += '市'
                cArea = Area(parentArea=province['name'], childArea=city['name'])
                add(cArea)

    globalCountryData = Spider.getData(3)
    add(Area(parentArea='global', childArea='中国'))
    for country in globalCountryData:
        area = Area(parentArea='global', childArea=country['name'])
        add(area)

    yUrl, tUrl, yUSUrl, dUSUrl = Spider.getData(7)
    worldMappingPath = './world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        globalProvinces = Spider.getCSVDictReader(yUrl)
        for province in globalProvinces:
            #print(province['Province_State'])
            if province['Country_Region'] != 'US' and province['Province_State'] != '' and province['Admin2'] == '' and province['Province_State'] != 'Unknown':
                parent = ''
                if province['Country_Region'] in worldMapping:
                    parent = worldMapping[province['Country_Region']]['cn']
                else:
                    parent = province['Country_Region']
                child = province['Province_State']
                area = Area(parentArea=parent, childArea=child)
                #print(parent)
                add(area)

        usProvinces = Spider.getCSVDictReader(yUSUrl)
        for province in usProvinces:
            parent = '美国'
            child = province['Province_State']
            area = Area(parentArea=parent, childArea=child)
            add(area)



def getHisVac():
    vacMessage = Spider.getData(0)
    worldMappingPath = './world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        lastname = ''
        i = 0
        v1 = VacMessage()
        for v in vacMessage:
            if v['location'] in worldMapping:
                name = 'global' if v['location'] == 'World' else worldMapping[v['location']]['cn']
            else:
                name = v['location']
            totalNum = 0 if v['total_vaccinations'] == '' else int(v['total_vaccinations'])
            addNum = 0 if v['daily_vaccinations_raw'] == '' else (v['daily_vaccinations_raw'])
            vacRate = 0 if v['total_vaccinations_per_hundred'] == '' else float(v['total_vaccinations_per_hundred'])
            vac = VacMessage(time=v['date'], areaName=name, totalNum=totalNum, addNum=addNum, vacRate=vacRate)
            add(vac)
            if name != lastname and i != 0:
                nowVac = NowVacMessage(time=v1.time, areaName=v1.areaName, totalNum=v1.totalNum, addNum=v1.addNum, vacRate=v1.vacRate)
                add(nowVac)
            lastname = name
            v1 = vac
            i += 1
        nowVac = NowVacMessage(time=v1.time, areaName=v1.areaName, totalNum=v1.totalNum, addNum=v1.addNum,
                               vacRate=v1.vacRate)
        add(nowVac)


def getChinaHisInf():
    clearTable('chinaInfMessages')
    provinces = Spider.getData(5)
    provinceName = db.session.query(Area).filter(Area.parentArea == "中国")
    for name in provinceName:
        cityName = db.session.query(Area).filter(Area.parentArea == name.childArea)
        try:
            province = provinces[name.childArea]
            provinceData = province['self']
            for date in provinceData:
                t = str(date['year']) + "-" + date['date'][:2] + "-" + date['date'][3:5]
                x = ChinaInfMessage(time=t,
                                    areaName=date['province'],
                                    currentNum=date['confirm'],
                                    totalNum=date['confirm'] - date['heal'],
                                    addNum=date['newConfirm'],
                                    cured=date['heal'],
                                    totalDead=date['dead'],
                                    addDead=date['newDead'])
                add(x)

            for city in cityName:
                try:
                    city = city.childArea
                    if city == "吉林市":
                        city = "吉林"
                    if city in province:
                        cityData = province[city]
                        for date in cityData:
                            t = date['y'] + "-" + date['date'][:2] + "-" + date['date'][3:5]
                            name = date['city'] if date['city'] != "吉林" else "吉林市"
                            x = ChinaInfMessage(time=t,
                                                areaName=date['city'],
                                                currentNum=date['confirm'],
                                                totalNum=date['confirm'] - date['heal'],
                                                addNum=int(date['confirm_add'] if date['confirm_add'] != '' else 0),
                                                cured=date['heal'],
                                                totalDead=date['dead'],
                                                addDead=0)
                            add(x)
                except Exception as e:
                    print(e)
        except Exception as e:
            print (e)



def getGlobalCountryHisInf():
    countryData = Spider.getData(8)
    countries = db.session.query(Area).filter(Area.parentArea == 'global').filter(Area.childArea != '中国').all()
    for countryName in countries:
        name = countryName.childArea
        hisMessages = countryData[name]
        for m in hisMessages:
            t = m['y'] + "-" + m['date'][:2] + "-" + m['date'][3:5]
            x = InfMessage(time=t,
                           areaName=name,
                           currentNum=m['confirm'] - m['heal'],
                           totalNum=m['confirm'],
                           addNum=m['confirm_add'],
                           cured=m['heal'],
                           totalDead=m['dead'],
                           addDead=0)
            add(x)


def getGlobalProvinceHisInf():
    foreignCityUrls, USUrls = Spider.getData(6)
    worldMappingPath = './world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        for url in foreignCityUrls:
            date = Spider.getCSVDictReader(url)
            for province in date:
                countryName = province['Country_Region'] if province['Country_Region'] in worldMapping else worldMapping[province['Country_Region']]['cn']
                provinceName = province['Province_State']
                cityName = province['Admin2']
                if countryName != 'US' and cityName == '' and provinceName != 'Unknown':
                    Last_Update = province['Last_Update']
                    t = Last_Update[0:4]
                    if Last_Update[6] == '/' and Last_Update[8] == ' ':
                        t = t + '-0' + Last_Update[5] + '-0' + Last_Update[7]
                    elif Last_Update[6] == '/' and Last_Update[9] == ' ':
                        t = t + '-0' + Last_Update[5] + '-' + Last_Update[7:9]
                    elif Last_Update[7] == '/' and Last_Update[10] == ' ':
                        t = t + '-' + Last_Update[5:7] + '-' + Last_Update[8:10]
                    x = InfMessage(time=t,
                                   areaName=provinceName,
                                   currentNum=int(province['Active']),
                                   totalNum=int(province['Confirmed']),
                                   addNum=0,
                                   cured=int(province['Recovered']),
                                   totalDead=int(province['Dead']),
                                   addDead=0)
                    add(x)

        for url in USUrls:
            date = Spider.getCSVDictReader(url)
            for province in date:
                t = province['Last_Update'][:10]
                x = InfMessage(time=t,
                               areaName=provinceName,
                               currentNum=int(float(province['Active'])),
                               totalNum=int(float(province['Confirmed'])),
                               addNum=0,
                               cured=int(float(province['Recovered'])),
                               totalDead=int(float(province['Dead'])),
                               addDead=0)
                add(x)



def Init():
    getArea()
    getHisVac()
    getChinaHisInf()
    getGlobalCountryHisInf()
    getGlobalProvinceHisInf()



getArea()