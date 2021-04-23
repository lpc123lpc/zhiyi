from flask import Flask
from controller import map


app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎来到知疫'


@app.route('/worldMapVaccine', methods=["GET"])
def getWorldMapVaccine():
    return map.getWorldMapVaccine()


@app.route('/worldMapInfection', methods=["GET"])
def getWorldMapInfection():
    return map.getWorldMapInfection()


@app.route('/CountryMapVaccine/<country>', methods=["GET"])
def getCountryMapVaccine(country):
    return map.getCountryMapVaccine(country)


@app.route('/CountryMapInfection/<country>', methods=["GET"])
def getCountryMapInfection(country):
    return map.getCountryMapInfection(country)


if __name__ == '__main__':
    app.debug = True
    app.run()

