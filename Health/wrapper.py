
def write_to_db(data):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
    firebase.post('/RPI-health/', data)

def get_check_interval():
    from firebase import firebase
    db = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
    result = db.get("/rpi-setting/health-check-period", None)
    return result;