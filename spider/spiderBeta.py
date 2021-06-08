
from bs4 import BeautifulSoup
import requests

import hashlib

import json
import datetime
from urllib import parse
from database.static.table import *
from database.static.dao import clearTable


def updateCovidNews():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}
	url = "https://www.baidu.com/s?ie=utf-8&medium=1&rtt=1&bsst=1&rsv_dl=news_t_sk&cl=2&wd=%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E+%E5%9B%BD%E5%A4%96&rn=50&tn=news&rsv_bp=1&rsv_sug3=1&oq=&rsv_btype=t&f=8&rsv_sug4=673"
	response = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(response.text, features="lxml")
	items = soup.find_all("div", class_="result-op c-container xpath-log new-pmd")

	dataInDict = {}
	"""
	index: 
	tittle: 
	href: 
	info: 
	source:
	updateTime:
	imgUrl:
	"""
	cnt = 0
	for index, item in enumerate(items):
		dataItem = {}
		print(index)
		if (len(item.find_all("div", class_="c-span3 img-margin-bottom_BzjMI")) != 0):
			print("有图像！")
			cnt += 1
			itemHeader = item.div.h3.a
			title = "".join(list(itemHeader.strings))
			dataItem["title"] = title
			dataItem["href"] = itemHeader["href"]
			itemContent = item.div.div.contents
			itemSourceTimeBody = itemContent[1].div
			info = "".join(list(itemContent[1].contents[1].strings))
			dataItem["info"] = info
			mgsSources = itemSourceTimeBody.find_all("span")
			for sourceInfo in mgsSources:
				if sourceInfo["class"][0] == "c-color-gray":
					source = sourceInfo.string
					dataItem["source"] = source
				elif sourceInfo["class"][0] == "c-color-gray2":
					updateTime = sourceInfo.string
					dataItem["updateTime"] = updateTime
			"""source=itemSourceTimeBody.find_all("span")[0].string
			dataItem["source"]=source
			updateTime=itemSourceTimeBody.find_all("span")[1].string
			dataItem["updateTime"]=updateTime"""
			imgUrl = itemContent[0].find("img")["src"]
			dataItem["imgUrl"] = imgUrl

			dataInDict[cnt] = dataItem
			"""else:
			print("没有图像！")
			#if index==6:
			#    print(item.prettify())
			itemHeader=item.div.h3.a
			title="".join(list(itemHeader.strings))
			dataItem["title"]=title
			dataItem["href"]=itemHeader["href"]
			itemBody=item.div.div.div.contents
			info="".join(list(itemBody[1].strings))
			dataItem["info"]=info
			itemSourceTimeBody=itemBody[0]
			mgsSources=itemSourceTimeBody.find_all("span")
			for sourceInfo in mgsSources:
				if sourceInfo["class"][0]=="c-color-gray":
					source=sourceInfo.string
					dataItem["source"]=source
				elif  sourceInfo["class"][0]=="c-color-gray2":
					updateTime=sourceInfo.string
					dataItem["updateTime"]=updateTime"""
			"""   
			source=itemSourceTimeBody.find_all("span")[0].string
			dataItem["source"]=source
			updateTime=itemSourceTimeBody.find_all("span")[1].string
			dataItem["updateTime"]=updateTime"""

		print(index)
		if cnt >= 20:
			break

	clearTable("infNews")

	for index, news in dataInDict.items():
		title = news['title']
		href = news['href']
		info = news['info']
		source = news['source']
		updateTime = news['updateTime']
		imgUrl = news['imgUrl']
		print(news)
		x = InfNews(time=updateTime,
		            title=title,
		            urls=href,
		            source=source,
		            abstracts=info,
		            picUrls=imgUrl)
		add(x)

	"""print(dataInDict)
	path = "baiduNewsDemo.json"
	with open(path, mode="w", encoding="utf-8") as f:
		json.dump(dataInDict, f)
		print("写入文件成功！")"""


