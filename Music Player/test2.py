from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk,Image
import process, Frame2
import shutil

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("490x700+200+30")

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=490, height=700)
        self.fr1.config(bg="black")
        self.img=PhotoImage(file='sphere.gif')
        self.lbl=Label(self.fr1, image=self.img)
        self.lbl.place(x=-5,y=100)

        self.lbl = Label

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.update()
    obj.root.mainloop()