from logger import *


def write_to_db(db_name, data):
    try:
        from firebase import firebase
        firebase = firebase.FirebaseApplication(
            "https://me-arash.firebaseio.com/", None)
        return firebase.post('/' + db_name + '/', data)
    except Exception as e:
        save_error_log(e, "Health/wrapper.py", "write_to_db")


def get_check_interval():
    try:
        from firebase import firebase
        db = firebase.FirebaseApplication(
            "https://me-arash.firebaseio.com/", None)
        result = db.get(
            "/rpi-setting/-Lt5KH3Bf2TqR80XCWhp/healthCheckPeriod", None)
        return result
    except Exception as e:
        save_error_log(e, "Health/wrapper.py", "get_check_interval",
                       "I have error in get_check_interval method and returing 60 as default.")
        return 60


def write_moisture_to_db(data):
    from firebase import firebase
    firebase = firebase.FirebaseApplication(
        "https://me-arash.firebaseio.com/", None)
    firebase.post('/test-moisture/', data)


# def get_check_interval():
#     from firebase import firebase
#     db = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
#     result = db.get(
#         "/rpi-setting/-Lt5KH3Bf2TqR80XCWhp/healthCheckPeriod", None)
#     return result
