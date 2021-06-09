from flask import request, jsonify
from flask_cors import CORS
from controller import map, tables, sidebar, vaccineAgency, search, news, safeLevel
from database.static import dao, table
from database.static.getInitData import *
from spider import spiderBeta


app = table.app
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# 初始化数据库，第一次执行完后就可以注释掉
'''spiderBeta.updateRiskList()
spiderBeta.updateVaccineInstitutions()'''
'''clearTable('chinaInfMessages')
clearTable('hisInfMessages')
getGlobalProvinceHisInf()'''
'''Init()'''
'''updateInf()
updateVac()'''
'''getArea()
getChinaHisInf()'''
'''getGlobalCountryHisInf()'''


@app.route('/')
def index():
    return '欢迎来到知疫'


@app.route('/worldData', methods=["GET"])
def getWordData():
    return tables.getWorldData()


@app.route('/countryInfData/<country>', methods=["GET"])
def getCountryInfData(country):
    return tables.getCountryInfData(country)


@app.route('/countryVacData/<country>', methods=["GET"])
def getCountryVacData(country):
    return tables.getCountryVacData(country)


@app.route('/countryInfection/<country>', methods=["GET"])
def getCountryInfection(country):
    return tables.getCountryInfection(country)


@app.route('/countryVaccine/<country>', methods=["GET"])
def getCountryVaccine(country):
    return tables.getCountryVaccine(country)


@app.route('/provinceInfection/country/<province>', methods=["GET"])
def getCountryData(province):
    return tables.getProvinceInfection(province)


@app.route('/vaccineHome/worldMapVaccineDataMsg', methods=["GET"])
def getWorldMapVaccineDataMsg():
    return map.getMapVaccine('global')


@app.route('/vaccineDetail/countryMapVaccineDataMsg/<country>', methods=["GET"])
def getWorldMapVaccineDataMsgCountry(country):
    return map.getMapVaccine(country)


@app.route('/infectHome/worldMapInfectionDataMsg', methods=["GET"])
def getWorldMapInfectionDataMsg():
    return map.getMapInfectionGlobal('global')


@app.route('/infectDetail/countryMapInfectionDataMsg/<country>', methods=["GET"])
def getWorldMapInfectionDataMsgCountry(country):
    return map.getMapInfection(country)


@app.route('/infectDetail/provinceMapInfectionDataMsg/<province>', methods=["GET"])
def getInfectionProvince(province):
    return map.getMapInfection(province)


@app.route('/vaccineHomeHeadbar/vaccineSum', methods=["GET"])
def getVaccineSumHeadbar():
    return sidebar.getVaccinationTotalSidebar('global')


@app.route('/vaccineHomeHeadbar/vaccineSumAdd', methods=["GET"])
def getVaccineSumAddHeadbar():
    return sidebar.getVaccinationTotalAddSidebar('global')


@app.route('/vaccineHomeHeadbar/vaccineCover', methods=["GET"])
def getVaccineCoverHeadbar():
    return sidebar.getVaccinationCovSidebar('global')


@app.route('/vaccineDetailSidebar/vaccineSum/<country>', methods=["GET"])
def getVaccineSumHeadbarSon(country):
    return sidebar.getVaccinationTotalSidebar(country)


@app.route('/vaccineDetailSidebar/vaccineSumAdd/<country>', methods=["GET"])
def getVaccineSumAddHeadbarSon(country):
    return sidebar.getVaccinationTotalAddSidebar(country)


@app.route('/vaccineDetailSidebar/vaccineCover/<country>', methods=["GET"])
def getVaccineCoverHeadbarSon(country):
    return sidebar.getVaccinationCovSidebar(country)


@app.route('/infectHomeHeadbar/infectSum', methods=["GET"])
def getInfectionSumHeadbar():
    return sidebar.getInfectionTotalSidebar('global')


@app.route('/infectHomeHeadbar/infectSumAdd', methods=["GET"])
def getInfectionSumAddHeadbar():
    return sidebar.getInfectionTotalAddSidebar('global')


@app.route('/infectHomeHeadbar/infectDeath', methods=["GET"])
def getInfectionDeadHeadbar():
    return sidebar.getInfectionDeadSidebar('global')


