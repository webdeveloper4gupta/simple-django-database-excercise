from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=255)