from tkinter import *
from tkinter import messagebox, filedialog
import speech_recognition as sr
from multiprocessing import Process
import cv2
import PySimpleGUI as sg
import time

def one():
    recording = sr.Recognizer()
    with sr.Microphone() as source: 
            recording.adjust_for_ambient_noise(source)
            audio = recording.listen(source)
    try:
        print("You said: \n" + recording.recognize_google(audio))
    except:
          print('not working')
def one1():
    sg.popup('Please Speak now',auto_close=True, auto_close_duration=5)
if __name__=='__main__':
    a1=Process(target=one)
    a2=Process(target=one1)
    a1.start()
    time.sleep(2)
    a2.start()
    time.sleep(5)
    a2.close()
    a1.close()