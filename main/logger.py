import datetime


def save_error_log(exception, file, method, message=None):
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
    print(str(data))
    return 1  # write_to_db("RPI-health", data)
