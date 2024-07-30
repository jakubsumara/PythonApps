# tests/test_driver.py

import pytest
from personnel.driver import Driver

def test_driver_creation():
    driver = Driver('John', 'Doe', 1, 5000, 'LIC123', ['BLS'])
    assert driver.first_name == 'John'
    assert driver.last_name == 'Doe'
    assert driver.license_number == 'LIC123'

def test_display_info():
    driver = Driver('John', 'Doe', 1, 5000, 'LIC123', ['BLS'])
    info = driver.display_info()
    assert 'John Doe' in info
    assert 'LIC123' in info
