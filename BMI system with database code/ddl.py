from tkinter import *
from tkinter.ttk import *
import csv


class Dg:
    # '''Display a GUI allowing key->value lookup'''
    def __init__(self, parent, row, column, dictionary):
        self.dictionary = dictionary
        self.selection = StringVar()
        self.value = StringVar()

        username_label = Label(parent, text="Key:")
        username_label.grid(row=row, column=column)
        keys = list(sorted(dictionary.keys()))
        self.selection.trace('w', self.update)  ## Added this line
        self.selection.set(keys[0])
        select = Combobox(parent, textvariable=self.selection,
                        values=keys,
                        width=8)
        select.grid(row=row, column=column+1)

        name = Label(parent, textvariable=self.value)
        name.grid(row=row, column=column+3)

    def update(self, *a):
        self.value.set(self.dictionary[self.selection.get()])

def main():
    window = Tk()
    test_dict = {'first_name': 'Fred', 'last_name': 'Bloggs', 'age' : 20}
    gui = Dg(window, 0, 0, test_dict)
    window.mainloop()

main() 