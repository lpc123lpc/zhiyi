from database.static import vacInstitutions
import json


def getVaccineAgency(region):
    vacAgencys = vacInstitutions.getVacInstitutions(region)
    data = []
    for i in vacAgencys:
        data.append({"name": getattr(i, "name"),
                     "addr": getattr(i, "address"),
                     "tel": getattr(i, "tel")})
    return json(data)
