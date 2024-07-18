from tkinter import *
from tkinter import messagebox
import Frame23, Frame3

class Frame22:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Resumer")
        self.root.geometry("1000x650+200+20")

    hp=360
    hp1=360
    var=[]
    var1=[]

    def skip(self):
        Frame3.Frame3.a3 = False
        Frame3.Frame3.data.append({})
        self.fr22.destroy()
        obj=Frame23.Frame23(self.root)
        obj.create23()

    def addnew(self):
        if self.hp<540 and int(self.ent5.get())<4:
            for i in range(6,6+int(self.ent5.get())):
                self.var.append('self.ent'+str(i))
                self.var1.append('self.lbl1'+str(i))
            for i in range(0,len(self.var1)):
                if self.hp<540:
                    self.var1[i]=Entry(self.fr22)
                    self.var1[i].place(x=100, y=self.hp, width=200, height=30)
                    self.var1[i].config(font=('Times New Roman',16,'bold'),bg="white",fg="black")
                    self.hp+=60

            for i in range(0,len(self.var)):
                if self.hp1<540:
                    self.var[i]=Entry(self.fr22)
                    self.var[i].place(x=300, y=self.hp1, width=600, height=30)
                    self.var[i].config(font=('Times New Roman',16,'bold'),bg="white",fg="black")
                    self.hp1+=60
        else:
            messagebox.showwarning('Warning', 'Maximum 3 Fields allowed')
        # print(self.var)

    def getdata(self):
        a=self.ent1.get()
        b=self.ent2.get()
        c=self.ent3.get()
        d=self.ent4.get()
        if a!='' and b!='' and c!='' and d!='':
            data2={'Current Job - ':a,'Past Experience - ':b,'Internship - ':c,'Business - ':d}
            for i in range(0,len(self.var1)):
                if self.var1[i].get()!='' and self.var[i].get()!='':
                    data2.update({self.var1[i].get()+' - ':self.var[i].get()})
                else:
                    messagebox.showwarning('Attention', 'All Fields are mandatory')
                    break
            # print(data)
            Frame3.Frame3.data.append(data2)
            self.fr22.destroy()
            obj=Frame23.Frame23(self.root)
            obj.create23()
        else:
            data={}
            messagebox.showwarning('Attention', 'All Fields are mandatory')
            
    total1=[]
    def callback1(self,key):
        self.total1.append(key.char)
        if len(self.total1)>=100:
            messagebox.showwarning("Attention","Maximun 100 characters are allowed")
    
    total2=[]
    def callback2(self,key):
        self.total2.append(key.char)
        if len(self.total2)>=100:
            messagebox.showwarning("Attention","Maximun 100 characters are allowed")

    total3=[]
    def callback3(self,key):
        self.total3.append(key.char)
        if len(self.total3)>=100:
            messagebox.showwarning("Attention","Maximun 100 characters are allowed")
            
    total4=[]
    def callback4(self,key):
        self.total4.append(key.char)
        if len(self.total4)>=100:
            messagebox.showwarning("Attention","Maximun 100 characters are allowed")

    def create22(self):
        # with open('file.txt','r') as file:
        #     self.a=file.read()
        self.fr22 = Frame(self.root)
        self.fr22.place(x=0, y=0, width=1000, height=650)
        self.fr22.config(bg="black")

        # self.img = Image.open(a).convert("RGBA")
        # self.w, self.h = self.img.size
        # self.screen_width = self.root.winfo_screenwidth()
        # self.screen_height = self.root.winfo_screenheight()
        # self.cw=self.w/2
        # self.ch=self.h/2
        self.lbl=Label(self.fr22, text='Fill Your Professional Information')
        self.lbl.place(x=150, y=50, width=700, height=30)
        self.lbl.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.lbl11=Label(self.fr22, text='Current Job - ')
        self.lbl11.place(x=100, y=120, width=200, height=30)
        self.lbl11.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")

        self.ent1=Entry(self.fr22)
        self.ent1.place(x=300, y=120, width=600, height=30)
        self.ent1.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")
        self.ent1.bind('<Key>',self.callback1)

        self.lbl12=Label(self.fr22, text='Past Experience - ')
        self.lbl12.place(x=100, y=180, width=200, height=30)
        self.lbl12.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")

        self.ent2=Entry(self.fr22)
        self.ent2.place(x=300, y=180, width=600, height=30)
        self.ent2.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")
        self.ent2.bind('<Key>',self.callback2)

        self.lbl13=Label(self.fr22, text='Internship - ')
        self.lbl13.place(x=100, y=240, width=200, height=30)
        self.lbl13.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")

        self.ent3=Entry(self.fr22)
        self.ent3.place(x=300, y=240, width=600, height=30)
        self.ent3.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")
        self.ent3.bind('<Key>',self.callback3)

        self.lbl14=Label(self.fr22, text='Business - ')
        self.lbl14.place(x=100, y=300, width=200, height=30)
        self.lbl14.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")

        self.ent4=Entry(self.fr22)
        self.ent4.place(x=300, y=300, width=600, height=30)
        self.ent4.config(font=('Times New Roman',16,'bold'),bg="white",fg="black")
        self.ent4.bind('<Key>',self.callback4)

        # self.lbl2=Label(self.fr22, text='Work Experience')
        # self.lbl2.place(x=170, y=350, width=300, height=30)
        # self.lbl2.config(font=('Times New Roman',20,'bold'),bg="black",fg="white")

        # self.lbl21=Label(self.fr22, text='Current - ')
        # self.lbl21.place(x=70, y=400, width=100, height=30)

        # self.ent5=Entry(self.fr22)
        # self.ent5.place(x=170, y=400, width=300, height=30)

        # self.lbl22=Label(self.fr22, text='Past - ')
        # self.lbl22.place(x=70, y=450, width=100, height=30)

        # self.ent6=Entry(self.fr22)
        # self.ent6.place(x=170, y=450, width=300, height=30)

        # self.lbl23=Label(self.fr22, text='Internship - ')
        # self.lbl23.place(x=70, y=500, width=100, height=30)

        # self.ent7=Entry(self.fr22)
        # self.ent7.place(x=170, y=500, width=300, height=30)

        # self.lbl24=Label(self.fr22, text='Self - ')
        # self.lbl24.place(x=70, y=550, width=100, height=30)

        # self.ent8=Entry(self.fr22)
        # self.ent8.place(x=170, y=550, width=300, height=30)

        # self.lbl3=Label(self.fr22, text='Education')
        # self.lbl3.place(x=530, y=80, width=300, height=30)
        # self.lbl3.config(font=('Times New Roman',20,'bold'),bg="black",fg="white")

        # self.lbl31=Label(self.fr22, text=' - School')
        # self.lbl31.place(x=830, y=130, width=100, height=30)

        # self.ent9=Entry(self.fr22)
        # self.ent9.place(x=530, y=130, width=300, height=30)

        # self.lbl32=Label(self.fr22, text=' - High School')
        # self.lbl32.place(x=830, y=180, width=100, height=30)

        # self.ent10=Entry(self.fr22)
        # self.ent10.place(x=530, y=180, width=300, height=30)

        # self.lbl33=Label(self.fr22, text=' - College')
        # self.lbl33.place(x=830, y=230, width=100, height=30)

        # self.ent11=Entry(self.fr22)
        # self.ent11.place(x=530, y=230, width=300, height=30)

        # self.lbl34=Label(self.fr22, text=' - University')
        # self.lbl34.place(x=830, y=280, width=100, height=30)

        # self.ent12=Entry(self.fr22)
        # self.ent12.place(x=530, y=280, width=300, height=30)

        # self.lbl4=Label(self.fr22, text='Extra-Curicular')
        # self.lbl4.place(x=530, y=350, width=300, height=30)
        # self.lbl4.config(font=('Times New Roman',20,'bold'),bg="black",fg="white")

        # self.lbl41=Label(self.fr22, text=' - Hobbies')
        # self.lbl41.place(x=830, y=400, width=100, height=30)

        # self.ent13=Entry(self.fr22)
        # self.ent13.place(x=530, y=400, width=300, height=30)

        # self.lbl42=Label(self.fr22, text=' - Sports')
        # self.lbl42.place(x=830, y=450, width=100, height=30)

        # self.ent14=Entry(self.fr22)
        # self.ent14.place(x=530, y=450, width=300, height=30)

        # self.lbl43=Label(self.fr22, text=' - Achievements')
        # self.lbl43.place(x=830, y=500, width=100, height=30)

        # self.ent15=Entry(self.fr22)
        # self.ent15.place(x=530, y=500, width=300, height=30)

        # self.lbl44=Label(self.fr22, text=' - Others')
        # self.lbl44.place(x=830, y=550, width=100, height=30)

        # self.ent16=Entry(self.fr22)
        # self.ent16.place(x=530, y=550, width=300, height=30)

        self.ent5 = Entry(self.fr22)
        self.ent5.place(x=100, y=550, width=550, height=30)
        self.ent5.insert(0, 'Enter no. of Fields (Max. 3)')

        self.btn2 = Button(self.fr22, text='Add no. of new field', command=self.addnew)
        self.btn2.place(x=700, y=550, width=200, height=30)

        self.btn=Button(self.fr22,text='Next >', command=lambda :self.getdata())
        self.btn.place(x=600, y=600, width=300, height=50)

        self.btn1=Button(self.fr22,text='Skip ^', command=lambda :self.skip())
        self.btn1.place(x=100, y=600, width=300, height=50)


if __name__== '__main__':
    obj = Frame22()
    obj.create22()
    obj.root.mainloop()