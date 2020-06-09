from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index-start.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    articles = list(db.metas.find({}, {"_id":0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'articles':articles, 'result':'success', 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    posting_url = request.form['posting_url_key']
    posting_comment = request.form['posting_comment_key']
    # 1. 클라이언트로부터 데이터를 받기

    ##########################################
    
    # 2. meta tag를 스크래핑하기

    
    img_url = "https://movie-phinf.pstatic.net/20190115_228/1547528180168jgEP7_JPEG/movie_image.jpg?type=m665_443_2"
    title ="test title"
    description = " test desc"

    data_dict = {    }
    data_dict['img'] = img_url
    data_dict['title'] = title
    data_dict['desc'] = description
    data_dict['comment'] = posting_comment
    data_dict['url'] = posting_url

    # 3. mongoDB에 데이터 넣기
    
    db.metas.insert_one(data_dict)

    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)