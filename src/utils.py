from logger import logging
from exception import CustomException
import os
import dill
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np



def save_object(object,object_path):
    try:
        with open(object_path,"wb") as f:
            return dill.dump(object,f)

    except Exception as e:
        raise CustomException(e)
    

def load_object(object_path):
    try:
        with open(object_path,"rb") as f:
            model=dill.load(f)
            return model
    except Exception as e:
        raise CustomException(e)
    

def evaluate_models(models,params,x_train,y_train,x_test,y_test):
    try:
        report={}
        for i in range(len(list(models))):
            model_name=list(models.keys())[i]
            model=list(models.values())[i]
            rf=RandomizedSearchCV(model,params[model_name],cv=3)
            rf.fit(x_train,y_train)
            model.set_params(**rf.best_params_)
            model.fit(x_train,y_train)
            y_test_pred=model.predict(x_test)
            score=accuracy_score(y_test_pred,y_test)
            # print(f"Model: {model_name} and score: {score}")
            report[model]=score
        return report 
  
    except Exception as e:
        raise CustomException(e)
    

# def Best_model_evaluation(models,report):
#     try:
#         score_data=pd.DataFrame({
#             "Models":models.keys(),
#             "Score":report.values()
#         })

#         # print(score_data)
#         best_model_name=list(score_data[score_data["Score"]>0.95].loc[0:1,:]["Models"])[0]
#         best_model=models[best_model_name]
#         best_score=list(score_data[score_data["Score"]>0.95].loc[0:1,:]["Score"])[0]
   
#         return (best_model,
#                 best_score)

    except Exception as e:
        raise CustomException(e)
    

    