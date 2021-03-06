from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index-start.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']

    print(request.args.get('title'))
    data_dict = {}
    data_dict['title'] = title
    data_dict['author'] = author
    data_dict['review'] = review

    db.review.insert_one(data_dict)

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    print(db.review.find({},{'_id':0}))
    reviews = list(db.review.find({},{'_id':0}))
    print(reviews)

    return jsonify({'reviews':reviews, 'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)