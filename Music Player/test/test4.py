from tkinter import filedialog
title1="This file"
tps=[('mp4 (Video)','.mp4')]
fl=filedialog.asksaveasfile(initialfile=title1,filetypes=tps)
print(fl.name.split('/')[-1])