from tkinter import *
from tkcalendar import DateEntry
from datetime import date
from tktimepicker import AnalogPicker, AnalogThemes, constants

# https://pypi.org/project/tkTimePicker/
# pip install tkTimePicker

class Calenders():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x400')

        self.today = date.today()
        self.dates=DateEntry(self.root,bd=2,date_pattern='yyyy/mm/dd',mindate = self.today)
        self.dates.place(x=40,y=300,width=250,height=35)

        self.time_lbl = Label(self.root, text="Time:")
        self.time_lbl.pack()

        self.time_btn = Button(self.root, text="Get Time", command=self.get_time)
        self.time_btn.pack()

        self.root.mainloop()

    def updateTime(self, time):
        self.time_lbl.configure(text="{}:{} {}".format(*time)) 
        self.top.destroy()

    def get_time(self):

        self.top = Toplevel(self.root)

        time_picker = AnalogPicker(self.top, type=constants.HOURS12)
        time_picker.pack(expand=True, fill="both")

        theme = AnalogThemes(time_picker)
        # theme.setDracula()
        # theme.setNavyBlue()
        theme.setPurple()
        ok_btn = Button(self.top, text="ok", command=lambda: self.updateTime(time_picker.time()))
        ok_btn.pack()


if __name__ == '__main__':
    Calenders()