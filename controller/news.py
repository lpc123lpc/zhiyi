from flask import jsonify
from database.static import newsDao


def getNews():
    vacNews = newsDao.getVacNews(10)
    infNews = newsDao.getInfNews(10)
    vac, inf = [], []
    for news in vacNews:
        vac.append({"time": getattr(news, "time"),
                    "title": getattr(news, "title"),
                    "urls": getattr(news, "urls"),
                    "source": getattr(news, "source"),
                    "abstracts": getattr(news, "abstracts"),
                    "picUrls": getattr(news, "picUrls"), })
    for news in infNews:
        inf.append({"time": getattr(news, "time"),
                    "title": getattr(news, "title"),
                    "urls": getattr(news, "urls"),
                    "source": getattr(news, "source"),
                    "abstracts": getattr(news, "abstracts"),
                    "picUrls": getattr(news, "picUrls"), })
    return jsonify({
        "vacNews": vac,
        "infNews": inf
    })