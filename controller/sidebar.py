from flask import jsonify
from database.static import dao
import datetime


def getVaccinationSidebar(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayData = dao.getVacMessage(country, today)
    yesData = dao.getVacMessage(country, yesterday)
    return jsonify({
        "vaccined": {
            {
                "date": today,
                "value": getattr(todayData, 'totalNum')
            },
            {
                "date": yesterday,
                "value": getattr(yesData, 'totalNum')
            }
        },
        "coverage": {
            {
                "date": today,
                "value": getattr(todayData, 'vacRate')
            },
            {
                "date": yesterday,
                "value": getattr(yesData, 'vacRate')
            }
        }
    })


def getInfectionSidebar(country):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayData = dao.getInfMessage(country, today)
    yesData = dao.getInfMessage(country, yesterday)
    return jsonify({
        "confirmed": {
            {
                "date": today,
                "value": getattr(todayData, 'totalNum')
            },
            {
                "date": yesterday,
                "value": getattr(yesData, 'totalNum')
            }
        },
        "death": {
            {
                "date": today,
                "value": getattr(todayData, 'totalDead')
            },
            {
                "date": yesterday,
                "value": getattr(yesData, 'totalDead')
            }
        },
        "cured": {
            {
                "date": today,
                "value": getattr(todayData, 'cured')
            },
            {
                "date": yesterday,
                "value": getattr(yesData, 'cured')
            }
        }
    })


def getOtherSidebar():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    todayInfData = dao.getInfMessage('world', today)
    yesInfData = dao.getInfMessage('world', yesterday)
    todayVacData = dao.getVacMessage('world', today)
    yesVacData = dao.getVacMessage('world', yesterday)
    return jsonify({
        "vaccined": {
            {
                "date": today,
                "value": getattr(todayVacData, 'totalNum')
            },
            {
                "date": yesterday,
                "value": getattr(yesVacData, 'totalNum')
            }
        },
        "confirmed": {
            {
                "date": today,
                "value": getattr(todayInfData, 'totalNum')
            },
            {
                "date": yesterday,
                "value": getattr(yesInfData, 'totalNum')
            }
        },
        "cured": {
            {
                "date": today,
                "value": getattr(todayInfData, 'cured')
            },
            {
                "date": yesterday,
                "value": getattr(yesInfData, 'cured')
            }
        }
    })
