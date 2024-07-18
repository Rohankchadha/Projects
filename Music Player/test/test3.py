import moviepy.editor as ed
from tkinter import messagebox,filedialog

mp3file=ed.VideoFileClip("test/test.mp4")
mp3file.audio.write_audiofile('test/file.mp3')
mp3file.close()
print(mp3file)