from spider import spiderBeta
from spider.covidSpider import Spider
def updateDaily():
	"""
	调用该函数爬取并更新所有需要实时更新的数据
	可以设为定时任务
	:return:
	"""
	Spider.timelyJob()
	spiderBeta.updateRiskList()
	spiderBeta.updateCovidNews()
	spiderBeta.updateVaccineNews()
	spiderBeta.updateStringency()
	# spiderBeta.updateVaccineInstitutions()