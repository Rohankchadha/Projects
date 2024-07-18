import stegano
from tkinter import filedialog
a=stegano.lsb.hide(filedialog.askopenfilename(),"Fuck You")
a.save(filedialog.asksaveasfilename())
b=stegano.lsb.reveal(filedialog.askopenfilename())
print(b)