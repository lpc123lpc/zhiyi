import json
from flask import Flask, request
from flask_cors import CORS
from controller import map, table, sidebar
from database.static import dao
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return '欢迎来到知疫'


@app.route('/worldData', methods=["GET"])
def getWordData():
    return table.getWorldData()


@app.route('/countryInfData/<country>', methods=["GET"])
def getCountryInfData(country):
    return table.getCountryInfData(country)


@app.route('/countryVacData/<country>', methods=["GET"])
def getCountryVacData(country):
    return table.getCountryVacData(country)


@app.route('/countryInfection/<country>', methods=["GET"])
def getCountryInfection(country):
    return table.getCountryInfection(country)


@app.route('/countryVaccine/<country>', methods=["GET"])
def getCountryVaccine(country):
    return table.getCountryInfection(country)


@app.route('/provinceInfection/country/<province>', methods=["GET"])
def getCountryData(province):
    return table.getProvinceInfection(province)


@app.route('/vaccineHome/worldMapVaccineDataMsg', methods=["GET"])
def getWorldMapVaccineDataMsg():
    return map.getMapVaccine('global')


@app.route('/vaccineDetail/countryMapVaccineDataMsg/<country>', methods=["GET"])
def getWorldMapVaccineDataMsgCountry(country):
    return map.getMapVaccine(country)


@app.route('/infectHome/worldMapInfectionDataMsg', methods=["GET"])
def getWorldMapInfectionDataMsg():
    return map.getMapInfection('global')


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


post_data = []


@app.route('/feedback', methods=["GET", "POST"])
def getFeedBack():
    if request.method == "POST":
        data = request.get_json()
        for key in data:
            post_data.append(data[key])
            dao.saveAdvice(data[key])
    if request.method == "GET":
        return json.dumps(post_data)


if __name__ == '__main__':
    os.chdir("/Users/liuqian/PycharmProjects/covid-19")  # 注意这里请改成自己电脑上该文件夹的绝对路径 通用方法目前仍在查找 by:zzy
    os.system("python database\\static\\initCreate.py")
    app.config['JSON_AS_ASCII'] = False
    app.debug = True
    app.run()
