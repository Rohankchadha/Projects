import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import demoji
import pickle
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector
def process():
    a=pd.read_csv('amazon_new.csv')
    a['Category']=a['Category'].apply(lambda x:0 if x=='__label__1' else 1)
    a=a.drop('Unnamed: 2',axis=1)
    return a[:][0:100]

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

# def get_lang_detector(nlp, name):
#     return LanguageDetector(seed=42)

# nlp_model = spacy.load("en_core_web_sm")
# Language.factory("language_detector", func=get_lang_detector)
# nlp_model.add_pipe('language_detector', last=True)

# def Language_Detection(txt):
#     doc = nlp_model(txt)
#     return (doc._.language['language'])

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

def processed(dataa):
    data=dataa
    data["text"] = data["text"].str.lower()
    data["text"] = data["text"].apply(lambda i: Text_Cleaning(i))
    data['text'] = data["text"].str.replace('\n' , ' ')
    data['text'] = data['text'].str.replace(r'[^\w\s]+', ' ')
    # data['lan'] = data['Text'].apply(lambda x: Language_Detection(x))
    # inx = data[data['lan']!='en'].index
    # data.drop(inx, inplace = True)
    data['text']=data['text'].apply(lambda z: clean_func(z))
    data["text"] = data['text'].apply(lambda x: remove_stopwords(x))
    # iname = data[data['Text']==''].index
    # data.drop(iname, inplace = True)
    # data.reset_index(inplace = True)
    dflm = data.copy()
    dflm['text'] = data['text'].apply(newlemma)
    # a=pd.read_csv('Datatomerge.csv')
    # print(a.shape)
    # print(len(dflm['Text']))
    dta=pd.read_csv('Cleaned_complaints.csv')
    dta=dta.dropna()
    data1=dta['text'][0:5000]
    # print(data1)
    data2=pd.concat([data1,dflm['text']],ignore_index=True)
    # print(data2.shape)
    # for i in dflm['Text']:
    #     data1.append(i)
    tfidf = TfidfVectorizer(use_idf=True,max_features=1000)
    result = tfidf.fit_transform(data2)
    fet=tfidf.get_feature_names_out()
    arr=result.toarray()
    dfff=pd.DataFrame(arr, columns=fet)
    x=dfff[:][:5000]
    print(x.shape)
    # return dfff
    # x=dfff
    y=dta['Category'][0:5000]
    # print(y.shape)
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.10, random_state=0)
    model=LogisticRegression()
    j=model.fit(x_train,y_train)
    # prdd=j.predict(x_test)
    # prddd=model.score(prdd,y_test)
    # print(prddd)
    prediction=j.predict(dfff[:][5000:])
    pred={}
    for i,j in zip(dataa['text'],prediction):
        pred.update({i:j})
    pp={}
    nn={}
    for i in pred.keys():
        if pred[i] == 0:
            nn.update({i:pred[i]})
        else:
            pp.update({i:pred[i]})

    print(pp)
    print(nn)
    return pp,nn
    
    # sc=model.score(prediction,y_test)
    # print(sc)
    # pred=[]
    # for i in x_test.index():
    #     pred.append(i)
    # print(pred)
    # a=pickle.load(open('TwitterModel.txt','rb'))
    # pred=a.predict(dfff)
    # return pred
# process()
