from flask import jsonify
from database.static import dao
import datetime
from testcode.lq import testData

todayVacData = testData.vacdata[1]
yesVacData = testData.vacdata[0]
todayInfData = testData.infdata[1]
yesInfData = testData.infdata[0]


def getVaccinationSidebar(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    '''todayVacData = dao.getVacMessage(country, today)
    yesVacData = dao.getVacMessage(country, yesterday)'''
    return jsonify({
        "vaccined": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayVacData, 'totalNum')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesVacData, 'totalNum')
            }
        },
        "coverage": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayVacData, 'vacRate')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesVacData, 'vacRate')
            }
        }
    })


def getInfectionSidebar(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    '''todayInfData = dao.getInfMessage(country, today)
    yesInfData = dao.getInfMessage(country, yesterday)'''
    return jsonify({
        "confirmed": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayInfData, 'totalNum')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesInfData, 'totalNum')
            }
        },
        "death": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayInfData, 'totalDead')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesInfData, 'totalDead')
            }
        },
        "cured": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayInfData, 'cured')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesInfData, 'cured')
            }
        }
    })


def getOtherSidebar():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    '''todayInfData = dao.getInfMessage('world', today)
    yesInfData = dao.getInfMessage('world', yesterday)
    todayVacData = dao.getVacMessage('world', today)
    yesVacData = dao.getVacMessage('world', yesterday)'''
    return jsonify({
        "vaccined": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayVacData, 'totalNum')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesVacData, 'totalNum')
            }
        },
        "confirmed": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayInfData, 'totalNum')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesInfData, 'totalNum')
            }
        },
        "cured": {
            "today": {
                "date": today.strftime("%Y-%m-%d"),
                "value": getattr(todayInfData, 'cured')
            },
            "yesterday": {
                "date": yesterday.strftime("%Y-%m-%d"),
                "value": getattr(yesInfData, 'cured')
            }
        }
    })
