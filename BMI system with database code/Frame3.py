from tkinter import *
import tkinter.ttk as t2
from tkinter import messagebox, filedialog
import cv2
from PIL import ImageTk,Image
import Frame2

class Frame3:   
    data=''
    prfr=''
    cal=0
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1100x700+200+10")

    def back(self):
        self.fr3.destroy()
        obj=Frame2.Frame2(self.root)
        obj.create2()

    def update(self,*a):
        selection=self.sel.get()
        # print(selection)
        y=250
        for i in self.data:
        #    print(i)
            if selection==i[0].split('-')[1]:
                self.val.set(i)
            #    print(type(self.val.get()))
                newvar=self.val.get().strip(')(').split(', ')
        for k in newvar:
            j=k.replace("'","").split('-')
            # print(k)
            # print(j)
            self.lbl = Label(self.fr3, text=j[0])
            self.lbl.place(x=50,y=y,width=150,height=30)
            self.lbl.config(font=('Times New Roman',18,'bold'),bg="black",fg="white")
            self.lbl1 = Label(self.fr3, text=j[1])
            self.lbl1.place(x=50+220,y=y,width=200,height=30)
            self.lbl1.config(font=('Times New Roman',16,'bold'))
            y+=40
           

    def create3(self):
        self.cal=0
        for i in self.data:
            for j in i:
                # print(j.split('-'))
                dta=j.split('-')
                if dta[0]=='Calories':
                    self.cal+=float(dta[1])
        if (self.prfr-self.cal)>0:


            self.fr3 = Frame(self.root)
            self.fr3.place(x=0, y=0, width=1100, height=700)
            self.fr3.config(bg="black")

            self.val=StringVar()
            self.sel=StringVar()

            self.label = Label(self.fr3, text="Nutritionist")
            self.label.place(x=365,y=50,width=300,height=70)
            self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
            # print(self.data)
            # print(type(self.h))
            # print(self.w)
            self.keys=[]
            x=50
            for i in self.data:
                self.keys.append(i[0])

            # print(self.keys)
            self.values=[i.split('-')[1] for i in self.keys]
            # print(self.values)
            # print(self.sel.get())
            # print(self.val.get())
            self.cb=t2.Combobox(self.fr3, textvariable=self.sel, values=self.values)
            self.cb.place(x=100, y=100, width=200, height=30)
            self.sel.trace('w',self.update)
            self.sel.set(self.values[0])
            self.btn=Button(self.fr3, text='back', bg='red', fg='white', command=self.back)
            self.btn.place(x=800, y=100, width=100, height=30)

            self.rmn=round(int(self.prfr)-self.cal,2)

            self.lbl = Label(self.fr3, text='Total Calories consumed')
            self.lbl.place(x=700, y=200+30, width=300, height=40)
            self.lbl.config(font=('Times New Roman',18,'bold'),bg="black",fg="white")
            self.lbl = Label(self.fr3, text=self.cal)
            self.lbl.place(x=800, y=250+30, width=100, height=40)
            self.lbl.config(font=('Times New Roman',14,'bold'),bg="black",fg="white")

            self.lbl = Label(self.fr3, text='Total Calories Target')
            self.lbl.place(x=700, y=320+50, width=300, height=40)
            self.lbl.config(font=('Times New Roman',18,'bold'),bg="black",fg="white")
            self.lbl = Label(self.fr3, text=self.prfr)
            self.lbl.place(x=800, y=370+50, width=100, height=40)
            self.lbl.config(font=('Times New Roman',14,'bold'),bg="black",fg="white")

            self.lbl = Label(self.fr3, text='Total Calories Remaining')
            self.lbl.place(x=700, y=450+70, width=300, height=40)
            self.lbl.config(font=('Times New Roman',18,'bold'),bg="black",fg="white")
            self.lbl = Label(self.fr3, text=self.rmn)
            self.lbl.place(x=800, y=500+70, width=100, height=40)
            self.lbl.config(font=('Times New Roman',14,'bold'),bg="black",fg="white")
        else:
            self.fr3 = Frame(self.root)
            self.fr3.place(x=0, y=0, width=1100, height=700)
            self.fr3.config(bg="red")
            messagebox.showerror("Bas Kar Moteee","Bas kar kitna khaega\nFatega kya?")
        
if __name__== '__main__':
    obj = Frame3()
    obj.create3()
    obj.root.mainloop()