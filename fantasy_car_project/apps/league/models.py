from django.db import models

class Season(models.Model):
    year = models.IntegerField()


class Track(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    # Needs to be a float.
    length = models.FloatField()


class Race(models.Model):
    name = models.CharField(max_length=80)
    length = models.IntegerField()
    date = models.DateField()
    driver_limit = models.IntegerField()
    
    track = models.ForeignKey(Track, related_name="races")
    season = models.ForeignKey(Season, related_name="races")

    # This may need to get moved out into a class for some additional
    # attributes
    drivers = models.ManyToManyField("Driver", through="RaceParticipant", related_name="races")

    def __init__(self, *args, **kwargs):
        super(Race, self).__init__(*args, **kwargs)
        self._winner = None
        

    @property
    def winner(self):
        """
        Return the winner based on the finishing position of participants
        
        """
        if self._winner: return self._winner
        
        winning_participant = RaceParticipant.objects.get(finish_position=1, race=self)
        
        # Winner may be null if the race hasn't yet been run.
        if winning_participant: self._winner = winning_participant.driver
        
        return self._winner
        
        

class Driver(models.Model):
    name = models.CharField(max_length=100)
    number= models.IntegerField()
    
    seasons = models.ManyToManyField(Season, related_name="drivers")


class RaceParticipant(models.Model):
    """
    Information about a driver's participation in a race.
    """
    race = models.ForeignKey(Race)
    driver = models.ForeignKey(Driver)
    
    start_position = models.IntegerField(blank=True)
    finish_position = models.IntegerField(blank=True)
