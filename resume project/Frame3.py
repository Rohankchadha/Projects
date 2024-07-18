from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image,ImageTk, ImageFont, ImageDraw
import img2pdf
import cv2
import textwrap

class Frame3:

   a=''
   b=''
   a1=True
   a2=True
   a3=True
   a4=True
   data=[]
   fontstyle=""
   fontstyle1=""

   def create3(self):
      if(self.b==1):
         print(self.b)
         # self.fr3 = Frame(self.root)
         # self.fr3.place(x=0, y=0, width=1000, height=650)
         # self.fr3.config(bg="black")
         self.num=150
         self.num1=60
         # print(data)
         self.img = Image.open(self.a).convert("RGBA")
         self.w, self.h = self.img.size
         self.screen_width = 1366
         self.screen_height = 768
         # print(self.screen_width,self.screen_height)
         self.cw=self.w/2
         self.ch=self.h/2
         if self.h<(2*self.w):
               # print(self.h,self.w)
               self.rw=self.h/1.6
               self.cal_w=self.w-self.rw
               self.left = self.w/2-self.rw/2
               self.right = self.w/2+self.rw/2
               self.upper = 0
               self.lower = self.h
               # print(1)
         else:
               self.rh=2*self.w
               self.cal_h=self.h-self.rh
               self.left =0 
               self.right =self.w 
               self.upper = self.h/2-self.rh/2
               self.lower = self.h/2+self.rh/2

         self.img2 = self.img.crop([ self.left, self.upper, self.right, self.lower])
         self.img2 = self.img2.resize((int(self.screen_width-800),self.screen_height-100))

         self.text = ImageDraw.Draw(self.img2)
         self.font = ImageFont.truetype(self.fontstyle, size=32)
         self.font1 = ImageFont.truetype(self.fontstyle, size=20)
         self.font2 = ImageFont.truetype(self.fontstyle1, size=16)
         self.font3 = ImageFont.truetype(self.fontstyle1, size=12)
         self.text.text((190, 50),self.data[0]['Name - '], fill=(0, 0, 0), font=self.font)

         def pattern1(self):

            self.text.text((self.num1, self.num), "Personal", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for i in self.data[0].keys():
               self.lines = textwrap.wrap(i+' - '+self.data[0][i], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines), fill=(0, 0, 0), font=self.font3)
               if len(self.data[0][i])>60:
                  dif=len(self.data[0][i])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            self.num+= 50
            self.num1-=20

         def pattern2(self):
            self.text.text((self.num1, self.num), "Education", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for j in self.data[1].keys():
               self.lines1 = textwrap.wrap(j+' - '+self.data[1][j], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines1), fill=(0, 0, 0), font=self.font3)
               if len(self.data[1][j])>60:
                  dif=len(self.data[1][j])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            if self.num<400:
               self.num+=50
               self.num1-=20
            else:
               self.num1+=230
               self.num=150

         def pattern3(self):
            self.text.text((self.num1, self.num), "Experience", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for k in self.data[2].keys():
               self.lines2 = textwrap.wrap(k+' - '+self.data[2][k], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines2), fill=(0, 0, 0), font=self.font3)
               if len(self.data[2][k])>60:
                  dif=len(self.data[2][k])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            if self.num<400:
               self.num+=50
               self.num1-=20
            else:
               self.num1+=230
               self.num=150

         def pattern4(self):
            self.text.text((self.num1, self.num), "Extras", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for l in self.data[3].keys():
               self.lines3 = textwrap.wrap(l+' - '+self.data[3][l], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines3), fill=(0, 0, 0), font=self.font3)
               if len(self.data[3][l])>60:
                  dif=len(self.data[3][l])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            if self.num<400:
               self.num+=40
               self.num1-=20
            else:
               self.num1+=230
               self.num=150
         
         if(self.a1):
               pattern1(self)
         if(self.a2):
               pattern2(self)
         if(self.a3):
               pattern3(self)
         if(self.a4):
               pattern4(self)
         
      elif(self.b==2):
         print(self.b)
         self.num=100
         self.num1=60
         self.img = Image.open(self.a).convert("RGBA")
         self.w, self.h = self.img.size
         self.screen_width = 1366
         self.screen_height = 768
         self.cw=self.w/2
         self.ch=self.h/2
         if self.h<(2*self.w):
               self.rw=self.h/1.6
               self.cal_w=self.w-self.rw
               self.left = self.w/2-self.rw/2
               self.right = self.w/2+self.rw/2
               self.upper = 0
               self.lower = self.h
         else:
               self.rh=2*self.w
               self.cal_h=self.h-self.rh
               self.left =0 
               self.right =self.w 
               self.upper = self.h/2-self.rh/2
               self.lower = self.h/2+self.rh/2

         self.img2 = self.img.crop([ self.left, self.upper, self.right, self.lower])
         self.img2 = self.img2.resize((int(self.screen_width-800),self.screen_height-100))

         self.text = ImageDraw.Draw(self.img2)
         self.font = ImageFont.truetype(self.fontstyle, size=32)
         self.font1 = ImageFont.truetype(self.fontstyle, size=20)
         self.font2 = ImageFont.truetype(self.fontstyle1, size=16)
         self.font3 = ImageFont.truetype(self.fontstyle1, size=12)
         self.text.text((190, 50),self.data[0]['Name - '], fill=(0, 0, 0), font=self.font)

         def pattern1(self):

            self.text.text((self.num1, self.num), "Personal", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for i in self.data[0].keys():
               self.lines = textwrap.wrap(i+' - '+self.data[0][i], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines), fill=(0, 0, 0), font=self.font3)
               if len(self.data[0][i])>60:
                  dif=len(self.data[0][i])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            self.num+= 20
            self.num1-=20

         def pattern2(self):
            self.text.text((self.num1, self.num), "Education", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for j in self.data[1].keys():
               self.lines1 = textwrap.wrap(j+' - '+self.data[1][j], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines1), fill=(0, 0, 0), font=self.font3)
               if len(self.data[1][j])>60:
                  dif=len(self.data[1][j])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            self.num+=20
            self.num1-=20

         def pattern3(self):
            self.text.text((self.num1, self.num), "Experience", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for k in self.data[2].keys():
               self.lines2 = textwrap.wrap(k+' - '+self.data[2][k], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines2), fill=(0, 0, 0), font=self.font3)
               if len(self.data[2][k])>60:
                  dif=len(self.data[2][k])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            self.num+=20
            self.num1-=20

         def pattern4(self):
            self.text.text((self.num1, self.num), "Extras", fill=(0, 0, 0), font=self.font1)
            self.num+=30
            self.num1+=20
            for l in self.data[3].keys():
               self.lines3 = textwrap.wrap(l+' - '+self.data[3][l], width=60)
               self.text.multiline_text((self.num1, self.num), '\n'.join(self.lines3), fill=(0, 0, 0), font=self.font3)
               if len(self.data[3][l])>60:
                  dif=len(self.data[3][l])/60
                  self.num+=20*dif
               else:
                  self.num+=20
            self.num+=20
            self.num1-=20
         
         if(self.a1):
               pattern1(self)
         if(self.a2):
               pattern2(self)
         if(self.a3):
               pattern3(self)
         if(self.a4):
               pattern4(self)
      elif(self.b==3):
          pass
      self.photo=ImageTk.PhotoImage(self.img2)
      self.img=self.img2.convert('RGB')
      self.img.save('sample.jpg')
      img = cv2.imread("sample.jpg")
      cv2.imshow("cat image", img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      self.b=open('sample.jpg','rb')
      self.files = [('PDF', '*.pdf')]
      #,('All Files', '*.*')
      self.name=filedialog.asksaveasfilename(filetypes = self.files, defaultextension = self.files)
      if self.name!='':
            with open(self.name,'wb') as file:
               file.write(img2pdf.convert(self.b))
            self.b.close()
            messagebox.showinfo('Success','Saved Successfully')
      else:
            messagebox.showerror('Save unsucessful','Operation cancelled by user' )
      exit()
