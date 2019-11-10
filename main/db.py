import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from logger import *



class Context:
    cred = {}
    def __init__(self):
        cred = credentials.Certificate('me-arash-firebase-adminsdk.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://me-arash.firebaseio.com/'
        })
        print("inited")
    def add(self,path, data):
        try:
            ref = db.reference(path)
            return ref.push(data).key
        except Exception as e:
            print('Error in Context/add')
            print(str(e))
    def delete(self,path,key):
        ref = db.reference(path)
        ref.child(key).delete()
    def update(self):
        pass
    def get(self, path):
        ref = db.reference(path)
        return ref.get()
