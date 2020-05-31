from flask import Flask, render_template
app_6 = Flask(__name__)

@app_6.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':  
   app_6.run('0.0.0.0',port=7000,debug=True)