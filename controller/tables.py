from flask import jsonify
from database.static import dao
import datetime
import json
from testcode.lq import testData


'''worldInfData = testData.infdata
worldVacData = testData.vacdata'''


def dealWithNone(i):
    if i == -1:
        return None
    else:
        return i


def getWorldData():
    worldVacData = dao.getNowVacMessageInclude('global')
    worldInfData = dao.getNowInfMessageInclude('global')
    all_data = []
    for i in worldInfData:
        for j in worldVacData:
            if getattr(i, 'areaName') == getattr(j, 'areaName'):
                all_data.append({"name": getattr(i, 'areaName'),
                                 "confirmed": dealWithNone(getattr(i, 'totalNum')),
                                 "newConfirmed": dealWithNone(getattr(i, 'addNum')),
                                 "cured": dealWithNone(getattr(i, 'cured')),
                                 "deceased": dealWithNone(getattr(i, 'totalDead')),
                                 "vaccined": dealWithNone(getattr(j, 'totalNum')),
                                 "newVaccined": dealWithNone(getattr(j, 'addNum')),
                                 "vaccine_coverage": dealWithNone(getattr(j, 'vacRate'))})
                break
    return json.dumps(all_data)


def getCountryInfData(country):
    infData = dao.getHisInfMessage(country)
    times, confirmed, deceased, cure = [], [], [], []
    if infData is None:
        return jsonify({})
    for i in infData:
        times.append(getattr(i, 'time'))
        confirmed.append(getattr(i, 'totalNum'))
        deceased.append(getattr(i, 'totalDead'))
        cure.append(getattr(i, 'cured'))
    return jsonify({
        "name": country,
        "time": times,
        "confirmed": confirmed,
        "deceased": deceased,
        "cured": cure
    })


def getCountryVacData(country):
    vacData = dao.getHisVacMessage(country)
    times, vaccined = [], []
    if vacData is None:
        return jsonify({})
    for i in vacData:
        times.append(getattr(i, 'time'))
        vaccined.append(getattr(i, 'totalNum'))
    return jsonify({
        "name": country,
        "time": times,
        "vaccined": vaccined
    })


def getCountryInfection(country):
    all_data = []
    data = dao.getHisInfMessageInclude(country)
    if data is None:
        return jsonify({})
    for i in data:
        position = ''
        confirmed, deceased, cured, times = [], [], [], []
        for j in i:
            position = getattr(i[0], 'areaName')
            times.append(getattr(j, 'time'))
            cured.append(getattr(j, 'cured'))
            confirmed.append(getattr(j, 'totalNum'))
            deceased.append(getattr(j, 'totalDead'))
        all_data.append({"name": position, "time": times, "confirmed": confirmed, "deceased": deceased, "cured": cured})
    return json.dumps(all_data)


def getCountryVaccine(country):
    all_data = []
    data = dao.getHisVacMessageInclude(country)
    if data is None:
        return jsonify({})
    for i in data:
        position = getattr(i[0], 'areaName')
        times, vaccined, covrtage = [], [], []
        for j in i:
            times.append(getattr(j, 'time'))
            vaccined.append(getattr(j, 'totalNum'))
            covrtage.append(getattr(j, 'vacRate'))
        all_data.append({"name": position, "time": times, "vaccined": vaccined, "coverage": covrtage})
    return json.dumps(all_data)


def getProvinceInfection(province):
    times, confirmed, deceased, cure = [], [], [], []
    infData = dao.getHisInfMessage(province)
    if infData is None:
        return jsonify({})
    for i in infData:
        confirmed.append(getattr(i, 'totalNum'))
        deceased.append(getattr(i, 'totalDead'))
        cure.append(getattr(i, 'cured'))
        times.append(getattr(i, 'time'))
    return jsonify({
        "name": province,
        "time": times,
        "confirmed": confirmed,
        "deceased": deceased,
        "cured": cure
    })
