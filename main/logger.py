import datetime


def save_error_log(exception, file, method, message=None):
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
    return write_to_db("RPI-health", data)


def write_to_db(db_name, data):
    try:
        from firebase import firebase
        firebase = firebase.FirebaseApplication(
            "https://me-arash.firebaseio.com/", None)
        return firebase.post('/' + db_name + '/', data)
    except Exception as e:
        save_error_log(e, "Health/wrapper.py", "write_to_db")
