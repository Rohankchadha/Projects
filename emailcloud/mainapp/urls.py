from django.urls import path,include
from . import views

urlpatterns=[
    path('page1/', views.page1, name='page1'),
    path('page2/', views.send, name="page2"),
    path('addimg/', views.addimg, name='addimg'),
    path('showimg/', views.showimg, name='showimg'),
]