from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import dataBase,view_daily
from datetime import date
import home
class task:
    def __init__(self):
        self.root = Tk()

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.width = int((self.width-800)/2)
        self.height = int((self.height-600)/2)
        # 'width x height'+ 'x' + 'y'
        s = '800x600+'+str(self.width)+"+"+str(self.height)
        self.root.geometry(s)
        self.root.resizable(False,False)

    def task_data(self,data):
        self.data = data
        print("i am data",data)
        self.task_fr = Frame(self.root,bg="white")
        self.task_fr.place(x=0,y=0,width=400,height=600)

        #labels
        self.tit=Label(self.task_fr,text="DAILY TASK",bg="white",font=('Cambria',25,'bold'))
        self.tit.place(x=100,y=20,width=200,height=60)
        
        self.lab1=Label(self.task_fr,text="TASK NAME",bg="white",font=('Cambria',18))
        self.lab1.place(x=20,y=80,width=150,height=30)

        self.lab2=Label(self.task_fr,text="DESCRIPTION",bg="white",font=('Cambria',18))
        self.lab2.place(x=20,y=170,width=190,height=30)

        self.lab3=Label(self.task_fr,text="STARTED DATE",bg="white",font=('Cambria',18))
        self.lab3.place(x=20,y=260,width=190,height=30)

        self.lab4=Label(self.task_fr,text="END DATE",bg="white",font=('Cambria',18))
        self.lab4.place(x=20,y=350,width=130,height=30)

        self.lab5=Label(self.task_fr,text="Priority",bg="white",font=('Cambria',18))
        self.lab5.place(x=20,y=440,width=130,height=30)
        #ENTRY
        self.first_en=Entry(self.task_fr,bd=2)
        self.first_en.place(x=40,y=120,width=250,height=35)

        self.sec_en=Entry(self.task_fr,bd=2)
        self.sec_en.place(x=40,y=200,width=250,height=35)

        self.today = date.today()
        self.thir_en=DateEntry(self.task_fr,bd=2,date_pattern='yyyy/mm/dd',mindate = self.today)
        self.thir_en.place(x=40,y=300,width=250,height=35)

        self.four_en=DateEntry(self.task_fr,bd=2,date_pattern='yyyy/mm/dd',mindate = self.today)
        self.four_en.place(x=40,y=390 ,width=250,height=35)

        self.five_en=ttk.Combobox(self.task_fr,state="readonly",values=('Important','Intermediate','Normal'))
        self.five_en.place(x=40,y=480 ,width=250,height=35)
        
        #button
        self.btn=Button(self.task_fr,text="Cave(IN)",command=self.create,bg="black",fg="white",font=('Cambria',18))
        self.btn.place(x=50,y=540,width=150,height=40)
        
        self.img = Image.open('img/dtask.jpg')
        self.resize_img = self.img.resize((800,600))
        self.img1 = ImageTk.PhotoImage(self.resize_img)
        self.lab = Label(self.root,image=self.img1)
        self.lab.place(x=400,y=0)

        
        self.btn = Button(self.task_fr,text="Back",command=self.back,bg="black",fg="white",font=('Cambria',18))
        self.btn.place(x =210,y=540,width=150,height=40)


        self.root.mainloop()
        
    def back(self):
        self.root.destroy() 
        obj = home.menubar()
        obj.firstFrame(self.data)
    
    def create(self):

        data = (
            self.data[0],
            self.first_en.get(),
            self.sec_en.get(),
            self.thir_en.get(),
            self.four_en.get(),
            self.five_en.get()
       )

        if(self.first_en.get() ==""):
            messagebox.showinfo('Alert','Enter your name' )
        elif(self.sec_en.get() ==""):
            messagebox.showinfo('Alert', 'Enter your gender')
        elif (self.thir_en.get() == ''):
            messagebox.showinfo('Alert', 'Enter your contact no')
        elif (self.four_en.get() == ''):
            messagebox.showinfo('Alert', 'Enter email ID')
        elif (self.five_en.get() == ''):
            messagebox.showinfo('Alert', 'Enter Importanece level. ')
        else:
            print(data)
            res  = dataBase.addtask(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Task added successfully.')
                self.root.destroy()
                obj = view_daily.daily()
                obj.daily_task(data)
            else:
                messagebox.showinfo('Alert', 'something went wrong')

if __name__=='__main__':
    obj = task()
    obj.task_data('data')


