from django.db import models
from django.db.models.fields import DateField

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    date = models.DateField()
    pages = models.IntegerField()
