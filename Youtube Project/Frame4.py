from tkinter import *
from PIL import ImageTk, Image

class Frame4:
 image=[]
 def __init__(self):
    self.root= Tk()
    print("Frame4", self.image)
    self.root.title('IMAGE ')
    self.root.geometry('990x660')
    self.root.resizable(0, 1)
    self.frame = Frame(self.root) 
    self.frame.place(x=0, y=0, width=990, height=660)
    self.frame.config(bg="grey")
    

    
    self.image=Image.open(self.image[0])
    self.img=ImageTk.PhotoImage(self.image)
    self.heading = Label(self.frame, image=self.img)
    self.heading.place(x=400,y=100,width=990,height=660)
    self.heading.image=self.img
    
    
    """self.submitButton1=Button(self.frame,text='select',font=('open Sans', 15, 'bold'),bg='white',fg='firebrick1')
    self.submitButton1.place(x=400, y=350, width=200, height=30)

    self.submitButton2=Button(self.frame,text='SUBMIT',font=('open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',
                    activebackground='firebrick1',activeforeground='white',width=17)
    self.submitButton2.place(x=400,y=390,width=220,height=50)"""

    self.root.mainloop()

if __name__=='__main__':
  Frame4()