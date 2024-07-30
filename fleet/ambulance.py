# ambulance.py

from datetime import datetime
import math
from logger_config import logger

class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment', 'incident', 'state']
    __instances_count = 0
    __max_id = 1

    def __init__(self, vehicle_type, status, location, medical_equipment):
        self.id = Ambulance.__max_id
        self.vehicle_type = vehicle_type
        self.status = status  
        self.location = location
        self.medical_equipment = medical_equipment
        self.incident = []
        self.state = 'coffee break'
        Ambulance.__instances_count += 1
        Ambulance.__max_id += 1
        logger.info(f'Ambulance {self.id} created at location {self.location}')

    def update_location(self, new_location):
        if not (-90 <= new_location[0] <= 90 and -180 <= new_location[1] <= 180):
            logger.error(f'Invalid location: {new_location}')
            raise ValueError('Invalid location coordinates')
        self.state = 'hitting the road'
        self.location = new_location
        logger.info(f'Ambulance {self.id} moved to {self.location}')
    
    def add_incident(self, incident):
        self.incident.append(incident)
        logger.info(f'Added incident {self.incident[-1].id} to ambulance {self.id}')
        self.state = 'got incident'
        logger.info(f'ambulance {self.id} got incident') 
    
    def sort_incident(self):
        self.incident = sorted(self.incident, key=lambda x: (x.priority, x.time))  
        self.state = u'\U0001F914'
        logger.info(f'Sorted incident: {self.incident}')

    def time_from_incident_happend(self, incident):
        time_now = datetime.now().strftime("%H:%M")
        time_of_incident = datetime.strptime(incident.time, '%H:%M').strftime("%H:%M")
        logger.info(f'Time right now: {time_now}, incident time: {time_of_incident}')
    
    def distance_from_incident(self, incident):
        distance = math.sqrt((self.location[0] - incident.location[0]) ** 2 + (self.location[1] - incident.location[1]) ** 2)
        logger.info(f"Shortest distance from an incident: {distance}")

    def ambulance_done(self):
        self.sort_incident()
        assert self.state == u'\U0001F914'
        for accident in self.incident:
            self.time_from_incident_happend(accident)
            self.distance_from_incident(accident)
        self.state = 'done'
        logger.info(f'Ambulance {self.id} is done with all incidents')

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        return self.id == other.id and self.vehicle_type == other.vehicle_type
    
    def __str__(self):
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}")
    
    @staticmethod
    def validate_id(ambulance_id):
        valid = isinstance(ambulance_id, int) and ambulance_id > 0
        logger.info(f'Validating ambulance ID {ambulance_id}: {valid}')
        return valid

    @classmethod
    def get_instances_count(cls):
        count_info = f"Number of working ambulances: {cls.__instances_count}"
        logger.info(count_info)
        return count_info

if __name__ == "__main__":
    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())
