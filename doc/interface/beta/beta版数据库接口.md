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