from tkinter import *  
from PIL import ImageTk,Image
from tkinter import filedialog
import img2pdf
from PIL import ImageDraw, ImageFont

class Frame1:    
    def __init__(self, win=""):
        if(win==""):
            self.win = Tk()
        else:
            self.win = win
        self.win.title("Welcome")
        self.win.geometry("1000x600+200+30")

    def photo(self):
        self.img = Image.open(filedialog.askopenfilename()).convert("RGBA")

        self.w, self.h = self.img.size
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.cw=self.w/2
        self.ch=self.h/2
        self.img1=self.img.resize((300,400))
        self.image = ImageTk.PhotoImage(self.img1)
        self.label = Label(self.root, image = self.image)
        self.label.place(x=10, y=10, width=300, height=400)

    def go(self):
        if self.h<(2*self.w):
            print(self.h,self.w)
            self.rw=self.h/1.6
            self.cal_w=self.w-self.rw
            self.left = self.w/2-self.rw/2
            self.right = self.w/2+self.rw/2
            self.upper = 0
            self.lower = self.h
            print(1)
        else:
            self.rh=2*self.w
            self.cal_h=self.h-self.rh
            self.left =0 
            self.right =self.w 
            self.upper = self.h/2-self.rh/2
            self.lower = self.h/2+self.rh/2

        img2 = self.img.crop([ self.left, self.upper, self.right, self.lower])
        img2 = img2.resize((int(self.screen_width-800),self.screen_height-100))


        self.fname=self.ent1.get()
        self.lname=self.ent2.get()
        self.age=self.ent3.get()
        self.height=self.ent4.get()
        self.status=self.ent5.get()
        self.text = ImageDraw.Draw(img2)
        self.font = ImageFont.truetype('OpenSans-ExtraBold.ttf', size=32)
        self.font1 = ImageFont.truetype('OpenSans-ExtraBold.ttf', size=20)
        self.font2 = ImageFont.truetype('OpenSans-Bold.ttf', size=16)
        self.font3 = ImageFont.truetype('OpenSans-Bold.ttf', size=12)
        self.text.text((290, 50), "Sample Resume", fill=(0, 0, 0), font=self.font)
        self.text.text((60, 150), "Personal", fill=(0, 0, 0), font=self.font1)
        self.text.text((60, 300), "Education", fill=(0, 0, 0), font=self.font1)
        self.text.text((60, 450), "Experience", fill=(0, 0, 0), font=self.font1)
        self.text.text((340, 150), "Hobby", fill=(0, 0, 0), font=self.font1)
        self.text.text((340, 300), "Sports", fill=(0, 0, 0), font=self.font1)
        self.text.text((340, 450), "Contact", fill=(0, 0, 0), font=self.font1)
        self.text.text((80, 180), self.fname+' '+self.lname, fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 200), "Age - "+self.age, fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 220), "Height - "+self.height, fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 240), self.status, fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 330), "B.Tech CSE", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 350), "Computer Science Engineering Diploma", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 370), "+2 Non. Medical 64%", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 390), "10th 84%", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 480), "2 Years Industrial Experience", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 500), "2 Years Industrial Experience", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 520), "1 Years Work from Home", fill=(0, 0, 0), font=self.font3)
        self.text.text((80, 540), "6 Month Internship", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 180), "Travelling", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 200), "Singing", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 220), "Karate", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 330), "Cricket", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 350), "Football", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 370), "Badminton", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 480), "9988776655", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 500), "Rohan@gmail.com", fill=(0, 0, 0), font=self.font3)
        self.text.text((360, 520), "Rohan1@gmail.com", fill=(0, 0, 0), font=self.font3)
        self.imgg=self.img2.convert('RGB')
        self.imgg.save('sample.jpg')
        self.b=open('sample.jpg','rb')
        with open('sample.pdf','wb') as file:
            file.write(img2pdf.convert(self.b))
        self.b.close()
    
    def create1(self):
        self.root=Frame(self.win)
        self.root.place(x=0,y=0, width=1000, height=600)

        # print(w,h)

        
        # Add Text to an image

        # font4 = ImageFont.truetype('OpenSans-Bold.ttf', size=32)
        # font5 = ImageFont.truetype('OpenSans-Bold.ttf', size=32)

        self.label = Button(self.root,text='Add Picture', command=self.photo)
        self.label.place(x=10, y=10, width=200, height=100)

        self.ent1=Entry(self.root)
        self.ent1.place(x=500, y=50)

        self.ent2=Entry(self.root)
        self.ent2.place(x=500, y=100)

        self.ent3=Entry(self.root)
        self.ent3.place(x=500, y=150)

        self.ent4=Entry(self.root)
        self.ent4.place(x=500, y=200)

        self.ent5=Entry(self.root)
        self.ent5.place(x=500, y=250)

        self.ent6=Entry(self.root)
        self.ent6.place(x=500, y=300)

        self.btn=Button(self.root, text='CLICK', command=self.go)
        self.btn.place(x=500,y=350)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()