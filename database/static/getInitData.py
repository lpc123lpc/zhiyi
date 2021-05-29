from database.static.table import *
#from spider.spider import *
from database.static.dao import *
from spider.covidSpider import Spider
import pymysql


def getArea():
    clearTable('areas')
    chinaData = Spider.getData(4)
    chinaData = chinaData['areaTree'][0]
    name = chinaData['name']
    provinces = chinaData['children']
    for province in provinces:
        pArea = Area(parentArea=name, childArea=province['name'], population=0)
        add(pArea)
        cities = province['children']
        for city in cities:
            if errorName(city['name']) == 1:
                if city['name'] == "吉林":
                    city['name'] += '市'
                cArea = Area(parentArea=province['name'], childArea=city['name'], population=0)
                add(cArea)

    globalCountryData = Spider.getData(3)
    add(Area(parentArea='global', childArea='中国', population=0))
    add(Area(parentArea='global', childArea='格陵兰', population=0))
    add(Area(parentArea='global', childArea='global', population=0))
    for country in globalCountryData:
        if country['name'] == '日本本土':
            country['name'] = '日本'
        area = Area(parentArea='global', childArea=country['name'], population=0)
        add(area)

    yUrl, tUrl, yUSUrl, dUSUrl = Spider.getData(7)
    glolist, uslist = Spider.getData(6)
    worldMappingPath = 'world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        globalProvinces = Spider.getCSVDictReader(yUrl)
        for province in globalProvinces:
            #print(province['Province_State'])
            if province['Country_Region'] != 'US' and province['Province_State'] != '' and province['Admin2'] == '' and province['Country_Region'] != 'China' and province['Province_State'] != 'Unknown':
                parent = ''
                if province['Country_Region'] in worldMapping:
                    parent = worldMapping[province['Country_Region']]['cn']
                else:
                    parent = province['Country_Region']
                child = province['Province_State']
                area = Area(parentArea=parent, childArea=child, population=0)
                #print(parent)
                add(area)

        usProvinces = Spider.getCSVDictReader(uslist[5])
        print(yUSUrl)
        for province in usProvinces:
            parent = '美国'
            child = province['Province_State']
            area = Area(parentArea=parent, childArea=child, population=0)
            add(area)


def getNewArea():
    clearTable('areas')
    try:
        with open('areas.sql', encoding='utf-8', mode='r') as f:
            # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
            sql_list = f.read().split(';')[:-1]
            for x in sql_list:
                # 判断包含空行的
                if '\n' in x:
                    # 替换空行为1个空格
                    x = x.replace('\n', ' ')

                # 判断多个空格时
                if '    ' in x:
                    # 替换为空
                    x = x.replace('    ', '')

                # sql语句添加分号结尾
                sql_item = x + ';'
                # print(sql_item)
                db.session.execute(sql_item)
    except Exception as e:
        print(e)
        print('执行失败sql: %s' % sql_item)
    finally:
        db.session.commit()
        db.session.close()


