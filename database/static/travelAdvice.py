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

