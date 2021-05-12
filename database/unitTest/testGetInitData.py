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


if __name__ == '__main__':
    unittest.main()
