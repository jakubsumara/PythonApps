# tests/test_employee.py

import pytest
from personnel.employee import Employee

def test_employee_creation():
    employee = Employee('John', 'Doe', 1, 5000)
    assert employee.first_name == 'John'
    assert employee.last_name == 'Doe'

def test_update_salary():
    employee = Employee('John', 'Doe', 1, 5000)
    employee.update_salary(6000)
    assert employee.salary == 6000
