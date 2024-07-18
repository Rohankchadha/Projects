from django.urls import path
from . import views

urlpatterns=[
	path('loginpage', views.loginpage, name='loginpage'),
	path('registerpage', views.registerpage, name='registerpage'),
	path('addstudent', views.addstudent, name='addstudent'),
	path('showstudent', views.showstudent, name='showstudent'),
	path('homepage', views.homepage, name='homepage'),
	path('mainpage', views.mainpage, name='mainpage'),
	path('tables', views.tables, name='tables'),
	path('dtat', views.dtat, name='dtat')
]