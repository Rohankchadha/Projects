from tkinter import *
import login
import register

class Welcome:
    def __init__(self):
        self.root = Tk()
        #If tkinter doent load image than use Toplevel() instead of Tk()
        self.root.title("Main Page")
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 500) / 2)-50
        s = "800x500+" + str(self.width) + "+" + str(self.height)
        self.root.resizable(height=False, width=False)

        self.root.geometry(s)
    def frame(self):
        self.fra = Frame(self.root, bg='white')
        self.fra.place(x=0, y=0, width="800", height="500")

        # self.img=PhotoImage(file='images/travelhealth.png')
        # self.imglab=Label(self.fra,image=self.img)
        # self.imglab.place(x=0,y=0,width="800",height="500")

        self.btn=Button(self.fra,text="register",bg="Brown",fg="White",font="30",command=self.register)
        self.btn.place(x=150,y=300,width="200",height="50")

        self.btn = Button(self.fra, text="Login", bg="Brown",fg="White",font="30",command=self.Login)
        self.btn.place(x=500, y=300, width="200",height="50")
        self.root.mainloop()

    def register(self):
        self.root.destroy()
        obj = register.register_page()
        obj.log()

    def Login(self):
        self.root.destroy()
        obj1 = login.login()
        obj1.log()
        
if __name__=="__main__":
    obj=Welcome()
    obj.frame()
