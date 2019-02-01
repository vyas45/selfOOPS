'''
This is the head, here I get the daily data, connect to DB and store data
'''

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/anikvyas/Desktop/Pers/Code/Projects/selfOOPS/.local/iLife-firebase.json")
firebase_admin.initialize_app(cred)
