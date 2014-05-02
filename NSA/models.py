from django.db import models
import datetime


class Event(models.Model):
    sport = models.CharField(max_length=30)
    #number of players the event has
    players = models.IntegerField(default=0)
    #extra information about the event
    #info = models.CharField(max_length=128)
    #date = models.CharField()
    weekday = models.CharField(max_length=30)
    time = models.TimeField()
    address = models.CharField(max_length=300)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.sport

    def get_address(self):
        return self.address