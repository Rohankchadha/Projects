from tkinter import *
from tkinter import filedialog, messagebox
import pygame.mixer as mixer
import os

mixer.init()

class Musicall:
    # def load():
    #     a=filedialog.askopenfile()
    #     mixer.music.load(a)
    #     return " ".join(a.name.split("/")[-1].split(" ")[:3])
    
    # Create a function to open a file
    def load():
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)

            for song in songs:
                if song.endswith(".mp3"):
                    Playlist.insert(END, song)


    def play():
        Music_Name = Playlist.get(ACTIVE)
        print(Music_Name[0:-4])
        mixer.music.load(Playlist.get(ACTIVE))
        mixer.music.play()
        lbl = Label(root, text=Music_Name)
        lbl.place(x=40, y=30, width=500, height=100)

    # def play():
    #     mixer.music.play()
    #     lbl = Label(root, text=name)
    #     lbl.place(x=40, y=30, width=500, height=100)
    
    def pause():
        mixer.music.pause()

    def resume():
        mixer.music.unpause()

    def rewind():
        mixer.music.rewind()
    
    def close():
        a=messagebox.askyesno("Attention", "Exit ??")
        if a:
            exit()


root = Tk()
root.geometry('720x220')
root.title('PythonGeeks Music Player')
root.resizable(0, 0)
Musicall.load()
Playlist = Listbox(root)
Playlist.place(x=40, y=30, width=500, height=100)
btn =Button(root, text='Play', command=Musicall.play)
btn.place(x=20,y=170,width=100, height=30)
btn =Button(root, text='Pause', command=Musicall.pause)
btn.place(x=150,y=170,width=100, height=30)
btn =Button(root, text='Resume', command=Musicall.resume)
btn.place(x=300,y=170,width=100, height=30)
btn =Button(root, text='Rewind', command=Musicall.rewind)
btn.place(x=450,y=170,width=100, height=30)
btn =Button(root, text='Close', command=Musicall.close)
btn.place(x=600,y=170,width=100, height=30)
# btn =Button(root, text='Play', command=Musicall.play)
# btn.place(x=20,y=170,width=100, height=30)
root.update()
root.mainloop()