from flask import jsonify
from database.static import dao
import datetime
from testcode.lq import testData

'''todayVacData = testData.vacdata[1]
yesVacData = testData.vacdata[0]
todayInfData = testData.infdata[1]
yesInfData = testData.infdata[0]'''


def getVaccinationMain(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayVacData = dao.getVacMessage(country, today.strftime("%Y-%m-%d"))
    yesVacData = dao.getVacMessage(country, yesterday.strftime("%Y-%m-%d"))
    return jsonify({
        "vaccined": {
            "today": {
                "name": country,
                "value": getattr(todayVacData, 'totalNum')
            },
            "yesterday": {
                "name": country,
                "value": getattr(yesVacData, 'totalNum')
            }
        },
        "coverage": {
            "today": {
                "name": country,
                "value": getattr(todayVacData, 'vacRate')
            },
            "yesterday": {
                "name": country,
                "value": getattr(yesVacData, 'vacRate')
            }
        }
    })


def getVaccinationTotalSidebar(country):
    today = datetime.date.today()
    todayVacData = dao.getVacMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayVacData, 'totalNum')
    })


def getVaccinationTotalAddSidebar(country):
    today = datetime.date.today()
    todayVacData = dao.getVacMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayVacData, 'addNum')
    })


def getVaccinationCovSidebar(country):
    today = datetime.date.today()
    todayVacData = dao.getVacMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayVacData, 'vacRate')
    })


def getVaccinationCovAddSidebar(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayVacData = dao.getVacMessage(country, today.strftime("%Y-%m-%d"))
    yesVacData = dao.getVacMessage(country, yesterday.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayVacData, 'vacRate') - getattr(yesVacData, 'vacRate')
    })


def getInfectionMain(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    yesInfData = dao.getInfMessage(country, yesterday.strftime("%Y-%m-%d"))
    return jsonify({
        "nowConfirmed": {
            "today": {
                "name": country,
                "value": getattr(todayInfData, 'currentNum')
            },
            "yesterday": {
                "name": country,
                "value": getattr(yesInfData, 'currentNum')
            }
        },
        "totalConfirmed": {
            "today": {
                "name": country,
                "value": getattr(todayInfData, 'totalNum')
            },
            "yesterday": {
                "name": country,
                "value": getattr(yesInfData, 'totalNum')
            }
        },
        "cured": {
            "today": {
                "name": country,
                "value": getattr(todayInfData, 'cured')
            },
            "yesterday": {
                "name": country,
                "value": getattr(yesInfData, 'cured')
            }
        },
        "death": {
            "today": {
                "name": country,
                "value": getattr(todayInfData, 'totalDead')
            },
            "yesterday": {
                "name": country,
                "value": getattr(yesInfData, 'totalDead')
            }
        },
    })


def getInfectionTotalSidebar(country):
    today = datetime.date.today()
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayInfData, 'totalNum')
    })


def getInfectionTotalAddSidebar(country):
    today = datetime.date.today()
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayInfData, 'addNum')
    })


def getInfectionDeadSidebar(country):
    today = datetime.date.today()
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayInfData, 'totalDead')
    })


def getInfectionDeadAddSidebar(country):
    today = datetime.date.today()
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayInfData, 'addDead')
    })


def getInfectionCureSidebar(country):
    today = datetime.date.today()
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayInfData, 'cured')
    })


def getInfectionCureAddSidebar(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayInfData = dao.getInfMessage(country, today.strftime("%Y-%m-%d"))
    yesInfData = dao.getInfMessage(country, yesterday.strftime("%Y-%m-%d"))
    return jsonify({
        "value": getattr(todayInfData, 'cure') - getattr(yesInfData, 'cure')
    })

