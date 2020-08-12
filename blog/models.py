from django.db import models
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('post', str(instance.id), filename)

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField('Дата публикации')
    img = models.ImageField(upload_to=get_image_path, null=True)
    