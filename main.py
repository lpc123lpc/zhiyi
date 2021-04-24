from flask import Flask
from flask import jsonify
from controller import map
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


if __name__ == '__main__':
    os.system("python database/static/createTable.py")
    app.debug = True
    app.run()

