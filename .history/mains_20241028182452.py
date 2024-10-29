from flask import Flask,render_template,request

from utils import TitanicSurvival

app = Flask(__name__)
@app.route('/')

def hello_flask(self):
    print('Titaic Survival Prediction....')
    return render_template('index.html')

@app.route('/predict_survival',methods=['GET','POST'])

def 
