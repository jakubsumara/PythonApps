# tests/test_station.py

import pytest
from fleet.station import Station

def test_station_creation():
    station = Station((50.0, 20.0), 'AZ124', 'John Doe', 'Jane Smith')
    assert station.id == 0
    assert station.location == (50.0, 20.0)

def test_station_check_location():
    class MockAmbulance:
        def __init__(self, location):
            self.location = location

    ambulance = MockAmbulance((50.0, 20.0))
    station = Station((50.0, 20.0), ambulance, 'John Doe', 'Jane Smith')
    station.check_location()

def test_station_invalid_id():
    assert not Station.validate_id('abc')
    assert Station.validate_id(1)