def getHisVac():
    clearTable('hisVacMessages')
    vacMessage = Spider.getData(0)
    worldMappingPath = './world-mapping.json'
    with open(worldMappingPath, mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        lastname = ''
        i = 0
        v1 = VacMessage()
        for v in vacMessage:
            if v['location'] in worldMapping:
                name = worldMapping[v['location']]['cn']
            else:
                name = 'global' if v['location'] == 'World' else v['location']
            totalNum = -1 if v['total_vaccinations'] == '' else int(v['total_vaccinations'])
            addNum = -1 if v['daily_vaccinations_raw'] == '' else int(v['daily_vaccinations_raw'])
            vacRate = -1 if v['total_vaccinations_per_hundred'] == '' else float(v['total_vaccinations_per_hundred'])
            vac = VacMessage(time=v['date'], areaName=name, totalNum=totalNum, addNum=addNum, vacRate=vacRate)
            if totalNum > 0:
                add(vac)
            if name != lastname and i != 0 and v1.totalNum > 0:
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
                cNum = 0 if (date['confirm'] - date['heal'] - date['dead']) < 0 else date['confirm'] - date['heal'] - date['dead']
                tNum = db.session.query(Area).filter(Area.childArea == date['province']).first().population
                rate = -1 if tNum == 0 else cNum / tNum
                rate = ('%.5f' % rate)
                #print(rate)
                x = ChinaInfMessage(time=t,
                                    areaName=date['province'],
                                    currentNum=cNum ,
                                    totalNum=date['confirm'],
                                    addNum=date['newConfirm'],
                                    cured=date['heal'],
                                    totalDead=date['dead'],
                                    addDead=date['newDead'],
                                    infRate=rate)
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
                            cNum = 0 if (date['confirm'] - date['heal'] - date['dead']) < 0 else date['confirm'] - date['heal'] - date['dead']
                            tNum = db.session.query(Area).filter(Area.childArea == name).first().population
                            rate = -1 if tNum == 0 else cNum / tNum
                            rate = ('%.5f' % rate)
                            #print(rate)
                            x = ChinaInfMessage(time=t,
                                                areaName=name,
                                                currentNum=cNum,
                                                totalNum=date['confirm'],
                                                addNum=int(date['confirm_add'] if date['confirm_add'] != '' else -1),
                                                cured=date['heal'],
                                                totalDead=date['dead'],
                                                addDead=-1,
                                                infRate=rate)
                            add(x)
                except Exception as e:
                    print(e)
        except Exception as e:
            print (e)



def getGlobalCountryHisInf():
    clearTable('hisInfMessages')
    countryData = Spider.getData(8)
    countries = db.session.query(Area).filter(Area.parentArea == 'global').filter(Area.childArea != '中国').filter(Area.childArea != 'global').filter(Area.childArea != '格陵兰').all()
    for countryName in countries:
        name = countryName.childArea
        if name == '日本':
            hisMessages = countryData['日本本土']
        else:
            hisMessages = countryData[name]
        for m in hisMessages:
            t = m['y'] + "-" + m['date'][:2] + "-" + m['date'][3:5]
            cNum = m['confirm'] - m['heal']
            tNum = db.session.query(Area).filter(Area.childArea == name).first().population
            rate = -1 if tNum == 0 else cNum / tNum
            rate = ('%.5f' % rate)
            x = InfMessage(time=t,
                           areaName=name,
                           currentNum=m['confirm'] - m['heal'],
                           totalNum=m['confirm'],
                           addNum=m['confirm_add'],
                           cured=m['heal'],
                           totalDead=m['dead'],
                           addDead=-1,
                           infRate=rate)
            print(rate)
            add(x)


def getGlobalProvinceHisInf():
    foreignCityUrls, USUrls = Spider.getData(6)
    for url in foreignCityUrls:
        date = Spider.getCSVDictReader(url)
        china = ChinaInfMessage(time='', areaName='中国', currentNum=0, totalNum=0, addNum=0, cured=0, totalDead=0, addDead=0, infRate=0)
        for province in date:
            try:
                countryName = province['Country_Region']
                provinceName = province['Province_State']
                if provinceName == 'Greenland':
                    provinceName = '格陵兰'
                cityName = province['Admin2']
                if countryName != 'US' and countryName != 'China' and countryName != 'Taiwan*' and cityName == '' and provinceName != 'Unknown' and provinceName != '':
                    Last_Update = province['Last_Update']
                    t = Last_Update[:10]
                    try:
                        t = tChangeType(t)
                    except Exception as e:
                        print(e)

                    cNum = -1 if province['Active'] == '' else int(province['Active'])
                    tNum = db.session.query(Area).filter(Area.childArea == provinceName).first().population
                    rate = -1 if tNum == 0 else cNum / tNum
                    rate = ('%.5f' % rate)
                    x = InfMessage(time=t,
                                   areaName=provinceName,
                                   currentNum=-1 if province['Active'] == '' else int(province['Active']),
                                   totalNum=-1 if province['Confirmed'] == '' else int(province['Confirmed']),
                                   addNum=-1,
                                   cured=-1 if province['Recovered'] == '' else int(province['Recovered']),
                                   totalDead=-1 if province['Deaths'] == '' else int(province['Deaths']),
                                   addDead=-1,
                                   infRate=rate)
                    add(x)
                if countryName == 'China' or countryName == 'Taiwan*':
                    t = province['Last_Update'][:10]
                    try:
                        t = tChangeType(t)
                        print(t)
                    except Exception as e:
                        print(e)
                    china.time = t
                    currentNum =-1 if province['Active'] == '' else int(province['Active'])
                    china.currentNum += currentNum
                    totalNum = -1 if province['Confirmed'] == '' else int(province['Confirmed'])
                    china.totalNum += totalNum
                    cured = -1 if province['Recovered'] == '' else int(province['Recovered'])
                    china.cured += cured
                    totalDead = -1 if province['Deaths'] == '' else int(province['Deaths'])
                    china.totalDead += totalDead
            except Exception as e:
                print(e)

        tNum = db.session.query(Area).filter(Area.childArea == '中国').first().population
        r = china.currentNum / tNum
        r = ('%.5f' % r)
        china.infRate = r
        add(china)

    for url in USUrls:
        date = Spider.getCSVDictReader(url)
        for province in date:
            t = province['Last_Update'][:10]
            try:
                t = tChangeType(t)
            except Exception as e:
                print(e)
            try:
                cNum = -1 if province['Active'] == '' else int(province['Active'].split('.')[0])
                tNum = db.session.query(Area).filter(Area.childArea == province['Province_State']).first().population
                rate = -1 if tNum == 0 else cNum / tNum
                rate = ('%.5f' % rate)
                x = InfMessage(time=t,
                               areaName=province['Province_State'],
                               currentNum=-1 if province['Active'] == '' else int(province['Active'].split('.')[0]),
                               totalNum=-1 if province['Confirmed'] == '' else int(province['Confirmed'].split('.')[0]),
                               addNum=-1,
                               cured=-1 if province['Recovered'] == '' else int(province['Recovered'].split('.')[0]),
                               totalDead=-1 if province['Deaths'] == '' else int(province['Deaths'].split('.')[0]),
                               addDead=-1,
                               infRate=rate)
                add(x)
            except Exception as e:
                print(e)




def Init():
    getNewArea()       #github
    print(1)
    getHisVac()
    print(2)
    getChinaHisInf()
    print(3)
    getGlobalCountryHisInf()
    print(4)
    getGlobalProvinceHisInf()       #github

'''clearTable('nowVacMessages')
getHisVac()'''