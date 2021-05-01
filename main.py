from flask import Flask
from flask_cors import CORS
from controller import map, table, sidebar
import os


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return '欢迎来到知疫'


@app.route('/worldMapVaccine', methods=["GET"])
def getWorldMapVaccine():
    return map.getMapVaccine('world')


@app.route('/worldMapInfection', methods=["GET"])
def getWorldMapInfection():
    return map.getMapInfection('world')


@app.route('/CountryMapVaccine/<country>', methods=["GET"])
def getCountryMapVaccine(country):
    return map.getMapVaccine(country)


@app.route('/CountryMapInfection/<country>', methods=["GET"])
def getCountryMapInfection(country):
    return map.getMapInfection(country)


@app.route('/worldData', methods=["GET"])
def getWordData():
    return table.getWorldData()


@app.route('/countryData/<country>', methods=["GET"])
def getcountryData(country):
    return table.getCountryData(country)


@app.route('/countryInfection/<country>', methods=["GET"])
def getCountryInfection(country):
    return table.getCountryInfection(country)


@app.route('/countryVaccine/<country>', methods=["GET"])
def getCountryVaccine(country):
    return table.getCountryInfection(country)


@app.route('/vaccineHome/worldMapVaccineDataMsg', methods=["GET"])
def getWorldMapVaccineDataMsg():
    return sidebar.getVaccinationMain('global')


@app.route('/vaccineDetail/countryMapVaccineDataMsg/<country>', methods=["GET"])
def getWorldMapVaccineDataMsgCountry(country):
    return sidebar.getVaccinationMain(country)


@app.route('/vaccineHomeHeadbar/vaccineSum', methods=["GET"])
def getVaccineSum():
    return sidebar.getVaccinationTotalSidebar('global')


@app.route('/vaccineHomeHeadbar/vaccineSumAdd', methods=["GET"])
def getVaccineSumAdd():
    return sidebar.getVaccinationTotalAddSidebar('global')


@app.route('/vaccineHomeHeadbar/vaccineCover', methods=["GET"])
def getVaccineCover():
    return sidebar.getVaccinationCovSidebar('global')


@app.route('/vaccineHomeHeadbar/vaccineCoverAdd', methods=["GET"])
def getVaccineCoverAdd():
    return sidebar.getVaccinationCovAddSidebar('global')


@app.route('/vaccineDetailSidebar/vaccineSum/<country>', methods=["GET"])
def getVaccineSum(country):
    return sidebar.getVaccinationTotalSidebar(country)


@app.route('/vaccineDetailSidebar/vaccineSumAdd/<country>', methods=["GET"])
def getVaccineSumAdd(country):
    return sidebar.getVaccinationTotalAddSidebar(country)


@app.route('/vaccineDetailSidebar/vaccineCover/<country>', methods=["GET"])
def getVaccineCover(country):
    return sidebar.getVaccinationCovSidebar(country)


@app.route('/vaccineDetailSidebar/vaccineCoverAdd/<country>', methods=["GET"])
def getVaccineCoverAdd(country):
    return sidebar.getVaccinationCovAddSidebar(country)


@app.route('/infectHome/worldMapInfectionDataMsg', methods=["GET"])
def getWorldMapInfectionDataMsg():
    return sidebar.getInfectionMain('global')


@app.route('/infectDetail/countryMapInfectionDataMsg/<country>', methods=["GET"])
def getWorldMapInfectionDataMsgCountry(country):
    return sidebar.getInfectionMain(country)


@app.route('/infectHomeHeadbar/infectSum', methods=["GET"])
def getInfectionSum():
    return sidebar.getInfectionTotalSidebar('global')


@app.route('/infectHomeHeadbar/infectSumAdd', methods=["GET"])
def getInfectionSumAdd():
    return sidebar.getInfectionTotalAddSidebar('global')


@app.route('/infectHomeHeadbar/infectDeath', methods=["GET"])
def getInfectionDead():
    return sidebar.getInfectionDeadSidebar('global')


@app.route('/infectHomeHeadbar/infectDeathAdd', methods=["GET"])
def getInfectionDeadAdd():
    return sidebar.getInfectionDeadAddSidebar('global')


@app.route('/infectHomeHeadbar/infectCure', methods=["GET"])
def getInfectionCure():
    return sidebar.getInfectionCureSidebar('global')


@app.route('/infectHomeHeadbar/infectCureAdd', methods=["GET"])
def getInfectionCureAdd():
    return sidebar.getInfectionCureAddSidebar('global')


@app.route('/infectDetailSidebar/infectSum/<country>', methods=["GET"])
def getInfectionSumCountry(country):
    return sidebar.getInfectionTotalSidebar(country)


@app.route('/infectDetailSidebar/infectSumAdd/<country>', methods=["GET"])
def getInfectionSumAddCountry(country):
    return sidebar.getInfectionTotalAddSidebar(country)


@app.route('/infectDetailSidebar/infectDeath/<country>', methods=["GET"])
def getInfectionDeadCountry(country):
    return sidebar.getInfectionDeadSidebar(country)


@app.route('/infectDetailSidebar/infectDeathAdd/<country>', methods=["GET"])
def getInfectionDeadAddCountry(country):
    return sidebar.getInfectionDeadAddSidebar(country)


@app.route('/infectDetailSidebar/infectCure/<country>', methods=["GET"])
def getInfectionCureCountry(country):
    return sidebar.getInfectionCureSidebar(country)


@app.route('/infectDetailSidebar/infectCureAdd/<country>', methods=["GET"])
def getInfectionCureAddCountry(country):
    return sidebar.getInfectionCureAddSidebar(country)


@app.route('/vaccineSidebar/vaccineSum', methods=["GET"])
def getVaccineSumSidebar():
    return sidebar.getVaccinationTotalSidebar('global')


@app.route('/vaccineSidebar/vaccineSumAdd', methods=["GET"])
def getVaccineSumAddSidebar():
    return sidebar.getVaccinationTotalAddSidebar('global')


@app.route('/infectSidebar/infectSum', methods=["GET"])
def getInfectionSumSidebar():
    return sidebar.getInfectionTotalSidebar('global')


@app.route('/infectSidebar/infectSumAdd', methods=["GET"])
def getInfectionSumAddSideBar():
    return sidebar.getInfectionTotalAddSidebar('global')


@app.route('/infectSidebar/infectCure', methods=["GET"])
def getInfectionCureSiadebar():
    return sidebar.getInfectionCureSidebar('global')


@app.route('/infectSidebar/infectCureAdd', methods=["GET"])
def getInfectionCureAddSidebar():
    return sidebar.getInfectionCureAddSidebar('global')


if __name__ == '__main__':
    os.chdir("/Users/liuqian/PycharmProjects/covid-19")  # 注意这里请改成自己电脑上该文件夹的绝对路径 通用方法目前仍在查找 by:zzy
    os.system("python database\\static\\initCreate.py")
    app.debug = True
    app.run()
