import pandas as pd
import numpy as np
from logger import logging 
from exception import CustomException
from dataclasses import dataclass
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from utils import save_object
from utils import load_object

@dataclass
class DataTransformationConfig:
    preprocessor_path=os.path.join("Artifacts","Preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation_object(self,train_data_path,test_data_path):
        try:
            logging.info("Data Transfomation has been started.")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            logging.info("Read the train data and test data successfully")
            Target="ProdTaken"
            y=train_data[Target]
            x=train_data.drop(Target,axis=1)
            # num_features=x.select_dtypes([int,float]).columns
            num_features=['Age', 'CityTier', 'DurationOfPitch', 'NumberOfPersonVisiting',
       'NumberOfFollowups', 'PreferredPropertyStar', 'NumberOfTrips',
       'Passport', 'PitchSatisfactionScore', 'OwnCar',
       'NumberOfChildrenVisiting', 'MonthlyIncome']
            cat_features=x.select_dtypes(object).columns
            logging.info("Differeciate numeric features and categorical features")
            logging.info(f"Our Numeric features are {num_features}")
            logging.info(f"Our categorical Features are{cat_features}")

            num_pipeline=Pipeline(steps=[
                ("Imputer",SimpleImputer(strategy="mean")),
                ("scaling",StandardScaler())
            ])
            logging.info("created numeric pipeline")

            cat_pipeline=Pipeline(steps=[
                ("Imputer",SimpleImputer(strategy="most_frequent")),
                ("Encoding",OneHotEncoder())
            ])
            logging.info("createc categorical features.")

            preprocessor=ColumnTransformer([
                ("numeric",num_pipeline,num_features),
                ("categorical",cat_pipeline,cat_features)
            ])

            logging.info("Ready to train the Preprocessor on the training data")

            

            return preprocessor


        except Exception as e:
            raise CustomException(e)
        

    def Initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_data_path_=train_data_path
            test_data_path_=test_data_path
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            Target="ProdTaken"
            logging.info("Read the Training and testing data set successfully.")

            preprocessor=self.get_data_transformation_object(train_data_path=train_data_path_,test_data_path=test_data_path_)
            logging.info("Load the Preprocessor Sucessfully..")

            y_train=train_data[Target]
            x_train=train_data.drop(Target,axis=1)

            y_test=test_data[Target]
            x_test=test_data.drop(Target,axis=1)

            preprocessor=preprocessor.fit(x_train)
            logging.info("Train the Preprocessor Successfully.")
            preprocessor_path=self.data_transformation_config.preprocessor_path
            save_object(preprocessor,preprocessor_path)
            logging.info("Save the Object Successfully..")
            x_train_arr=preprocessor.transform(x_train)
            x_test_arr=preprocessor.transform(x_test)

            logging.info("Transform the Train data into the array using the transformer.")
            logging.info("Transform the Test data into the arr using the preprocessor.")

            return (x_train_arr,y_train,x_test_arr,y_test)


        except Exception as e:
            raise CustomException(e)



        
    
