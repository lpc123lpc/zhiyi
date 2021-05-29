import unittest
from database.static.dao import *
from database.static.table import *


class MyTestCase(unittest.TestCase):
    def test_getNowInfMessage(self):
        inf = getNowInfMessage('global')
        self.assertIs('global', inf.areaName)

    def test_getNowInfMessageInclude(self):
        inf = getNowInfMessageInclude('global')
        area = db.session.query(Area).filter(Area.parentArea == 'global').first()
        name = area.childArea
        book = 0
        for i in inf:
            if i.areaName == name:
                book = 1
                break
        self.assertIs(1, book)

    def test_getHisInfMessage(self):
        inf = getHisInfMessage('global')
        self.assertIs('global', inf[0].areaName)

    def test_getHisInfMessageInclude(self):
        inf = getHisInfMessageInclude('global')
        area = db.session.query(Area).filter(Area.parentArea == 'global').first()
        name = area.childArea
        book = 0
        for i in inf:
            if i.areaName == name:
                book = 1
                break
        self.assertIs(1, book)

    def test_getNowVacMessage(self):
        vac = getNowVacMessage('global')
        self.assertIs('global', vac.areaName)

    def test_getNowVacMessageInclude(self):
        vac = getNowVacMessageInclude('global')
        area = db.session.query(NowVacMessage).filter(Area.parentArea == 'global').filter(Area.childArea == NowVacMessage.areaName).first()
        book = 0
        for v in vac:
            if v.areaName == area.childArea:
                book = 1
                break
        self.assertIs(1, book)

    def test_getHisVacMessage(self):
        vac = getHisVacMessage('global')
        self.assertIs('global', vac[0].areaName)


    def test_getHisVacMessageInclude(self):
        vac = getNowVacMessageInclude('global')
        area = db.session.query(NowVacMessage).filter(Area.parentArea == 'global').filter(
            Area.childArea == NowVacMessage.areaName).first()
        book = 0
        for v in vac:
            if v.areaName == area.childArea:
                book = 1
                break
        self.assertIs(1, book)

    def test_saveAdvice(self):
        saveAdvice('aaa', '2021-05-09')
        m = db.session.query(Advice).filter(Advice.text == 'aaa').filter(Advice.time == '2021-05-09')
        self.assertIs('aaa', m.text)


if __name__ == '__main__':
    unittest.main()
