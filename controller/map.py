from flask import jsonify
from database.static import dao
import datetime
from testcode.lq import testData

'''vacdata = testData.vacdata
infdata = testData.infdata'''


def getMapVaccine(country):
    data = dao.getNowVacMessageInclude(country)
    vaccined, coverage = [], []
    if data is None:
        return jsonify({})
    for i in data:
        vaccined.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum') / 10000.0})
        coverage.append({"name": getattr(i, 'areaName'), "vacRate": getattr(i, 'vacRate')})
    return jsonify({
        "vaccined": vaccined,
        "coverage": coverage
    })


def getMapInfection(country):
    data = dao.getNowInfMessageInclude(country)
    nowConfirm, totalConfirm, cured, dead = [], [], [], []
    if data is None:
        return jsonify({})
    for i in data:
        nowConfirm.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'currentNum') / 10000.0})
        totalConfirm.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum') / 10000.0})
        cured.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'cured') / 10000.0})
        dead.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalDead') / 10000.0})
    return jsonify({
        "nowConfirm": nowConfirm,
        "totalConfirm": totalConfirm,
        "cured": cured,
        "dead": dead
    })
