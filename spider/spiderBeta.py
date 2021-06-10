import numpy as np
from bs4 import BeautifulSoup
import requests

import hashlib

import json
import datetime
from urllib import parse
from database.static.table import *
from database.static.dao import clearTable
from spider.xlsxParserClass import xlsxParser
import pandas as pd

def getAbsTime(deltaStr:str):
    pass
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
    with open('spider/city-map.json', mode='r', encoding='utf-8') as f:
        cityMap = json.load(f)
    with open('spider/rankListProcess.json', mode='r', encoding='utf-8') as f:
        provinceMap = json.load(f)

    for item in highlist:
        print(item)
        province = item["province"]
        province = provinceMap[province]
        city = item["city"]
        cities = cityMap[province]
        if province == "海南" or province == "湖北" or province == "河南" or province == "新疆":
            if cities.get(city) == None:
                cities = cities["省直辖县级行政单位"]
                city = cities[city]
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
    for item in middlelist:
        print(item)
        province = item["province"]
        province = provinceMap[province]
        city = item["city"]
        cities = cityMap[province]
        if province == "海南" or province == "湖北" or province == "河南" or province == "新疆":
            if cities.get(city) == None:
                county = item["county"]
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
                         level=1,
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

    path = "spider/testStrict.json"
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
    with open('spider/world-mapping-policy.json', mode='r', encoding='utf-8') as f:
        worldMapping = json.load(f)
        with open('spider/country-codes-lat-long-alpha3.json', mode='r', encoding='utf-8') as c:
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
    """
    完成xlsx的数据处理与存储： 1. 贵州省1，2
                           2. 海南省
                           3. 黑龙江省
                           4. 江苏省
                           5. 江西省
                           6. 山西省
                           7. 重庆市
    :return:
    """
    insertVaccineInstitutionsChongqing()
    insertVaccineInstitutionsGuizhou()
    insertVaccineInstitutionsHainan()
    insertVaccineInstitutionsHeilongjiang()
    insertVaccineInstitutionsJiangsu()
    insertVaccineInstitutionsJiangxi()
    insertVaccineInstitutionsShanxi()

def insertVaccineInstitutionsChongqing():
    print("正在存储重庆市疫苗接种点信息......")
    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    ChongqingPath = r"spider/vaccinationLocations/重庆市-新冠疫苗接种点名单.xlsx"
    data = pd.read_excel(ChongqingPath, engine="openpyxl")
    province = "重庆"
    # districts={}
    districts = manualCityMap[province]
    for index, row in data.iterrows():
        district = row[1]
        if pd.isna(district) or district == None:
            continue
        elif districts.get(district) == None:
            continue
        else:
            district = districts[district]
        # districts[district]=index
        name = row[2]
        addr = row[3]
        if pd.isna(addr):
            addr = ""
        tel = row[4]
        if pd.isna(tel):
            tel = ""
        if tel == None or pd.isna(tel) or tel == "" or tel == "——":
            tel = "暂未公布"
        x = VacInstitution(
            city=district,
            name=name,
            addr=addr,
            tel=tel
        )
        add(x)
    # print(districts)
    print("重庆市疫苗接种点信息存储完毕！")


def insertVaccineInstitutionsGuizhou():
    print("正在存储贵州省疫苗接种点信息......")
    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    GuizhouPath = r"spider/vaccinationLocations/贵州省新冠肺炎疫苗固定接种点一览表（1839个）.xlsx"
    GuizhouParser = xlsxParser(GuizhouPath)
    GuizhouParser.displayConfig()
    GuizhouParser.setMaxRowCol(1842, 7)
    province = "贵州"
    # cities={}
    cities = manualCityMap[province]
    for row in range(4, GuizhouParser.max_row + 1):
        for col in range(1, GuizhouParser.max_col + 1):
            if col == 2:
                city = GuizhouParser.getValue(row, col)
                city = cities[city]
            elif col == 4:
                name = GuizhouParser.getValue(row, col)
            elif col == 5:
                addr = GuizhouParser.getValue(row, col)
            elif col == 7:
                tel = GuizhouParser.getValue(row, col)
                if tel == "" or tel == None:
                    tel = "暂未公布"
        # print(city+" "+name+" "+addr+" "+str(tel))
        x = VacInstitution(
            city=city,
            name=name,
            addr=addr,
            tel=tel
        )
        # cities[city]=1
        add(x)
    print("贵州省疫苗接种点信息存储完毕！")


