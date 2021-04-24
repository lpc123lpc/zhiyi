from flask import jsonify
from database.static import dao
import datetime


def getMapVaccine(country):
    time = datetime.date.today()
    data = dao.getVacMessageInclude(country, time)
    vaccined, coverage = [], []
    for i in data:
        vaccined.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum')})
        coverage.append({"name": getattr(i, 'areaName'), "vacRate": getattr(i, 'vacRate')})
    return jsonify({
        "vaccined": vaccined,
        "coverage": coverage
    })


def getMapInfection(country):
    time = datetime.date.today()
    data = dao.getInfMessageInclude(country, time)
    nowConfirm, totalConfirm, cured, dead = [], [], [], []
    for i in data:
        nowConfirm.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'currentNum')})
        totalConfirm.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum')})
        cured.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'cured')})
        dead.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalDead')})
    return jsonify({
        "nowConfirm": nowConfirm,
        "totalConfirm": totalConfirm,
        "cured": cured,
        "dead": dead
        })



