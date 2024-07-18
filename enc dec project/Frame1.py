from tkinter import *
from tkinter import messagebox
import Frame2
import db

class frame1:
    def login(self):

        username = self.txt1.get()
        password = self.pas1.get()
        data = (username, password)
        self.a = db.find(data)
        if db.find(data) != None:
            self.fr1.destroy()
            obj = Frame2.frame2(self.root)
            obj.create2()
        else:
            messagebox.showerror("Attention", "Password is incorrect. Please check username and password again")

    def quit(self):
        yesno = messagebox.askyesno("Attention", "Do you really want to quit?")
        if(yesno):
            self.root.quit()

    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Welcome")
        self.root.geometry("1000x500+250+120")


    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=500)
        self.ingfr = PhotoImage()
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="HASHTAG")
        self.label.place(x=365,y=40,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.txt = Label(self.fr1, text="USERNAME")
        self.txt.place(x=220,y=165)
        self.txt.config(bg="black", fg="white")
        self.txt1 = Entry(self.fr1)
        self.txt1.place(x=320, y=160, width=380, height=30)

        self.pas = Label(self.fr1, text="PASSWORD")
        self.pas.place(x=220,y=228)
        self.pas.config(bg="black", fg="white")
        self.pas1 = Entry(self.fr1, show="*")
        self.pas1.place(x=320, y=223, width=380, height=30)
        self.btn = Button(self.fr1, text="Login", command=self.login)
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=320,width=220,height=50)
        self.btn1 = Button(self.fr1, text="Quit", command=self.quit)
        self.btn1.config(font=(20),fg="white", bg="red")
        self.btn1.place(x=400,y=390,width=220,height=50)

if __name__== '__main__':
    obj = frame1()
    obj.create1()
    obj.root.mainloop()