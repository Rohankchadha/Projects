from tkinter import *
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter import messagebox
import Frame1
import Frame21
import Frame31

class frame2:
    def logout(self):
        a=messagebox.askyesno("HASHTAG", "Are you sure?")
        if(a):
            self.fr2.destroy()
            obj = Frame1.frame1(self.root)
            obj.create1()
    def cloud(self):
        self.fr2.destroy()
        obj = Frame21.frame21(self.root)
        obj.create21()
    def stgn(self):
        self.fr2.destroy()
        obj=Frame31.frame31(self.root)
        obj.create31()
    def info(self):
        messagebox.showinfo("About HASHTAG", "HASHTAG® is a multipurpose file handling system that deals with encryption-decryption, steganography and cloud operations all together at one stop")

    def file(self):
        a = filedialog.askopenfilenames()
        print(a)
        b = messagebox.askyesno("Attention", "You really want to encrypt the file?")
        if (b):
            print(a)
            for i in a:
                with open("mykey.key", "rb") as mykey:
                    key = mykey.read()
                f = Fernet(key)
                with open(i, "rb") as original_file1:
                    original = original_file1.read()
                encfile = f.encrypt(original)
                with open(i, "wb") as enc_file:
                    enc_file.write(encfile)
                messagebox.showinfo("HASHTAG", "File encrypted successfully")

    def file1(self):
        a = filedialog.askopenfilenames()
        b = messagebox.askyesno("Attention", "You really want to decrypt the file?")
        if (b):
            for i in a:
                with open("mykey.key", "rb") as mykey:
                    key = mykey.read()
                f = Fernet(key)
                with open(i, "rb") as original_file2:
                    original = original_file2.read()
                decfile = f.decrypt(original)
                with open(i, "wb") as dec_file:
                    dec_file.write(decfile)
                messagebox.showinfo("HASHTAG", "File decrypted successfully")
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Admin, Welcome to your profile")
        self.root.geometry("1000x500+250+120")


    def create2(self):
        self.fr2 = Frame(self.root)
        self.fr2.place(x=0, y=0, width=1000, height=500)
        self.fr2.config(bg="black")

        self.img0=PhotoImage(file="black_lock.png")
        self.lbl0=Label(self.fr2, image=self.img0)
        self.lbl0.place(x=0, y=0, width=1000, height=500)

        self.lbl = Label(self.fr2, text="HASHTAG")
        self.lbl.place(x=20, y=20, width=250, height=40)
        self.lbl.config(font=('Times New Roman', 30, 'bold'), bg="black", fg="white")

        self.btn0 = Button(self.fr2, text="Information", command=self.info)
        self.btn0.place(x=400, y=20, width=80, height=30)
        self.btn0.config(fg="white", bg="navy blue")

        self.btn1 = Button(self.fr2, text="Encrypt",command=self.file)
        self.btn1.place(x=500,y=20,width=80,height=30)
        self.btn1.config(fg="white", bg="navy blue")

        self.btn2 = Button(self.fr2, text="Decrypt", command=self.file1)
        self.btn2.place(x=600, y=20, width=80, height=30)
        self.btn2.config(fg="white", bg="navy blue")

        self.btn3 = Button(self.fr2, text="Cloud", command=self.cloud)
        self.btn3.place(x=700, y=20, width=80, height=30)
        self.btn3.config(fg="white", bg="navy blue")

        self.btn4 = Button(self.fr2, text="Stegano", command=self.stgn)
        self.btn4.place(x=800, y=20, width=80, height=30)
        self.btn4.config(fg="white", bg="navy blue")

        self.btn = Button(self.fr2, text="Logout", command=self.logout)
        self.btn.place(x=900,y=20,width=80,height=30)
        self.btn.config(fg="white", bg="red")

if __name__== '__main__':
    obj = frame2()
    obj.create2()
    obj.root.mainloop()