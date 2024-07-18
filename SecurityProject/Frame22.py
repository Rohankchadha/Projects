from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from mega import Mega
import Frame21
import Frame2
import Frame1
a1=open("newfile.txt","r+")
txt1=a1.read()
a2 = open("newfile1.txt", "r+")
pas1 = a2.read()
mega=Mega()
m=mega.login(txt1,pas1)

class frame22():

    def search(self):
        file=m.find(self.lbl3.get())
        print(file)
        if(file!=None):
            messagebox.showinfo("MEGA", "Searched File is present in the cloud")
        else:
            messagebox.showerror("MEGA", "File not found")
    def info(self):
        details=m.get_user()
        print(details)
        data="Name - "+details["name"]+"\nemail - "+details["email"]+"\n\nPublic key is - "+details["pubk"]+"\n\nPriavte key is - "+details["privk"]
        messagebox.showinfo("MEGA", data)
    def logout(self):
        self.fr22.destroy()
        obj = Frame21.frame21(self.root)
        obj.create21()

    def upload(self):
        file_up=filedialog.askopenfilename()
        upl = m.upload(file_up)
        messagebox.showinfo("MEGA", "File uploaded successfully")
        uplink = m.get_upload_link(upl)
        print(uplink)
        data1=file_up+"::"+uplink+"\n"
        with open("uploaded_file.txt","w") as f:
            f.write(data1)
        with open("uploaded_files.txt","a") as g:
            g.write(data1)
    def storage(self):
        quota=m.get_quota()
        space=m.get_storage_space(mega=True)
        left=str(quota)
        used=str(space["used"])
        total=str(space["total"])
        data="Space left = "+left+" MB"+"\n\nSpace used = "+used+" MB"+"\n\nTotal Space = "+total+" MB"
        messagebox.showinfo("MEGA", data)

    def back(self):
        pass
    def __init__(self, root=""):
        if (root == ""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Welcome to Object Section")
        self.root.geometry("1000x500+250+120")

    def create22(self):
        #self.details=details
        self.fr22 = Frame(self.root)
        self.fr22.place(x=0, y=0, width=1000, height=500)
        self.fr22.config(bg="black")

        self.img1 = PhotoImage(file="black_cloud.png")
        self.lbl0=Label(self.fr22,image=self.img1)
        self.lbl0.place(x=0, y=0, width=1000, height=500)

        self.lbl = Label(self.fr22, text="MEGA dashboard")
        self.lbl.place(x=375, y=30, width=250, height=40)
        self.lbl.config(font=('Times New Roman', 24, 'bold'), bg="black", fg="white")
        details=m.get_user()
        name=details["name"]
        self.lbl1 = Label(self.fr22, text=name)
        self.lbl1.place(x=40,y=80,width=300,height=40)
        self.lbl1.config(font=('Bell MT',16,'bold'), fg="white", bg="black")

        self.btn = Button(self.fr22, text="Logout", command=self.logout)
        self.btn.place(x=900, y=80, width=80, height=30)
        self.btn.config(fg="white", bg="red")

        self.btn1 = Button(self.fr22, text="Search", command=self.search)
        self.btn1.place(x=900, y=120, width=80, height=30)
        self.btn1.config(fg="white", bg="navy blue")

        self.lbl3 = Entry(self.fr22)
        self.lbl3.place(x=720, y=120, width=170, height=30)

        self.btn2 = Button(self.fr22, text="Storage", command=self.storage)
        self.btn2.place(x=50, y=300, width=150, height=30)
        self.btn2.config(fg="white", bg="navy blue")

        self.btn3 = Button(self.fr22, text="Upload", command=self.upload)
        self.btn3.place(x=50, y=250, width=150, height=30)
        self.btn3.config(fg="white", bg="navy blue")

        self.btn4 = Button(self.fr22, text="Account Information", command=self.info)
        self.btn4.place(x=720, y=80, width=170, height=30)
        self.btn4.config(fg="white", bg="navy blue")

if __name__== '__main__':
    obj = frame22()
    obj.create22()
    obj.root.mainloop()