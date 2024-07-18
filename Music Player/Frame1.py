from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk,Image
import process, Frame2, login
import shutil

class Frame1:  
    lgn=False  
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1000x600+200+30")

    def back(self):
        self.fr1.destroy()
        obj=Frame2.Frame2(self.root)
        obj.create2()

    def process(self,a):
        print(a)
        ret,data=process.get_data(a)
        print(data)
        if ret:
            messagebox.showinfo("Attention", data)
            self.fr1.destroy()
            obj=Frame2.Frame2(self.root)
            obj.create2()
        else:
            messagebox.showerror("Warning", data)
    
    def login(self):
        self.fr1.destroy
        obj=login.frame1(self.root)
        obj.create1()

    def file(self):
        a=filedialog.askopenfilenames()
        dst='F:/Back-End/Projects/Python projects/Music Player/songs/'
        for i in a:
            if str(i).endswith('.mp3'):
                name=i.split("/")
                # print(name[-1])
                org=i
                shutil.copy(org,dst+name[-1])
        print("added Successfully")
        self.fr1.destroy()
        obj=Frame2.Frame2(self.root)
        obj.create2()
        
    def next(self):
        exit()

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="YTD")
        self.label.place(x=365,y=40,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        if(self.lgn):
            self.txt = Label(self.fr1, text="Paste URL")
            self.txt.place(x=220,y=195)
            self.txt.config(bg="black", fg="white")
            self.ent = Entry(self.fr1)
            self.ent.place(x=320, y=190, width=380, height=30)
            self.btn = Button(self.fr1, text="GO", command=lambda: self.process(self.ent.get()))
            self.btn.config( font=(20),fg="white", bg="navy blue")
            self.btn.place(x=400,y=420,width=220,height=50)
        else:
            self.txt = Label(self.fr1, text="Paste URL")
            self.txt.place(x=220,y=195)
            self.txt.config(bg="black", fg="white")
            self.ent = Label(self.fr1, text="Login to access Youtube Option")
            self.ent.place(x=320, y=190, width=380, height=30)
            self.btn = Button(self.fr1, text="Login First", command=self.login)
            self.btn.config( font=(20),fg="white", bg="navy blue")
            self.btn.place(x=400,y=420,width=220,height=50)
        self.label = Label(self.fr1, text="OR")
        self.label.place(x=365,y=240,width=300,height=40)
        self.label.config(font=('Times New Roman',20,'bold'),bg="black",fg="white")
        self.btn0 = Button(self.fr1, text="Search Music Locally", command=lambda: self.file())
        self.btn0.config( font=(20),fg="white", bg="navy blue")
        self.btn0.place(x=330,y=320,width=370,height=50)
        self.btn1 = Button(self.fr1, text="Quit", command=self.next)
        self.btn1.config(font=(20),fg="white", bg="red")
        self.btn1.place(x=400,y=490,width=220,height=50)
        self.btn2 = Button(self.fr1, text="<", command=self.back)
        self.btn2.config(font=('Times New Roman',26,'bold'),fg="white", bg="red")
        self.btn2.place(x=0,y=0,width=50,height=50)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()