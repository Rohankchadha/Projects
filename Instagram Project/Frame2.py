from tkinter import *
from tkinter import messagebox, filedialog
import speech_recognition as sr
from multiprocessing import Process
import cv2,pyttsx3
from PIL import ImageTk,Image
import process
import PySimpleGUI as sg

class Frame2: 
    engine = pyttsx3.init()  
    data=''
    cap=''
    cll=''
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1100x700+200+30")

    def voice(self):
        recording = sr.Recognizer()
        with sr.Microphone() as source: 
            recording.adjust_for_ambient_noise(source)
            self.engine.say("Please speak now")
            self.engine.runAndWait()
            audio = recording.listen(source)
        try:
            print("You said: \n" + recording.recognize_google(audio))
            a=recording.recognize_google(audio)
            if 'Instagram'in a or 'upload'in a or 'change' in a:
                if 'post' in a:
                    self.engine.say("Select the image or video first")
                    self.engine.runAndWait()
                    self.data=filedialog.askopenfilename()
                    self.capt()
                    self.post(self.cll)
                elif 'story' in a:
                    self.engine.say("Select the image or video first")
                    self.engine.runAndWait()
                    self.data=filedialog.askopenfilename()
                    self.capt()
                    self.story(self.cll)
                elif 'profile picture' or 'dp':
                    self.engine.say("Select the image first")
                    self.engine.runAndWait()
                    self.data=filedialog.askopenfilename()
                    self.dpchange(self.cll)
                else:
                    self.engine.say("Command not available")
                    self.engine.runAndWait()
                    self.voice()
            else:
                self.engine.say("Please speak to the mic or enter correct command")
                self.engine.runAndWait()
                self.engine.say("Available commands are")
                self.engine.runAndWait()
                self.engine.say("Upload photo video")
                self.engine.runAndWait()
                self.engine.say("Upload story")
                self.engine.runAndWait()
                self.engine.say("Change Profile Picture")
                self.engine.runAndWait()
                self.voice()
        except Exception as e:
            print(e)

    def capt(self):
        caption=self.ent.get()
        if caption!="":
            self.cap=caption
        else:
            recording = sr.Recognizer()
            with sr.Microphone() as source: 
                recording.adjust_for_ambient_noise(source)
                self.engine.say("Please speak up the caption")
                self.engine.runAndWait()
                audio = recording.listen(source)
            try:
                print("You said: \n" + recording.recognize_google(audio))
                a=recording.recognize_google(audio)
                print(a)
                with sr.Microphone() as source: 
                    recording.adjust_for_ambient_noise(source)
                    self.engine.say("Your caption is "+recording.recognize_google(audio)+". Speak Yes for confirm and No for cancel")
                    self.engine.runAndWait()
                    chk=recording.listen(source)
                if recording.recognize_google(chk)=='Yes':
                    self.cap=a
                elif recording.recognize_google(chk)=='No':
                    self.capt()
            except:
                with sr.Microphone() as source: 
                    recording.adjust_for_ambient_noise(source)
                    chk=recording.listen(source)
                if recording.recognize_google(chk)=='Yes':
                    self.capt()

    def post(self,cl):
        a,res=process.post(cl,self.data,self.cap)
        if res:
            self.engine.say("Posted successfully")
            self.engine.runAndWait()
        else:
            self.engine.say("Choose another picture")
            self.engine.runAndWait()
    def story(self,cl):
        a,res=process.story(cl,self.data,self.cap)
        if res:
            self.engine.say("Posted successfully")
            self.engine.runAndWait()
        else:
            self.engine.say("Choose another picture")
            self.engine.runAndWait()
    def dpchange(self,cl):
        a,res=process.dpchange(cl,self.data)
        if res:
            self.engine.say("Posted successfully")
            self.engine.runAndWait()
        else:
            self.engine.say("Choose another picture")
            self.engine.runAndWait()

    def file(self):
        self.data=filedialog.askopenfilename()
        self.ent1 = Button(self.fr2, text=self.data, command=self.dis)
        self.ent1.place(x=320, y=240, width=380, height=30)

    def dis(self):
        self.ent1 = Button(self.fr2, text="Select a File", command=self.file)
        self.ent1.place(x=320, y=240, width=380, height=30)

    def save(self):
        exit()
    
    def create2(self,cl):
        self.cll=cl
        self.fr2 = Frame(self.root)
        self.fr2.place(x=0, y=0, width=1100, height=700)
        self.fr2.config(bg="black")
        
        self.txt = Label(self.fr2, text="Enter Caption")
        self.txt.place(x=220,y=195)
        self.txt.config(bg="black", fg="white")
        self.ent = Entry(self.fr2)
        self.ent.place(x=320, y=190, width=380, height=30)
        self.txt1 = Label(self.fr2, text="Select Picture")
        self.txt1.place(x=220,y=245)
        self.txt1.config(bg="black", fg="white")
        self.ent1 = Button(self.fr2, text="Select a File", command=self.file)
        self.ent1.place(x=320, y=240, width=380, height=30)

        self.btn = Button(self.fr2, text="Post", command=lambda: self.post(cl))
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=320,width=220,height=50)

        self.btn = Button(self.fr2, text="Voice", command=lambda: self.voice())
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=1000,y=0,width=100,height=50)

if __name__== '__main__':
    obj = Frame2()
    obj.create2()
    obj.root.mainloop()