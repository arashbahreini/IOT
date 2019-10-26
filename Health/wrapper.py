
def write_to_db(data):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
    firebase.post('/RPI-health/', data)

