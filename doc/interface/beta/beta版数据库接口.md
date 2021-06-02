# $\beta$版数据库接口

## 新闻咨询相关接口（与前端对接）

* database/static/newsDao.py

```python
'''
description:get infection news
number:the amount of infection news required
return:infection news
'''

def getInfNews(number):
    return m


'''
description:get vaccine news
number:the amount of vaccine news required
return:vaccine news
'''

def getVacNews(number):
    return m
```

## 接种机构相关接口（与前端对接）

* database/static/vacInstitutions.py

```python
'''
description:get vaccination institutions
city:city name
return:vaccination institutions of this city
'''

def getVacInstitutions(city):
    return m
```

## 存取优化

* database/static/countryInfo.json

国家列表的信息整合而成的json文件，格式与前端相匹配，每日随定时更新而更新

生成json文件的函数：database/static/dao.py

```python
def getCountryInfoJson()
```

## 搜索

* database/static/searchData.json

生成json文件的函数：database/static/dao.py

```python
'''
返回一个符合前端接口Data格式的List
'''
def getSearchData():
	return searchData
```

