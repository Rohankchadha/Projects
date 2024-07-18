from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def Encryption(name):
    f = Fernet(key)
    with open(name, "rb") as original_file1:
        original = original_file1.read()
    encfile = f.encrypt(original)
    with open(name,"wb") as enc_file:
        enc_file.write(encfile)

def Decryption(name):
    f = Fernet(key)
    with open(name,"rb") as original_file2:
        original = original_file2.read()
    decfile = f.decrypt(original)
    with open(name, "wb") as dec_file:
        dec_file.write(decfile)
def file():
    a=filedialog.askopenfilenames()
    if(a!=""):
        b=messagebox.askyesno("Attention","You really want to encrypt the file?")
        if(b):
            print(a)
            for i in a:
                Encryption(i)
def file1():
    a=filedialog.askopenfilenames()
    if(a!=""):
        b=messagebox.askyesno("Attention","You really want to decrypt the file?")
        if(b):
            for i in a:
                Decryption(i)
win1=Tk()
win1.title("file")
win1.geometry("500x500+100+100")
win1.config(bg="black")
btn = Button(win1,text="Encrypt",command=file)
btn1 = Button(win1,text="Decrypt",command=file1)
btn.pack()
btn1.pack()

with open("mykey.key","rb") as mykey:
    key = mykey.read()

win1.mainloop()