from flask import jsonify
from database.static import dao


def getMapVaccine(country):
    a = 1.0
    if country == 'global':
        a = 10000.0
    data = dao.getNowVacMessageInclude(country)
    vaccined, coverage = [], []
    if data is None:
        return jsonify({})
    for i in data:
        vaccined.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum') / a})
        coverage.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'vacRate')})
    return jsonify({
        "vaccined": vaccined,
        "coverage": coverage
    })


def getMapInfection(country):
    a = 1.0
    if country == 'global':
        a = 10000.0
    data = dao.getNowInfMessageInclude(country)
    nowConfirm, totalConfirm, cured, dead, couverage = [], [], [], [], []
    if data is None:
        return jsonify({})
    for i in data:
        nowConfirm.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'currentNum') / a})
        totalConfirm.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalNum') / a})
        cured.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'cured') / a})
        dead.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'totalDead') / a})
        couverage.append({"name": getattr(i, 'areaName'), "value": getattr(i, 'infRate')})
    return jsonify({
        "nowConfirm": nowConfirm,
        "totalConfirm": totalConfirm,
        "cured": cured,
        "dead": dead
    })
