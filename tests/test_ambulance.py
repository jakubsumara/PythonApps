import pytest
from fleet.ambulance import Ambulance

def test_ambulance_creation():
    ambulance = Ambulance('AZ124', 'Available', (50.0, 20.0), ['defibrillator', 'stretcher'])
    assert ambulance.id == 1
    assert ambulance.vehicle_type == 'AZ124'
    assert ambulance.location == (50.0, 20.0)

def test_ambulance_update_location():
    ambulance = Ambulance('AZ124', 'Available', (50.0, 20.0), ['defibrillator', 'stretcher'])
    ambulance.update_location((40.0, 30.0))
    assert ambulance.location == (40.0, 30.0)

def test_ambulance_invalid_location():
    ambulance = Ambulance('AZ124', 'Available', (50.0, 20.0), ['defibrillator', 'stretcher'])
    with pytest.raises(ValueError):
        ambulance.update_location((100.0, 200.0))
