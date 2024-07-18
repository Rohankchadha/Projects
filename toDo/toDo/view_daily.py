from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import home
import dataBase
import edit_daily_task
import dataBase
class daily():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('daily task')

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()


        self.width = int((self.width-800)/2)
        self.height = int((self.height-500)/2)
        # 'width x height'+ 'x' + 'y'
        s = '800x500+'+str(self.width)+"+"+str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def daily_task(self,data):
        self.data = data
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=25, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'D', 'E','F','G','H'), selectmode="extended")

        self.btn = Button(self.fr,text="back",command=self.back)
        self.btn.place(x =700,y=450,width=50,height=20)

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Task Name")
        self.tr.column('#1', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#2', text="description")
        self.tr.column('#2', minwidth=0, width=160, stretch=NO)

        # self.tr.heading('#3', text="Price")
        # self.tr.column('#3', minwidth=0, width=100, stretch=NO
        self.tr.heading('#3', text="start date")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="end date")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#5', text="importance")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#6', text="Status")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#7', text="edit")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#8', text="delete")
        self.tr.column('#8', minwidth=0, width=100, stretch=NO)

        
        
        self.combodata = ttk.Combobox(self.root,values=('Important','Intermediate','Normal','All Tasks'))
        self.combodata.pack()
        self.combodata.bind("<<ComboboxSelected>>",self.maindata)

        value = (self.data[0],)
        for i in dataBase.view_tasks(value):
            print(i)
            self.tr.insert('', 0, text = i[0], values=(i[2],i[3],i[4],i[5],i[6],i[7],"Edit","Delete"),tags=(i[6]))

        self.h=Scrollbar(self.root, orient='vertical')
        self.h.pack(side=RIGHT, fill='y')

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.tag_configure('Important', background='#FF7F50')
        self.tr.tag_configure('Intermediate', background='#90ee90')
        self.tr.place(x=0, y=0,height=500,width= 800)

        self.root.mainloop() 

    def maindata(self,e):
        for item in self.tr.get_children():
            self.tr.delete(item)

        value = (self.data[0],)
        print(value)

        if self.combodata.get()=="All Tasks":
            for i in dataBase.view_tasks(value):
                print(i)
                self.tr.insert('', 0, text = i[0], values=(i[2],i[3],i[4],i[5],i[6],i[7],"Edit","Delete"),tags=(i[6]))

        elif self.combodata.get()!='Important' or self.combodata.get()!='Intermediate' or self.combodata.get()!='Normal':
            val = self.data[0],self.combodata.get()
            res = dataBase.singleSearch(val)
            for i in res:
                print(res)
                self.tr.insert('', 0, text = i[0], values=(i[2],i[3],i[4],i[5],i[6],i[7],"Edit","Delete"),tags=(i[6]))
            
       


    def back(self):
        self.root.destroy() 
        obj = home.menubar()
        obj.firstFrame(self.data)
        
    def actions(self,e):
        # print("i am e",e)
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'cols {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        print("i am gup",gup)
        if col == '#8':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = dataBase.deleteTask(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = daily()
                    obj.daily_task(self.data)
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#7':
            self.root.destroy()
            obj = edit_daily_task.daily()
            obj.daily_task(gup,self.data)
   
if __name__ == '__main__':
    obj = daily()
    obj.daily_task('data')