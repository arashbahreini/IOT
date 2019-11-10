import datetime
import psutil

# Todo: Error handling...
def get_ram_info():
    ram = psutil.virtual_memory()
    result = {
        "total": ram.total,
        "available": ram.available,
        "used": ram.used
    }
    return result

def provide_info():
    data = {
        "Status": "I am alive",
        "CPU": {
            "Usage": psutil.cpu_percent(),
            "Temprature": "--"
        },
        "RAM": get_ram_info(),
        "time": str(datetime.datetime.now()),
        "success": True,
    }
    return data
