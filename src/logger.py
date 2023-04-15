import logging
from datetime import datetime
import os

folder=os.path.join(os.getcwd(),"LOGS")
file_name=f"{datetime.now().strftime('%H_%M_%S_%y_%m_%d')}.log"
sub_folder_name=datetime.now().strftime('%H_%M_%S_%y_%m_%d')
sub_folder=os.path.join(folder,sub_folder_name)
os.makedirs(sub_folder,exist_ok=True)
file_location=os.path.join(sub_folder,file_name)



logging.basicConfig(
    filename=file_location,
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s-%(lineno)s- %(message)s",
    level=logging.INFO,
)

# logging.info(f"Files is logging on ")