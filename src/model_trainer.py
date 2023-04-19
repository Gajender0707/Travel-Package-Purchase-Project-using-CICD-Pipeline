from logger import logging
from exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import f1_score,classification_report,accuracy_score
import dill
from sklearn.model_selection import RandomizedSearchCV
from dataclasses import dataclass
import os
from utils import evaluate_models,save_object

@dataclass
class ModelTrainerConfig:
    model_path=os.path.join("Artifacts","Model.pkl")
    logging.info("Give the Model path for the saving the model.")

class ModelTrainer:
    
    def __init__(self):
        self.model_path_config=ModelTrainerConfig()
        logging.info("Model Path Initilize.")
    

    def Initiate_model_trainer(self,x_train_arr,x_test_arr,y_train,y_test):
        try:
            x_train_arr=x_train_arr
            x_test_arr=x_test_arr
            y_train=y_train
            y_test=y_test

            models={
                "LogisticRegression":LogisticRegression(),
                "RandomForestClassifier":RandomForestClassifier(),
                "DecisionTreeClassifier":DecisionTreeClassifier(),
                "SVC":SVC(),
                "KNeighborsClassifier":KNeighborsClassifier(),
                "GaussianNB":GaussianNB()
            }
            logging.info("Give the Details about the Models")

            param={

                    "RandomForestClassifier":{
                    'criterion':['gini', 'log_loss', 'entropy'],
                    'max_features':['sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256] },

                        "DecisionTreeClassifier":{
                        'criterion':['entropy', 'gini', 'log_loss'],
                                    'splitter':['best','random'],
                                    'max_features':['sqrt','log2']},
                        
                        "KNeighborsClassifier":{'n_neighbors' : [5,7,9,11,13,15],
                            'weights' : ['uniform','distance'],
                            'metric' : ['minkowski','euclidean','manhattan']},
                        
                        "SVC":{
                            'C': [0.1, 1, 10, 100, 1000], 
                            'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
                            'kernel': ['rbf']},
                        
                        "LogisticRegression":{},
                        
                        "GaussianNB":{}
                           }
            logging.info("Define the paramters for the Hyperparamter tuning.")
            
            report:dict=evaluate_models(models,param,x_train_arr,y_train,x_test_arr,y_test)
            logging.info("Fetch the Report about the Model using the utils define function.")
            print(report)
            best_score=max(list(report.values()))
            print(best_score)
            best_model=list(report.keys())[list(report.values()).index(best_score)]
            print(best_model)
            # best_model=models[best_model_name]
            # print(best_model)
            # best_model,best_score=Best_model_evaluation(models=models,report=report)
            # logging.info("Find out the best model and its accuracy by using utils defined function.")
            # print(best_model)
            # print(best_score)

            save_object(best_model,self.model_path_config.model_path)
            # logging.info("Save the Model Successfully.")


        except Exception as e:
            raise CustomException(e)
        