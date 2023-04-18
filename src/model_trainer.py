from logger import logging
from exception import CustomException

import pandas as pd

data_points={
    "Name":["suyesh"],
    "Age":[23]
}

data=pd.DataFrame(data_points)
print(data)