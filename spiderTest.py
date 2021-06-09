from spider import spiderBeta
from spider import covidSpider

if __name__ == '__main__':
	spiderBeta.updateCovidNews()
	spiderBeta.updateVaccineNews()
	spiderBeta.updateRiskList()
	spiderBeta.updateVaccineInstitutions()
	spiderBeta.updateStringency()
	#clearTable('vacInstitutions')