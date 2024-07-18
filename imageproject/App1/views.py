from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def img(request):
    if request.method == "POST":
        captionname = request.POST["imagename"]
        
        u = UploadImage()
        u.caption_name = captionname
        u.caption_image = request.FILES["simage"]
        u.save()

        return redirect(show)

    return render(request, "App1/fileupload.html")

def show(request):
    ui = UploadImage.objects.all()
    return render(request, "App1/fileshow.html",{"ui": ui})

