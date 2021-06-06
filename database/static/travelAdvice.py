from database.static.table import *

def getPolicyIndex(region):
    parent = ''
    area = db.session.query(Area).filter(Area.childArea == region).filter(Area.population != 0).first()
    if area is None:
        return None
    else:
        parent = area.parentArea
        while parent != 'global':
            area = db.session.query(Area).filter(Area.childArea == region).first()
            parent = area.parentArea
        name = area.childArea
        policy = db.session.query(PolicyStrict).filter(PolicyStrict.countryName == name).first()
        if policy is None:
            return None
        else:
            return policy.strictIndex


def getIfAddInf(region):
    addList = []
    ack = 0
    data = db.session.query(InfMessage).filter(InfMessage.areaName == region).order_by(InfMessage.time.desc()).limit(14).all()
    if len(data) == 0:
        data = db.session.query(ChinaInfMessage).filter(ChinaInfMessage.areaName == region).order_by(ChinaInfMessage.time.desc()).limit(14).all()
        if len(data) == 0:
            return None
    data.reverse()
    for d in data:
        addList.append(d.addNum)
        print(d.addNum)
        if d.addNum > 0:
            ack = 1
    if ack == 0:
        return []
    else:
        return addList
