import firebase_admin
from firebase_admin import credentials
from tkinter import filedialog

cred = credentials.Certificate(filedialog.askopenfilename())
firebase_admin.initialize_app(cred)