from django.urls import path
from . import views

urlpatterns = [
    path('img/', views.img, name='img'),
    path('show/', views.show, name='show'),
]