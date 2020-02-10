from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,default='abc@gmail.com')
    text = models.TextField(max_length=264)

    def __str__(self):
        return self.name
