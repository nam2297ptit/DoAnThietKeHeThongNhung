from django.conf import settings
from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    SensorID = models.CharField(max_length=5)
    Date_and_Time = models.CharField(max_length=30)
    Temperature = models.IntegerField()
    Humidity = models.IntegerField()
