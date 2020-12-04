from django.db import models

# Create your models here.
class Airport(models.Model):
    iata = models.CharField(max_length=30)
    icao = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    gps = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
