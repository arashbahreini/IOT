import datetime


def save_error_log(exception, file, method, message=None):
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
<<<<<<< HEAD
    print(exception)
    return 1#write_to_db("RPI-health", data)
=======
    return write_to_db("RPI-health", data)

>>>>>>> bd1e317a7ceeccf1269afe90ba622eea0e17a26c

def write_to_db(db_name, data):
    try:
        from firebase import firebase
        firebase = firebase.FirebaseApplication(
            "https://me-arash.firebaseio.com/", None)
        return firebase.post('/' + db_name + '/', data)
    except Exception as e:
        save_error_log(e, "Health/wrapper.py", "write_to_db")
