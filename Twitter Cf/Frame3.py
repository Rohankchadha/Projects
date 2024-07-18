from tkinter import *
from tkinter import messagebox
import Frame2
import Frame1

class frame3:

    def delete1(self):
        pass

    def delete2(self):
        pass

    def logout(self):
        self.fr3.destroy()
        obj = Frame1.frame1(self.root)
        obj.create1()

    def back(self):
        self.fr3.destroy()
        obj = Frame2.frame2(self.root)
        obj.create2()

    def __init__(self, root=""):
        if (root == ""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Welcome to Object Section")
        self.root.geometry("1000x500+250+120")

    def create3(self):
        self.fr3 = Frame(self.root)
        self.fr3.place(x=0, y=0, width=1000, height=500)
        self.fr3.config(bg="black")

        self.lbl = Label(self.fr3, text="HASHTAG")
        self.lbl.place(x=20, y=20, width=250, height=40)
        self.lbl.config(font=('Times New Roman', 30, 'bold'), bg="black", fg="white")

        self.lbl1 = Label(self.fr3, text="Object 1")
        self.lbl1.place(x=40,y=100,width=100,height=40)
        self.lbl1.config(font=('Bell MT',20,'bold'), fg="white", bg="black")

        self.btn1 = Button(self.fr3, text="Chg")
        self.btn1.place(x=70, y=150, width=60, height=30)
        self.btn1.config(font=('Bell MT',15, 'bold'), fg="white", bg="navy blue")

        self.btn2 = Button(self.fr3, text="Data")
        self.btn2.place(x=160, y=150, width=80, height=30)
        self.btn2.config(font=('Bell MT', 15, 'bold'), fg="white", bg="navy blue")

        self.btn3 = Button(self.fr3, text="Block")
        self.btn3.place(x=270, y=150, width=70, height=30)
        self.btn3.config(font=('Bell MT', 15, 'bold'), fg="white", bg="navy blue")

        self.btn4 = Button(self.fr3, text="Delete", command=self.delete1)
        self.btn4.place(x=370, y=150, width=70, height=30)
        self.btn4.config(font=('Bell MT', 15, 'bold'), fg="white", bg="red")

        self.lbl2 = Label(self.fr3, text="Object 2")
        self.lbl2.place(x=40,y=250,width=120,height=40)
        self.lbl2.config(font=('Bell MT', 20, 'bold'), fg="white", bg="black")

        self.btn1 = Button(self.fr3, text="Chg")
        self.btn1.place(x=70, y=300, width=60, height=30)
        self.btn1.config(font=('Bell MT', 15, 'bold'), fg="white", bg="navy blue")

        self.btn1 = Button(self.fr3, text="Data")
        self.btn1.place(x=160, y=300, width=80, height=30)
        self.btn1.config(font=('Bell MT', 15, 'bold'), fg="white", bg="navy blue")

        self.btn1 = Button(self.fr3, text="Block")
        self.btn1.place(x=270, y=300, width=70, height=30)
        self.btn1.config(font=('Bell MT', 15, 'bold'), fg="white", bg="navy blue")

        self.btn1 = Button(self.fr3, text="Delete", command=self.delete2)
        self.btn1.place(x=370, y=300, width=70, height=30)
        self.btn1.config(font=('Bell MT', 15, 'bold'), fg="white", bg="red")

        self.btn = Button(self.fr3, text="Logout", command=self.logout)
        self.btn.place(x=900, y=20, width=80, height=30)
        self.btn.config(fg="white", bg="red")

        self.btn = Button(self.fr3, text="Back", command=self.back)
        self.btn.place(x=800, y=20, width=80, height=30)
        self.btn.config(fg="white", bg="navy blue")

if __name__== '__main__':
    obj = frame3()
    obj.create3()
    obj.root.mainloop()