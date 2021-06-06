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

## 近14天新增感染情况

* database/static/travelAdvice.py

```python
'''
参数：`region	`	 地区名称

返回值：`list<int>`

- 若有新增，返回近十四天的新增感染人数，时间从前到后。eg：[十四天前的， 十三天前的， ...]

- 若无新增，返回一个空的列表

- 若无该地区信息，返回None

'''

def getIfAddInf(region):
	return list
```

## 政策严格指数查询

* database/static/travelAdvice.py

```python
'''
参数：`region	`	 地区名称

返回值：`double`

- 若`region`是国家，直接返回该国家的值

- 若`region`是地区，返回该地区对应国家的值

- 若不存在`region`的数据，则返回`none`
'''

def getPolicyIndex(region):
    return double
```

