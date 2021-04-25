from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/covid_19'
# 跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)


class BaseModelVac(db.Model):
    __abstract__ = True
    areaName = db.Column(db.String(200), primary_key=True)
    totalNum = db.Column(db.Integer)
    addNum = db.Column(db.Integer)
    vacRate = db.Column(db.FLOAT)


class BaseModelInf(db.Model):
    __abstract__ = True
    areaName = db.Column(db.String(200), primary_key=True)
    currentNum = db.Column(db.Integer)
    totalNum = db.Column(db.Integer)
    addNum = db.Column(db.Integer)
    cured = db.Column(db.Integer)
    totalDead = db.Column(db.Integer)
    addDead = db.Column(db.Integer)
    infRate = db.Column(db.FLOAT)


class VacMessage(BaseModelVac):
    __tablename__ = 'hisVacMessages'
    time = db.Column(db.String(20), primary_key=True)


class NowVacMessage(BaseModelVac):
    __tablename__ = 'nowVacMessages'
    time = db.Column(db.String(20), primary_key=True)


class InfMessage(BaseModelInf):
    __tablename__ = 'hisInfMessages'
    time = db.Column(db.String(20), primary_key=True)


class NowInfMessage(BaseModelInf):
    __tablename__ = 'nowInfMessages'
    time = db.Column(db.String(20), primary_key=True)


class ChinaInfMessage(BaseModelInf):
    __tablename__ = 'chinaInfMessages'
    time = db.Column(db.String(20), primary_key=True)


class Advice(db.Model):
    __tablename__ = 'advices'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20))
    text = db.Column(db.String(800))


class Area(db.Model):
    __tablename__ = 'areas'

    parentArea = db.Column(db.String(100), primary_key=True)
    childArea = db.Column(db.String(100), primary_key=True)
    number = db.Column(db.BIGINT)


db.drop_all()
db.create_all()
