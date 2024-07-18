from dateutil.relativedelta import relativedelta
import datetime
import yfinance as yf
import pandas as pd
t1 = datetime.datetime.now() - relativedelta(days=0,months=1,years=0)
data2=yf.download(['BNB-EUR'], start=str(t1.date()))
dd=data2.index
d1=dd.astype('str')
a=pd.DataFrame({'a':d1})
b=a['a'].apply(lambda x:x[8:10])
a["Day"]=b
print(a)