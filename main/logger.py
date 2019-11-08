import datetime
from wrapper import write_to_db


def save_error_log(exception, file, method, message=None):
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
    return write_to_db("RPI-health", data)
