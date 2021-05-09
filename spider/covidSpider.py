import json
import requests
import pandas as pd
import time

from io import StringIO
import csv
import re
import datetime
from urllib import parse
import schedule

class Spider:
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}

	# 疫苗-ALL-ALL-数据
	# OurWorldInData
	worldVaccDataurl = 'https://covid.ourworldindata.org/data/vaccinations/vaccinations.csv'

	# 感染-全球-实时-数据
	# Tencent News
	nowGlobalCovidDataUrl = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'
	# 感染-全球-历史-数据 从2020-01-28开始
	# Tencent News
	hisGlobalCovidDataUrl = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'

	# 感染-海外国家-实时-数据
	# Tencent News
	nowForeignCovidDataUrl = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
	#  感染-中国、各省、市-实时-数据
	# Tencent News
	nowDomesticCovidDataUrl = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
	# 感染-国内各省、市-历史-数据
	# Tencent News
	provinceCityMapPath = './provinceCityMap.json'
	provinceCityUrlsPath = './provinceCityUrlsMap.json'

	# 感染-各国(包括中国)、主要国家的各行政区-历史-数据
	# JHU
	"""
	该数据源中包含中国的历史数据，但分成了China、Macao、Hongkong、Taiwan四块，注意处理
	返回网页csv文件的url列表
	@:return urls:类型 list
	"""

	@classmethod
	def getHisWorldCovidUrls(cls):

		prefix = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
		USPrefix="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"
		# 网页url
		url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
		USUrl='https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us'

		r = requests.get(url, headers=cls.headers)
		data = r.text
		#print(type(data))
		# print(data)
		reg = r'(?<=href=\"/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/).*\.csv(?=\">)'
		list = re.findall(reg, data)
		# print(type(list))
		urls = []
		for i in list:
			i = prefix + i
			urls.append(i)

		r = requests.get(USUrl, headers=cls.headers)
		data = r.text
		#print(type(data))
		# print(data)
		reg = r'(?<=href=\"/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports_us/).*\.csv(?=\">)'
		list = re.findall(reg, data)
		# print(type(list))
		USUrls = []
		for i in list:
			i = USPrefix + i
			USUrls.append(i)
		# print(urls)
		# print(len(urls))
		return urls,USUrls

	# 感染-各国(包括中国)、主要国家的各行政区-实时-数据
	"""
	返回假设数据源更新的条件下**昨天**和**当前日期**对应csv文件的url,**昨天**和**当前日期**美国对应csv文件的url
	@:return yesterdayUrl, todayUrl
	"""

	@classmethod
	def getUpdateCovidUrls(cls):
		urlPrefix = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
		USUrlPrefix="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"
		curTime = time.strftime("%m-%d-%Y", time.localtime())
		todayUrl = urlPrefix + curTime + ".csv"
		USTodayUrl= USUrlPrefix+curTime+".csv"

		today = datetime.date.today()
		oneday = datetime.timedelta(days=1)
		yesterday = (today - oneday).strftime('%m-%d-%Y')
		yesterdayUrl = urlPrefix + yesterday + ".csv"
		USYesterdayUrl=USUrlPrefix+yesterday+".csv"

		return yesterdayUrl, todayUrl, USYesterdayUrl,USTodayUrl

	# 国内省市的历史数据
	"""
	获取访问省、市数据的url，模拟访问省市历史数据的url
	"""

	@classmethod
	def getTencentProvinceCityUrl(cls, province, city=None):
		if city == None:
			url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province={0}&'.format(
				parse.quote(province))
		else:
			url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province={0}&city={1}&'.format(
				parse.quote(province), parse.quote(city))
		return url

	"""
	根据provinceCityMap.json（省市映射图）生成provinceCityUrlsMap.json
	@return: 生成provinceCityUrlsMap.json，用于具体省市与URL的映射
	"""

	@classmethod
	def gerUrlsMap(cls):
		provinceCityMapPath = './provinceCityMap.json'
		provinceCityUrlsPath = './provinceCityUrlsMap.json'
		with open(provinceCityMapPath, mode='r', encoding='utf-8') as f:
			locationsMap = json.load(f)
			# print(locationsMap)
			# print(type(locationsMap))
			for province in locationsMap:
				for city in locationsMap[province]:
					if city == 'self':
						url = cls.getTencentProvinceCityUrl(province)
					else:
						url = cls.getTencentProvinceCityUrl(province, city)
					locationsMap[province][city] = url

		print(locationsMap)
		with open(provinceCityUrlsPath, mode='w+', encoding='utf-8') as f:
			json.dump(locationsMap, f)

	"""
	根据provinceCityUrlsMap.json生成 json对象对应的python对象<class 'dict'>字典类型
	@:return <class 'dict'>，字典类型，可以直接通过saveToJson存储到json文件进行查看
	"""

	@classmethod
	def getProvinceCityJsonData(cls):
		provinceCityUrlsPath = './provinceCityUrlsMap.json'
		provinceCityJson = {}
		with open(provinceCityUrlsPath, mode='r', encoding='utf-8') as f:
			urlsMap = json.load(f)
			for province in urlsMap:
				if provinceCityJson.get(province) == None:
					provinceCityJson[province] = {}

				provinceJson = provinceCityJson[province]
				for city in urlsMap[province]:
					r = requests.get(urlsMap[province][city], headers=cls.headers)
					dataList = json.loads(r.text)['data']
					provinceJson[city] = dataList
		return provinceCityJson

	"""
	模拟请求爬取网站相应数据,返回格式为json对象
	@:param url: str类型，模拟请求
	@:return <class 'dict'>，字典类型，可以直接通过saveToJson存储到json文件进行查看
	"""

	@classmethod
	def getJsonData(cls, url):
		if url ==   cls.nowGlobalCovidDataUrl:
			r = requests.post(url, headers=cls.headers)
			data_json = json.loads(r.text)
			data = data_json['data']
			nowGlobalStatics = data['FAutoGlobalStatis']
			return nowGlobalStatics
		elif url == cls.hisGlobalCovidDataUrl:
			r = requests.post(url, headers=cls.headers)
			data_json = json.loads(r.text)
			data = data_json['data']
			hisGlobalStatics = data['FAutoGlobalDailyList']
			return hisGlobalStatics
		elif url == cls.nowForeignCovidDataUrl:
			r = requests.post(url, headers=cls.headers)
			data_json = json.loads(r.text)
			nowForeignCountryData = data_json['data']
			return nowForeignCountryData
		elif url == cls.nowDomesticCovidDataUrl:
			r = requests.get(url, headers=cls.headers)
			data_json = json.loads(r.text)
			Domesticdata = json.loads(data_json['data'])
			return Domesticdata

	"""
	将json对象写入文件中，文件路径为filePath
	可以在notepad++中查看生成的json文件的格式来处理json对象
	"""

	@classmethod
	def saveToJsonFile(cls, jsonObj, filePath):
		with open(filePath, 'w') as f:
			json.dump(jsonObj, f)

	"""
	如何使用dictReader ：
	print(dictReader.fieldnames)
	for row in dictReader:
		print(row)
	@:param url: 网页的csv文件
	@:return csv.DictReader
	"""

	@classmethod
	def getCSVDictReader(cls, url):
		r = requests.get(url, headers=cls.headers)
		data = r.text
		dataFile = StringIO(data)
		dictReader = csv.DictReader(dataFile)
		return dictReader

	@classmethod
	def getData(cls, idx):
		if idx == 0:
			# worldVaccDataurl，疫苗-ALL-ALL-数据
			# 返回csv.DictReader 类型
			return cls.getCSVDictReader(cls.worldVaccDataurl)
		elif idx == 1:
			# nowGlobalCovidDataUrl，# 感染-全球-实时-数据
			# 返回 dict 类型,可用saveToJson存储到json文件进行查看
			return cls.getJsonData(cls.nowGlobalCovidDataUrl)
		elif idx == 2:
			#   hisGlobalCovidDataUrl，# 感染-全球-历史-数据
			# 返回 dict 类型，可用saveToJson存储到json文件进行查看
			return cls.getJsonData(cls.hisGlobalCovidDataUrl)
		elif idx == 3:
			# nowForeignCovidDataUrl，# 感染-海外国家-实时-数据
			# 返回 dict 类型，可用saveToJson存储到json文件进行查看
			return cls.getJsonData(cls.nowForeignCovidDataUrl)
		elif idx == 4:
			# nowDomesticCovidDataUrl，#  感染-中国、各省、市-实时-数据
			# 返回 dict 类型，可用saveToJson存储到json文件进行查看
			return cls.getJsonData(cls.nowDomesticCovidDataUrl)
		elif idx == 5:
			# provinceCityUrlsPath，#感染-国内各省、市-历史-数据
			# 返回 dict 类型，可用saveToJson存储到json文件进行查看
			return cls.getProvinceCityJsonData()
		elif idx == 6:
			# 感染-各国(包括中国)、主要国家的各行政区-历史-数据
			# 返回url list，类型为list，存储了网页csv的urls，需要遍历用getCSVDictReader处理存储
			return cls.getHisWorldCovidUrls()
		elif idx == 7:
			# 感染-各国(包括中国)、主要国家的各行政区-实时-数据（判断是否存在）
			# 返回（yesterday url，today url），需要用getCSVDictReader处理存储，判断是否存在该url
			# 若不存在该url，返回的dictReader.fieldnames为 ['404: Not Found']
			return cls.getUpdateCovidUrls()
		elif idx==8:
			#感染-海外国家-历史-数据
			# 返回 dict 类型，可用saveToJson存储到json文件进行查看
			countriesUrlsMapPath = "./countriesUrlsMap.json"
			#countriesDataMapPath = "./countriesDataMap.json"
			headers = {
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
			}
			with open(countriesUrlsMapPath, mode='r', encoding='utf-8') as f:
				data = json.load(f)

			for item in data.keys():
				url = data[item]
				r = requests.post(url, headers=headers)
				data_list = json.loads(r.text)
				data_list = data_list['data']
				data[item] = data_list
			return data
			# time.sleep(10)
			#with open(countriesDataMapPath, mode='w', encoding='utf-8') as f:
			#	json.dump(data, f)
		# wit
		else:
			return None
		"""
		1.如何使用dictReader ：
		print(dictReader.fieldnames)
		for row in dictReader:
		print(row)
		可直接在浏览器中搜索相应url，即可下载
		2.如何使jsonData：
		1.可用saveToJson存储到json文件本地查看
		2.内存中是python的dict类型，可以当成字典进行操作
		"""
	@classmethod
	def importDataBasePackages(cls):
		from database.static.dao import updateChinaInf
		from database.static.dao import updateGlobalInf
		from database.static.dao import updateVac
		from database.static.dao import clearTable
		from database.static.dao import updateForeignProvinceInf
		from database.static.getInitData import Init
		pass
	@classmethod
	def updateTencentNews(cls):
		# 爬取、存入 nowGlobalCovidDataUrl，# 感染-全球-实时-数据
		# 爬取、存入 nowForeignCovidDataUrl，# 感染-海外国家-实时-数据
		# 爬取、存入 nowDomesticCovidDataUrl，#  感染-中国、各省、市-实时-数据
		#cls.importDataBasePackages()
		clearTable('nowInfMessages')
		updateChinaInf()
		updateGlobalInf()
		pass

	@classmethod
	def updateOWID(cls):
		# 爬取、存入 worldVaccDataurl，疫苗-ALL-ALL-数据 的实时数据
		#cls.importDataBasePackages()
		updateVac()
		pass

	@classmethod
	def updateJHU(cls):
		#cls.importDataBasePackages()
		updateForeignProvinceInf()
		# 爬取、存入 感染-各国(包括中国)、主要国家的各行政区-实时-数据（判断是否存在）
		pass

	@classmethod
	def crawlAndStoreHistory(cls):
		print(time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time())))
		cls.importDataBasePackages()
		cls.gerUrlsMap()
		# 爬取、存入  感染-全球-历史-数据
		# 爬取、存入  感染-国内各省、市-历史-数据
		# 爬取、存入  感染-各国(包括中国)、主要国家的各行政区-历史-数据
		# 爬取、存入  worldVaccDataurl，疫苗-ALL-ALL-数据中的历史数据
		Init()
		cls.timelyJob()
		print(time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time())))

	@classmethod
	def timelyJob(cls):
		#cls.importDataBasePackages()
		print(time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time())))
		cls.updateTencentNews()
		cls.updateOWID()
		cls.updateJHU()
		print(time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime(time.time())))



	@classmethod
	def jobTest(cls):
		import numpy
		print(datetime.datetime.now())
		print("the job is excuted in")
		print()
		print(time.localtime)
		time.sleep(3)
		print(datetime.datetime.now())
		print(numpy.array("100"))

if __name__=='__main__':
	#Spider.importDataBasePackages()
	from database.static.dao import updateChinaInf
	from database.static.dao import updateGlobalInf
	from database.static.dao import updateVac
	from database.static.dao import clearTable
	from database.static.dao import updateForeignProvinceInf
	from database.static.getInitData import Init


	schedule.every().day.at("09:00:00").do(job_func=Spider.timelyJob)
	while True:
		schedule.run_pending()
	"""yes,tod=Spider.getData(7)
	print(yes,tod)
	todayCsv=Spider.getCSVDictReader(tod)
	print(todayCsv.fieldnames)"""
