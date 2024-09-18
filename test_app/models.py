from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=30)
    npm = models.CharField(max_length=10)
    course = models.CharField(max_length=15)
