# driver.py

from .employee import Employee
from logger_config import logger

class Driver(Employee):
    def __init__(self, first_name, last_name, employee_id, salary, license_number, qualifications):
        super().__init__(first_name, last_name, employee_id, salary)
        self.license_number = license_number
        self.qualifications = qualifications
        logger.info(f'Driver {self.first_name} {self.last_name} with ID {self.employee_id} created')

    def display_info(self):
        info = (f"Driver ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, "
                f"Salary: {self.salary}, License Number: {self.license_number}, "
                f"Qualifications: {', '.join(self.qualifications)}")
        logger.info(info)
        return info

if __name__ == "__main__":
    driver1 = Driver("Jane", "Smith", 1, 12000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
