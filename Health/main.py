from wrapper import *
from health_information import *
import time
import sys
import os

sys.path.append("/home/arash/work/IOT/Health/venv/lib/python3.7/site-packages/")
os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
# Todo: Error handling...

while (True):
    try:
        interval = get_check_interval()
        data = provide_info()
        write_to_db(data)
        print(str(data))
        time.sleep(interval)
    except Exception as e:
        print(str(e))
        time.sleep(interval)
