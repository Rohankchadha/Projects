import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import demoji
import pickle
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector
# import snscrape.modules.twitter as sntwitter
import pandas as pd
import random as r
def process(a1):

    # Creating list to append tweet data to
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    # for i,tweet in enumerate(sntwitter.TwitterSearchScraper('(#example OR #suggestion) since:2020-09-01 until:2022-09-01').get_items()):
    #     if i>100:
    #         break
    #     tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
    # # Creating a dataframe from the tweets list above 
    # tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

    # print(tweets_df1['Text'])
    b='from:'+a1

    # for i,tweet in enumerate(sntwitter.TwitterSearchScraper(b).get_items()):
    #     if i>100:
    #         break
    #     tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
    # Creating a dataframe from the tweets list above 
    # tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    # print(tweets_df1['Text'])
    # return tweets_df1

def Text_Cleaning(a):
        #Remove URL's
    a = re.sub(r'https?://\S+', ' ', a)
        
        #Remove Tags
    a = re.sub(r'@\w*', ' ' , a)
        
        #Remove HashTags
    a = re.sub(r'#\w*', ' ' , a)
        
        #Remove Email
    a = re.sub(r'[A-Za-z0-9]*@[A-Za-z]*\.?[A-Za-z0-9]*',' ', a)
        
        #Remove apostrophe
    a = re.sub(r"['’](\s)*[a-z]+", ' ', a)
        
        #Remove Number
    a = re.sub(r"[\d]+" , ' ' , a)
        
        #Remove Emoji
    a = demoji.replace(a,' ')
        
    return a

def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)

nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)

def Language_Detection(txt):
    doc = nlp_model(txt)
    return (doc._.language['language'])

def clean_func(a):
    #Remove single chr
    a = re.sub("( [a-z] )|( [a-z]$)", ' ',a)
    
    #Remove Special Chr
    a = re.sub("[^a-zA-Z0-9\s]", ' ', a)
    
    #Remove Space
    a = re.sub(' +', " " , a.strip())
    
    return a

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])

nlp1 = spacy.load('en_core_web_sm')
def newlemma(sentence):
    doc = nlp1(sentence)
    return ' '.join([token.lemma_ for token in doc])

def processed(data):
    data["Text"] = data["Text"].str.lower()
    data["Text"] = data["Text"].apply(lambda i: Text_Cleaning(i))
    data['Text'] = data["Text"].str.replace('\n' , ' ')
    data['Text'] = data['Text'].str.replace(r'[^\w\s]+', ' ')
    data['lan'] = data['Text'].apply(lambda x: Language_Detection(x))
    inx = data[data['lan']!='en'].index
    data.drop(inx, inplace = True)
    data['Text']=data['Text'].apply(lambda z: clean_func(z))
    data["Text"] = data['Text'].apply(lambda x: remove_stopwords(x))
    iname = data[data['Text']==''].index
    data.drop(iname, inplace = True)
    data.reset_index(inplace = True)
    dflm = data.copy()
    dflm['Text'] = data['Text'].apply(newlemma)
    a=pd.read_csv('Datatomerge.csv')
    print(a.shape)
    print(len(dflm['Text']))
    data1=a['tweets']
    data2=pd.concat([data1,dflm['Text']],ignore_index=True)
    print(data2.shape)
    # for i in dflm['Text']:
    #     data1.append(i)
    tfidf = TfidfVectorizer(use_idf=True)
    result = tfidf.fit_transform(data2)
    fet=tfidf.get_feature_names_out()
    arr=result.toarray()
    dfff=pd.DataFrame(arr, columns=fet)
    x=dfff[:6818]
    print(x.shape)
    # return dfff
    # x=dfff
    y=a['account_type']
    print(y.shape)
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.10, random_state=0)
    model=LogisticRegression()
    j=model.fit(x_train,y_train)
    # prdd=j.predict(x_test)
    # prddd=model.score(prdd,y_test)
    # print(prddd)
    prediction=j.predict(dfff[6818:])
    print(prediction)
    bot=np.count_nonzero(prediction=='bot')
    human=np.count_nonzero(prediction=='human')
    print(bot,human)
    txt="Human - "+str(human)+" // Bot - "+str(bot)
    rto = "Ratio of Human/Bot - "+str(round(human/bot,3))
    ff=(bot*100)/(bot+human)
    pct= "Percentage of Bot Tweets - "+str(round(ff,3))+"%"
    return prediction,txt,rto,pct
    # a=pickle.load(open('TwitterModel.txt','rb'))
    # pred=a.predict(dfff)
    # return pred
    