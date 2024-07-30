# tests/test_incident_queue.py

import pytest
from operations.incident_queue import IncidentQueue
from operations.incident import Incident

def test_incident_queue_creation():
    queue = IncidentQueue()
    assert len(queue) == 0

def test_add_incident():
    queue = IncidentQueue()
    incident = Incident(1, (50.0, 20.0), 5)
    queue.add_incident(incident)
    assert len(queue) == 1

def test_get_next_incident():
    queue = IncidentQueue()
    incident1 = Incident(1, (50.0, 20.0), 5)
    incident2 = Incident(2, (51.0, 21.0), 7)
    queue.add_incident(incident1)
    queue.add_incident(incident2)
    next_incident = queue.get_next_incident()
    assert next_incident.id == 1
    assert len(queue) == 1
