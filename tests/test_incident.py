# tests/test_incident.py

import pytest
from operations.incident import Incident

def test_incident_creation():
    incident = Incident(1, (50.0, 20.0), 5)
    assert incident.id == 1
    assert incident.location == (50.0, 20.0)
    assert incident.severity == 5

def test_incident_update_severity():
    incident = Incident(1, (50.0, 20.0), 5)
    incident.update_severity(7)
    assert incident.severity == 7

def test_incident_invalid_severity():
    incident = Incident(1, (50.0, 20.0), 5)
    with pytest.raises(ValueError):
        incident.update_severity(11)
