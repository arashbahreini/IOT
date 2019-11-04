import datetime


def save_error_log(exception, file: str, method: str, message=None):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
    data = {
        "date": datetime.datetime.now(),
        "detail": str(exception),
        "file": file,
        "method": method
    }
    result = firebase.post('/error-logs/rpi', data)
    aaaa = str(result["name"])
    return result
