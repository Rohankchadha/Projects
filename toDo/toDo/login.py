from tkinter import *
from PIL import Image,ImageTk
import dataBase
import home
from tkinter import messagebox
class login:
    def __init__(self):
        self.root = Tk()

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.width = int((self.width-800)/2)
        self.height = int((self.height-500)/2)
        # 'width x height'+ 'x' + 'y'
        s = '800x500+'+str(self.width)+"+"+str(self.height)
        self.root.geometry(s)
        self.root.resizable(False,False)

    def log(self):
        self.login_fr = Frame(self.root,bg="white")
        self.login_fr.place(x=0,y=0,width=400,height=500)
        #labels
        self.tit=Label(self.login_fr,text="User Login",bg="white",font=('MS Trebuchet',30)) 
        self.tit.place(x=20,y=50,width=350,height=60)
        
        self.lab1=Label(self.login_fr,text="E-Mail Id",bg="white",font=('MS Trebuchet',18,'bold'))
        self.lab1.place(x=40,y=160,width=115,height=30)

        self.lab2=Label(self.login_fr,text="Password",bg="white",font=('MS Trebuchet',18,'bold'))
        self.lab2.place(x=40,y=260,width=138,height=30)
        # self.lab3=Label(self.login_fr,text="CONFIRM PASSWORD")
        # self.lab3.place(x=40,y=350,width=150,height=30)
        #ENTRY
        self.first_en=Entry(self.login_fr,bd=2,bg="white")
        self.first_en.place(x=40,y=200,width=300,height=35)
        self.sec_en=Entry(self.login_fr,bd=2,bg="white")
        self.sec_en.place(x=40,y=300,width=300,height=35)
        # self.thir_en=Entry(self.login_fr,bd=6)
        # self.thir_en.place(x=40,y=400,width=300,height=40)
        #button
        self.btn=Button(self.login_fr,text="Cave(IN)",command=self.create,bg="#D1D1D1",fg="black",font=('arial',18,'bold'))
        self.btn.place(x=100,y=380,width=150,height=40)
        #image widget
        
        self.img = Image.open('img/sch..jpeg')
        self.resize_img = self.img.resize((500,500))
        self.img1 = ImageTk.PhotoImage(self.resize_img)
        self.lab = Label(self.root,image=self.img1)
        self.lab.place(x=400,y=0)

        self.label1=Label(self.root,text="SIGN IN  with ",fg="black",bg="#D1D1D1",font=('MS Trebuchet',20))
        self.label1.place(x=550,y=30, width=250, height=30)

        # self.label2 = Label(self.root,text="E-Mail ",fg="black",bg="#A1CBD7",font=('impact',16))
        # self.label2.place(x=30,y=160, width=150, height=30)

        self.label3=Label(self.root,text="ORARIO",fg="black",bg="#D1D1D1",font=('MS Trebuchet',20))
        self.label3.place(x=550,y=60, width=250, height=30)



        self.root.mainloop()
    
    def create(self):

        data = (
            self.first_en.get(),
            self.sec_en.get()
        )

        if (self.first_en.get() == ''):
            messagebox.showinfo('Alert', 'Enter your user name.')
        elif (self.sec_en.get() == ''):
            messagebox.showinfo('Alert', 'Enter your password.')
        else:
            res= dataBase.login(data)
            if res:
                messagebox.showinfo('Success', 'Login successfully.')
                self.root.destroy()
                obj = home.menubar()
                obj.firstFrame(res)
            else:
                messagebox.showerror("Alert","Invalid Username and/or Password")
     
     

if __name__=='__main__':
    obj = login()
    obj.log()


