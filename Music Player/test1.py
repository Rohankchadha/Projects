from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk,Image
import pygame.mixer as mixer
import os
mixer.init(44100)
class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("YTD")
        self.root.geometry("1000x600+200+30")

    def load(self):
        path = filedialog.askdirectory()
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
        # lbl = Label(self.fr1, text=Music_Name)
        # lbl.place(x=40, y=30, width=500, height=100)

    def pause(self):
        mixer.music.pause()

    def resume(self):
        mixer.music.unpause()

    def rewind(self):
        mixer.music.rewind()
    
    def close(self):
        a=messagebox.askyesno("Attention", "Exit ??")
        if a:
            exit()

    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")
        
        self.Playlist = Listbox(self.fr1)
        self.Playlist.place(x=40, y=30, width=500, height=100)
        self.scroll=Scrollbar(self.fr1)
        self.scroll.config(command=self.Playlist.yview)
        self.scroll.place(x=540,y=30, width=15, height=100)
        self.load()
        self.btn =Button(self.fr1, text='Play', command=self.play)
        self.btn.place(x=20,y=170,width=100, height=30)
        self.btn =Button(self.fr1, text='Pause', command=self.pause)
        self.btn.place(x=150,y=170,width=100, height=30)
        self.btn =Button(self.fr1, text='Resume', command=self.resume)
        self.btn.place(x=300,y=170,width=100, height=30)
        self.btn =Button(self.fr1, text='Rewind', command=self.rewind)
        self.btn.place(x=450,y=170,width=100, height=30)
        self.btn =Button(self.fr1, text='Close', command=self.close)
        self.btn.place(x=600,y=170,width=100, height=30)

if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()