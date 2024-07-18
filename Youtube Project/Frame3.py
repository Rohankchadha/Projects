from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import process, Frame2, db

class Frame3:   
    data='' 
    cnt=0
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1000x600+200+30")
        images=db.view()
        self.data = images.split(',')
        
    def next(self):
        try:
            self.w=50
            self.h=100
            for i in range(self.cnt,self.cnt+18):
                if (self.w<=850 and self.h<=500):
                    self.image=Image.open(self.data[i])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.lbl = Button(self.fr3, image=self.image1, command=lambda:self.get(self.data[i]))
                    self.lbl.place(x=self.w,y=self.h)
                    self.lbl.image=self.image1
                    self.w+=150
                elif(self.w>850 and self.h<=500):
                    self.w=50
                    self.h+=150
                else:
                    break
        except:
            messagebox.showinfo("Attention", "End of images")
        self.cnt+=18


    def create3(self):
        self.fr3 = Frame(self.root)
        self.fr3.place(x=0, y=0, width=1000, height=600)
        self.fr3.config(bg="black")
        try:
            self.w=50
            self.h=100
            if len(self.data)<18:
                length=len(self.data)
            else:
                length=18
            for i in range(0,length):
                if (self.w<=850 and self.h<=500):
                    self.image=Image.open(self.data[i])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.lbl = Button(self.fr3, image=self.image1, command=lambda:self.get(self.data[i]))
                    self.lbl.place(x=self.w,y=self.h)
                    self.lbl.image=self.image1
                    self.w+=150
                elif(self.w>850 and self.h<=500):
                    self.w=50
                    self.h+=150
                else:
                    break
        except:
            messagebox.showinfo("Attention", "End of images")
        self.btn=Button(self.fr3, text='Next', command=self.next)
        self.btn.place(x=900, y=570, width=50, height=20)

if __name__== '__main__':
    obj = Frame3()
    obj.create3()
    obj.root.mainloop()