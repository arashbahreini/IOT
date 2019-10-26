
def write_to_db(data):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
    result = firebase.post('/RPI-health/', data)
    print(result)
