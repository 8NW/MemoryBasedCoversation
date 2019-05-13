import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./serviceAccountKey.json")
default_app.initialize_app(cred)
db = firestore.client() 


