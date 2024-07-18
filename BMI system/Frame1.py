from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import process, Frame2, Frame3

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1100x700+200+10")

    def process(self):
        # ret,got_data=process.get_data(a)
        h=self.ent1.get()
        w=self.ent2.get()
        ag=self.ent3.get()
        Frame2.Frame2.h=int(h)
        Frame2.Frame2.w=int(w)
        Frame2.Frame2.ag=int(ag)
        obj=Frame2.Frame2(self.root)
        obj.create2()

    def next(self):
        self.fr1.destroy()
        obj=Frame2.Frame2(self.root)
        obj.create2()

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1100, height=700)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="Nutritionist")
        self.label.place(x=365,y=50,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
        self.label = Label(self.fr1, text="Tell me What you ate")
        self.label.place(x=300,y=170,width=400,height=30)
        self.label.config(font=('Times New Roman',24,'bold'),bg="black",fg="white")
        
        self.txt = Label(self.fr1, text="Height(cm)")
        self.txt.place(x=220,y=275)
        self.txt.config(bg="black", fg="white")
        self.ent1 = Entry(self.fr1)
        self.ent1.place(x=320, y=270, width=380, height=30)
        self.txt = Label(self.fr1, text="Weight(kg)")
        self.txt.place(x=220,y=315)
        self.txt.config(bg="black", fg="white")
        self.ent2 = Entry(self.fr1)
        self.ent2.place(x=320, y=310, width=380, height=30)
        self.txt = Label(self.fr1, text="Age(Yrs)")
        self.txt.place(x=220,y=355)
        self.txt.config(bg="black", fg="white")
        self.ent3 = Entry(self.fr1)
        self.ent3.place(x=320, y=350, width=380, height=30)
        self.btn = Button(self.fr1, text="Process", command=lambda: self.process())
        self.btn.config( font=(20),fg="white", bg="navy blue")
        self.btn.place(x=400,y=420,width=220,height=50)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()