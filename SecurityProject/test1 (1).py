import stegano
from tkinter import filedialog
def hide():
    text=input("Enter data to be hidden : ")
    file=filedialog.askopenfilename()
    hide1=stegano.lsb.hide(file,text)
    hide1.save(filedialog.asksaveasfilename())
    print("Data hidden in file ",file)
def reveal():
    print("select file")
    text=stegano.lsb.reveal(filedialog.askopenfilename())
    print("The hidden text is : ",text)

a=int(input("enter your choice : \t1. hide\t2. reveal"))
if(a==1):
    hide()
elif(a==2):
    reveal()
else:
    print("Invalid choice")
