from spider.spider import *
from database.static.table import *
from database.static.dao import *

"""
data=getJsonData(hisGlobalDataUrl)
saveToJsonFile(data, "his.json")
"""

message = getInfMessage('美国', '2021-04-29')
print(message)