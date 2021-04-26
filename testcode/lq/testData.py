from database.static import createTable
import datetime

vacdata = []
for i in range(0, 10):
    vacdata.append(createTable.VacMessage(areaName="a" + str(i),
                                          totalNum=i * 10,
                                          addNum=i,
                                          vacRate=i * 0.1,
                                          time=datetime.date.today()))

infdata = []
for i in range(0, 10):
    infdata.append(createTable.InfMessage(areaName="a" + str(i),
                                          currentNum=i,
                                          totalNum=i * 10,
                                          addNum=i,
                                          cured=i,
                                          totalDead=i,
                                          addDead=i,
                                          infRate=i * 0.1,
                                          time=datetime.date.today()))