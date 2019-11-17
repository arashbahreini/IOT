import firebase_admin
from firebase_admin import credentials
from logger import save_error_log
from firebase_admin import firestore
import datetime
import json

class Context:
    cred = {}
    db_firestore = {}

    def __init__(self):
        try:
            cred = credentials.Certificate('me-arash-firebase-adminsdk.json')
            firebase_admin.initialize_app(cred, {
                'projectId': "me-arash",
            })
            self.db_firestore = firestore.client()
        except Exception as e:
            save_error_log(e, "db.py", "__init__(self)")

    def add(self, path, data):
        try:
            doc_ref = self.db_firestore.collection(
                path).document(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
            doc_ref.set(data)
            return doc_ref
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

    def get(self, collection, document):
        try:
            doc_ref = self.db_firestore.collection(collection).document(document)
            return doc_ref.get().to_dict()
        except Exception as e:
            save_error_log(e, "db.py", "get(self, " + collection + "/" + document + ")")
