import tinydb
import datetime


def write(infoCases, infoTests, infoBeds):
    """

    :param infoCases:
    type: list
    format:
    [total cases, total deaths, active cases, recovered]

    :param infoTests:
    type: list
    format:
    [total tests, daily tests, remaining tests]

    :param infoBeds:
    type: list
    format:
    [Occupied, Vacant]

    :return:
    None
    """

#   create db instance
    dbCases = tinydb.TinyDB('./data/dataCases.json')
    dbTests = tinydb.TinyDB('./data/dataTests.json')
    dbBeds = tinydb.TinyDB('./data/dataBeds.json')

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

#   update db
    dbCases.insert({
        'date': date,
        'totalcases': infoCases[0],
        'totaldeaths': infoCases[1],
        'activecases': infoCases[2],
        'recovered': infoCases[3]
    })

    dbTests.insert({
        'date': date,
        'totaltests': infoTests[0],
        'dailytests': infoTests[1],
        'remainingtests': infoTests[2]
    })

    dbBeds.insert({
        'date': date,
        'occupied': infoBeds[0],
        'vacant': infoBeds[1]
    })


def read(name, date):
    """

    :param name:
    type:string
    expected values: "infoCases" or "infoBeds" or "infoTests"

    :param date:
    type:string
    format: fullYear-month-day

    :return:
    type:dict
    Use the keys mentioned in write to get the corresponding value
    """

#   Init db and Query() instance
    db = tinydb.TinyDB("./data/"+name)
    Query = tinydb.Query()

#   search db for specific date
    info = db.search(Query.date == date)[0]
    return info

