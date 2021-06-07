from flask import jsonify
from database.static import dao


def getRegion(region):
    places = region.splite(str="  ")
    return places[len(places) - 1]


def getAllMassage(oriRegion):
    region = getRegion(oriRegion)
    vacData = dao.getNowVacMessage(region)
    infData = dao.getNowInfMessage(region)
    return jsonify({
        "infect": {
            "nowConfirm": getattr(infData, "currentNum"),
            "totalConfirm": getattr(infData, "totalNum"),
            "cured": getattr(infData, "cured"),
            "dead": getattr(infData, "totalDead"),
            "coverage": getattr(infData, "infRate")
        },
        "vaccine": {
            "vaccined": getattr(vacData, "totalNum"),
            "coverage": getattr(vacData, "vacRate")
        }
    })
