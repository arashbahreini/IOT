
def write_to_db(data):
    from firebase import firebase
    # /home/arash/work/IOT/Health/venv/lib/python3.7/site-packages
    firebase = firebase.FirebaseApplication("https://me-arash.firebaseio.com/", None)
    firebase.post('/RPI-health/', data)

