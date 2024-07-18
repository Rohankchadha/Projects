from django.shortcuts import render,HttpResponse
from .models import *
from django.core.mail import send_mail, EmailMessage

# Create your views here.
def page1(request):
        data=mdl.objects.all()
        return render(request, 'mainapp/page1.html', {'data':data})
def send(request):
        if request.method == "POST":
                subject = request.POST['subject']
                msg = request.POST['message']
                to_send = request.POST['to_send']
                # files = request.FILE.getlist('attachment')
                files=request.POST['attachment']
                print(files)
                pic=mdl.objects.get(id=files)
                f=pic.images.path
        try:
                mail=EmailMessage(subject,msg,settings.EMAIL_HOST_USER,[to_send])
                # for f in files:
                #     mail.attach(f.name, f.read(), f.content_type)
                mail.attach_file(f)
                mail.send()
                return render(request, 'mainapp/page2.html')
        except:
                return HttpResponse("Error")
        
def showimg(request):
        data=mdl.objects.all()
        # print(data)
        # print(data[0].images)
        return render(request, 'mainapp/showimg.html',{'data':data})

def addimg(request):
       if request.method == "POST":
                a=request.FILES.getlist('files')
                for i in a:
                        u = mdl()
                        u.images = i
                        u.save()

                return HttpResponse("images saved")
       else:
               return render(request, 'mainapp/addimg.html')