@app.route('/infectHomeHeadbar/infectDeathAdd', methods=["GET"])
def getInfectionDeadAddHeadbar():
    return sidebar.getInfectionDeadAddSidebar('global')


@app.route('/infectHomeHeadbar/infectCure', methods=["GET"])
def getInfectionCureHeadbar():
    return sidebar.getInfectionCureSidebar('global')


@app.route('/infectDetailSidebar/infectSum/<country>', methods=["GET"])
def getInfectionSumCountryHeadbarSon(country):
    return sidebar.getInfectionTotalSidebar(country)


@app.route('/infectDetailSidebar/infectSumAdd/<country>', methods=["GET"])
def getInfectionSumAddCountryHeadbarSon(country):
    return sidebar.getInfectionTotalAddSidebar(country)


@app.route('/infectDetailSidebar/infectDeath/<country>', methods=["GET"])
def getInfectionDeadCountryHeadbarSon(country):
    return sidebar.getInfectionDeadSidebar(country)


@app.route('/infectDetailSidebar/infectDeathAdd/<country>', methods=["GET"])
def getInfectionDeadAddCountryHeadbarSon(country):
    return sidebar.getInfectionDeadAddSidebar(country)


@app.route('/infectDetailSidebar/infectCure/<country>', methods=["GET"])
def getInfectionCureCountryHeadbarSon(country):
    return sidebar.getInfectionCureSidebar(country)


@app.route('/vaccineSidebar/vaccineSum', methods=["GET"])
def getVaccineSumMain():
    return sidebar.getVaccinationTotalSidebar('global')


@app.route('/vaccineSidebar/vaccineSumAdd', methods=["GET"])
def getVaccineSumAddMain():
    return sidebar.getVaccinationTotalAddSidebar('global')


@app.route('/infectSidebar/infectSum', methods=["GET"])
def getInfectionSumMain():
    return sidebar.getInfectionTotalSidebar('global')


@app.route('/infectSidebar/infectSumAdd', methods=["GET"])
def getInfectionSumAddMain():
    return sidebar.getInfectionTotalAddSidebar('global')


@app.route('/infectSidebar/infectCure', methods=["GET"])
def getInfectionCureMain():
    return sidebar.getInfectionCureSidebar('global')


@app.route('/infectDetailProvinceSidebar/infectSum/<province>', methods=["GET"])
def getInfectionSumProvince(province):
    return sidebar.getInfectionTotalSidebar(province)


@app.route('/infectDetailProvinceSidebar/infectProvinceSumAdd/<province>', methods=["GET"])
def getInfectionSumAddProvince(province):
    return sidebar.getInfectionTotalAddSidebar(province)


@app.route('/infectDetailProvinceSidebar/infectProvinceDeath/<province>', methods=["GET"])
def getInfectionDeathProvince(province):
    return sidebar.getInfectionDeadSidebar(province)


@app.route('/infectDetailProvinceSidebar/infectProvinceDeathAdd/<province>', methods=["GET"])
def getInfectionDeathAddProvince(province):
    return sidebar.getInfectionDeadAddSidebar(province)


@app.route('/infectDetailProvinceSidebar/infectProvinceCure/<province>', methods=["GET"])
def getInfectionCureProvince(province):
    return sidebar.getInfectionCureSidebar(province)


@app.route('/feedback', methods=["GET", "POST"])
def getFeedBack():
    if request.method == "POST":
        data = request.get_json()
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dao.saveAdvice(data['desc'], now_time, data['value'])
        return jsonify({})
    if request.method == "GET":
        return jsonify({})


@app.route('/search/<region>/regionInfectDataMsg', methods=["GET"])
def getSearchMsg(region):
    return search.getAllMassage(region)


@app.route('/search/<region>/regionVaccineDataMsg', methods=["GET"])
def getVaccineMsg(region):
    return vaccineAgency.getVaccineAgency(region)


@app.route('/news', methods=["GET"])
def getNews():
    return news.getNews()


@app.route('/travelAdvice', methods=["POST"])
def getTravelAdvice():
    if request.method == "POST":
        data = request.get_json()
        return safeLevel.safeLevel(data['region'], data['time'])
    if request.method == "GET":
        return jsonify({})


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    '''app.debug = True'''
    app.run()
