from database.static.getInitData import getChinaHisInf
from database.static.modelTrain import getChinaCsv
from spider.covidSpider import *
from database.static.getInitData import *
from database.static.dao import *
from database.static.modelTrain import *
from database.static.search import *
from database.static.travelAdvice import *
from spider.spiderBeta import *

def getInf():
   data = Spider.getData(1)
   print(data)

def getCSV():
   dictReader = Spider.getData(0)
   for d in dictReader:
      print(d)


def SaveAdviceTest():
   saveAdvice("sbzzy", "2021-04-30")
   print("sace1 ok")
   saveAdvice("sbzzy2", "2021-04-30")
   print("save2 ok")

def getTodayInf():
   yesterdayUrl, todayUrl = Spider.getData(7)
   areaInf = Spider.getCSVDictReader(yesterdayUrl)
   for a in areaInf:
      print(a)

def getChinaHisInfTest():
   getChinaHisInf()

def getCountryHisTest():
   data = Spider.getData(8)
   Spider.saveToJsonFile(data, 'country.json')

#clearTable('nowInfMessages')
#db.drop_all()
#db.create_all()
#getNewArea()

updateStringency()
print(5)
updateVaccineInstitutions()
print(6)