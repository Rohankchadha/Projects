import pandas as pd
dta=pd.read_csv('Cleaned_complaints.csv')
data1=dta['text']
# print(data1)
data1.dropna()
# print(f.isnull().sum())