# station.py

from logger_config import logger

class Station:
    __station_id = 0
    
    def __init__(self, location, ambulance, driver, employee):
        self.location = location 
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        self.id = Station.__station_id
        Station.__station_id += 1
        logger.info(f'Station {self.id} created at location {self.location} with ambulance {self.ambulance}, driver {self.driver}, employee {self.employee}')

    def __str__(self):
        return f"Station {self.id}: location: {self.location}, ambulance: {self.ambulance}, driver: {self.driver}, employee: {self.employee}"
    
    def check_location(self):
        if self.location == self.ambulance.location:
            logger.info("Ambulance is on coffee break")
            print("Ambulance is on coffee break")
        else:
            logger.info("Ambulance hitting the road")
            print("Ambulance hitting the road")
    
    def __eq__(self, other):
        if not isinstance(other, Station):
            return NotImplemented
        return self.id == other.id
    
    @staticmethod
    def validate_id(station_id):
        valid = isinstance(station_id, int) and station_id > 0
        logger.info(f'Validating station ID {station_id}: {valid}')
        return valid

    @classmethod
    def get_instances_count(cls):
        count_info = f"Number of working stations: {cls.__station_id}"
        logger.info(count_info)
        return count_info

if __name__ == "__main__":
    station1 = Station(
        location=(50.095340, 19.920282),
        ambulance="AZ124",
        driver="John Doe",
        employee="Jane Smith"
    )
    station2 = Station(
        location=(51.095340, 20.920282),
        ambulance="AZ2000",
        driver="Alice Johnson",
        employee="Bob Brown"
    )

    print(station1 == station2)
    print(station1)

    print(Station.validate_id(1))
    print(Station.validate_id("1"))

    print(Station.get_instances_count())