# print(cities)
def insertVaccineInstitutionsHainan():
    print("正在存储海南省疫苗接种点信息......")
    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    HainanPath = r"spider/vaccinationLocations/海南省-新冠疫苗接种点名单.xlsx"
    HainanParser = xlsxParser(HainanPath)
    HainanParser.displayConfig()

    province = "海南"
    # cities={}
    cities = manualCityMap[province]
    for row in range(3, HainanParser.max_row + 1):
        for col in range(1, HainanParser.max_col + 1):
            if col == 1:
                city = HainanParser.getValue(row, col)
                if cities.get(city) == None:
                    city = ""
                else:
                    city = cities[city]
            elif col == 2:
                name = HainanParser.getValue(row, col)
            elif col == 3:
                addr = HainanParser.getValue(row, col)
            elif col == 4:
                tel = HainanParser.getValue(row, col)
                if tel == "" or tel == None:
                    tel = "暂未公布"
        #print(city + " " + name + " " + addr + " " + str(tel))
        # cities[city]=1
        if city != "":
            x = VacInstitution(
                city=city,
                name=name,
                addr=addr,
                tel=tel
            )
            # cities[city]=1
            add(x)
    print("海南省疫苗接种点信息存储完毕！")


def insertVaccineInstitutionsHeilongjiang():
    print("正在存储黑龙江省疫苗接种点信息......")
    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    HeilongjiangPath = r"spider/vaccinationLocations/黑龙江省新冠疫苗接种单位信息表0426.xlsx"
    HeilongjiangParser = xlsxParser(HeilongjiangPath)
    HeilongjiangParser.displayConfig()
    HeilongjiangParser.setMaxRowCol(1974, 9)
    province = "黑龙江"
    # cities={}
    cities = manualCityMap[province]
    for row in range(3, HeilongjiangParser.max_row + 1):
        for col in range(1, HeilongjiangParser.max_col + 1):
            if col == 1:
                city = HeilongjiangParser.getValue(row, col)
                city = cities[city]
            elif col == 4:
                name = HeilongjiangParser.getValue(row, col)
            elif col == 5:
                addr = HeilongjiangParser.getValue(row, col)
            elif col == 6:
                tel = HeilongjiangParser.getValue(row, col)
                if tel == "" or tel == None:
                    tel = "暂未公布"
        # cities[city] = 1
        x = VacInstitution(
            city=city,
            name=name,
            addr=addr,
            tel=tel
        )
        add(x)
    # print(cities)
    print("黑龙江省疫苗接种点信息存储完毕！")


def insertVaccineInstitutionsJiangsu():
    print("正在存储江苏省疫苗接种点信息......")
    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    JiangsuPath = r"spider/vaccinationLocations/江苏省指定承担新冠病毒疫苗使用的接种单位1574家 (1).xlsx"
    JiangsuParser = xlsxParser(JiangsuPath)
    JiangsuParser.displayConfig()
    JiangsuParser.setMaxRowCol(1576, 7)
    province = "江苏"
    # cities = {}
    cities = manualCityMap[province]
    for row in range(4, JiangsuParser.max_row + 1):
        for col in range(1, JiangsuParser.max_col + 1):
            if col == 2:
                city = JiangsuParser.getValue(row, col)
                city = cities[city]
            elif col == 4:
                name = JiangsuParser.getValue(row, col)
            elif col == 5:
                addr = JiangsuParser.getValue(row, col)
            elif col == 7:
                tel = JiangsuParser.getValue(row, col)
                if tel == "" or tel == None:
                    tel = "暂未公布"
        # cities[city]=1
        x = VacInstitution(
            city=city,
            name=name,
            addr=addr,
            tel=tel
        )
        add(x)
    # print(cities)
    print("江苏省疫苗接种点信息存储完毕！")


def insertVaccineInstitutionsJiangxi():
    print("正在存储江西省疫苗接种点信息......")
    # city: (max_row,max_col,start_row,name_col,addr_col,tel_col)
    configDict = {
        "新余市": (27, 5, 3, 2, 3, 4),
        "抚州市": (51, 4, 3, 2, 3, 4),
        "南昌市": (64, 4, 2, 2, 3, 4),
        "九江市": (58, 5, 3, 3, 4, 5),
        "萍乡市": (17, 5, 3, 3, 4, 5),
        "景德镇市": (15, 5, 3, 3, 4, 5),
        "鹰潭市": (15, 5, 2, 3, 4, 5),
        "赣州市": (106, 7, 2, 3, 5, 6),
        "吉安市": (25, 5, 2, 3, 4, 5)
    }

    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    JiangxiPath = r"spider/vaccinationLocations/江西省-新冠疫苗接种点名单.xlsx"
    JiangxiParser=xlsxParser(JiangxiPath)
    province="江西"
    cities=manualCityMap[province]
    for cityName in configDict:
        configItem=configDict[cityName]
        JiangxiParser.changeSheet(cityName)
        for row in range(configItem[2], configItem[0] + 1):
            for col in range(1, configItem[1] + 1):
                if col == configItem[3]:
                    name = JiangxiParser.getValue(row, col)
                elif col == configItem[4]:
                    addr = JiangxiParser.getValue(row, col)
                elif col == configItem[5]:
                    tel = JiangxiParser.getValue(row, col)
                    if tel == "" or tel == None:
                        tel = "暂未公布"
            city=cities[cityName]
            x = VacInstitution(
                city=city,
                name=name,
                addr=addr,
                tel=tel
            )
            add(x)

    print("江西省疫苗接种点信息存储完毕！")
