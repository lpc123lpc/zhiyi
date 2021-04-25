from database.static.createTable import InfMessage, VacMessage, Advice, db

'''description:get infection information
    name:"world"(世界)/国家姓名/地区姓名
    time:日期，格式为“XXXX-XX-XX”
    return:返回该区域的感染信息
'''


def getInfMessage(name, time):
    InfMessage.infmessage = None
    return InfMessage.infmessage


'''
description:get infection information
name:"world"(世界)/国家姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域所包含的国家/地区的感染信息
'''


def getInfMessageInclude(name, time):
    InfMessage.infmessages = []
    return InfMessage.infmessages


'''
description:get infection information
name:"world"(世界)/国家姓名/地区姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域的接种信息
'''


def getVacMessage(name, time):
    VacMessage.vacmessage = None
    return VacMessage.vacmessage


'''
description:get infection information
name:"world"(世界)/国家姓名
time:日期，格式为“XXXX-XX-XX”
return:返回该区域所包含的国家/地区的接种信息
'''


def getVacMessageInclude(name, time):
    VacMessage.vacmessages = []
    return VacMessage.vacmessages


'''
description:save infection information
对接爬虫
'''


def saveInfMessage(messages):
    return None


'''
description:save vaccination information
对接爬虫
'''


def saveVacMessage(messages):
    return None


'''
description:save advice
对接前端
'''


def saveAdvice(message, time):
    return None

