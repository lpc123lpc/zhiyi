from flask import jsonify
from database.static import dao
from testcode.lq import testData

'''todayVacData = testData.vacdata[1]
yesVacData = testData.vacdata[0]
todayInfData = testData.infdata[1]
yesInfData = testData.infdata[0]'''


def getVaccinationTotalSidebar(country):
    todayVacData = dao.getNowVacMessage(country)
    if todayVacData is None:
        print(1)
        return jsonify({})
    return jsonify({
        "value": getattr(todayVacData, 'totalNum')
    })


def getVaccinationTotalAddSidebar(country):
    todayVacData = dao.getNowVacMessage(country)
    if todayVacData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayVacData, 'addNum')
    })


def getVaccinationCovSidebar(country):
    todayVacData = dao.getNowVacMessage(country)
    if todayVacData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayVacData, 'vacRate')
    })


def getInfectionTotalSidebar(country):
    todayInfData = dao.getNowInfMessage(country)
    if todayInfData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayInfData, 'totalNum')
    })


def getInfectionTotalAddSidebar(country):
    todayInfData = dao.getNowInfMessage(country)
    if todayInfData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayInfData, 'addNum')
    })


def getInfectionDeadSidebar(country):
    todayInfData = dao.getNowInfMessage(country)
    if todayInfData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayInfData, 'totalDead')
    })


def getInfectionDeadAddSidebar(country):
    todayInfData = dao.getNowInfMessage(country)
    if todayInfData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayInfData, 'addDead')
    })


def getInfectionCureSidebar(country):
    todayInfData = dao.getNowInfMessage(country)
    if todayInfData is None:
        return jsonify({})
    return jsonify({
        "value": getattr(todayInfData, 'cured')
    })
