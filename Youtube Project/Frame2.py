from tkinter import *
from tkinter import messagebox, filedialog
import cv2
from PIL import ImageTk,Image
import db, Frame4
class Frame2:   
    data=''
    images=[]
    cnt=15
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1100x700+200+30")

    def gett(self,path):
        self.images.append(path)
        Frame4.Frame4.image.append(path)
        Frame4.Frame4()

    def save(self):
        a=db.save(self.images)
        if a:
            messagebox.showinfo("Success","Images stored in DataBase")
        else:
            messagebox.showerror("Error","Images not saved")
        exit()
    
    def next(self):
        try:
                    self.image=Image.open(self.data[0+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name1 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[0+self.cnt-15]))
                    self.name1.place(x=50,y=100)
                    self.name1.image=self.image1
                    
                    self.image=Image.open(self.data[1+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name2 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[1+self.cnt-15]))
                    self.name2.place(x=200,y=100)
                    self.name2.image=self.image1
                    
                    self.image=Image.open(self.data[2+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name3 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[2+self.cnt-15]))
                    self.name3.place(x=350,y=100)
                    self.name3.image=self.image1
                    
                    self.image=Image.open(self.data[3+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name4 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[3+self.cnt-15]))
                    self.name4.place(x=500,y=100)
                    self.name4.image=self.image1
                    
                    self.image=Image.open(self.data[4+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name5 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[4+self.cnt-15]))
                    self.name5.place(x=650,y=100)
                    self.name5.image=self.image1
                    
                    self.image=Image.open(self.data[5+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name6 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[5+self.cnt-15]))
                    self.name6.place(x=50,y=250)
                    self.name6.image=self.image1
                    
                    self.image=Image.open(self.data[6+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name7 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[6+self.cnt-15]))
                    self.name7.place(x=200,y=250)
                    self.name7.image=self.image1
                    
                    self.image=Image.open(self.data[7+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name8 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[7+self.cnt-15]))
                    self.name8.place(x=350,y=250)
                    self.name8.image=self.image1
                    
                    self.image=Image.open(self.data[8+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name9 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[8+self.cnt-15]))
                    self.name9.place(x=500,y=250)
                    self.name9.image=self.image1
                    
                    self.image=Image.open(self.data[9+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name10 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[9+self.cnt-15]))
                    self.name10.place(x=650,y=250)
                    self.name10.image=self.image1
                    
                    self.image=Image.open(self.data[10+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name11 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[10+self.cnt-15]))
                    self.name11.place(x=50,y=400)
                    self.name11.image=self.image1
                    
                    self.image=Image.open(self.data[11+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name12 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[11+self.cnt-15]))
                    self.name12.place(x=200,y=400)
                    self.name12.image=self.image1
            
                    self.image=Image.open(self.data[12+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name13 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[12+self.cnt-15]))
                    self.name13.place(x=350,y=400)
                    self.name13.image=self.image1
                    
                    self.image=Image.open(self.data[13+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name14 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[13+self.cnt-15]))
                    self.name14.place(x=500,y=400)
                    self.name14.image=self.image1
                    
                    self.image=Image.open(self.data[14+self.cnt])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name15 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[14+self.cnt-15]))
                    self.name15.place(x=650,y=400)
                    self.name15.image=self.image1
            
        except:
            messagebox.showinfo("Attention", "End of images")
        self.cnt+=15

    def create2(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1100, height=700)
        self.fr1.config(bg="black")
        try:
                    self.image=Image.open(self.data[0])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name1 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[0]))
                    self.name1.place(x=50,y=100)
                    self.name1.image=self.image1
                    
                    self.image=Image.open(self.data[1])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name2 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[1]))
                    self.name2.place(x=200,y=100)
                    self.name2.image=self.image1
                    
                    self.image=Image.open(self.data[2])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name3 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[2]))
                    self.name3.place(x=350,y=100)
                    self.name3.image=self.image1
                    
                    self.image=Image.open(self.data[3])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name4 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[3]))
                    self.name4.place(x=500,y=100)
                    self.name4.image=self.image1
                    
                    self.image=Image.open(self.data[4])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name5 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[4]))
                    self.name5.place(x=650,y=100)
                    self.name5.image=self.image1
                
                    self.image=Image.open(self.data[5])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name6 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[5]))
                    self.name6.place(x=50,y=250)
                    self.name6.image=self.image1
                    
                    self.image=Image.open(self.data[6])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name7 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[6]))
                    self.name7.place(x=200,y=250)
                    self.name7.image=self.image1
                    
                    self.image=Image.open(self.data[7])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name8 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[7]))
                    self.name8.place(x=350,y=250)
                    self.name8.image=self.image1
                    
                    self.image=Image.open(self.data[8])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name9 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[8]))
                    self.name9.place(x=500,y=250)
                    self.name9.image=self.image1
                    
                    self.image=Image.open(self.data[9])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name10 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[9]))
                    self.name10.place(x=650,y=250)
                    self.name10.image=self.image1
                    
                    self.image=Image.open(self.data[10])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name11 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[10]))
                    self.name11.place(x=50,y=400)
                    self.name11.image=self.image1
                    
                    self.image=Image.open(self.data[11])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name12 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[11]))
                    self.name12.place(x=200,y=400)
                    self.name12.image=self.image1
                    
                    self.image=Image.open(self.data[12])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name13 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[12]))
                    self.name13.place(x=350,y=400)
                    self.name13.image=self.image1
                    
                    self.image=Image.open(self.data[13])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name14 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[13]))
                    self.name14.place(x=500,y=400)
                    self.name14.image=self.image1
                    
                    self.image=Image.open(self.data[14])
                    self.img=self.image.resize((100,100))
                    self.image1=ImageTk.PhotoImage(self.img)
                    self.name15 = Button(self.fr1, image=self.image1, command=lambda:self.gett(self.data[14]))
                    self.name15.place(x=650,y=400)
                    self.name15.image=self.image1
            
        except:
            messagebox.showinfo("Attention", "End of images")
        self.btn=Button(self.fr1, text='Next', command=self.next)
        self.btn.place(x=900, y=70, width=50, height=20)

        self.btn=Button(self.fr1, text='Save', command=self.save)
        self.btn.place(x=100, y=70, width=50, height=20)

if __name__== '__main__':
    obj = Frame2()
    obj.create2()
    obj.root.mainloop()