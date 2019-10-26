from wrapper import *
from health_information import *
import time

# Todo: Error handling...
while (True):
    data = provide_info()
    write_to_db(data)
    print(str(data))
    time.sleep(5)
