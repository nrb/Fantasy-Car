from unittest import TestCase

from league.models import Race


class RaceTest(TestCase):
    def test_create_race(self):
        race = Race(length=500, name="Daytona 500")
        assert race.length == 500
        
    def test_race_has_drivers(self):
        pass
    
    def test_race_driver_limit(self):
        pass
    
    def test_race_has_track(self):
        pass
    
    def test_race_in_season(self):
        pass

