from spider.spider import *
from database.static.table import *
from database.static.dao import *

"""
data=getJsonData(hisGlobalDataUrl)
saveToJsonFile(data, "his.json")
"""


def getCSV():
   dictReader = getCSVDictReader(nowWorldVaccDataurl)
   print(dictReader.fieldnames)
   for row in dictReader:
      print(row)
      break

def SaveAdviceTest():
   saveAdvice("sbzzy", "2021-04-30")
   print("sace1 ok")
   saveAdvice("sbzzy2", "2021-04-30")
   print("save2 ok")

SaveAdviceTest()