import unittest
from database.static.getInitData import *
from database.static.table import *

class GetInitDataTestCase(unittest.TestCase):
    def test_getArea(self):
        getArea()
        globalData = db.session.query(Area).filter(Area.parentArea == 'global').all()
        chinaData = db.session.query(Area).filter(Area.parentArea == '中国').all()
        usData = db.session.query(Area).filter(Area.parentArea == '美国').all()
        self.assertIsNotNone(globalData)
        self.assertIsNotNone(chinaData)
        self.assertIsNotNone(usData)

    def test_getHisVac(self):
        getHisVac()
        globalData = db.session.query(VacMessage).filter(Area.parentArea == 'global').fliter(Area.childArea == VacMessage.areaName).all()
        self.assertIsNotNone(globalData)

    def test_getChinaHisInf(self):
        getChinaHisInf()
        hubeiData = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == '湖北').all()
        self.assertIsNotNone(hubeiData)

    def test_getGlobalCountryHisInf(self):
        getGlobalCountryHisInf()
        usData = db.session.query(InfMessage).filter(InfMessage.areaName == '美国').all()
        indiaData = db.session.query(InfMessage).filter(InfMessage.areaName == '印度').all()
        self.assertIsNotNone(usData)
        self.assertIsNotNone(indiaData)

    def test_getGlobalProvinceHisInf(self):
        getGlobalProvinceHisInf()
        chinaData = db.session.query(InfMessage).filter(InfMessage.areaName == '中国').all()
        usProvinceData = db.session.query(InfMessage).filter(Area.parentArea == '美国').filter(Area.childArea == InfMessage.areaName).all()
        self.assertIsNotNone(chinaData)
        self.assertIsNotNone(usProvinceData)

if __name__ == '__main__':
    unittest.main()
