import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from logger import save_error_log
from firebase_admin import firestore
import datetime

class Context:
    cred = {}
    db_firestore = {}

    def __init__(self):
        try:
            cred = credentials.Certificate('me-arash-firebase-adminsdk.json')
            # firebase_admin.initialize_app(cred, {
            #     'databaseURL': 'https://me-arash.firebaseio.com/'})
            firebase_admin.initialize_app(cred, {
                'projectId': "me-arash",
            })
            self.db_firestore = firestore.client()
        except Exception as e:
            save_error_log(e, "db.py", "__init__(self)")

    def add(self, path, data):
        try:
            print(path)
            doc_ref = self.db_firestore.collection(u'users').document(u'alovelace')
            # doc_ref = self.db.collection(u'aaa').document(str(datetime.datetime.now()))
            doc_ref.set(data)
            return doc_ref
            # ref = db.reference(path)
            # return ref.push(data).key
        except Exception as e:
            save_error_log(e, "db.py", "add(self, " + path +
                           ", " + str(data) + ")", "", True)

    def delete(self, path, key):
        try:
            ref = db.reference(path)
            ref.child(key).delete()
        except Exception as e:
            save_error_log(
                e, "db.py", "delete(self, " + path + ", " + key + ")")

    def update(self):
        pass

    def get(self, path):
        try:
            ref = db.reference(path)
            return ref.get()
        except Exception as e:
            save_error_log(e, "db.py", "get(self, " + path + ")")
