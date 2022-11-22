import logging
from DateTime import DateTime
import os

LOG_DIR= "housing_logs"
CURRENT_TIME_STAMP=f"(DatetTime.now().strftime('%Y-%m-%d_%H-%M_%S'))"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.LOG"
os.makedirs(LOG_DIR)
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicconfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(sctime)s] %(name)s - %(levelname)s-%(message)s',

level=logging.INFO)

