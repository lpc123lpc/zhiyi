from spider import *

data=getJsonData(nowForeignCouDataUrl)
saveToJsonFile(data, "nowForeign.json")