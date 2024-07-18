from django.db import models

# Create your models here.
class UploadImage(models.Model):
    caption_name = models.CharField(max_length=200)
    caption_image = models.ImageField(upload_to="images/")
