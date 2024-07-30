# employee.py

from logger_config import logger

class Employee:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        logger.info(f'Employee {self.first_name} {self.last_name} with ID {self.employee_id} created')

    def display_info(self):
        info = f"Employee ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary} zł"
        logger.info(info)
        print(info)

    def update_salary(self, new_salary):
        self.salary = new_salary
        logger.info(f'Updated salary: {self.salary}')
        print(f"Updated salary: {self.salary}")
