from database.static.table import *
from spider.covidSpider import *
import json
import pandas as pd
import datetime

def getChinaCsv():
    china = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == '中国')\
        .filter(ChinaInfMessage.totalNum != 0).order_by(ChinaInfMessage.time.asc()).all()
    list = []
    num = 1
    for c in china:
        childList = [num, c.time, c.totalNum]
        list.append(childList)
        num += 1
    name = ['序号', '时间', '累计确诊']
    test = pd.DataFrame(columns=name, data=list)
    print(test)
    test.to_csv('china.csv', encoding='gbk')


def getForeignCsv(n):
    area = db.session.query(InfMessage).filter(InfMessage.areaName == n)\
        .filter(InfMessage.totalNum != 0).order_by(InfMessage.time.asc()).all()
    list = []
    num = 1
    for c in area:
        childList = [num, c.time, c.totalNum]
        list.append(childList)
        num += 1
    name = ['序号', '时间', '累计确诊']
    test = pd.DataFrame(columns=name, data=list)
    print(test)
    test.to_csv(n+'.csv', encoding='gbk')


def getProvinceCsv(n):
    area = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == n)\
        .filter(ChinaInfMessage.totalNum != 0).order_by(ChinaInfMessage.time.asc()).all()
    list = []
    num = 1
    for c in area:
        childList = [num, c.time, c.totalNum]
        list.append(childList)
        num += 1
    name = ['序号', '时间', '累计确诊']
    test = pd.DataFrame(columns=name, data=list)
    print(test)
    test.to_csv(n+'.csv', encoding='gbk')


def getTrainCsv():
    dirc = getAreaMapping()
    i = 1
    q = 0
    mapList = []
    mapListName = ['序号', '地区名', '开始时间']
    while i in dirc:
        areaName = dirc[i]
        area = db.session.query(InfMessage).filter(InfMessage.areaName == areaName)\
        .filter(InfMessage.totalNum != 0).order_by(InfMessage.time.asc()).all()
        if len(area) == 0:
            area = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == areaName)\
                .filter(ChinaInfMessage.totalNum != 0).order_by(ChinaInfMessage.time.asc()).all()
        try:
            start = area[0].time
            mapList.append([i-q, areaName, start])
            start = datetime.datetime(int(start[0:4]), int(start[5:7]), int(start[8:10]))
            cList = []
            for a in area:
                atime = datetime.datetime(int(a.time[0:4]), int(a.time[5:7]), int(a.time[8:10]))
                childList = [(atime - start).days + 1, a.time, a.totalNum]
                cList.append(childList)
            cListName = ['no', 'time', 'num']
            cCsv = pd.DataFrame(columns=cListName, data=cList)
            cCsv.to_csv('./trainCsv/' + str(i-q) + '.csv', encoding='gbk')
        except Exception as e:
            print(areaName)
            q += 1
        i += 1
    mapCsv = pd.DataFrame(columns=mapListName, data=mapList)



'''
返回有数据地区的字典映射
dirc[num] = name
num:int
name:String
'''
def getAreaMapping():
    areas = db.session.query(Area).filter(Area.population != 0).filter(Area.childArea != 'global').all()
    dirc = {}
    num = 1
    for a in areas:
        dirc[num] = a.childArea
        num += 1

    return


def getAreaJson():
    areas = db.session.query(Area).filter(Area.population != 0).filter(Area.childArea != 'global').all()
    jsonDirc = {}
    num = 1
    startTime = ''
    population = 0
    for a in areas:
        name = a.childArea
        population = a.population
        hisMes = db.session.query(InfMessage).filter(InfMessage.areaName == name).order_by(InfMessage.time.asc()).first()
        if hisMes is None:
            hisMes = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == name).order_by(ChinaInfMessage.time.asc()).first()
            if hisMes is None:
                continue
            else:
                startTime = hisMes.time
        else:
            startTime = hisMes.time
        jsonDirc[name] = {'num': num, 'begindate': startTime, 'population': population}
        num += 1
    fp = open('./trainCsv/area.json', 'w')
    fp.write(json.dumps(jsonDirc, ensure_ascii=False))
    fp.close()