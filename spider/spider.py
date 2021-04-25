import json
import requests
import pandas as pd
import time
#全球实时数据
nowGlobalDataUrl='https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'
#全球历史数据 从2020-01-28开始
hisGlobalDataUrl='https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'
#海外国家的实时数据
nowForeignCouDataUrl='https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
#中国国内全国、省份、地级市的实时数据
nowDomesticDataUrl='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
"""
模拟请求爬取网站相应数据,返回格式为json对象
@:param url: str类型，模拟请求
@:return json对象
"""
def getJsonData(url):
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
	}
	if url==nowGlobalDataUrl:
		r = requests.post(url, headers=headers)
		data_json = json.loads(r.text)
		data = data_json['data']
		nowGlobalStatics = data['FAutoGlobalStatis']
		return nowGlobalStatics
	elif url==hisGlobalDataUrl:
		r = requests.post(url, headers=headers)
		data_json = json.loads(r.text)
		data = data_json['data']
		hisGlobalStatics = data['FAutoGlobalDailyList']
		return hisGlobalStatics
	elif url==nowForeignCouDataUrl:
		r = requests.post(url, headers=headers)
		data_json = json.loads(r.text)
		nowForeignCountryData = data_json['data']
		return nowForeignCountryData
	elif url==nowDomesticDataUrl:
		r = requests.get(url, headers=headers)
		data_json = json.loads(r.text)
		Domesticdata = json.loads(data_json['data'])
		return Domesticdata
"""
将json对象写入文件中，文件路径为filePath
可以在notepad++中查看生成的json文件的格式来处理json对象
"""
def saveToJsonFile(jsonObj,filePath):
	with open(filePath,'w') as f:
		json.dump(jsonObj,f)