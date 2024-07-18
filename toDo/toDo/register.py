from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import dataBase,login
from PIL import Image, ImageTk
class register_page:
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
        self.frame=Frame(self.root,bg="#A1CBD7",bd=4)
        self.frame.place(x=0,y=0,width=450, height=500)

        # heading labels
        # identity labels
        self.tit=Label(self.frame,text="USER REGISTER",bg="#A1CBD7",font=('Arvo',20)) 
        self.tit.place(x=25,y=10, width=350, height=60)

        self.label1=Label(self.frame,text="Name",fg="black",bg="#A1CBD7",font=('Arvo',16))
        self.label1.place(x=20,y=80, width=120, height=30)

        self.label2 = Label(self.root,text="Gender",fg="black",bg="#A1CBD7",font=('Arvo',16))
        self.label2.place(x=20,y=120, width=150, height=30)

        self.label3=Label(self.root,text="Phone Number",fg="black",bg="#A1CBD7",font=('Arvo',16))
        self.label3.place(x=20,y=160, width=200, height=30)

        self.label4=Label(self.frame,text="E-Mail ID",fg="black",bg="#A1CBD7",font=('Arvo',16))
        self.label4.place(x=20,y=200,width=125, height=30)

        self.label=Label(self.frame,text="Password",fg="black",bg="#A1CBD7",font=('Arvo',16))
        self.label.place(x=20,y=240, width=150, height=30)

        self.label=Label(self.frame,text="Confirm Password",fg="black",bg="#A1CBD7",font=('Arvo',16))
        self.label.place(x=20, y=280, width=220, height=30)
        # #entry widgets
        self.nameEntry=Entry(self.frame,bd=2)
        self.nameEntry.place(x=220,y=80,width=200, height=30)

        self.genderEntry=ttk.Combobox(self.frame,state="readonly",values=('Male','Female','other'))
        self.genderEntry.place(x=220,y=120,width=200,height=30)

        self.contactEntry=Entry(self.frame,bd=2)
        self.contactEntry.place(x=220,y=160, width=200, height=30)
        
        self.emailEntry=Entry(self.frame,bd=2)
        self.emailEntry.place(x=220,y=200, width=200, height=30)

        self.passwordEntry=Entry(self.frame,bd=2)
        self.passwordEntry.place(x=220,y=240, width=200, height=30)

        self.confirmEntry=Entry(self.root,bd=2)
        self.confirmEntry.place(x=220, y=280, width=200, height=30)

        self.tit=Label(self.root,text="SIGN UP",bg="#A1CBD7",font=('Arvo',30)) 
        self.tit.place(x=440,y=0, width=320, height=30)
        #Button
        self.btn=Button(self.frame,text="Cave(IN)",bg="black",fg="white",font=('arial',18,'bold'))
        self.btn.place(x=125,y=555)
        
        
        self.img = Image.open('img/reg2.jpg')
        self.resize_img = self.img.resize((350,500))
        self.img1 = ImageTk.PhotoImage(self.resize_img)
        self.lab = Label(self.root,text="SIGN UP",image=self.img1)
        self.lab.place(x=450,y=0)

        self.label1=Label(self.root,text="SIGN UP WITH ",fg="black",bg="#A1CBD7",font=('Arvo',20))
        self.label1.place(x=500,y=30, width=250, height=30)

        self.label3=Label(self.root,text="ORARIO",fg="black",bg="#A1CBD7",font=('Arvo',20))
        self.label3.place(x=500,y=60, width=250, height=30)

        self.btn=Button(self.frame,text="Submit",command=self.create,bg="#D1D1D1",fg="black",font=('arial',18,'bold'))
        self.btn.place(x=100,y=380,width=150,height=40)


        self.root.mainloop()
    
    def create(self):

        data = (
            self.nameEntry.get(),
            self.genderEntry.get(),
            self.contactEntry.get(),
            self.emailEntry.get(),
            self.passwordEntry.get()
       )

        if(self.nameEntry.get() ==""):
            messagebox.showinfo('Alert','Enter your name' )
        elif(self.genderEntry.get() ==""):
            messagebox.showinfo('Alert', 'Enter your gender')
        elif (self.contactEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your contact no')
        elif (self.emailEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter email ID')
        elif (self.passwordEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter password. ')
        elif (self.confirmEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your confirm password')
        elif ((self.nameEntry.get().isdigit())):
            messagebox.showinfo('Alert', 'Enter Valid Name') 
        elif (len(self.contactEntry.get())!=10):
            messagebox.showinfo('Alert', 'Enter 10 Digits ')
        else:
            if self.passwordEntry.get()==self.confirmEntry.get():
                print(data)
                res  = dataBase.addUser(data)
                if res:
                    print(data)
                    messagebox.showinfo('Success', 'Employee added successfully.')
                    self.root.destroy()
                    obj = login.login()
                    obj.log() 
                else:
                    messagebox.showinfo('Alert', 'something went wrong')
            else:
                messagebox.showinfo('Alert', 'password not matched.')


if __name__=='__main__':
    obj=register_page()
    obj.log()
    
