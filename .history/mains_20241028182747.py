from flask import Flask,render_template,request

from utils import TitanicSurvival

app = Flask(__name__)
@app.route('/')

def hello_flask():
    print('Titaic Survival Prediction....')
    return render_template('index.html')

@app.route('/predict_survival',methods=['GET','POST'])

def survival_info():
    
    if request.method =='GET':
        
        print('In GET Method....')
        
        data = request.form
        Pclass = data['Pclass']
            
    
    
