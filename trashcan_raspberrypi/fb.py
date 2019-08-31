import firebase_admin

from firebase_admin import credentials

from firebase_admin import firestore

from firebase_admin import storage

cred = credentials.Certificate('serviceKey.json')

firebase_admin.initialize_app(cred, {

})
'''
bucket = storage.bucket()

blob = bucket.blob('img1.jpg')

blob.upload_from_filename(filename='img1.png')
print(blob.public_url)
'''

db = firestore.client()


doc_ref = db.collection(u'trashcan').document('7pjZHJSghAQlZh3Bb8TN')
doc_ref.set({
    u'trash': 2,

})