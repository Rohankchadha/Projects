from tkinter import *
from tkinter import messagebox
import Frame2
import Complaintss

class frame1:
    def login(self):
        # username = self.txt1.get()
        a=Complaintss.process()
        pp,nn=Complaintss.processed(a)

        # print(a['Text'])
        # print(b)
        self.fr1.destroy()
        obj = Frame2.frame2(self.root)
        obj.create2(pp,nn)
        # messagebox.showerror("Attention", "Password is incorrect. Please check username and password again")

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
        self.root.geometry("1000x700+200+0")


    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=700)
        self.ingfr = PhotoImage()
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="AmaZooon")
        self.label.place(x=365,y=90,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.txt = Label(self.fr1, text="USERNAME")
        self.txt.place(x=220,y=290)
        self.txt.config(bg="black", fg="white")
        self.txt1 = Entry(self.fr1)
        self.txt1.place(x=320, y=290, width=380, height=30)

        self.btn = Button(self.fr1, text="Search", command=self.login)
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=380,width=220,height=50)

if __name__== '__main__':
    obj = frame1()
    obj.create1()
    obj.root.mainloop()