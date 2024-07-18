from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import process, Frame2

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1000x600+200+30")

    def process(self,a):
        data,ret=process.get_data(a)
        print(data)
        print(len(data))
        print(data[0:17])
        if ret:
            messagebox.showinfo("Attention", "Screenshots Saved\nYou can access them in data folder")
            Frame2.Frame2.data = data
            obj=Frame2.Frame2(self.root)
            obj.create2()
        else:
            messagebox.showerror("Warning", "Age restricted or private video")
        
    def next(self):
        self.fr1.destroy()
        obj=Frame2.Frame2(self.root)
        obj.create2()

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="YTD")
        self.label.place(x=365,y=40,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.txt = Label(self.fr1, text="Paste URL")
        self.txt.place(x=220,y=195)
        self.txt.config(bg="black", fg="white")
        self.ent = Entry(self.fr1)
        self.ent.place(x=320, y=190, width=380, height=30)
        self.btn = Button(self.fr1, text="Process", command=lambda: self.process(self.ent.get()))
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=320,width=220,height=50)
        self.btn1 = Button(self.fr1, text="Quit", command=self.next)
        self.btn1.config(font=(20),fg="white", bg="red")
        self.btn1.place(x=400,y=390,width=220,height=50)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()