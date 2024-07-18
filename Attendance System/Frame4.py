# import the opencv library
import cv2,os,shutil
from tkinter import *
from tkinter import messagebox, filedialog
import process

class Frame4:
    face=''    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1000x600+200+30")

    def add(self):
        a=self.ent.get()
        b=self.ent1.get()
        c=self.ent2.get()
        if a!='' and b!='' and c!='':
            crt=process.create(self.face,str(a)+","+str(b)+","+str(c))
            print(crt)

    def create4(self):
        self.fr4 = Frame(self.root)
        self.fr4.place(x=0, y=0, width=1000, height=600)
        self.fr4.config(bg="black")

        self.label = Label(self.fr4, text="Attendance System")
        self.label.place(x=315,y=40,width=400,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.label = Label(self.fr4, text="Enter Details")
        self.label.place(x=315,y=170,width=400,height=40)
        self.label.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        self.txt = Label(self.fr4, text="Name")
        self.txt.place(x=220,y=255)
        self.txt.config(bg="black", fg="white")
        self.ent = Entry(self.fr4)
        self.ent.place(x=320, y=250, width=380, height=30)

        self.txt = Label(self.fr4, text="Class")
        self.txt.place(x=220,y=305)
        self.txt.config(bg="black", fg="white")
        self.ent1 = Entry(self.fr4)
        self.ent1.place(x=320, y=300, width=380, height=30)

        self.txt = Label(self.fr4, text="Roll No")
        self.txt.place(x=220,y=355)
        self.txt.config(bg="black", fg="white")
        self.ent2 = Entry(self.fr4)
        self.ent2.place(x=320, y=350, width=380, height=30)

        # self.btn = Button(self.fr4, text="Process", command=lambda: self.process(self.ent.get()))
        # self.btn.config( font=(20),fg="white", bg="navy blue")
        # self.btn.place(x=400,y=320,width=220,height=50)
        self.btn1 = Button(self.fr4, text="Add Person", command=self.add)
        self.btn1.config(font=(20),fg="white", bg="red")
        self.btn1.place(x=350,y=430,width=320,height=50)
        self.btn2 = Button(self.fr4, text="Exit", command=exit)
        self.btn2.config(font=(20),fg="white", bg="red")
        self.btn2.place(x=350,y=500,width=320,height=40)

if __name__== '__main__':
    obj = Frame4()
    obj.create4()
    obj.root.mainloop()