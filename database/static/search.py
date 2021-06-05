# -*- coding:utf-8 -*-

from sqlalchemy.sql import text
from database.static.table import *
from spider.covidSpider import *
import json
import pandas as pd

def getSearchData():
    jsonChina = {}
    jsonForeign = {}
    value = 1
    jsonForeign['value'] = value
    jsonForeign['label'] = '国外'
    value += 1
    foreignChildren = []
    foreignCountries = db.session.query(Area)\
        .from_statement(text("select * from areas where parentArea = 'global' and childArea != 'global' and childArea != '中国' ORDER BY CONVERT(childArea USING gbk) ASC")).all()
    for country in foreignCountries:
        pName = country.childArea
        foreignCountry = {'value': value, 'label': pName}
        value += 1
        countryAreas = db.session.query(Area).filter(Area.parentArea == pName).filter(Area.population != 0).order_by(Area.childArea.asc()).all()
        if len(countryAreas) != 0:
            foreignCountryChildren = []
            foreignCountryChildren.append({'value': value, 'label': pName})
            value += 1
            for area in countryAreas:
                cName = area.childArea
                foreignCountryChild = {'value': value, 'label': cName}
                value += 1
                foreignCountryChildren.append(foreignCountryChild)
            foreignCountry['children'] = foreignCountryChildren
        foreignChildren.append(foreignCountry)
    jsonForeign['children'] = foreignChildren

    jsonChina['value'] = value
    jsonChina['label'] = '国内'
    value += 1
    chinaChildren = []
    china = {'value': value, 'label': '中国'}
    value += 1
    chinaChildren.append(china)
    provinces = db.session.query(Area).from_statement(text("select * from areas where parentArea = '中国'ORDER BY CONVERT(childArea USING gbk) ASC")).all()
    for p in provinces:
        pName = p.childArea
        province = {'value': value, 'label': pName}
        value += 1
        pChildren = []
        cities = db.session.query(Area).from_statement(text("select * from areas where parentArea = :n ORDER BY CONVERT(childArea USING gbk) ASC")).params(n=pName).all()
        if len(cities) != 0:
            pChildren.append({'value': value, 'label': pName})
            value += 1
            for c in cities:
                city = {'value': value, 'label': c.childArea}
                value += 1
                pChildren.append(city)
            province['children'] = pChildren
        chinaChildren.append(province)
    jsonChina['children'] = chinaChildren

    searchData = [jsonForeign, jsonChina]
    fp = open('./searchData.json', 'w')
    fp.write(json.dumps(searchData, ensure_ascii=False))
    fp.close()
    return searchData

