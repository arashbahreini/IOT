import datetime
import psutil

# Todo: Error handling...
def get_ram_usage():
    result = 100 - abs(((psutil.virtual_memory().available * 100) / psutil.virtual_memory().total))
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
