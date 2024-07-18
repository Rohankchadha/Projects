import speech_recognition as sr
from tkinter import filedialog
import subprocess,os
import Frame1,process
recording = sr.Recognizer()
with sr.Microphone() as source: 
    recording.adjust_for_ambient_noise(source)
    print("Please Say something:")
    audio = recording.listen(source)
try:
   print("You said: \n" + recording.recognize_google(audio))
   a=recording.recognize_google(audio)
   if 'post' or 'upload' in a:
      if 'Instagram' in a:
         print("you need to login first")
         print(os.path.abspath('Frame1.py'))
         subprocess.call(['python', os.path.abspath('Frame1.py')])
         # file=filedialog.askopenfile()

except Exception as e:
   print(e)