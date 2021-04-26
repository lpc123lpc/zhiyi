from database.static import createTable
import datetime


vacdata = []
for i in range(0, 10):
    vacdata.append(createTable.VacMessage(areaName="a" + str(i),
                                          totalNum=i * 10,
                                          addNum=i,
                                          vacRate=round(i * 0.1, 3),
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
                                          infRate=round(i * 0.1, 3),
                                          time=datetime.date.today()))

halfYearVacData = []
halfYearVacData1 = []
for i in range(0, 180):
    halfYearVacData.append(createTable.VacMessage(areaName="a" + str(i),
                                                  totalNum=i * 10,
                                                  addNum=i,
                                                  vacRate=round(i * 0.001, 3),
                                                  time=datetime.date.today()))
    halfYearVacData1.append(createTable.VacMessage(areaName="b" + str(i),
                                                   totalNum=i * 2 * 10,
                                                   addNum=i * 2,
                                                   vacRate=round(i * 0.002, 3),
                                                   time=datetime.date.today()))
includeVac = [halfYearVacData, halfYearVacData1]
vacdatainclude = []
for i in range(0, 2):
    vacdatainclude.append(createTable.VacMessage(areaName="a" + str(i),
                                                 totalNum=i * 10,
                                                 addNum=i,
                                                 vacRate=round(i * 0.1, 3),
                                                 time=datetime.date.today()))

halfYearInfData = []
halfYearInfData1 = []
halfYearInfData2 = []
for i in range(0, 180):
    halfYearInfData.append(createTable.InfMessage(areaName="a" + str(i),
                                                  currentNum=i,
                                                  totalNum=i * 10,
                                                  addNum=i,
                                                  cured=i,
                                                  totalDead=i,
                                                  addDead=i,
                                                  infRate=round(i * 0.1, 3),
                                                  time=datetime.date.today()))
    halfYearInfData1.append(createTable.InfMessage(areaName="b" + str(i),
                                                   currentNum=i * 2,
                                                   totalNum=i * 20,
                                                   addNum=i * 2,
                                                   cured=i * 2,
                                                   totalDead=i * 2,
                                                   addDead=i * 2,
                                                   infRate=round(i * 0.002, 3),
                                                   time=datetime.date.today()))
    halfYearInfData2.append(createTable.InfMessage(areaName="c" + str(i),
                                                   currentNum=i * 3,
                                                   totalNum=i * 3 * 10,
                                                   addNum=i * 3,
                                                   cured=i * 3,
                                                   totalDead=i * 3,
                                                   addDead=i * 3,
                                                   infRate=round(i * 0.003, 3),
                                                   time=datetime.date.today()))
includeInf = [halfYearInfData, halfYearInfData1, halfYearInfData2]
infdatainclude = []
for i in range(0, 3):
    infdatainclude.append(createTable.InfMessage(areaName="a" + str(i),
                                                 currentNum=i,
                                                 totalNum=i * 10,
                                                 addNum=i,
                                                 cured=i,
                                                 totalDead=i,
                                                 addDead=i,
                                                 infRate=round(i * 0.1, 3),
                                                 time=datetime.date.today()))