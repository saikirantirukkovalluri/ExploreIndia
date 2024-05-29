from django.db import models

# Create your models here.
class StatesData(models.Model):
    statnam=models.CharField(max_length=100)
    lang=models.CharField(max_length=100)
    food=models.CharField(max_length=100)
    fest=models.CharField(max_length=100)
    art=models.CharField(max_length=500)
    sport=models.CharField(max_length=100)
    arch=models.CharField(max_length=1000)
    cloth=models.CharField(max_length=200)
    tribe=models.CharField(max_length=500)
class Loc(models.Model):
    statnam=models.CharField(max_length=100)
    lon=models.FloatField()
    lat=models.FloatField()