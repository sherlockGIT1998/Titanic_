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
        
        with open(config.):
        