def insertVaccineInstitutionsShanxi():
    print("正在存储山西省疫苗接种点信息......")
    with open('spider/vaccineProcess.json', mode='r', encoding='utf-8') as f:
        manualCityMap = json.load(f)
    ShanxiPath = r"spider/vaccinationLocations/山西省-新冠疫苗接种点名单.xlsx"
    ShanxiParser = xlsxParser(ShanxiPath)
    ShanxiParser.displayConfig()
    ShanxiParser.setMaxRowCol(2735, 9)
    province = "山西"
    # cities={}
    cities = manualCityMap[province]
    for row in range(3, ShanxiParser.max_row + 1):
        for col in range(1, ShanxiParser.max_col + 1):
            if col == 2:
                city = ShanxiParser.getValue(row, col)
                city = cities[city]
            elif col == 5:
                name = ShanxiParser.getValue(row, col)
            elif col == 7:
                addr = ShanxiParser.getValue(row, col)
            elif col == 9:
                tel = ShanxiParser.getValue(row, col)
                if tel == "" or tel == None:
                    tel = "暂未公布"
        # print(city+" "+name+" "+addr+" "+str(tel))
        # cities[city] = 1
        x = VacInstitution(
            city=city,
            name=name,
            addr=addr,
            tel=tel
        )
        # cities[city]=1
        add(x)
    # print(cities)
    print("山西省疫苗接种点信息存储完毕！")


def insertVaccineInstitutionsTencent():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://new.qq.com/'
    }
    with open('spider/city-map.json', mode='r', encoding='utf-8') as f:
        cityMap = json.load(f)
    with open('spider/rankListProcess.json', mode='r', encoding='utf-8') as f:
        provinceMap = json.load(f)
    provinces = ["北京", "天津", "河北", "内蒙古", "辽宁", "上海", "浙江", "安徽", "福建",
                 "山东", "河南", "湖北", "湖南", "广东", "广西", "四川", "云南", "陕西"]
    for province in provinces:
        # %E5%A4%A9%E6%B4%A5
        if province == "北京" or province == "天津" or province == "上海" or province == "重庆":
            region = province
            url = "https://apis.map.qq.com/place_cloud/search/region?region=" + parse.quote(
                region) + "&key=ZTCBZ-M6FWU-DFTVG-2HCU2-OM7SV-2LBCF&orderby=distance(39.90387,116.389893)&table_id=5fed45b33fc08460dcadf521&page_size=20&page_index=1"
            print(region)
            response = requests.get(url=url, headers=headers)
            data = json.loads(response.text)
            data = data["result"]["data"]
            if len(data) == 0:
                print("data is empty.")
                pass
            else:
                for item in data:
                    district = item["district"]
                    cities = cityMap[province]
                    district = cities[district]
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

        else:
            cities = cityMap[province]
            for city in cities:
                city = cities[city]
                if city == "济源示范区":
                    city = "济源"
                region = province + "," + city
                url = "https://apis.map.qq.com/place_cloud/search/region?region=" + parse.quote(
                    region) + "&key=ZTCBZ-M6FWU-DFTVG-2HCU2-OM7SV-2LBCF&orderby=distance(39.90387,116.389893)&table_id=5fed45b33fc08460dcadf521&page_size=20&page_index=1"
                print(region)
                response = requests.get(url=url, headers=headers)
                data = json.loads(response.text)
                # print(region)
                if data["status"] != 0:
                    print("ERROR: " + region)
                    continue

                data = data["result"]["data"]
                if len(data) == 0:
                    pass
                else:
                    for item in data:
                        # print(item)
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
    pass
# updateCovidNews()
# updateVaccineNews()
# updateRiskList()
# updateVaccineInstitutions()
# updateStringency()
# clearTable('vacInstitutions')
# def updateRiskList():
