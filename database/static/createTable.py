from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/covid_19'
# 跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class VacMessage(db.Model):
    __tablename__ = 'vacMessages'
    #
    time = db.Column(db.DATE)
    areaName = db.Column(db.VARCHAR(200), primary_key=True)
    totalNum = db.Column(db.Integer)
    addNum = db.Column(db.Integer)
    vacRate = db.Column(db.FLOAT)


class InfMessage(db.Model):
    __tablename__ = 'infMessages'

    time = db.Column(db.DATE)
    areaName = db.Column(db.VARCHAR(200), primary_key=True)
    currentNum = db.Column(db.Integer)
    totalNum = db.Column(db.Integer)
    addNum = db.Column(db.Integer)
    cured = db.Column(db.Integer)
    totalDead = db.Column(db.Integer)
    addDead = db.Column(db.Integer)
    infRate = db.Column(db.FLOAT)


class Advice(db.Model):
    __tablename__ = 'advices'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DATE)
    text = db.Column(db.String(800))


db.drop_all()
db.create_all()
