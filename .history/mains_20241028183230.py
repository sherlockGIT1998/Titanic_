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
        Gender = data['Gender']
        Age = data['Age']
        SibSp = data['SibSp']
        Parch = data['Parch']
        Fare = data['Fare']
        Embarked = data['Embarked']
        
        survival = TitanicSurvival(Gender,Age,SibSp,Parch,Fare,Embarked)
        
        predict = survival.get_predicted_survival()
        
        if predict == 0:
            
            predict = 'Passenger has NOT Survived...'
            
        else :
            
            predict = 'Passenger has Survived...'
            
            return 'Passenger has NOT Survived'

print('__name__ :',__name__)

if __name__ == '__main__':
        
    
