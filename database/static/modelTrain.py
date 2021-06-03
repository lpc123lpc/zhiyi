from database.static.table import *
from spider.covidSpider import *
import json
import pandas as pd

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


def getForeignCsv(name):
    area = db.session.query(InfMessage).filter(InfMessage.areaName == name)\
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
    test.to_csv('India.csv', encoding='gbk')


def getProvinceCsv(name):
    area = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == name)\
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
    test.to_csv('province.csv', encoding='gbk')

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

    return dirc