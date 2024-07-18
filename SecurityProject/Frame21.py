from tkinter import *
from tkinter import messagebox
from mega import Mega
from tkinter import filedialog
import webbrowser
import Frame2
import Frame22

class frame21():
    def login(self):
        userfile = open("newfile.txt", "w")
        userfile.write(self.txt1.get())
        userfile.close()
        passfile = open("newfile1.txt", "w")
        passfile.write(self.pas1.get())
        passfile.close()
        if(self.txt1.get()!=""):
            try:
                mega = Mega()
                m = mega.login(self.txt1.get(), self.pas1.get())
                details = m.get_user()
                self.fr21.destroy()
                obj = Frame22.frame22(self.root)
                obj.create22()
            except:
                messagebox.showerror("Attention", "Please check username and password again")
        else:
            messagebox.showerror("HASHTAG", "Please enter username and password")

    def create(self):
        webbrowser.open(url="https://mega.nz/register")
    def quit(self):
        yesno = messagebox.askyesno("MEGA", "Are you sure?")
        if(yesno):
            self.fr21.destroy()
            obj=Frame2.frame2(self.root)
            obj.create2()

    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Welcome")
        self.root.geometry("1000x500+250+120")


    def create21(self):
        self.fr21 = Frame(self.root)
        self.fr21.place(x=0, y=0, width=1000, height=500)
        self.fr21.config(bg="black")

        self.label = Label(self.fr21, text="MEGA")
        self.label.place(x=365,y=40,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.txt = Label(self.fr21, text="USERNAME")
        self.txt.place(x=220,y=165)
        self.txt.config(bg="black", fg="white")
        self.txt1 = Entry(self.fr21)
        self.txt1.place(x=320, y=160, width=380, height=30)

        self.pas = Label(self.fr21, text="PASSWORD")
        self.pas.place(x=220,y=228)
        self.pas.config(bg="black", fg="white")
        self.pas1 = Entry(self.fr21, show="*")
        self.pas1.place(x=320, y=223, width=380, height=30)

        self.btn = Button(self.fr21, text="Login", command=self.login)
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=300,width=220,height=50)

        self.btn1 = Button(self.fr21, text="Create", command=self.create)
        self.btn1.config(font=(20),fg="black", bg="white")
        self.btn1.place(x=400,y=360,width=220,height=50)

        self.btn1 = Button(self.fr21, text="Back", command=self.quit)
        self.btn1.config(font=(20), fg="white", bg="red")
        self.btn1.place(x=400, y=420, width=220, height=50)

if __name__== '__main__':
    obj = frame21()
    obj.create21()
    obj.root.mainloop()