from django.db import models
from django.conf import settings
from django.core.mail import send_mail

# Create your models here.
class mdl(models.Model):
    name=models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    subject = models.CharField(max_length=70, default='')
    message = models.CharField(max_length=500, default='')
    files = models.FileField(default='', upload_to='files/')
    images=models.ImageField(upload_to='images/')
