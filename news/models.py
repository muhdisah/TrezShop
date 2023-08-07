from django.db import models


# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/news-images')
    description = models.CharField(max_length=500)
    post = models.TextField()
