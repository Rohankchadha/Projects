from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def loginpage(request):
	return render(request, 'AdminSide/loginpage.html')

def registerpage(request):
	return render(request, 'AdminSide/registerpage.html')

def addstudent(request):
	return render(request, 'AdminSide/addstudent.html')

def showstudent(request):
	return render(request, 'AdminSide/showstudent.html')

def homepage(request):
	return render(request, 'AdminSide/homepage.html')

def mainpage(request):
	return render(request, 'AdminSide/mainpage.html')

def tables(request):
	return render(request, 'AdminSide/tables.html')

def dtat(request):
	if request.method == "POST":
		name=request.POST['sname']
		classs=request.POST['sclass']
		s = Student()
		s.name=name
		s.classs=classs
		s.save()
		return HttpResponse(request, Student.name, Student.classs)
	else:
		return HttpResponse("Nothing to show")