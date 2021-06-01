from flask import jsonify
from database.static import dao


def getAllMassage(region):
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