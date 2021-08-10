from django.db import models

from django.utils import timezone

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100,default=None)
    email=models.CharField(max_length=100,default=None)
    password=models.CharField(max_length=100)