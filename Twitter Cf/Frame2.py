from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import Frame1

class frame2:
    def logout(self):
        a=messagebox.askyesno("TUViTTeR", "Are you sure?")
        if(a):
            self.fr2.destroy()
            obj = Frame1.frame1(self.root)
            obj.create1()
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("TUViTTeR")
        self.root.geometry("1000x700+200+0")


    def create2(self,a,b,c,d,e):
        
        self.fr2 = Frame(self.root)
        self.fr2.place(x=0, y=0, width=1000, height=700)
        self.fr2.config(bg="black")

        self.lbl = Label(self.fr2, text="TUViTTeR")
        self.lbl.place(x=20, y=20, width=250, height=40)
        self.lbl.config(font=('Times New Roman', 30, 'bold'), bg="black", fg="white")

        self.btn = Button(self.fr2, text='Back', command=self.logout)
        self.btn.place(x=800, y=20, width=70, height=30)
        self.btn.config(font=('Times New Roman', 15, 'bold'), bg="black", fg="white")

        self.columns = ('1', '2')
        self.tree = ttk.Treeview(self.fr2, columns=self.columns)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('1', width=80, anchor=CENTER)
        self.tree.column('2', width=800)
        self.tree.heading('1', anchor=CENTER, text='Sr No')
        self.tree.heading('2', anchor=CENTER, text='Tweets')
        for i in range(0,len(a)):
            self.tree.insert(parent='',index=i, values=(i,a['Text'][i]))
        self.tree.place(x=20, y=80, width=960, height=500)

        
        self.lbl1=Label(self.fr2, text=c)
        self.lbl1.place(x=50,y=600,width=200,height=50)
        self.lbl1.config(font=('Sans Serif', 13, 'bold'), bg="black", fg="white")
        self.lbl2=Label(self.fr2, text=d)
        self.lbl2.place(x=300,y=600,width=300,height=50)
        self.lbl2.config(font=('Sans Serif', 13, 'bold'), bg="black", fg="white")
        self.lbl3=Label(self.fr2, text=e)
        self.lbl3.place(x=650,y=600,width=300,height=50)
        self.lbl3.config(font=('Sans Serif', 13, 'bold'), bg="black", fg="white")

if __name__== '__main__':
    obj = frame2()
    obj.create2()
    obj.root.mainloop()