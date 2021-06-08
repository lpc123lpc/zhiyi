from flask import jsonify
from database.static import dao


def getRegion(region):
    places = region.split("  ")
    return places[len(places) - 1]


def getAllMassage(oriRegion):
    region = getRegion(oriRegion)
    vacData = dao.getNowVacMessage(region)
    infData = dao.getNowInfMessage(region)
    if vacData is None:
        return jsonify({
            "infect": {
                "nowConfirm": getattr(infData, "currentNum"),
                "totalConfirm": getattr(infData, "totalNum"),
                "cured": getattr(infData, "cured"),
                "dead": getattr(infData, "totalDead"),
                "coverage": getattr(infData, "infRate")
            },
            "vaccine": {
                "vaccined": -1,
                "coverage": -1
            }
        })
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
