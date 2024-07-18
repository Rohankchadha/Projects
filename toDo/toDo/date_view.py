from tkinter import *
from tkinter import messagebox
import dataBase
import dataBase
from datetime import date
import home
from tkcalendar import DateEntry
class daily():
    def __init__(self):
        self.root = Tk()
        self.root.title('Today tasks')

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()


        self.width = int((self.width-800)/2)
        self.height = int((self.height-500)/2)
        s = '800x500+'+str(self.width)+"+"+str(self.height)

        self.root.resizable(height=False,width=False)
        self.root.config(bg="white")
        self.root.geometry(s)
        
    def daily_task(self,data):
        self.data = data
        self.fr2 = Frame(self.root, bg="white")
        self.fr2.place(x=0, y=30, width="800", height="400")

        # today_date = date.today()
        # print(today_date)


        self.combodate = DateEntry(self.root,date_pattern='yyyy/mm/dd')
        self.combodate.pack()
        self.combodate.bind("<<DateEntrySelected>>", self.maindata)

        print("hello",self.combodate.get())
        # self.combodate.delete(0, 'ed')
        self.combodate.delete(0,'end')

        
        self.text = Label(self.fr2,text="Select Date",font=("Segoe Script",20,'bold'))
        self.text.config(width=800,height=800,highlightbackground = "black", 
                        highlightthickness = 2, bd=0,bg="white")
        self.text.pack()
                    
        self.btn = Button(self.root,text="Back",command=self.back,bg="black",fg="white",font=('Cambria',18))
        self.btn.place(x =450,y=440,width=150,height=40)

        self.btn=Button(self.root,text="Update",command=self.create,bg="black",fg="white",font=('Cambria',18))
        self.btn.place(x=280,y=440,width=150,height=40)

        self.taskList = []
        self.root.mainloop()
        

    def getTask(self, x, y):
        print(x)
        if globals()[f'self.v{y}'].get() == 1:
            self.taskList.append(x)
        else:
            self.taskList.remove(x)
        print("helloo",self.taskList)
        


    def back(self):
        self.root.destroy() 
        obj = home.menubar()
        obj.firstFrame(self.data) 

    def create(self):
        if len(self.taskList) > 0:
            for i in self.taskList:
                res = dataBase.updateStatus(i)
                if res:
                    messagebox.showinfo('Success', 'Task updated')
                    obj = daily()
                    obj.daily_task(self.data)

                else:
                    messagebox.showerror('Error', 'Something went wrong.')
        else:
            messagebox.showerror('Alert', 'Select task to complete')

    def maindata(self,e):
        self.taskList = []
        
        self.fr1 = Frame(self.root, bg="white")
        self.fr1.place(x=0, y=30, width="500", height="400")

        self.fr3 = Frame(self.root, bg="white")
        self.fr3.place(x=500, y=30, width="300", height="400")

        print(self.fr2.winfo_children())
        for i in self.fr2.winfo_children():
            i.destroy()

        self.h = Scrollbar(self.fr1,orient='vertical')
        self.h.pack(side=RIGHT,fill='y')

        value = (self.data[0],self.combodate.get())
        print(value)
        self.today_view = dataBase.view_today(value)
        print("today",self.today_view)
        if self.today_view:
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

            self.side_text = Label(self.fr3,text="Report File",font=("Segoe Script",20,'bold'),bg="white")
            self.side_text.pack()

            self.Tasklabel = Label(self.fr3, text="Total Tasks:",bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
            self.Tasklabel.pack()

            all = (self.data[0],self.combodate.get(),)
            self.label = Label(self.fr3, text=len(dataBase.view_today(all)),bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
            self.label.pack()

            self.menulabel = Label(self.fr3, text="Completed Tasks :",bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
            self.menulabel.pack()

            arg = (self.data[0],self.combodate.get(),)
            print("arg",dataBase.view_completed(arg))
            self.label = Label(self.fr3, text= len(dataBase.view_completed(arg)),bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
            self.label.pack()

            self.menulabel = Label(self.fr3, text="Pending Tasks :",bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
            self.menulabel.pack()

            arg = (self.data[0],self.combodate.get(),)
            print("arg",dataBase.view_pending(arg))
            self.label = Label(self.fr3, text= len(dataBase.view_pending(arg)),bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
            self.label.pack()
        else:
            self.text = Label(self.fr1,text="No Task Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=800,height=800,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()        


        print("jallazlkm",len(self.today_view),"nlk")
        
      
    def back(self):
        self.root.destroy() 
        obj = home.menubar()
        obj.firstFrame(self.data) 


if __name__ == '__main__':
    obj = daily()
    obj.daily_task('data')