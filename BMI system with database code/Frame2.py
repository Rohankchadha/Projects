from tkinter import *
import tkinter.ttk as t2
from tkinter import messagebox, filedialog
import cv2
from PIL import ImageTk,Image
import Frame1, Frame3, process

class Frame2:   
    data=''
    data1=''
    prfr=''
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1100x700+200+10")

    def back(self):
        self.fr2.destroy()
        obj=Frame1.Frame1(self.root)
        obj.create1()

    def bmicheck(self):
        bmi=round(int(self.data1[2])/(int(self.data1[3])/100)**2,2)
        if int(bmi)<18:
            return "orange"
        elif int(bmi)>=18 and int(bmi)<25:
            return "green"
        elif int(bmi)>=25:
            return "red"
        
    def bmrcheck(self):
        bmr=round(10*int(self.data1[2]) + 6.25*int(self.data1[3]) - 5*int(self.data1[1]) + 5,2)
        if int(bmr)<1600:
            return "blue"
        elif int(bmr)>=1600 and int(bmr)<1800:
            return "orange"
        elif int(bmr)>=1800 and int(bmr)<2100:
            return "green"
        elif int(bmr)>=2100:
            return "red"
        
    def fatcheck(self):
        if int(int(self.data1[1]))<=20:
            low=8.00
        elif int(int(self.data1[1]))<=25:
            low=10.00
        elif int(int(self.data1[1]))<=30:
            low=12.00
        elif int(int(self.data1[1]))<=40:
            low=15.00
        high=low+7.00

        fat=self.fat
        if fat<low:
            return "orange"
        elif fat>=low and fat<=high:
            return "green"
        elif fat>high:
            return "red"

    def update(self,*a):
        selection=self.sel.get()
        if selection=="Gain":
            self.prfr=self.gain
        elif selection=="Maintain":
            self.prfr=self.maint
        elif selection=="Fit":
            self.prfr=self.los
        elif selection=="Loose":
            self.prfr=self.loos
        print(self.prfr)
        self.prfr=self.prfr

    def process(self):
        a=self.ent.get()
        ret,got_data=process.get_data(a)

        if ret:
            Frame3.Frame3.data = got_data
            if self.prfr!='':
                messagebox.showinfo("", "Let's explore")
                Frame3.Frame3.prfr=self.prfr
                self.fr2.destroy()
                obj=Frame3.Frame3(self.root)
                obj.create3()
        else:
            messagebox.showerror("Warning", "Data not found")

    def create2(self,data):
        self.data1=data
        self.fr2 = Frame(self.root)
        self.fr2.place(x=0, y=0, width=1100, height=700)
        self.fr2.config(bg="black")

        self.val=StringVar()
        self.sel=StringVar()

        self.txt=Label(self.fr2, text="Enter what you ate")
        self.txt.place(x=100, y=350, width=100, height=30)
        self.txt.config(bg="black", fg="white")
        self.ent = Entry(self.fr2)
        self.ent.place(x=100, y=380, width=380, height=30)

        self.label = Label(self.fr2, text="Nutritionist")
        self.label.place(x=365,y=50,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
        
        self.bmi=round(int(data[2])/(int(data[3])/100)**2,2)
        self.bmr=round(10*int(data[2]) + 6.25*int(data[3]) - 5*int(data[1]) + 5,2)
        self.fat=round(1.20 * self.bmi + 0.23 * int(data[1]) - 16.2,2)
        self.bmii= str("BMI = ")+str(self.bmi)+str(" Points")
        self.bmrr= str("BMR = ")+str(self.bmr)+str(" Calories/Day")
        self.fatt=str("FAT = ")+str(self.fat)+str(" %")
        self.lbl=Label(self.fr2, text=self.bmii, font=('Times New Roman',14,'bold'), bg=self.bmicheck(), fg='white')
        self.lbl.place(x=50, y=180, width=300, height=50)
        self.lbl2=Label(self.fr2, text=self.bmrr, font=('Times New Roman',14,'bold'), bg=self.bmrcheck(), fg='white')
        self.lbl2.place(x=380, y=180, width=300, height=50)
        self.lbl3=Label(self.fr2, text=self.fatt, font=('Times New Roman',14,'bold'), bg=self.fatcheck(), fg='white')
        self.lbl3.place(x=710, y=180, width=300, height=50)
        self.keys=['Gain',"Maintain","Fit","Loose"]

        # print(self.keys)
        self.txt=Label(self.fr2, text="Select One")
        self.txt.place(x=100, y=270, width=100, height=30)
        self.txt.config(bg="black", fg="white")

        self.cb=t2.Combobox(self.fr2, textvariable=self.sel, values=self.keys)
        self.cb.place(x=100, y=300, width=380, height=30)
        self.sel.trace('w',self.update)
        # self.sel.set(self.keys[0])
        self.btn=Button(self.fr2, text='back', bg='red', fg='white', command=self.back)
        self.btn.place(x=800, y=100, width=100, height=30)

        self.lbl4=Label(self.fr2, text="",bg='blue')
        self.lbl4.place(x=800, y=300, width=30, height=30)
        self.lbl4=Label(self.fr2, text="",bg='orange')
        self.lbl4.place(x=800, y=340, width=30, height=30)
        self.lbl4=Label(self.fr2, text="",bg='green')
        self.lbl4.place(x=800, y=380, width=30, height=30)
        self.lbl4=Label(self.fr2, text="",bg='red')
        self.lbl4.place(x=800, y=420, width=30, height=30)
        self.lbl4=Label(self.fr2, text="Very Low", bg='black', fg='white')
        self.lbl4.place(x=850, y=300, width=100, height=30)
        self.lbl4=Label(self.fr2, text="Low", bg='black', fg='white')
        self.lbl4.place(x=850, y=340, width=100, height=30)
        self.lbl4=Label(self.fr2, text="Good", bg='black', fg='white')
        self.lbl4.place(x=850, y=380, width=100, height=30)
        self.lbl4=Label(self.fr2, text="High", bg='black', fg='white')
        self.lbl4.place(x=850, y=420, width=100, height=30)

        self.lbl4=Label(self.fr2, text="Essential Calorie intake values", font=('Times New Roman',18,'bold'), bg='black', fg='white')
        self.lbl4.place(x=680, y=420+50, width=350, height=30)
        
        self.gain=int(self.bmr)+int(30*self.bmr/100)
        self.maint=int(self.bmr)+int(15*self.bmr/100)
        self.los=int(self.bmr)+int(5*self.bmr/100)
        self.loos=int(self.bmr)-int(7*self.bmr/100)

        self.gain1="To Gain - "+str(int(self.bmr)+int(30*self.bmr/100))+" Calories/day"
        self.maint1="To Maintain - "+str(int(self.bmr)+int(15*self.bmr/100))+" Calories/day"
        self.los1="To Fit - "+str(int(self.bmr)+int(5*self.bmr/100))+" Calories/day"
        self.loos1="To Loose - "+str(int(self.bmr)-int(7*self.bmr/100))+" Calories/day"

        self.lbl4=Label(self.fr2, text=self.gain1, font=('Times New Roman',14,'bold'),bg='red', fg='white')
        self.lbl4.place(x=700, y=460+70, width=350, height=30)
        self.lbl4=Label(self.fr2, text=self.maint1, font=('Times New Roman',14,'bold'),bg='green', fg='white')
        self.lbl4.place(x=700, y=500+70, width=350, height=30)
        self.lbl4=Label(self.fr2, text=self.los1, font=('Times New Roman',14,'bold'),bg='orange', fg='white')
        self.lbl4.place(x=700, y=540+70, width=350, height=30)
        self.lbl4=Label(self.fr2, text=self.loos1, font=('Times New Roman',14,'bold'),bg='blue', fg='white')
        self.lbl4.place(x=700, y=580+70, width=350, height=30)

        self.btn=Button(self.fr2, text='Next', bg='blue', fg='white', command=self.process)
        self.btn.place(x=100, y=450, width=100, height=30)

if __name__== '__main__':
    obj = Frame2()
    obj.create2()
    obj.root.mainloop()