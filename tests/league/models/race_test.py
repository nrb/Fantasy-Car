from unittest import TestCase

from tests.league.factories import RaceFactory, TrackFactory, SeasonFactory, SeasonFactory

class RaceTest(TestCase):
    def test_create_race(self):
        race = RaceFactory()
        assert race.length == 500
        
    def test_race_has_drivers(self):
        race = RaceFactory()
        assert race.drivers
        
    def test_race_driver_limit(self):
        race = RaceFactory.build()
        
        assert race.driver_limit == 43

    def test_race_has_track(self):
        race = RaceFactory()
        
        assert race.track
    
    def test_race_in_season(self):
        race = RaceFactory()
        
        assert race.season

