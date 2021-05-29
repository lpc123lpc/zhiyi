from database.static.table import *
from spider.covidSpider import *

'''
description:get vaccination institutions
city:city name
return:vaccination institutions of this city
'''

def getVacInstitutions(city):
    m = db.session.query(VacInstitution).filter(VacInstitution.city == city).all()
    return m