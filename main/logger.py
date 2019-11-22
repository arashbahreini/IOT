import io
import os
import json
import datetime

def save_error_log(exception, file, method, message=None, cache_it=False):
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
    print(str(data))
    # Only use it when application is unable to store logs in db.
    if cache_it:
        write_to_file(str(data))
    else:
        pass

    return 1  # write_to_db("RPI-health", data)



def write_to_file(data):
    # data = {'a':'b'}
    # This function should be more smart, if file exist get content, add log and save it.
    # If file is not exist then create file.
    file_name = "error-log.json"
    f = open(file_name, 'a+')
    f.write(data)
    f.close()
