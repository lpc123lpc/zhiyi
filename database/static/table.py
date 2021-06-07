from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/covid_19'
# 跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
pymysql.install_as_MySQLdb()  #在我这里需要有这条指令才能正常运行，因此在此添加 by:lq
db = SQLAlchemy(app)


class BaseModelVac(db.Model):
    __abstract__ = True
    areaName = db.Column(db.String(200), primary_key=True)
    totalNum = db.Column(db.Integer)
    addNum = db.Column(db.Integer)
    vacRate = db.Column(db.FLOAT)


class BaseModelInf(db.Model):
    __abstract__ = True
    time = db.Column(db.String(20), primary_key=True)
    areaName = db.Column(db.String(200), primary_key=True)
    currentNum = db.Column(db.Integer)
    totalNum = db.Column(db.Integer)
    addNum = db.Column(db.Integer)
    cured = db.Column(db.Integer)
    totalDead = db.Column(db.Integer)
    addDead = db.Column(db.Integer)
    infRate = db.Column(db.FLOAT)


class BaseModelNews(db.Model):
    __abstract__ = True
    time = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(60), primary_key=True)
    urls = db.Column(db.String(200), primary_key=True)
    source = db.Column(db.String(50))
    abstracts = db.Column(db.String(200))
    picUrls = db.Column(db.String(200))


class VacMessage(BaseModelVac):
    __tablename__ = 'hisVacMessages'
    time = db.Column(db.String(20), primary_key=True)


class NowVacMessage(BaseModelVac):
    __tablename__ = 'nowVacMessages'
    time = db.Column(db.String(20), primary_key=True)


class InfMessage(BaseModelInf):
    __tablename__ = 'hisInfMessages'


class NowInfMessage(BaseModelInf):
    __tablename__ = 'nowInfMessages'


class ChinaInfMessage(BaseModelInf):
    __tablename__ = 'chinaInfMessages'


class Advice(db.Model):
    __tablename__ = 'advices'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DATETIME)
    text = db.Column(db.String(800))
    point = db.Column(db.Integer)


class Area(db.Model):
    __tablename__ = 'areas'

    parentArea = db.Column(db.String(100), primary_key=True)
    childArea = db.Column(db.String(100), primary_key=True)
    population = db.Column(db.BIGINT)


class InfNews(BaseModelNews):
    __tablename__ = 'infNews'


class VacNews(BaseModelNews):
    __tablename__ = 'vacNews'


class VacInstitution(db.Model):
    __tablename__ = 'vacInstitutions'

    city = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), primary_key=True)
    addr = db.Column(db.String(100))
    tel = db.Column(db.String(20))
    

class RiskArea(db.Model):
    __tablename__ = 'riskAreas'

    province = db.Column(db.String(20), primary_key=True)
    city = db.Column(db.String(20), primary_key=True)
    childArea = db.Column(db.String(20))
    level = db.Column(db.Integer)
    abstract = db.Column(db.String(100), primary_key=True)


class PolicyStrict(db.Model):
    __tablename__ = 'policyStrict'

    countryName = db.Column(db.String(20), primary_key=True)
    strictIndex = db.Column(db.FLOAT)
    date = db.Column(db.String(20))


# 插入数据
def add(x):
    db.session.merge(x)
    db.session.commit()


# 清除表单
def clearTable(name):
    db.reflect(app=app)
    db.get_engine().execute(f"truncate table {name}")