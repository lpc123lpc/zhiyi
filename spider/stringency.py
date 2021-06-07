import requests
import json
import datetime
from database.static.table import *
from database.static.dao import clearTable

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

today = datetime.date.today()
beginDay = today - datetime.timedelta(days=7)
# print(type(beginDay.__format__("%Y%Y%Y%Y-%m%m-%d%d")))
beginStr = beginDay.__format__("%Y-%m-%d")
endStr = today.__format__("%Y-%m-%d")
url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/" + beginStr + "/" + endStr
response = requests.get(url=url, headers=headers)

data = json.loads(response.text)
# print(data)

path = "testStrict.json"
with open(path, mode="w", encoding="utf-8") as f:
	json.dump(data, f)
# print("写入文件成功！")

data = data["data"]
# print(len(data))
latestDate = ""
# print(data)
for day in data:
	# print(day)
	if latestDate == "":
		latestDate = day
	elif latestDate < day:
		latestDate = day
	# latestDataDay=dataDay
	# latestDataDay=dataDay
latestDataDay = data[day]
# print(latestDataDay)

"""
country-codes-lat-long-alpha3.json 存储了各个国家的alpha3 country code与国家名称（英文）的对应关系
testStrict.json是对于爬取出的结果的序列化结果，存储为json文件，用于查看格式
latestDataDay是要存储的数据，存储了最新一天的国家政策严格性指数
参照country-codes-lat-long-alpha3.json 和 testStrict.json，以及国家中英文映射文件，
存储latestDataDay中内容到数据库中
有用的信息有： 国家名 数据对应的日期 严格性指数（stringency字段）
"""

