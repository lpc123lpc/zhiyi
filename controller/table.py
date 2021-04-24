from flask import jsonify
from database.static import dao
import datetime


def getWordData():
    time = datetime.date.today()
    worldInfData = dao.getVacMessageInclude('world', time)
    worldVacData = dao.getInfMessageInclude('world', time)



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
        "data": {
            "time": times,
            "vaccined": vaccined,
            "confirmed": confirmed,
            "deceased": deceased,
            "cured": cure
        }
    })


def getCountryInfection(country):
    time = datetime.date.today() - datetime.timedelta(days=179)
    times, confirmed, deceased, cure = [], [], [], []
    for i in range(0, 180):
        infData = dao.getInfMessage(country, time)
        times.append(time)
        confirmed.append(getattr(infData, 'totalNum'))
        deceased.append(getattr(infData, 'totalDead'))
        cure.append(getattr(infData, 'cured'))
        time = datetime.date.today() + datetime.timedelta(days=1)
    return jsonify({
        "name": country,
        "data": {
            "time": times,
            "confirmed": confirmed,
            "deceased": deceased,
            "cured": cure
        }
    })
