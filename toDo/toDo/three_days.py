from tkinter import *
from tkinter import messagebox
from turtle import right
import dataBase
import dataBase
from datetime import date,timedelta
import home
class daily():
    def __init__(self):
        self.root = Tk()
        self.root.title('Today tasks')

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()


        self.width = int((self.width-800)/2)
        self.height = int((self.height-500)/2)
        # 'width x height'+ 'x' + 'y'
        s = '800x500+'+str(self.width)+"+"+str(self.height)

        self.root.resizable(height=False,width=False)
        self.root.config(bg="white")
        self.root.geometry(s)
        
        
    def daily_task(self,data):
        self.data = data

        self.fr = Frame(self.root, bg="white",highlightbackground = "black",highlightthickness = 2, bd=5)
        self.fr.place(x=0, y=0, width="260", height="400")

        self.tit=Label(self.fr,text="Yesterday",bg="white",font=('Cambria',25,'bold'))
        self.tit.pack()

        self.fr1 = Frame(self.root, bg="white",highlightbackground = "black",highlightthickness = 2, bd=5)
        self.fr1.place(x=260, y=0, width="270", height="400")

        self.tit=Label(self.fr1,text="Today",bg="white",font=('Cambria',25,'bold'))
        self.tit.pack()

        self.fr2 = Frame(self.root, bg="white",highlightbackground = "black",highlightthickness = 2, bd=5)
        self.fr2.place(x=530, y=0, width="260", height="400")

        self.tit=Label(self.fr2,text="Tomorrow",bg="white",font=('Cambria',25,'bold'))
        self.tit.pack()

        
        today_date = date.today()
        print("Today was: ",today_date)

        yesterday = today_date - timedelta(days = 1)
        print("Yesterday was: ", yesterday)

        Tomorrow = today_date + timedelta(days = 1)
        print("Tomorrow was: ", Tomorrow)
        # self.btn = Button(self.root,text="Back",command=self.back,bg="black",fg="white",font=('Cambria',18))
        # self.btn.place(x =230,y=540,width=150,height=40)
        yesterday = (self.data[0],yesterday)
        today = (self.data[0],today_date)
        Tomorrow = (self.data[0],Tomorrow)

        self.today_view = dataBase.view_today(yesterday)
        print(self.today_view)
        if len(self.today_view)>0:
            for i in range(len(self.today_view)):              
                self.fr6 = Frame(self.fr,highlightbackground = "black",highlightthickness = 2, bd=0)
                self.fr6.pack()
                # print(i)

                globals()[f'self.v{i}'] = IntVar()
                globals()[f'self.text{i}'] = Checkbutton(self.fr6, text = self.today_view[i][2]+"\n"+self.today_view[i][3], variable=globals()[f'self.v{i}'] ,onvalue = 1,font=("Segoe Script",10,'bold'),offvalue = 0, command= lambda x = self.today_view[i][0], y = i: self.getTask(x, y))
                globals()[f'self.text{i}'].config(width=800,height=2,bg="white")
                globals()[f'self.text{i}'].pack() 
                
                if self.today_view[i][7]=='Completed':
                    globals()[f'self.text{i}'].config(bg="#90ee90",state="disabled")
        else:
            self.text = Label(self.fr,text="No Task Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=260,height=40,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()

        self.today_view = dataBase.view_today(today)
        print(self.today_view)
        if len(self.today_view)>0:
            for i in range(len(self.today_view)):            
                self.fr = Frame(self.fr1,highlightbackground = "black",highlightthickness = 2, bd=0)
                self.fr.pack()
                # print(i)

                globals()[f'self.v{i}'] = IntVar()
                globals()[f'self.text{i}'] = Checkbutton(self.fr, text = self.today_view[i][2]+"\n"+self.today_view[i][3], variable=globals()[f'self.v{i}'] ,onvalue = 1,font=("Segoe Script",10,'bold'),offvalue = 0, command= lambda x = self.today_view[i][0], y = i: self.getTask(x, y))
                globals()[f'self.text{i}'].config(width=800,height=2,bg="white")
                globals()[f'self.text{i}'].pack() 
                
                if self.today_view[i][7]=='Completed':
                    globals()[f'self.text{i}'].config(bg="#90ee90",state="disabled")
        else:
            self.text = Label(self.fr1,text="No Task Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=260,height=40,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()

        self.today_view = dataBase.view_today(Tomorrow)
        print(self.today_view)
        if len(self.today_view)>0:
            for i in range(len(self.today_view)):            
                self.fr = Frame(self.fr2,highlightbackground = "black",highlightthickness = 2, bd=0)
                self.fr.pack()
                # print(i)

                globals()[f'self.v{i}'] = IntVar()
                globals()[f'self.text{i}'] = Checkbutton(self.fr, text = self.today_view[i][2]+"\n"+self.today_view[i][3], variable=globals()[f'self.v{i}'] ,onvalue = 1,font=("Segoe Script",10,'bold'),offvalue = 0, command= lambda x = self.today_view[i][0], y = i: self.getTask(x, y))
                globals()[f'self.text{i}'].config(width=800,height=2,bg="white")
                globals()[f'self.text{i}'].pack() 
                
                if self.today_view[i][7]=='Completed':
                    globals()[f'self.text{i}'].config(bg="#90ee90",state="disabled")

        else:
            self.text = Label(self.fr2,text="No Task Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=260,height=40,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()

        self.btn = Button(self.root,text="Back",command=self.back,bg="black",fg="white",font=('Cambria',18))
        self.btn.place(x =350,y=440,width=150,height=40)

        # self.btn=Button(self.root,text="Update",command=self.create,bg="black",fg="white",font=('Cambria',18))
        # self.btn.place(x=250,y=440,width=150,height=40)

        # print("task",self.taskList)
        self.root.mainloop()
        
    def create(self):
        pass

    def back(self):
        self.root.destroy() 
        obj = home.menubar()
        obj.firstFrame(self.data) 

    def getTask(self, x, y):
        self.taskList = []
        print(x)
        if globals()[f'self.v{y}'].get() == 1:
            self.taskList.append(x)
        else:
            self.taskList.remove(x)
        print("helloo",self.taskList)

    def create(self):
        if len(self.taskList) > 0:
            for i in self.taskList:
                res = dataBase.updateStatus(i)
                if res:
                    messagebox.showinfo('Success', 'Task updated')
                else:
                    messagebox.showerror('Error', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Select task to complete')
        

if __name__ == '__main__':
    obj = daily()
    obj.daily_task('data')