def updateVaccineNews():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}
	url = "https://www.baidu.com/s?ie=utf-8&medium=1&rtt=1&bsst=1&rsv_dl=news_t_sk&cl=2&wd=%E6%96%B0%E5%86%A0%E7%96%AB%E8%8B%97+%E5%85%A8%E7%90%83&rn=50&tn=news&rsv_bp=1&rsv_sug3=15&rsv_sug1=9&rsv_sug7=100&oq=&rsv_sug2=0&rsv_btype=t&f=8&inputT=25794&rsv_sug4=25941"
	response = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(response.text, features="lxml")
	items = soup.find_all("div", class_="result-op c-container xpath-log new-pmd")

	dataInDict = {}
	"""
	index: 
	tittle: 
	href: 
	info: 
	source:
	updateTime:
	imgUrl:
	"""
	cnt = 0
	for index, item in enumerate(items):
		dataItem = {}
		print(index)
		if (len(item.find_all("div", class_="c-span3 img-margin-bottom_BzjMI")) != 0):
			print("有图像！")
			cnt += 1
			itemHeader = item.div.h3.a
			title = "".join(list(itemHeader.strings))
			dataItem["title"] = title
			dataItem["href"] = itemHeader["href"]
			itemContent = item.div.div.contents
			itemSourceTimeBody = itemContent[1].div
			info = "".join(list(itemContent[1].contents[1].strings))
			dataItem["info"] = info
			mgsSources = itemSourceTimeBody.find_all("span")
			for sourceInfo in mgsSources:
				if sourceInfo["class"][0] == "c-color-gray":
					source = sourceInfo.string
					dataItem["source"] = source
				elif sourceInfo["class"][0] == "c-color-gray2":
					updateTime = sourceInfo.string
					dataItem["updateTime"] = updateTime
			"""source=itemSourceTimeBody.find_all("span")[0].string
			dataItem["source"]=source
			updateTime=itemSourceTimeBody.find_all("span")[1].string
			dataItem["updateTime"]=updateTime"""
			imgUrl = itemContent[0].find("img")["src"]
			dataItem["imgUrl"] = imgUrl

			dataInDict[cnt] = dataItem
			"""else:
			print("没有图像！")
			#if index==6:
			#    print(item.prettify())
			itemHeader=item.div.h3.a
			title="".join(list(itemHeader.strings))
			dataItem["title"]=title
			dataItem["href"]=itemHeader["href"]
			itemBody=item.div.div.div.contents
			info="".join(list(itemBody[1].strings))
			dataItem["info"]=info
			itemSourceTimeBody=itemBody[0]
			mgsSources=itemSourceTimeBody.find_all("span")
			for sourceInfo in mgsSources:
				if sourceInfo["class"][0]=="c-color-gray":
					source=sourceInfo.string
					dataItem["source"]=source
				elif  sourceInfo["class"][0]=="c-color-gray2":
					updateTime=sourceInfo.string
					dataItem["updateTime"]=updateTime"""
			"""   
			source=itemSourceTimeBody.find_all("span")[0].string
			dataItem["source"]=source
			updateTime=itemSourceTimeBody.find_all("span")[1].string
			dataItem["updateTime"]=updateTime"""

		print(index)
		if cnt >= 20:
			break

	clearTable("vacNews")

	for index, news in dataInDict.items():
		title = news['title']
		href = news['href']
		info = news['info']
		source = news['source']
		updateTime = news['updateTime']
		imgUrl = news['imgUrl']
		print(news)
		x = VacNews(time=updateTime,
		            title=title,
		            urls=href,
		            source=source,
		            abstracts=info,
		            picUrls=imgUrl)
		add(x)

	"""print(dataInDict)
	path = "baiduNewsDemo.json"
	with open(path, mode="w", encoding="utf-8") as f:
		json.dump(dataInDict, f)
		print("写入文件成功！")"""


