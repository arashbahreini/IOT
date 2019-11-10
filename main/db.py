import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from logger import save_error_log


class Context:
    cred = {}

    def __init__(self):
        try:
            cred = credentials.Certificate('me-arash-firebase-adminsdk.json')
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://me-arash.firebaseio.com/'})
        except Exception as e:
            save_error_log(e, "db.py", "__init__(self)")

    def add(self, path, data):
        try:
            ref = db.reference(path)
            return ref.push(data).key
        except Exception as e:
            save_error_log(e, "db.py", "add(self, path, data)")

    def delete(self, path, key):
        try:
            ref = db.reference(path)
            ref.child(key).delete()
        except Exception as e:
            save_error_log(e, "db.py", "delete(self, path, key)")

    def update(self):
        pass

    def get(self, path):
        try:
            ref = db.reference(path)
            return ref.get()
        except Exception as e:
            save_error_log(e, "db.py", "get(self, path)")
