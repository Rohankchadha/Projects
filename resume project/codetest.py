# from tkinter import *  
# from PIL import ImageTk,Image
# from tkinter import filedialog
# import img2pdf
# from PIL import ImageDraw, ImageFont

# def go():
#     imgg=img2.convert('RGB')
#     imgg.save('sample.jpg')
#     b=open('sample.jpg','rb')
#     with open('sample.pdf','wb') as file:
#         file.write(img2pdf.convert(b))
#     b.close()

# root = Tk()

# img = Image.open(filedialog.askopenfilename()).convert("RGBA")

# w, h = img.size
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# cw=w/2
# ch=h/2

# # print(w,h)
# if h<(2*w):
#     print(h,w)
#     rw=h/1.6
#     cal_w=w-rw
#     left = w/2-rw/2
#     right = w/2+rw/2
#     upper = 0
#     lower = h
#     print(1)
# else:
#     rh=2*w
#     cal_h=h-rh
#     left =0 
#     right =w 
#     upper = h/2-rh/2
#     lower = h/2+rh/2

# img2 = img.crop([ left, upper, right, lower])
# img2 = img2.resize((int(screen_width-800),screen_height-100))

# text = ImageDraw.Draw(img2)
 
# # Add Text to an image
# font = ImageFont.truetype('OpenSans-ExtraBold.ttf', size=32)
# font1 = ImageFont.truetype('OpenSans-ExtraBold.ttf', size=20)
# font2 = ImageFont.truetype('OpenSans-Bold.ttf', size=16)
# font3 = ImageFont.truetype('OpenSans-Bold.ttf', size=12)
# # font4 = ImageFont.truetype('OpenSans-Bold.ttf', size=32)
# # font5 = ImageFont.truetype('OpenSans-Bold.ttf', size=32)

# text.text((290, 50), "Sample Resume", fill=(0, 0, 0), font=font)
# text.text((60, 150), "Personal", fill=(0, 0, 0), font=font1)
# text.text((60, 300), "Education", fill=(0, 0, 0), font=font1)
# text.text((60, 450), "Experience", fill=(0, 0, 0), font=font1)
# text.text((340, 150), "Hobby", fill=(0, 0, 0), font=font1)
# text.text((340, 300), "Sports", fill=(0, 0, 0), font=font1)
# text.text((340, 450), "Contact", fill=(0, 0, 0), font=font1)
# text.text((80, 180), "Rohan Kumar", fill=(0, 0, 0), font=font3)
# text.text((80, 200), "Age - 23", fill=(0, 0, 0), font=font3)
# text.text((80, 220), "Height - 5.8", fill=(0, 0, 0), font=font3)
# text.text((80, 240), "Religiously Active", fill=(0, 0, 0), font=font3)
# text.text((80, 330), "B.Tech CSE", fill=(0, 0, 0), font=font3)
# text.text((80, 350), "Computer Science Engineering Diploma", fill=(0, 0, 0), font=font3)
# text.text((80, 370), "+2 Non. Medical 64%", fill=(0, 0, 0), font=font3)
# text.text((80, 390), "10th 84%", fill=(0, 0, 0), font=font3)
# text.text((80, 480), "2 Years Industrial Experience", fill=(0, 0, 0), font=font3)
# text.text((80, 500), "2 Years Industrial Experience", fill=(0, 0, 0), font=font3)
# text.text((80, 520), "1 Years Work from Home", fill=(0, 0, 0), font=font3)
# text.text((80, 540), "6 Month Internship", fill=(0, 0, 0), font=font3)
# text.text((360, 180), "Travelling", fill=(0, 0, 0), font=font3)
# text.text((360, 200), "Singing", fill=(0, 0, 0), font=font3)
# text.text((360, 220), "Karate", fill=(0, 0, 0), font=font3)
# text.text((360, 330), "Cricket", fill=(0, 0, 0), font=font3)
# text.text((360, 350), "Football", fill=(0, 0, 0), font=font3)
# text.text((360, 370), "Badminton", fill=(0, 0, 0), font=font3)
# text.text((360, 480), "9988776655", fill=(0, 0, 0), font=font3)
# text.text((360, 500), "Rohan@gmail.com", fill=(0, 0, 0), font=font3)
# text.text((360, 520), "Rohan1@gmail.com", fill=(0, 0, 0), font=font3)

# image = ImageTk.PhotoImage(img2)

# label = Label(root, image = image)
# label.pack()

# btn=Button(root, text='CLICK', image=image, command=go)
# btn.pack()

# root.mainloop()

a=[{'a':10},{'b':20}]
print(a[0]['a'])