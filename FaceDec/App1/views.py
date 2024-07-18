from django.shortcuts import render
from opencv.fr.persons.schemas import PersonBase
from pathlib import Path
from . models import *
from django.conf import settings
from opencv.fr.search.schemas import SearchRequest, SearchMode, SearchOptions,DetectionRequest
import wikipediaapi,os
from PIL import Image

# Create your views here.
def one(request):
#     if request.method == 'POST':
#         imgpath=request.FILE['attachment']
#         image_path=imgpath.path
#         person = PersonBase([image_path], name="Charles")
#         person = settings.SDK.person.create(person)
#         return render(request, 'App1/page2.html')
    return render(request, 'App1/page1.html')

def two(request):
    c=Sample.objects.get(id=6)
    totaldata = settings.SDK.persons.list()
    data="Total Faces Registered - "+str(totaldata.count)
    print(data)
    data2=''
    for i in range(0,totaldata.count):
        data2+="\n"+str(i+1)+". "+totaldata.persons[i].name
    return render(request, 'App1/page2.html',{'data':data, 'data1':c, 'data2':data2})

def sub(request):
    if request.method == 'POST':
        imgpath=request.FILES['attachment']
        print(imgpath)
        a=Sample.objects.get(id=5)
        a.file=imgpath
        a.save()
        return render(request, 'App1/page1.html',{'msg':'Photo Uploaded','data':a})
    return render(request, 'App1/page1.html')


def three(request):
    try:
        b=Sample.objects.get(id=5)
        print(b.file)
        image_path=b.file.path
        print(image_path)
        search_request = SearchRequest([image_path])
        result = settings.SDK.search.search(search_request)
        wik=wikipediaapi.Wikipedia(language='en')
        print(result)
        page=wik.page(result[0].person.name)
        data=" Matching Profile : "+page.title
        data1=b
        data2=page.summary[0:1500]
        # data3=(result[0].person.images)
        data3=""
        return render(request, 'App1/page2.html', {'data':data, 'data1':data1, 'data2':data2, 'data3':data3})
    except:
        return four(request)

def four(request):
    try:
        b=Sample.objects.get(id=5)
        print(b.file)
        image_path=b.file.path
        print(image_path)
        options=SearchOptions(min_score = 0.6, search_mode = SearchMode.FAST)
        rqst=DetectionRequest(image_path, options)
        result=settings.SDK.search.detect(rqst)
        print(result)
        data="Matching Profiles : "
        data2=[]
        for i in range(0,len(result)):
            data2.append(str(i+1)+". "+result[i].persons[0].person.name)
        data1=b
        return render(request, 'App1/page2.html',{'data':data, 'data1':data1, 'data2':data2})
    except:
        return render(request, 'App1/page1.html')