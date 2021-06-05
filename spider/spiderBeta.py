from bs4 import BeautifulSoup
import requests
import html
import re
import json
from database.static.table import *
from database.static.dao import clearTable
def updateCovidNews():
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
	}
	url = "https://www.baidu.com/s?ie=utf-8&medium=1&rtt=1&bsst=1&rsv_dl=news_t_sk&cl=2&wd=%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E+%E5%9B%BD%E5%A4%96&rn=50&tn=news&rsv_bp=1&rsv_sug3=1&oq=&rsv_btype=t&f=8&rsv_sug4=673"
	response = requests.get(url=url, headers=headers)
	soup = BeautifulSoup(response.text)
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
		title = news['tittle']
		href = news['href']
		info = news['info']
		source = news['source']
		updateTime = news['updateTime']
		imgUrl = news['imgUrl']
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
	soup = BeautifulSoup(response.text)
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
		title = news['tittle']
		href = news['href']
		info = news['info']
		source = news['source']
		updateTime = news['updateTime']
		imgUrl = news['imgUrl']
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
#def updateRiskList():




