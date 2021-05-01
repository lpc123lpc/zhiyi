from flask import jsonify
from database.static import dao
import datetime
import json
from testcode.lq import testData


'''worldInfData = testData.infdata
worldVacData = testData.vacdata'''


def getWorldData():
    time = datetime.date.today()
    worldInfData = dao.getVacMessageInclude('world', time.strftime("%Y-%m-%d"))
    worldVacData = dao.getInfMessageInclude('world', time.strftime("%Y-%m-%d"))
    all_data = []
    for i in worldInfData:
        for j in worldVacData:
            if getattr(i, 'areaName') == getattr(j, 'areaName'):
                all_data.append({"name": getattr(i, 'areaName'),
                                 "confirmed": getattr(i, 'totalNum'),
                                 "newConfirmed": getattr(i, 'addNum'),
                                 "cured": getattr(i, 'cured'),
                                 "deceased": getattr(i, 'totalDead'),
                                 "vaccined": getattr(j, 'totalNum'),
                                 "newVaccined": getattr(j, 'addNum'),
                                 "vaccine_coverage": getattr(j, 'vacRate')})
                break
    return json.dumps(all_data)


def getCountryData(country):
    time = datetime.date.today() - datetime.timedelta(days=179)
    times, vaccined, confirmed, deceased, cure = [], [], [], [], []
    for i in range(0, 180):
        infData = dao.getInfMessage(country, time.strftime("%Y-%m-%d"))
        vacData = dao.getVacMessage(country, time.strftime("%Y-%m-%d"))
        '''infData = testData.halfYearInfData[i]
        vacData = testData.halfYearVacData[i]'''
        times.append(time.strftime("%Y-%m-%d"))
        vaccined.append(getattr(vacData, 'totalNum'))
        confirmed.append(getattr(infData, 'totalNum'))
        deceased.append(getattr(infData, 'totalDead'))
        cure.append(getattr(infData, 'cured'))
        time = time + datetime.timedelta(days=1)
    return jsonify({
        "name": country,
        "time": times,
        "vaccined": vaccined,
        "confirmed": confirmed,
        "deceased": deceased,
        "cured": cure
    })


def getCountryInfection(country):
    time = datetime.date.today() - datetime.timedelta(days=179)
    times, confirmed, deceased, cured = [], [], [], []
    all_data = []
    data = dao.getInfMessageInclude(country, time.strftime("%Y-%m-%d"))
    '''data = testData.infdatainclude'''
    k = 0
    for i in data:
        position = getattr(i, 'areaName')
        time = datetime.date.today() - datetime.timedelta(days=179)
        for j in range(0, 180):
            infData = dao.getInfMessage(position, time)
            '''infData = (testData.includeInf[k])[j]'''
            times.append(time.strftime("%Y-%m-%d"))
            confirmed.append(getattr(infData, 'totalNum'))
            deceased.append(getattr(infData, 'totalDead'))
            cured.append(getattr(infData, 'cured'))
            time = time + datetime.timedelta(days=1)
        k = k + 1
        all_data.append({"name": position, "time": times, "confirmed": confirmed, "deceased": deceased, "cured": cured})
    return json.dumps(all_data)


def getCountryVaccine(country):
    time = datetime.date.today() - datetime.timedelta(days=179)
    times, vaccined, covrtage = [], [], []
    all_data = []
    data = dao.getVacMessageInclude(country, time.strftime("%Y-%m-%d"))
    '''data = testData.vacdatainclude'''
    k = 0
    for i in data:
        position = getattr(i, 'areaName')
        time = datetime.date.today() - datetime.timedelta(days=179)
        for j in range(0, 180):
            vacData = dao.getVacMessage(position, time)
            '''vacData = (testData.includeVac[k])[j]'''
            times.append(time)
            vaccined.append(getattr(vacData, 'totalNum'))
            covrtage.append(getattr(vacData, 'vacRate'))
            time = datetime.date.today() + datetime.timedelta(days=1)
        k = k + 1
        all_data.append({"name": position, "time": times, "vaccined": vaccined, "coverage": covrtage})
    return json.dumps(all_data)
