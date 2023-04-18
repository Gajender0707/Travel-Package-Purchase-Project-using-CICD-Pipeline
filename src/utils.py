from logger import logging
from exception import CustomException
import os
import dill


def save_object(object,object_path):
    try:
        with open(object_path,"wb") as f:
            return dill.dump(object,f)

    except Exception as e:
        raise CustomException(e)
    

def load_object(object_path):
    try:
        with open(object_path,"rb") as f:
            return dill.load(f)
    except Exception as e:
        raise CustomException(e)