import re
from datetime import datetime
from flask import request

tasks = [
    {
        "end": None,
        "entity": "TOTAL_DAY",
        "start": None,
        "surface": None,
        "value": {
            "start": None,
            "end": None,
            "total": None
        }
    }
]
money_room_type = {
    'deluxe': 2000000,
    'luxury': 1500000,
    'family': 1000000,
    'unit': 'VNĐ'

}


def get_date(string):
    regex = r"ngày \d+\W\d+\W\d+ đến ngày \d+\W\d+\W\d+"
    extract = re.search(regex, string)
    tasks[0]['start'] = extract.start()
    tasks[0]['end'] = extract.end()
    tasks[0]['surface'] = re.findall(regex, string)[0]
    value = re.findall(r"\d+\W\d+\W\d+", tasks[0]['surface'])
    tasks[0]['value']['start'] = datetime.strptime(value[0], "%d/%m/%Y").date()
    tasks[0]['value']['end'] = datetime.strptime(value[1], "%d/%m/%Y").date()
    tasks[0]['value']['total'] = (tasks[0]['value']['end'] - tasks[0]['value']['start']).days
    return tasks


def money_room():
    roomtype = request.values.get('roomtype')
    indate = request.values.get('indate')
    outdate = request.values.get('outdate')
    in_date = datetime.strptime(indate, "%Y-%m-%d").date()
    out_date = datetime.strptime(outdate, "%Y-%m-%d").date()
    sub_day = (out_date - in_date).days
    money = sub_day * money_room_type[roomtype]
    return money

