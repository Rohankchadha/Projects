from django.urls import path
from . import views

urlpatterns=[
    path('main/', views.main, name='main'),
    path('get_data/', views.get_data, name='get_data')
]