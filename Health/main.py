from wrapper import *
from health_information import *
import time

while (True):
    time.sleep(1)
    data = provide_info()
    write_to_db(data)
    print("Done")
