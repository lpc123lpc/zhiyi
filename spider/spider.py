import json
import requests
import pandas as pd
import time
import datetime
from io import StringIO
import csv
import re
import datetime

# 全球历史感染数据 从2020-01-28开始
hisGlobalCovidDataUrl = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'
# 各国历史疫苗数据
hisWorldVaccDataurl = 'https://covid.ourworldindata.org/data/vaccinations/vaccinations.csv'

# source: tencent
# 全球实时感染数据
nowGlobalCovidDataUrl = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'
# 海外国家的实时感染数据
nowForeignCovidDataUrl = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# 中国国内全国、省份、地级市的实时感染数据
nowDomesticCovidDataUrl = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'

"""
模拟请求爬取网站相应数据,返回格式为json对象
@:param url: str类型，模拟请求
@:return <class 'dict'>，字典类型，可以直接通过saveToJson存储到json文件进行查看
"""
def getJsonData(url):
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
	}
	if url == nowGlobalCovidDataUrl:
		r = requests.post(url, headers=headers)
		data_json = json.loads(r.text)
		data = data_json['data']
		nowGlobalStatics = data['FAutoGlobalStatis']
		return nowGlobalStatics
	elif url == hisGlobalCovidDataUrl:
		r = requests.post(url, headers=headers)
		data_json = json.loads(r.text)
		data = data_json['data']
		hisGlobalStatics = data['FAutoGlobalDailyList']
		return hisGlobalStatics
	elif url == nowForeignCovidDataUrl:
		r = requests.post(url, headers=headers)
		data_json = json.loads(r.text)
		nowForeignCountryData = data_json['data']
		return nowForeignCountryData
	elif url == nowDomesticCovidDataUrl:
		r = requests.get(url, headers=headers)
		data_json = json.loads(r.text)
		Domesticdata = json.loads(data_json['data'])
		return Domesticdata


"""
将json对象写入文件中，文件路径为filePath
可以在notepad++中查看生成的json文件的格式来处理json对象
"""


def saveToJsonFile(jsonObj, filePath):
	with open(filePath, 'w') as f:
		json.dump(jsonObj, f)





#国内省市的历史数据
"""
获取访问省、市数据的url，模拟访问省市历史数据的url
"""
def getTencentProvinceCityUrl(province,city=None):
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    if city==None:
        url='https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province={0}&'.format(parse.quote(province))
    else:
        url='https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province={0}&city={1}&'.format(parse.quote(province),parse.quote(city))
    return url
"""
根据provinceCityMap.json（省市映射图）生成provinceCityUrlsMap.json
@return: 生成provinceCityUrlsMap.json，用于具体省市与URL的映射
"""
def gerUrlsMap():
    provinceCityMapPath='./provinceCityMap.json'
    provinceCityUrlsPath='./provinceCityUrlsMap.json'
    with open(provinceCityMapPath,mode='r',encoding='utf-8') as f:
        locationsMap=json.load(f)
        #print(locationsMap)
        #print(type(locationsMap))
        for province in locationsMap:
            for city in locationsMap[province]:
                if city=='self':
                    url=getTencentProvinceCityUrl(province)
                else:
                    url=getTencentProvinceCityUrl(province,city)
                locationsMap[province][city]=url

    print(locationsMap)
    with open(provinceCityUrlsPath,mode='w+',encoding='utf-8') as f:
        json.dump(locationsMap,f)

"""
根据provinceCityUrlsMap.json生成 json对象对应的python对象<class 'dict'>字典类型
@:return <class 'dict'>，字典类型，可以直接通过saveToJson存储到json文件进行查看
"""
def getProvinceCityJsonData():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
	}
	provinceCityUrlsPath = './provinceCityUrlsMap.json'
	provinceCityJson = {}
	with open(provinceCityUrlsPath, mode='r', encoding='utf-8') as f:
		urlsMap = json.load(f)
		for province in urlsMap:
			if provinceCityJson.get(province) == None:
				provinceCityJson[province] = {}

			provinceJson = provinceCityJson[province]
			for city in urlsMap[province]:
				r = requests.get(urlsMap[province][city], headers=headers)
				dataList = json.loads(r.text)['data']
				provinceJson[city] = dataList
	return provinceCityJson

# 各国历史、主要国家的行政区的历史感染数据
# JHU
"""
返回网页url目录下所有csv文件的链接
@:return urls:类型 list,返回网页csv文件的url
"""
def getHisWorldCovidUrls():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}
	prefix = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
	# 网页url
	url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
	r = requests.get(url, headers=headers)
	data = r.text
	print(type(data))
	# print(data)
	reg = r'(?<=href=\"/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/).*\.csv(?=\">)'
	list = re.findall(reg, data)
	# print(type(list))
	urls = []
	for i in list:
		i = prefix + i
		urls.append(i)
	# print(urls)
	# print(len(urls))
	return urls


"""
返回昨天和当前日期对应文件的url，达到更新的目的
@:return yesterdayUrl, todayUrl,返回假设数据源更新的条件下昨天和当前日期对应csv文件的url
下一步是将csv文件对应的url放入getCSVDictReader中获取csv.DictReader获取数据
"""
def getUpdateCovidUrls():
	urlPrefix = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
	curTime = time.strftime("%m-%d-%Y", time.localtime())
	todayUrl = urlPrefix + curTime + ".csv"

	today = datetime.date.today()
	oneday = datetime.timedelta(days=1)
	yesterday = (today - oneday).strftime('%m-%d-%Y')
	yesterdayUrl = urlPrefix + yesterday + ".csv"
	return yesterdayUrl, todayUrl


# OurWorldInData
# 各国实时疫苗数据
nowWorldVaccDataurl = 'https://covid.ourworldindata.org/data/vaccinations/vaccinations.csv'
"""
如何使用dictReader ：
print(dictReader.fieldnames)
for row in dictReader:
    print(row)
@:param url: 网页的csv文件
@:return csv.DictReader
"""


def getCSVDictReader(url):
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}
	r = requests.get(url, headers=headers)
	data = r.text
	dataFile = StringIO(data)
	dictReader = csv.DictReader(dataFile)
	return dictReader
