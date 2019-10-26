import datetime

def provide_info():
    data = {
        "Status": "I am alive",
        "CPU": {
            "Usage": "10%",
            "Temprature": "100cc"
        },
        "RAM": {
            "Usage": "10%",
            "Temprature": "100cc"
        },
        "time": datetime.datetime.now()
    }

    return data
