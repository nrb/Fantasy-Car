from django.db import models

class Season(models.Model):
    year = models.IntegerField()


class Track(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    length = models.IntegerField()


class Race(models.Model):
    name = models.CharField(max_length=80)
    length = models.IntegerField()
    date = models.DateField()
    
    track = models.ForeignKey(Track, related_name="races")
    season = models.ForeignKey(Season, related_name="races")


class Driver(models.Model):
    name = models.CharField(max_length=100)
    number= models.IntegerField()
    
    seasons = models.ManyToManyField(Season, related_name="drivers")

