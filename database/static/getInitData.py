from database.static.table import *
#from spider.spider import *
from database.static.dao import *
from spider.spider import Spider


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
        if country['name'] == '日本本土':
            country['name'] = '日本'
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
    #clearTable('hisInfMessages')
    countryData = Spider.getData(8)
    countries = db.session.query(Area).filter(Area.parentArea == 'global').filter(Area.childArea != '中国').all()
    for countryName in countries:
        name = countryName.childArea
        if name == '日本':
            hisMessages = countryData['日本本土']
        else:
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
    for url in foreignCityUrls:
        date = Spider.getCSVDictReader(url)
        china = ChinaInfMessage(time='', areaName='中国', currentNum=0, totalNum=0, addNum=0, cured=0, totalDead=0, addDead=0)
        for province in date:
            try:
                countryName = province['Country_Region']
                provinceName = province['Province_State']
                cityName = province['Admin2']
                if countryName != 'US' and countryName != 'China' and countryName != 'Taiwan*' and cityName == '' and provinceName != 'Unknown':
                    Last_Update = province['Last_Update']
                    t = Last_Update[:10]
                    x = InfMessage(time=t,
                                   areaName=provinceName,
                                   currentNum=0 if province['Active'] == '' else int(province['Active']),
                                   totalNum=0 if province['Confirmed'] == '' else int(province['Confirmed']),
                                   addNum=0,
                                   cured=0 if province['Recovered'] == '' else int(province['Recovered']),
                                   totalDead=0 if province['Deaths'] == '' else int(province['Deaths']),
                                   addDead=0)
                    add(x)
                if countryName == 'China' or countryName == 'Taiwan*':
                    china.time = province['Last_Update'][:10]
                    currentNum =0 if province['Active'] == '' else int(province['Active'])
                    china.currentNum += currentNum
                    totalNum = 0 if province['Confirmed'] == '' else int(province['Confirmed'])
                    china.totalNum += totalNum
                    cured = 0 if province['Recovered'] == '' else int(province['Recovered'])
                    china.cured += cured
                    totalDead = 0 if province['Deaths'] == '' else int(province['Deaths'])
                    china.totalDead += totalDead
            except Exception as e:
                print(e)

        add(china)

    for url in USUrls:
        date = Spider.getCSVDictReader(url)
        for province in date:
            t = province['Last_Update'][:10]
            x = InfMessage(time=t,
                           areaName=province['Province_State'],
                           currentNum=0 if province['Active'] == '' else int(province['Active'].split('.')[0]),
                           totalNum=0 if province['Confirmed'] == '' else int(province['Confirmed'].split('.')[0]),
                           addNum=0,
                           cured=0 if province['Recovered'] == '' else int(province['Recovered'].split('.')[0]),
                           totalDead=0 if province['Deaths'] == '' else int(province['Deaths'].split('.')[0]),
                           addDead=0)
            add(x)




def Init():
    getArea()       #github
    getHisVac()
    getChinaHisInf()
    getGlobalCountryHisInf()
    getGlobalProvinceHisInf()       #github

