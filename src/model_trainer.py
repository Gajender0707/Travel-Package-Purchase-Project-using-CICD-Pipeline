from logger import logging
from exception import CustomException
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import f1_score,classification_report,accuracy_score
import dill
from sklearn.model_selection import RandomizedSearchCV
from dataclasses import dataclass
import os

@dataclass
class ModelTrainerConfig:
    model_path=os.path.join("Artifacts","Model.pkl")

class ModelTrainer:
    
    def __init__(self):
        model_path_config=ModelTrainerConfig()
        logging.info("Model Path Initilize.")
    

    def Initiate_model_trainer(self,x_train_arr,x_test_arr,y_train,y_test):
        try:

            models={
                "LogisticRegression":LogisticRegression(),
                "RandomForestClassifier":RandomForestClassifier(),
                "DecisionTreeClassifier":DecisionTreeClassifier(),
                "SVC":SVC(),
                "KNeighborsClassifier":KNeighborsClassifier(),
                "GaussianNB":GaussianNB()
            }


            for i in range(len(list(models))):
                model=list(models.values())[i]
                model.fit(x_train_arr,y_train)
                print(model)
                y_train_pred=model.predict(x_train_arr)
                y_test_pred=model.predict(x_test_arr)

                traing_score=accuracy_score(y_train_pred,y_train)
                print(traing_score)
                test_score=accuracy_score(y_test_pred,y_test)
                print(test_score)

        except Exception as e:
            raise CustomException(e)
        