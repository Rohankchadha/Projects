import face_recognition,os
from tkinter import messagebox,filedialog
known_image = face_recognition.load_image_file(filedialog.askopenfilename())
a=os.listdir('faces')
for i in a:
    unknown_image = face_recognition.load_image_file('faces/'+i)

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    if results[0]:
        print('Found')
    else:
        print('.')
