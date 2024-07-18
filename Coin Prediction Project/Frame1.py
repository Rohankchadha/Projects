from tkinter import *
# from tkhtmlview import HTMLLabel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
import datetime,pickle,calendar
import yfinance as yf
# import seaborn as sns
# from currency_converter import CurrencyConverter
from dateutil.relativedelta import relativedelta

class Frame1:    
    def __init__(self, root=""):
        if(root==""):
            self.root = Tk()
        else:
            self.root = root
        self.root.title("Crypto made EZ")
        self.root.geometry("1300x800")
        
    def processbnb(self):
        model=pickle.load(open('SavedModel.txt', 'rb'))
        self.data=self.data1.drop(["Close","Adj Close"], axis=1)
        self.pred=model.predict(self.data)
        self.pred=str(round(self.pred[0][0],3))+' EUR'
                
        self.label11 = Label(self.fr1, text=self.pred)
        self.label11.place(x=370,y=610,width=200,height=70)
        self.label11.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.btn=Label(self.fr1, text="Predicted Price - ")
        self.btn.place(x=70,y=610, width=300, height=70)
        self.btn.config(bg='black', fg='white',font=('Times New Roman',30,'bold'))

    def processltc(self):
        model=pickle.load(open('finalized_model.pkl', 'rb'))
        self.data=self.data1.drop(["Close","Adj Close"], axis=1)
        self.pred=model.predict(self.data)
        self.pred=str(round(self.pred[0][0],3))+' EUR'
                
        self.label11 = Label(self.fr1, text=self.pred)
        self.label11.place(x=370,y=610,width=200,height=70)
        self.label11.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.btn=Label(self.fr1, text="Predicted Price - ")
        self.btn.place(x=70,y=610, width=300, height=70)
        self.btn.config(bg='black', fg='white',font=('Times New Roman',30,'bold'))

    def callback(self, var):
        self.content= var.get()
        aa=self.content
        self.data=[aa+"-EUR"]
        self.data1=yf.download(self.data, start=str(datetime.date.today().isoformat()))
        # print(self.data1)
        self.a1=str(round(self.data1['Open'][0],3))+" EUR"
        self.a2=str(round(self.data1['Volume'][0],3))+" EUR"
        self.a3=str(round(self.data1['High'][0],3))+" EUR"
        self.a4=str(round(self.data1['Low'][0],3))+" EUR"
        
        self.t1 = datetime.datetime.now() - relativedelta(days=0,months=1,years=0)
        self.data2=yf.download(self.data, start=str(self.t1.date()))
        self.data3=self.data2.loc[:][['Open','High','Low','Volume']]

        self.dd=self.data2.index
        self.d1=self.dd.astype('str')
        self.a=pd.DataFrame({'a':self.d1})
        day=self.a['a'].apply(lambda x:x[8:10])
        month=self.a['a'].apply(lambda x:x[5:7])
        # print(day)
        self.data3.insert(4,"Day",day)
        self.data3.insert(5,"Month",month)
        # print(self.data3.columns)
        
        self.label11 = Label(self.fr1, text=self.a1)
        self.label11.place(x=270,y=220,width=200,height=70)
        self.label11.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.label22 = Label(self.fr1, text=self.a2)
        self.label22.place(x=270,y=320,width=250,height=70)
        self.label22.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.label33 = Label(self.fr1, text=self.a3)
        self.label33.place(x=270,y=420,width=200,height=70)
        self.label33.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.label44 = Label(self.fr1, text=self.a4)
        self.label44.place(x=270,y=520,width=200,height=70)
        self.label44.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        if(aa=='BNB'):
            self.btn=Button(self.fr1, text='Predict Price', command=self.processbnb)
            self.btn.place(x=70,y=610, width=500, height=70)
            self.btn.config(bg='black', fg='white',font=('Times New Roman',22,'bold'))
        elif(aa=='LTC'):
            self.btn=Button(self.fr1, text='Predict Closing Price', command=self.processltc)
            self.btn.place(x=70,y=610, width=500, height=70)
            self.btn.config(bg='black', fg='white',font=('Times New Roman',22,'bold'))
        
        # self.figure = plt.Figure(figsize=(6,5), dpi=100)
        # self.ax = self.figure.add_subplot(111)
        # self.chart_type = FigureCanvasTkAgg(self.figure, self.fr1)
        # self.chart_type.get_tk_widget().place(x=600,y=200, width=600, height=400)
        # self.data3.plot(kind='line', x='Open',y='Close', legend=True, ax=self.ax)
        # self.ax.set_title('The Title for your chart')
        figure2 = plt.Figure(figsize=(6, 6), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.fr1)
        line2.get_tk_widget().place(x=600, y=50, width=600, height=600)
        self.data2 = self.data2[['High', 'Low']].groupby('Date').sum()
        self.data2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        self.dd1=self.data3
        # self.mm1=self.data3
        print(self.dd1)
        # print(self.mm1)
        # self.str=calendar.month_name[int(self.dd1)]
        # self.end=calendar.month_name[int(self.mm1)]
        # title="Data of "+self.str+" to "+self.end
        # ax2.set_title(title)

    
    def create1(self):
        self.fr1 = Frame(self.root)
        self.fr1.place(x=0, y=0, width=1300, height=800)
        self.fr1.config(bg="black")

        self.label = Label(self.fr1, text="EZcoins")
        self.label.place(x=65,y=20,width=300,height=70)
        self.label.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")

        self.txt = Label(self.fr1, text="Select Coins")
        self.txt.place(x=40,y=135)
        self.txt.config(bg="black", fg="white")
        options = ["BNB","LTC"]
        self.var = StringVar(self.fr1)
        self.var.trace("w", lambda name, index,mode, var=self.var: self.callback(var))
        self.var.set(options[0])
        self.ent = OptionMenu(self.fr1, self.var, *options)
        self.ent.place(x=120, y=130, width=380, height=30)
        
        self.label1 = Label(self.fr1, text="Open - ")
        self.label1.place(x=65,y=220,width=200,height=70)
        self.label1.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
        self.label11 = Label(self.fr1, text="-")
        self.label11.place(x=270,y=220,width=200,height=70)
        self.label11.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.label2 = Label(self.fr1, text="Volume - ")
        self.label2.place(x=65,y=320,width=200,height=70)
        self.label2.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
        self.label22 = Label(self.fr1, text="-")
        self.label22.place(x=270,y=320,width=250,height=70)
        self.label22.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.label3 = Label(self.fr1, text="High - ")
        self.label3.place(x=65,y=420,width=200,height=70)
        self.label3.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
        self.label33 = Label(self.fr1, text="-")
        self.label33.place(x=270,y=420,width=200,height=70)
        self.label33.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.label4 = Label(self.fr1, text="Low - ")
        self.label4.place(x=65,y=520,width=200,height=70)
        self.label4.config(font=('Times New Roman',30,'bold'),bg="black",fg="white")
        self.label44 = Label(self.fr1, text="-")
        self.label44.place(x=270,y=520,width=200,height=70)
        self.label44.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.lbl5=Label(self.fr1, text="")
        self.lbl5.place(x=600, y=50, width=600, height=600)
        self.lbl5.config(font=('Times New Roman',22,'bold'),bg="black",fg="white")
        
        self.btn=Label(self.fr1, text='')
        self.btn.place(x=70,y=610, width=500, height=70)
        self.btn.config(bg='black', fg='white',font=('Times New Roman',22,'bold'))


if __name__== '__main__':
    obj = Frame1()
    obj.create1()
    obj.root.mainloop()