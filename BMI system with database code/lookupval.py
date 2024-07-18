from tkinter import *
from tkinter.ttk import *
class Yes:
    a={'a':10,'b':20,'c':30}
    def __init__(self):
        self.root=Tk()
        self.root.geometry('500x500+100+100')
    def vars(self):
        self.fr1=Frame(self.root)
        self.fr1.place(x=0,y=0,width=500,height=500)
        self.sel=StringVar()
        self.dic=self.a
        self.keys=list(sorted(self.dic.keys()))
        self.val=StringVar()
        self.cb=Combobox(self.fr1, textvariable=self.sel, values=self.keys)
        self.cb.place(x=0,y=0,width=200, height=50)
        self.sel.trace('w',self.update)
        self.sel.set(self.keys[0])
        self.lbl=Label(self.fr1, textvariable=self.val)
        self.lbl.place(x=100, y=100, width=100, height=50)
    
    def update(self,*a):
       self.val.set(self.dic[self.sel.get()])

if __name__== '__main__':
    obj = Yes()
    obj.vars()
    obj.root.mainloop()