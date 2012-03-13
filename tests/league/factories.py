from datetime import date

import factory

from league.models import Season, Track, Race, Driver, RaceParticipant

class SeasonFactory(factory.Factory):
    FACTORY_FOR = Season
    
    year = 2012

class TrackFactory(factory.Factory):
    FACTORY_FOR = Track
    
    name = "Daytona International Speedway"
    city = "Daytona, FL"
    length = 1.5

    
class DriverFactory(factory.Factory):
    FACTORY_FOR = Driver
    
    name = "Jimmie Johnson"
    number = 48

class RaceFactory(factory.Factory):
    FACTORY_FOR = Race
    
    name = "Daytona 500"
    length = 500
    date = date(year=2012, month=2, day=14)
    driver_limit = 43
    
    track = factory.SubFactory(TrackFactory)
    season = factory.SubFactory(SeasonFactory)

class RaceParticipantFactory(factory.Factory):
    FACTORY_FOR = RaceParticipant
    
    finish_position = 1
    start_position = 1

    driver = factory.SubFactory(DriverFactory)
    race = factory.SubFactory(RaceFactory)
