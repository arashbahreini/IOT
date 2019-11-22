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
            id = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            doc_ref = self.db_firestore.collection(path).document(id)
            doc_ref.set(data)
            self.update_catalog(path, 'add', id)
            return doc_ref
        except Exception as e:
            save_error_log(e, "db.py", "add(self, " + path +
                           ", " + str(data) + ")", "", True)

    def update_catalog(self, path, operator, id):
        try:
            db_name = 'db-catalogs'
            data = self.get(db_name, path)
            if data:
                data_ref = self.db_firestore.collection(db_name).document(path)
                data_to_update = {
                    "count": int(data['count'] + 1),
                    "last_update": id
                }
                data_ref.update(data_to_update)
            else:
                data = {
                    "count": 1,
                    "last_update": id
                }
                self.db_firestore.collection(db_name).document(path).set(data)
        except Exception as e:
            save_error_log(e, "db.py", "update_catalog(self, " + path +
                           ", " + str(data) + ")", "", True)

    def delete(self, path, key):
        try:
            ref = self.db_firestore.reference(path)
            ref.child(key).delete()
        except Exception as e:
            save_error_log(
                e, "db.py", "delete(self, " + path + ", " + key + ")")

    def update(self):
        pass

    def get(self, collection, document):
        try:
            doc_ref = self.db_firestore.collection(
                collection).document(document)
            return doc_ref.get().to_dict()
        except Exception as e:
            save_error_log(e, "db.py", "get(self, " +
                           collection + "/" + document + ")")
