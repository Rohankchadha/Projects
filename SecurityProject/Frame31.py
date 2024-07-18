from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import stegano
import Frame1
import Frame2

class frame31:
    def info(self):
        messagebox.showinfo("STEGANOGRAPHY", "Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination. The use of steganography can be combined with encryption as an extra step for hiding or protecting data.")
    def back(self):
        self.fr31.destroy()
        obj=Frame2.frame2(self.root)
        obj.create2()
    def hide(self):
        if(self.txt.get()!=""):
            file = filedialog.askopenfilename()
            text=self.txt.get()
            hide1 = stegano.lsb.hide(file, text)
            hide1.save(filedialog.asksaveasfilename())
            messagebox.showinfo("STEGANOGRAPHY", "Data hidden in the selected file successfully")
        else:
            messagebox.showerror("STEGANOGRAPHY", "Please Enter data to hide")

    def show(self):
        text = stegano.lsb.reveal(filedialog.askopenfilename())
        if(text==""):
            messagebox.showerror("STEGANOGRAPHY", "No data found to show")
        else:
            messagebox.showinfo("STEGANOGRAPHY", text)

    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Steganography")
        self.root.geometry("1000x500+250+120")


    def create31(self):
        self.fr31 = Frame(self.root)
        self.fr31.place(x=0, y=0, width=1000, height=500)
        self.fr31.config(bg="black")

        #self.img=PhotoImage(file="black_stg.png")
        #self.lbl0=Label(self.fr31,image=self.img)
        #self.lbl0.place(x=0, y=0, width=1000, height=500)

        self.lbl = Label(self.fr31, text="STEGANOGRAPHY")
        self.lbl.place(x=40, y=20, width=300, height=40)
        self.lbl.config(font=('Times New Roman', 24, 'bold'), bg="black", fg="white")

        self.btn0 = Button(self.fr31, text="Information", command=self.info)
        self.btn0.place(x=800, y=20, width=80, height=30)
        self.btn0.config(fg="white", bg="navy blue")

        self.txt = Entry(self.fr31)
        self.txt.place(x=40, y=150, width=320, height=30)

        self.lbl1 = Label(self.fr31, text="Enter data to Hide")
        self.lbl1.place(x=40, y=130, width="100", height=10)
        self.lbl1.config(font=('Times New Roman',10, 'bold'), bg="black", fg="white")

        self.btn1 = Button(self.fr31, text="Hide Data",command=self.hide)
        self.btn1.place(x=40,y=200,width=150,height=30)
        self.btn1.config(fg="white", bg="navy blue")

        self.btn2 = Button(self.fr31, text="Show data", command=self.show)
        self.btn2.place(x=210, y=200, width=150, height=30)
        self.btn2.config(fg="white", bg="navy blue")

        self.btn = Button(self.fr31, text="Back", command=self.back)
        self.btn.place(x=900,y=20,width=80,height=30)
        self.btn.config(fg="white", bg="red")

if __name__== '__main__':
    obj = frame31()
    obj.create31()
    obj.root.mainloop()