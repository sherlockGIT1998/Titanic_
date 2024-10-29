import pickle 
import json 
import pandas as pd  
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import config 

class TitanicSurvival():
    
    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        
        self.Pclass = Pclass 
        self.Gender = Gender
        self.Age = Age 
        self.SibSp = SibSp
        self.Parch = Parch 
        self.Fare = Fare
        
        self.Embarked_col = 'Embarked_' + Embarked
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.save_data = json.load(f)
            
            self.column_names = np.array(self.save_data['column_names'])
            
    def get_predicted_survival(self):
        
        self.load_models()
        
        Embarked_col_index = np.where(self.column_names==self.Embarked_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.Pclass
        array[1] = self.save_data['Gender'][self.Gender]
        array[2] = self.Age
        array[3] = self.SibSp
        array[4] = self.Parch
        array[5] = self.Fare
        array[Embarked_col_index] == 1
        
        print('Array is :',array)
    
        predict = self.model.predict([array])[0]
        
        return predict 
    
if __name__ == '__main__':
    
    Pclass = 3
    Gender = 'male'
    Age	= 22.0
    SibSp = 1.0
    Parch = 0
    Fare = 7.25

    Embarked = 'C'

    survival = TitanicSurvival()