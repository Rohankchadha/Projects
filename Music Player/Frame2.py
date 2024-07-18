from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk,Image
import pygame.mixer as mixer
import os
import Frame1

mixer.init()
class Frame2:
    data=''
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("490x700+300+30")

    def add(self):
        self.fr2.destroy()
        obj=Frame1.Frame1(self.root)
        obj.create1()

    def load(self):
        path = 'F:/Back-End/Projects/Python projects/Music Player/songs/'
        if path:
            os.chdir(path)
            songs = os.listdir(path)

            for song in songs:
                if song.endswith(".mp3"):
                    self.Playlist.insert(END, song)

    def play(self):
        Music_Name = self.Playlist.get(ACTIVE)
        print(Music_Name[0:-4])
        mixer.music.load(self.Playlist.get(ACTIVE))
        mixer.music.play()
        self.lbl1 = Label(self.fr2, text=Music_Name, wraplength=350, anchor=CENTER)
        self.lbl1.place(x=40, y=550, width=400, height=50)
        self.lbl1.config(bg='black', fg='white')

        self.photo=PhotoImage(file=r'F:\Back-End\Projects\Python projects\Music Player\images\play.jpg')
        self.lbl1 = Label(self.fr2, image=self.photo)
        self.lbl1.place(x=230, y=520, width=30, height=30)
        self.lbl1.config(bg='black', fg='white')

    def pause(self):
        mixer.music.pause()
        # self.photo1=PhotoImage(file=r'F:\Back-End\Projects\Python projects\Music Player\images\pause.jpg')
        # self.lbl2 = Label(self.fr2, image=self.photo1)
        # self.lbl2.place(x=230, y=520, width=30, height=30)
        # self.lbl2.config(bg='black', fg='white')

    def resume(self):
        mixer.music.unpause()

    def rewind(self):
        mixer.music.rewind()
    
    def close(self):
        a=messagebox.askyesno("Attention", "Exit ??")
        if a:
            exit()

    def create2(self):
        self.fr2 = Frame(self.root)
        self.fr2.place(x=0, y=0, width=490, height=700)
        self.fr2.config(bg="black")
        file=Image.open(r'F:\Back-End\Projects\Python projects\Music Player\images\sphere.gif')
        self.img=ImageTk.PhotoImage(file)
        self.lbl=Label(self.fr2, image=self.img)
        self.lbl.place(x=-5,y=100)
        
        self.Playlist = Listbox(self.fr2)
        self.Playlist.place(x=0, y=0, width=480, height=100)
        self.scroll=Scrollbar(self.fr2)
        self.scroll.config(command=self.Playlist.yview)
        self.scroll.place(x=480,y=0, width=15, height=100)
        self.load()
        self.btn =Button(self.fr2, text='Play', command=self.play)
        self.btn.place(x=20,y=620,width=50, height=30)
        self.btn =Button(self.fr2, text='Pause', command=self.pause)
        self.btn.place(x=120,y=620,width=50, height=30)
        self.btn =Button(self.fr2, text='Resume', command=self.resume)
        self.btn.place(x=220,y=620,width=50, height=30)
        self.btn =Button(self.fr2, text='Rewind', command=self.rewind)
        self.btn.place(x=320,y=620,width=50, height=30)
        self.btn =Button(self.fr2, text='Close', command=self.close)
        self.btn.place(x=420,y=620,width=50, height=30)
        self.lbl1 = Label(self.fr2, text='No Song Playing')
        self.lbl1.place(x=40,y=550, width=400,height=50)
        self.lbl1.config(bg='black', fg='white')

        self.btn1=Button(self.fr2, text="Add Songs", command=self.add)
        self.btn1.place(x=400, y=105, width=80, height=30)
        self.btn1.config(bg='black', fg='white')
        if self.data!='':
            self.lbl2=Label(self.fr2, text=self.data['userid'])
            self.lbl2.place(x=10, y=105, width=80, height=30)
            self.lbl2.config(bg='black', fg='white')


if __name__== '__main__':
    obj = Frame2()
    obj.create2()
    obj.root.mainloop()