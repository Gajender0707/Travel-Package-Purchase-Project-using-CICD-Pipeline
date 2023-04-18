import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
from logger import logging
from exception import CustomException
from data_transformation import DataTransformationConfig,DataTransformation
from model_trainer import ModelTrainerConfig,ModelTrainer


@dataclass
class DataIngestionConfig:
        data_path=os.path.join("Artifacts","data.csv")
        training_data_path=os.path.join("Artifacts","train.csv")
        testing_data_path=os.path.join("Artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        
    def Initiate_data_ingestion(self):
         logging.info("Data Ingestion Has been Initilize")
         try:
              data=pd.read_csv(r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Tour_Package_Project\data\tour_package.csv")
              logging.info("Read the data successfully")
              os.makedirs(os.path.dirname(self.data_ingestion_config.data_path),exist_ok=True)
              train_data,test_data=train_test_split(data,test_size=0.2,random_state=42)
              data.to_csv(self.data_ingestion_config.data_path)
              train_data.to_csv(self.data_ingestion_config.training_data_path)
              test_data.to_csv(self.data_ingestion_config.testing_data_path)
              logging.info("Data Ingestion Has been Successfully.")

              return (
                   self.data_ingestion_config.training_data_path,
                   self.data_ingestion_config.testing_data_path
              )

         except Exception as e:
              raise CustomException(e)


if __name__=="__main__":
     data_ingestion_obj=DataIngestion()
     train_data_path,test_data_path=data_ingestion_obj.Initiate_data_ingestion()

     data_transformation_obj=DataTransformation()
     x_train_arr,y_train,x_test_arr,y_test=data_transformation_obj.Initiate_data_transformation(train_data_path=train_data_path,test_data_path=test_data_path)

     model_trainer_obj=ModelTrainer()
     model_trainer_obj.Initiate_model_trainer(x_train_arr=x_train_arr,x_test_arr=x_test_arr,y_train=y_train,y_test=y_test)

