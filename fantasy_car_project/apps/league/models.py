from django.db import models

class Season(models.Model):
    year = models.IntegerField()


class Track(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    # Needs to be a float.
    length = models.IntegerField()


class Race(models.Model):
    name = models.CharField(max_length=80)
    length = models.IntegerField()
    date = models.DateField()
    driver_limit = models.IntegerField()
    
    track = models.ForeignKey(Track, related_name="races")
    season = models.ForeignKey(Season, related_name="races")

    # This may need to get moved out into a class for some additional
    # attributes
    drivers = models.ManyToManyField("Driver", related_name="races")

class Driver(models.Model):
    name = models.CharField(max_length=100)
    number= models.IntegerField()
    
    seasons = models.ManyToManyField(Season, related_name="drivers")

