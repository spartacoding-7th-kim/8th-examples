from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.orderlist


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['GET'])
def listing():
    all_orders = list(db.info.find({}, {'_id': 0}))

    # 여기서 올오더스를 써서 노란색을 없애자!!
    return jsonify({'result': 'success', 'all_orders': all_orders})


@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.info.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문이 완료 되었습니다'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
