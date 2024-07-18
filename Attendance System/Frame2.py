from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os,cv2,shutil,datetime
import process,Frame2

class Frame1:   
    name='' 
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("600x600+200+30")
        
    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")

        # self.label = Label(self.fr1, text="Syyyyystem")
        # self.label.place(x=365,y=240,width=300,height=70)
        # self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        # self.txt = Label(self.fr1, text="Paste URL")
        # self.txt.place(x=220,y=195)
        # self.txt.config(bg="black", fg="white")
        # self.ent = Entry(self.fr1)
        # self.ent.place(x=320, y=190, width=380, height=30)
        # self.btn = Button(self.fr1, text="Process", command=lambda: self.process(self.ent.get()))
        # self.btn.config( font=(20),fg="white", bg="navy blue")
        # self.btn.place(x=400,y=320,width=220,height=50)
        self.image=Image.open(r'check\datafile.jpg')
        self.image.save(r'check\datafile.png')
        self.img=PhotoImage(file='check/datafile.png')
        self.lbl=Label(self.fr1, image=self.img)
        self.lbl.place(x=200,y=150,width=200,height=200)
        self.lbl.image=self.img
        data=self.name.split(',')

        self.label = Label(self.fr1, text=data[0])
        self.label.place(x=200,y=380,width=200,height=40)
        self.label.config(font=('Times New Roman',24,'bold'),bg="black",fg="white")
        self.label = Label(self.fr1, text=data[1])
        self.label.place(x=200,y=420,width=200,height=40)
        self.label.config(font=('Times New Roman',24,'bold'),bg="black",fg="white")
        self.label = Label(self.fr1, text=data[2])
        self.label.place(x=200,y=460,width=200,height=40)
        self.label.config(font=('Times New Roman',24,'bold'),bg="black",fg="white")

        self.btn2 = Label(self.fr1, text="Marked Present")
        self.btn2.config(font=(20),fg="white", bg="green")
        self.btn2.place(x=140,y=520,width=320,height=40)
        a=datetime.datetime.now()
        self.btn3 = Label(self.fr1, text=a)
        self.btn3.config(font=('BellMT',16,'bold'),fg="white", bg="green")
        self.btn3.place(x=140,y=560,width=320,height=40)
        self.root.after(7000,lambda:exit())
if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()

# image=Image.open(r'F:\Back-End\Projects\Python projects\Attendance System\check\datafile.jpg')
# image=image.resize((300,300))
# image.show()