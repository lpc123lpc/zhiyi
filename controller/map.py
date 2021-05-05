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
        vaccined.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum')})
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
