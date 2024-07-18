from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import Frame2,Frame3

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Resumer")
        self.root.geometry("1000x600+200+30")

    def process(self,a):
        if(self.value.get()=='Select Pattern') or (self.value1.get()=="Select Content Font") or (self.value2.get()=="Select Heading Font"):
            messagebox.showwarning("Attention", "All fields are mandatory")
        else:
            m=messagebox.askokcancel("Attention","Do you want to select this template ???")
            if m:
                with open('file.txt','w') as file:
                    file.write(a)
                Frame3.Frame3.a=a
                if(self.value.get()=="Row Column Pattern"):
                    Frame3.Frame3.b=1
                else:
                    Frame3.Frame3.b=2
                Frame3.Frame3.fontstyle1="Fonts/"+self.value1.get()+".ttf"
                Frame3.Frame3.fontstyle="Fonts/"+self.value2.get()+".ttf"
                print(Frame3.Frame3.fontstyle)
                self.fr1.destroy()
                obj=Frame2.Frame2(self.root)
                obj.create2()

    
    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="Select Template")
        self.label.place(x=265,y=10,width=400,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.options_list = ["Row Column Pattern", "Row Pattern"]
        self.value=StringVar(self.fr1)
        self.value.set("Select Pattern")
        self.opmenu=OptionMenu(self.fr1,self.value,*self.options_list)
        self.opmenu.place(x=100, y=100, width=200)

        self.options_list1 = ["OpenSans-ExtraBold","Ontario Free"]
        self.value1=StringVar(self.fr1)
        self.value1.set("Select Content Font")
        self.opmenu1=OptionMenu(self.fr1,self.value1,*self.options_list1)
        self.opmenu1.place(x=350, y=100, width=200)

        self.options_list2 = ["Olympia Free","Bluzonir"]
        self.value2=StringVar(self.fr1)
        self.value2.set("Select Heading Font")
        self.opmenu2=OptionMenu(self.fr1,self.value2,*self.options_list2)
        self.opmenu2.place(x=600, y=100, width=200)

        self.photo1=Image.open('Images/x1.png').convert("RGBA")
        self.photo1=self.photo1.resize((150,180))
        self.photo1=ImageTk.PhotoImage(self.photo1)
        self.var1='Images/x1.png'
        self.btn1 = Button(self.fr1, text='1', image=self.photo1, command=lambda: self.process(self.var1))
        self.btn1.place(x=100, y=170, width=150, height=180)

        self.photo2=Image.open('Images/x2.png').convert("RGBA")
        self.photo2=self.photo2.resize((150,180))
        self.photo2=ImageTk.PhotoImage(self.photo2)
        self.var2='Images/x2.png'
        self.btn2 = Button(self.fr1, text='', image=self.photo2, command=lambda: self.process(self.var2))
        self.btn2.place(x=300, y=170, width=150, height=180)

        self.photo3=Image.open('Images/x3.png').convert("RGBA")
        self.photo3=self.photo3.resize((150,180))
        self.photo3=ImageTk.PhotoImage(self.photo3)
        self.var3='Images/x3.png'
        self.btn3 = Button(self.fr1, text='', image=self.photo3, command=lambda: self.process(self.var3))
        self.btn3.place(x=500, y=170, width=150, height=180)

        self.photo4=Image.open('Images/x4.png').convert("RGBA")
        self.photo4=self.photo4.resize((150,180))
        self.photo4=ImageTk.PhotoImage(self.photo4)
        self.var4='Images/x4.png'
        self.btn4 = Button(self.fr1, text='', image=self.photo4, command=lambda: self.process(self.var4))
        self.btn4.place(x=700, y=170, width=150, height=180)

        self.photo5=Image.open('Images/x5.png').convert("RGBA")
        self.photo5=self.photo5.resize((150,180))
        self.photo5=ImageTk.PhotoImage(self.photo5)
        self.var5='Images/x5.png'
        self.btn5 = Button(self.fr1, text='', image=self.photo5, command=lambda: self.process(self.var5))
        self.btn5.place(x=100, y=400, width=150, height=180)

        self.photo6=Image.open('Images/x6.png').convert("RGBA")
        self.photo6=self.photo6.resize((150,180))
        self.photo6=ImageTk.PhotoImage(self.photo6)
        self.var6='Images/x6.png'
        self.btn6 = Button(self.fr1, text='', image=self.photo6, command=lambda: self.process(self.var6))
        self.btn6.place(x=300, y=400, width=150, height=180)

        self.photo7=Image.open('Images/x7.png').convert("RGBA")
        self.photo7=self.photo7.resize((150,180))
        self.photo7=ImageTk.PhotoImage(self.photo7)
        self.var7='Images/x7.png'
        self.btn7 = Button(self.fr1, text='', image=self.photo7, command=lambda: self.process(self.var7))
        self.btn7.place(x=500, y=400, width=150, height=180)

        self.photo8=Image.open('Images/x8.png').convert("RGBA")
        self.photo8=self.photo8.resize((150,180))
        self.photo8=ImageTk.PhotoImage(self.photo8)
        self.var8='Images/x8.png'
        self.btn8 = Button(self.fr1, text='', image=self.photo8, command=lambda: self.process(self.var8))
        self.btn8.place(x=700, y=400, width=150, height=180)


if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()