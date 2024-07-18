from opencv.fr.persons.schemas import PersonBase
from pathlib import Path
import cv2,os
from opencv.fr import FR
from opencv.fr.search.schemas import SearchRequest, SearchMode, SearchOptions,DetectionRequest
from PIL import Image


BACKEND_URL = "https://sg.opencv.fr"
DEVELOPER_KEY = "8TDucBbZWY4ZDYzMzEtNDRhMC00ZWIxLWJkY2ItYjFmNGIyYzJiMDZj"
SDK = FR(BACKEND_URL, DEVELOPER_KEY)
# Create your views here.
def create(image_path,name):
        try:
                person = PersonBase([image_path], name=name)
                person = SDK.persons.create(person)
                return True
        except:
               return False

    
def listall():
    totaldata = SDK.persons.list()
    data="Total Faces Registered - "+str(totaldata.count)
    print(data)
    data2=''
    for i in range(0,totaldata.count):
        data2+="\n"+str(i+1)+". "+totaldata.persons[i].name
    print(data2)


def search(image_path):
        search_request = SearchRequest([image_path])
        result = SDK.search.search(search_request)
        return result

def detect(image_path):
        options=SearchOptions(min_score = 0.6, search_mode = SearchMode.FAST)
        rqst=DetectionRequest(image_path, options)
        result=SDK.search.detect(rqst)
        print(result)
        data="Matching Profiles : "
        # try:
        #         data2=[]
        #         for i in range(0,len(result)):
        #                 data2.append(str(i+1)+". "+result[i].persons[0].person.name)
        #         return data2
        # except:
        #        return result[0].persons[0].person.name
        return result[0].persons[0]


