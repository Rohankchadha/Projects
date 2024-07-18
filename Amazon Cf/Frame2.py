from tkinter import *
from tkinter import ttk
# from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter import messagebox
import Frame1
# import Frame21
# import Frame31

class frame2:
    def logout(self):
        a=messagebox.askyesno("HASHTAG", "Are you sure?")
        if(a):
            self.fr2.destroy()
            obj = Frame1.frame1(self.root)
            obj.create1()
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Admin, Welcome to your profile")
        self.root.geometry("1000x700+200+0")


    def create2(self,b,c):
        # print(a)
        # print(b)
        self.fr2 = Frame(self.root)
        self.fr2.place(x=0, y=0, width=1000, height=700)
        self.fr2.config(bg="black")

        #self.img0=PhotoImage(file="black_lock.png")
        #self.lbl0=Label(self.fr2, image=self.img0)
        #self.lbl0.place(x=0, y=0, width=1000, height=500)

        self.lbl = Label(self.fr2, text="AmaZooon")
        self.lbl.place(x=20, y=20, width=250, height=40)
        self.lbl.config(font=('Times New Roman', 30, 'bold'), bg="black", fg="white")

        self.lbl1 = Label(self.fr2, text="Positive Reviews")
        self.lbl1.place(x=80, y=80, width=250, height=40)
        self.lbl1.config(font=('Times New Roman', 15, 'bold'), bg="black", fg="white")
        self.lbl2 = Label(self.fr2, text="Negative Reviews")
        self.lbl2.place(x=580, y=80, width=250, height=40)
        self.lbl2.config(font=('Times New Roman', 15, 'bold'), bg="black", fg="white")

        self.columns = ('1', '2')
        self.tree = ttk.Treeview(self.fr2, columns=self.columns)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('1', width=50, anchor=CENTER)
        self.tree.column('2', width=320)
        # self.tree.column('3', width=80, anchor=CENTER)
        self.tree.heading('1', anchor=CENTER, text='Sr No')
        self.tree.heading('2', anchor=CENTER, text='Reviews')
        # self.tree.heading('3', anchor=CENTER, text='Posted by')
        for i in range(0,len(b)):
            self.tree.insert(parent='',index=i, values=(i,list(b)[i]))
        self.horscrlbar = ttk.Scrollbar(self.tree,orient ="horizontal",command = self.tree.yview)
        self.horscrlbar.pack(side ='bottom', fill ='y')
        self.tree.place(x=50, y=150, width=400, height=500)
        
        self.columns1 = ('1', '2')
        self.tree1 = ttk.Treeview(self.fr2, columns=self.columns1)
        self.tree1.column('#0', width=0, stretch=NO)
        self.tree1.column('1', width=50, anchor=CENTER)
        self.tree1.column('2', width=350)
        # self.tree.column('3', width=80, anchor=CENTER)
        self.tree1.heading('1', anchor=CENTER, text='Sr No')
        self.tree1.heading('2', anchor=CENTER, text='Reviews')
        # self.tree.heading('3', anchor=CENTER, text='Posted by')
        for i in range(0,len(c)):
            self.tree1.insert(parent='',index=i, values=(i,list(c)[i]))
        self.horscrlbar1 = ttk.Scrollbar(self.tree1,orient ="horizontal",command = self.tree.yview)
        self.horscrlbar1.pack(side ='bottom', fill ='y')
        self.tree1.place(x=550, y=150, width=400, height=500)


        # self.lbl = Label(self.fr2, text=a)
        # self.lbl.place(x=20, y=80, width=600, height=300)
        # self.lbl.config(font=('Times New Roman', 12), bg="black", fg="white")
        


if __name__== '__main__':
    obj = frame2()
    obj.create2()
    obj.root.mainloop()