import datetime
import psutil

# Todo: Error handling...
def get_ram_usage():
    result = abs((psutil.virtual_memory().available / psutil.virtual_memory().total) * 100 - 100)
    return round(result, 2)

def provide_info():
    data = {
        "Status": "I am alive",
        "CPU": {
            "Usage": psutil.cpu_percent(),
            "Temprature": "--"
        },
        "RAM": {
            "Usage": get_ram_usage(),
        },
        "time": datetime.datetime.now()
    }

    return data
