from django.db import models
#from geoposition.fields import GeopositionField


class Event(models.Model):
    sport = models.CharField(max_length=30)
    #number of players the event has
    players = models.IntegerField(default=0)
    #extra information about the event
    info = models.CharField(max_length=128)
    #position = GeopositionField()

    def __str__(self):
        return self.sport, self.info