from database.static.table import *
from spider.covidSpider import *

'''
description:get infection news
number:the amount of infection news required
return:infection news
'''

def getInfNews(number):
    m = db.session.query(InfNews).order_by(InfNews.time.desc()).limit(number).all()
    return m


'''
description:get vaccine news
number:the amount of vaccine news required
return:vaccine news
'''

def getVacNews(number):
    m = db.session.query(VacNews).order_by(VacNews.time.desc()).limit(number).all()
    return m