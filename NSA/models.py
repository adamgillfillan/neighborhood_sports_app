from django.db import models


class Event(models.Model):
    sport = models.CharField(max_length=30)
    #number of players the event has
    players = models.IntegerField(default=0)
    #extra information about the event
    info = models.CharField(max_length=128)
    address = models.CharField(max_length=300)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.sport