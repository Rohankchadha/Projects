from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import process, Frame2

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1000x600+200+30")

    def process(self):
        a,res=process.login(self.ent.get(),self.ent1.get())
        # print(data)
        # print(len(data)
        # print(data[0:17])
        if res:
            messagebox.showinfo("Success", "Login Successfully")
            obj=Frame2.Frame2(self.root)
            obj.create2(a)
        else:
            messagebox.showerror("Warning", a)

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="INSTA")
        self.label.place(x=365,y=40,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.txt = Label(self.fr1, text="Enter Username")
        self.txt.place(x=220,y=195)
        self.txt.config(bg="black", fg="white")
        self.ent = Entry(self.fr1)
        self.ent.place(x=320, y=190, width=380, height=30)
        self.txt1 = Label(self.fr1, text="Enter Password")
        self.txt1.place(x=220,y=245)
        self.txt1.config(bg="black", fg="white")
        self.ent1 = Entry(self.fr1, show="*")
        self.ent1.place(x=320, y=240, width=380, height=30)
        self.btn = Button(self.fr1, text="Process", command=lambda: self.process())
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=320,width=220,height=50)
        self.btn1 = Button(self.fr1, text="Quit")
        self.btn1.config(font=(20),fg="white", bg="red")
        self.btn1.place(x=400,y=390,width=220,height=50)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()