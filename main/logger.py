import datetime


def save_error_log(exception, file, method, message=None):
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
    print(str(data))
    # Only use it when application is unable to store logs in db. 
    write_to_file(str(data))
    return 1  # write_to_db("RPI-health", data)

import io
import json
import os

def write_to_file(data):
    # This function should be more smart, if file exist get content, add log and save it. 
    # If file is not exist then create file. 
    file_name = "error-log.json"
    f = open(file_name, 'a+')  
    f.write(data)
    f.close()