from flask import Flask, jsonify, request
from module import get_date, money_room
from datetime import datetime
app = Flask(__name__)


@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    input_string = request.values.get('text')
    res = get_date(input_string)
    return jsonify(res)


@app.route('/check_room', methods=['GET'])
def check_room():
    money = money_room()
    return jsonify({'money': money, 'avail': 1})


@app.route('/check_room_post', methods=['POST'])
def check_room_post():
    data = request.get_json()
    indate = data['indate']
    outdate = data['outdate']
    room_type = data['roomtype']
    in_date = datetime.strptime(indate, "%Y-%m-%d").date()
    out_date = datetime.strptime(outdate, "%Y-%m-%d").date()
    sub_day = (out_date - in_date).days
    money = sub_day*100000
    return jsonify({'money': money, 'avail': 1})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
