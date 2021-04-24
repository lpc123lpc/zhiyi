from flask import Flask
from controller import map, table
import os

app = Flask(__name__)


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


@app.route('/wordData', methods=["GET"])
def getWordData():
    return table.getWordData()


@app.route('/countryData/<country>', methods=["GET"])
def getcountryData(country):
    return table.getCountryData(country)


@app.route('/countryInfection/<country>', methods=["GET"])
def getCountryInfection(country):
    return table.getCountryInfection(country)


@app.route('/countryVaccine/<country>', methods=["GET"])
def getCountryVaccine(country):
    return table.getCountryInfection(country)


if __name__ == '__main__':
    os.system("python database/static/createTable.py")
    app.debug = True
    app.run()
