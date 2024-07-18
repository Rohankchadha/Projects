from tkinter import *
from tkhtmlview import HTMLLabel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime,pickle
import yfinance as yf
import seaborn as sns
from currency_converter import CurrencyConverter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Crypto made EZ")
        self.root.geometry("1000x600+200+30")
        
    def callback(self, var):
        self.content= var.get()
        aa=self.content
        data=[aa+"-EUR"]
        data1=yf.download(data, start=str(datetime.date.today().isoformat()))
        print(data1)
        self.a1=str(data1['Open'][0])
        self.a2=str(data1['Close'][0])
        self.a3=str(data1['High'][0])
        self.a4=str(data1['Low'][0])
        self.lbl = Label(self.fr1, text='')
        self.lbl.place(x=550,y=150, width=400, height=400)
        
        
    def create(self):
        data1 = {'country': ['A', 'B', 'C', 'D', 'E'],'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]}
        df1 = pd.DataFrame(data1)
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1000, height=600)
        self.fr1.config(bg="black")
        
        options = ["BNB","LTC"]
        self.var = StringVar(self.fr1)
        self.var.trace("w", lambda name, index,mode, var=self.var: self.callback(var))
        self.var.set(options[0])
        self.ent = OptionMenu(self.fr1, self.var, *options)
        self.ent.place(x=320, y=90, width=380, height=30)
        
        self.lbl = Label(self.fr1, text='')
        self.lbl.place(x=50,y=150, width=200, height=100)
        self.lbl = Label(self.fr1, text='')
        self.lbl.place(x=50,y=280, width=00, height=100)
        self.lbl = Label(self.fr1, text='')
        self.lbl.place(x=50,y=400, width=200, height=100)
        self.lbl = Label(self.fr1, text='')
        self.lbl.place(x=50,y=500, width=200, height=100)
        
        
        
        
        # self.figure1 = plt.Figure(figsize=(3, 3), dpi=70)
        # self.ax1 = self.figure1.add_subplot(111)
        # self.bar1 = FigureCanvasTkAgg(self.figure1, self.fr1)
        # self.bar1.get_tk_widget().place(x=550,y=150, width=400, height=400)
        # self.df1.plot(kind='bar', legend=True, ax=self.ax1)
        # self.ax1.set_title('Country Vs. GDP Per Capita')
        
        # self.lbl = Label(self.fr1, text='')
        # self.lbl.place(x=550,y=150, width=400, height=400)
        
        

if __name__== '__main__':
    obj = Frame1()
    obj.create()
    obj.root.mainloop()