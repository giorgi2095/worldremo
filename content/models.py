from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.TextField()

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')