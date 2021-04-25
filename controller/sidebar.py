from flask import jsonify
from database.static import dao
import datetime
import json


def getVaccinationSiderbar():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    vaccined, coverage = [], []
    todayData = dao.getVacMessage('world', today)
    yesData = dao.getVacMessage('world', yesterday)


