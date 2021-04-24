from flask import jsonify
from database.static import dao
import datetime
import json


def getWordData():
    time = datetime.date.today()
    worldInfData = dao.getVacMessageInclude('world', time)
    worldVacData = dao.getInfMessageInclude('world', time)
    names, confirmed, newConfirmed, cured = [], [], [], []
    deceased, vaccined, newVaccined, vaccine_coverage = [], [], [], []
    for i in worldInfData:
        for j in worldVacData:
            if getattr(i, 'areaName') == getattr(j, 'areaName'):
                names.append(getattr(i, 'areaName'))
                confirmed.append(getattr(i, 'totalNum'))
                newConfirmed.append(getattr(i, 'addNum'))
                cured.append(getattr(i, 'cured'))
                deceased.append(getattr(i, 'totalDead'))
                vaccined.append(getattr(j, 'totalNum'))
                newVaccined.append(getattr(j, 'addNum'))
                vaccine_coverage.append(getattr(j, 'vacRate'))
                break
    return jsonify({
        "name": names,
        "confirmed": confirmed,
        "newConfirmed": newConfirmed,
        "cured": cured,
        "deceased": deceased,
        "vaccined": vaccined,
        "newVaccined": newVaccined,
        "vaccine_coverage": vaccine_coverage
    })


def getCountryData(country):
    time = datetime.date.today() - datetime.timedelta(days=179)
    times, vaccined, confirmed, deceased, cure = [], [], [], [], []
    for i in range(0, 180):
        infData = dao.getInfMessage(country, time)
        vacData = dao.getVacMessage(country, time)
        times.append(time)
        vaccined.append(getattr(vacData, 'totalNum'))
        confirmed.append(getattr(infData, 'totalNum'))
        deceased.append(getattr(infData, 'totalDead'))
        cure.append(getattr(infData, 'cured'))
        time = datetime.date.today() + datetime.timedelta(days=1)
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
    data = dao.getInfMessageInclude(country, time)
    for i in data:
        position = getattr(i, 'areaName');
        time = datetime.date.today() - datetime.timedelta(days=179)
        for j in range(0, 180):
            infData = dao.getInfMessage(position, time)
            times.append(time)
            confirmed.append(getattr(infData, 'totalNum'))
            deceased.append(getattr(infData, 'totalDead'))
            cured.append(getattr(infData, 'cured'))
            time = datetime.date.today() + datetime.timedelta(days=1)
        all_data.append({"name": position, "time": times, "confirmed": confirmed, "deceased": deceased, "cured": cured})
    return json.dumps(all_data)


def getCountryVaccine(country):
    time = datetime.date.today() - datetime.timedelta(days=179)
    times, vaccined, covrtage = [], [], []
    all_data = []
    data = dao.getVacMessageInclude(country, time)
    for i in data:
        position = getattr(i, 'areaName');
        time = datetime.date.today() - datetime.timedelta(days=179)
        for j in range(0, 180):
            vacData = dao.getVacMessage(position, time)
            times.append(time)
            vaccined.append(getattr(vacData, 'totalNum'))
            covrtage.append(getattr(vacData, 'vacRate'))
            time = datetime.date.today() + datetime.timedelta(days=1)
        all_data.append({"name": position, "time": times, "vaccined": vaccined, "coverage": covrtage})
    return json.dumps(all_data)
