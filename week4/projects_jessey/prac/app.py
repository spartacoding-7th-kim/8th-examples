from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/gradient')
def gradient():
    return render_template('gradient.html')

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)