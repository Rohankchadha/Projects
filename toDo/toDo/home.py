from tkinter import *
from PIL import Image, ImageTk
import dataBase,add_task,three_days
import view_daily,date_view
from datetime import date
class menubar:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Menu Demonstration')

        # Creating Menubar
        menubar = Menu(self.root)
        
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def firstFrame(self, data):

        self.data = data

         # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="350", height="500")
        
        self.homeLabel = Label(self.mainFrame, text="WELCOME!",bg = 'white',fg = 'black',font = ("Bell MT","20","bold italic"),highlightbackground="white",highlightthickness= 1)
        self.homeLabel.place(x = 20, y = 40, width="200")
        
        self.menulabel = Label(self.root, text="All Tasks :",bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
        self.menulabel.place(x = 0, y = 160, width="300")

        arg = (self.data[0],)
        self.label = Label(self.root, text= len(dataBase.view_tasks(arg)),bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
        self.label.place(x = 250, y = 160, width="30")

        self.Tasklabel = Label(self.root, text="Today:",bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
        self.Tasklabel.place(x = 0, y = 220, width="300")

        today = date.today()
        all = (self.data[0],today)
        self.label = Label(self.root, text=len(dataBase.view_today(all)),bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
        self.label.place(x = 220, y = 220, width="50")

        # self.Todaylabel = Label(self.root, text="Todays :",bg = 'white',fg = 'black',font = ("Imprint MT Shadow","25","bold italic"),highlightbackground="white",highlightthickness= 1)
        # self.Todaylabel.place(x = 0, y = 280, width="340")


        # set background image
        self.img=Image.open('img/h.jpg')
        self.resize_image = self.img.resize((450, 500))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.bgLabel = Label(self.root, image=self.image)
        self.bgLabel.config(bg="white")
        self.bgLabel.place(x = 350, y = 0)
       
       
        menubar=Menu(self.mainFrame)
        # Adding food types Menu and commands

        Booking = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Task', menu = Booking)
        Booking.add_command(label ='Add Task', command = self.opentask)
        Booking.add_command(label ='schedule', command = self.openManagetask)

        # Adding food Menu and commands
        
        menubar.add_command(label="Today Tasks",command=self.opendailytask)
        menubar.add_command(label="Tasks Details",command=self.openthreetask)
       
        menubar.add_command(label="Logout",command=self.root.destroy)

        # display Menu
        self.root.config(menu = menubar)
        self.root.mainloop()
        
    def openAddkitchen(self):
        # self.root.destroy()
        # obj =kitchen_add.add_kitchen_items()
        # obj.firstFrame()
        pass

    def opentask(self):
        self.root.destroy()
        obj = add_task.task()
        obj.task_data(self.data)

    def openthreetask(self):
        self.root.destroy()
        obj = three_days.daily()
        obj.daily_task(self.data)

    def openManagetask(self):
        self.root.destroy()
        obj = view_daily.daily()
        obj.daily_task(self.data)
    

    def opendailytask(self):
        self.root.destroy()
        obj = date_view.daily()
        obj.daily_task(self.data)

    def openManagefood(self):
    #     self.root.destroy()
    #     obj =Room.add_floor()
    #     obj.firstFrame()
        pass
    

if __name__ == '__main__':
    obj = menubar()
    obj.firstFrame('data')