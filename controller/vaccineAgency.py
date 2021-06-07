from database.static import vacInstitutions
import json


def getRegion(region):
    places = region.splite(str="  ")
    return places[len(places) - 1]


def delWithNone(string):
    if string is None:
        return ''
    else:
        return string


def getVaccineAgency(oriRegion):
    region = getRegion(oriRegion)
    vacAgencys = vacInstitutions.getVacInstitutions(region)
    data = []
    for i in vacAgencys:
        data.append({"name": delWithNone(getattr(i, "name")),
                     "addr": delWithNone(getattr(i, "address")),
                     "tel": delWithNone(getattr(i, "tel"))})
    return json(data)
