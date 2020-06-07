from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/app9')
def app9():
    return render_template('app_9.html')

@app.route('/gradient')
def gradient():
    return render_template('gradient.html')

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)