def updateRiskList():
	header = {}
	body = {}
	timestamp = int(datetime.datetime.now().timestamp())
	url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"
	STATE_COUNCIL_SIGNATURE_KEY = "fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA"
	STATE_COUNCIL_X_WIF_NONCE = "QkjjtiLM2dCratiA"
	STATE_COUNCIL_X_WIF_PAASID = "smt-application"

	STATE_COUNCIL_APP_ID = "NcApplication"
	STATE_COUNCIL_PASSID = "zdww"
	STATE_COUNCIL_NONCE = "123456789abcdefg"
	STATE_COUNCIL_TOEKN = "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA"
	STATE_COUNCIL_KEY = "3C502C97ABDA40D0A60FBEE50FAAD1DA"
	signatureStr = str(timestamp) + STATE_COUNCIL_SIGNATURE_KEY + str(timestamp)
	signature = hashlib.sha256(signatureStr.encode('utf-8')).hexdigest().upper()
	header["x-wif-nonce"] = STATE_COUNCIL_X_WIF_NONCE
	header["x-wif-paasid"] = STATE_COUNCIL_X_WIF_PAASID
	header["x-wif-signature"] = signature
	header["x-wif-timestamp"] = str(timestamp)
	header[
		"user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
	body["appId"] = STATE_COUNCIL_APP_ID
	body["paasHeader"] = STATE_COUNCIL_PASSID
	body["timestampHeader"] = timestamp
	body["nonceHeader"] = STATE_COUNCIL_NONCE
	signatureStr = str(timestamp) + STATE_COUNCIL_TOEKN + STATE_COUNCIL_NONCE + str(timestamp)
	signatureHeader = hashlib.sha256(signatureStr.encode('utf-8')).hexdigest().upper()
	body["signatureHeader"] = signatureHeader
	body["key"] = STATE_COUNCIL_KEY
	response = requests.post(url, json=body, headers=header)
	# print(response.text)
	data = json.loads(response.text)
	data = data["data"]
	highlist = data["highlist"]
	middlelist = data["middlelist"]

	clearTable('riskAreas')
	with open('../spider/city-map.json', mode='r', encoding='utf-8') as f:
		cityMap = json.load(f)
	with open('../spider/rankListProcess.json', mode='r', encoding='utf-8') as f:
		provinceMap = json.load(f)

	for item in highlist:
		print(item)
		province = item["province"]
		province = provinceMap[province]
		city = item["city"]
		cities=cityMap[province]
		if province == "海南" or province == "湖北" or province == "河南" or province == "新疆":
			if cities.get(city)==None:
				cities=cities["省直辖县级行政单位"]
				city=cities[city]
			else:
				city=cities[city]
		else:
			city=cities[city]
		county = item["county"]
		for community in item["communitys"]:
			x = RiskArea(province=province,
			             city=city,
			             childArea=county,
			             level=2,
			             abstract=community)
			add(x)
	for item in middlelist:
		print(item)
		province = item["province"]
		province = provinceMap[province]
		city = item["city"]
		cities = cityMap[province]
		if province == "海南" or province == "湖北" or province == "河南" or province == "新疆":
			if cities.get(city) == None:
				county=item["county"]
				city = cities[county]
			else:
				city = cities[city]
		else:
			city = cities[city]
		county = item["county"]
		for community in item["communitys"]:
			x = RiskArea(province=province,
			             city=city,
			             childArea=county,
			             level=2,
			             abstract=community)
			add(x)

	"""print(data)
	with open('riskList.json', 'w') as f:
		json.dump(data, f)"""


def updateStringency():
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

	path = "../spider/testStrict.json"
	with open(path, mode="w", encoding="utf-8") as f:
		json.dump(data, f)
	# print("写入文件成功！")

	countries = data['countries']

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
	latestDataDay = data[latestDate]
	print(latestDataDay)

	"""
	country-codes-lat-long-alpha3.json 存储了各个国家的alpha3 country code与国家名称（英文）的对应关系
	testStrict.json是对于爬取出的结果的序列化结果，存储为json文件，用于查看格式
	latestDataDay是要存储的数据，存储了最新一天的国家政策严格性指数
	参照country-codes-lat-long-alpha3.json 和 testStrict.json，以及国家中英文映射文件，
	存储latestDataDay中内容到数据库中
	有用的信息有： 国家名 数据对应的日期 严格性指数（stringency字段）
	"""

	clearTable('policyStrict')
	with open('../spider//world-mapping-policy.json', mode='r', encoding='utf-8') as f:
		worldMapping = json.load(f)
		with open('../spider/country-codes-lat-long-alpha3.json', mode='r', encoding='utf-8') as c:
			countryAlpha3 = json.load(c)["ref_country_codes"]
			cAlpha3Mapping = {}
			for country in countryAlpha3:
				cAlpha3Mapping[country['alpha3']] = country['country']
			for country in countries:
				try:
					countryName = worldMapping[cAlpha3Mapping[country]]['cn']
					p = PolicyStrict(countryName=countryName, strictIndex=latestDataDay[country]['stringency'],
									 date=latestDataDay[country]['date_value'])
					add(p)
				except Exception as e:
					print(latestDataDay[country])
					try:
						print(cAlpha3Mapping[country])
					except Exception as ex:
						print(country)


def insertVaccineInstitutionsFile():
	pass


def insertVaccineInstitutionsTencent():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
		'Accept': 'application/json, text/plain, */*',
		'Referer': 'https://new.qq.com/'
	}
	with open('../spider/city-map.json', mode='r', encoding='utf-8') as f:
		cityMap = json.load(f)
	with open('../spider/rankListProcess.json', mode='r', encoding='utf-8') as f:
		provinceMap = json.load(f)
	provinces = ["北京", "天津", "河北", "内蒙古", "辽宁", "上海", "浙江", "安徽", "福建",
	           "山东", "河南", "湖北", "湖南", "广东", "广西", "四川", "云南", "陕西"]
	for province in provinces:
		# %E5%A4%A9%E6%B4%A5
		if province=="北京" or province=="天津" or province=="上海"or province=="重庆":
			region=province
			url = "https://apis.map.qq.com/place_cloud/search/region?region=" + parse.quote(
				region) + "&key=ZTCBZ-M6FWU-DFTVG-2HCU2-OM7SV-2LBCF&orderby=distance(39.90387,116.389893)&table_id=5fed45b33fc08460dcadf521&page_size=20&page_index=1"
			response = requests.get(url=url, headers=headers)
			data = json.loads(response.text)
			data = data["result"]["data"]
			if len(data) == 0:
				pass
			else:
				for item in data:
					district=item["district"]
					cities=cityMap[province]
					district=cities[district]
					name = item["title"]
					addr = item["address"]
					tel = item["tel"]
					if tel == "":
						tel = "暂未公布"
					x = VacInstitution(
						city=district,
						name=name,
						addr=addr,
						tel=tel
					)
					add(x)

		else :
			cities=cityMap[province]
			for city in cities:
				city=cities[city]
				if city=="济源示范区":
					city="济源"
				region=province+","+city
				url="https://apis.map.qq.com/place_cloud/search/region?region=" + parse.quote(
			region) + "&key=ZTCBZ-M6FWU-DFTVG-2HCU2-OM7SV-2LBCF&orderby=distance(39.90387,116.389893)&table_id=5fed45b33fc08460dcadf521&page_size=20&page_index=1"
				response = requests.get(url=url, headers=headers)
				data = json.loads(response.text)
				#print(region)
				if data["status"]!=0:
					print("ERROR: "+region)
					continue

				data = data["result"]["data"]
				if len(data)==0:
					pass
				else:
					for item in data:
						#print(item)
						name = item["title"]
						addr = item["address"]
						tel = item["tel"]
						if tel == "":
							tel = "暂未公布"
						x = VacInstitution(
							city=city,
							name=name,
							addr=addr,
							tel=tel
						)
						add(x)

def updateVaccineInstitutions():
	clearTable('vacInstitutions')
	insertVaccineInstitutionsTencent()
	insertVaccineInstitutionsFile()


if __name__ == '__main__':
	#updateCovidNews()
	#updateVaccineNews()
	#updateRiskList()
	#updateVaccineInstitutions()
	updateStringency()

# def updateRiskList():
