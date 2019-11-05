import time
import sys
import os
from wrapper import *
from health_information import *
from logger import *

sys.path.append("/home/arash/work/IOT/Health/venv/lib/python3.7/site-packages/")
os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

count = 0
while True:
    count += 1
    if count >= 10:
        os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
        count = 0
    try:
        interval = get_check_interval()
        data = provide_info()
        write_result = write_to_db(data)
        if write_result != None:
            print(str(data))
        else:
            print("Health error")
        time.sleep(interval)
    except Exception as e:
        print(str(e))
        error_id = save_error_log(e, "Health/main.py", "...")
        data = {
            "success": False,
            "error": error_id
        }
        write_to_db(data)
        time.sleep(interval)