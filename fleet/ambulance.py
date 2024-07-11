# V1 - slajd 8
from datetime import datetime
import math
class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment','incident','state']
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

    def update_location(self, new_location):
        self.state = 'hitting the road'
        self.location = new_location
    
    def add_incident(self, incident):
        self.incident.append(incident)
        print(f'Added incident{self.incident[-1].id} to ambulance{self.id}')
        self.state = 'got incident'
        print(f'ambulance{self.id} got incident') 
    
    def sort_incident(self):
        self.incident = sorted(self.incident, key=lambda x: (x.priority, x.time))  
        self.state = u'\U0001F914'
        print(f'Sorted incident: {self.incident}')

    def time_from_incident_happend(self, incident):
        time_now = datetime.now()
        time_now = time_now.strftime("%H:%M")
        time_of_incident = datetime.strptime(incident.time, '%H:%M')
        time_of_incident = time_of_incident.strftime("%H:%M")

        print(f'Time right now: {time_now}, incident time: {time_of_incident}')
    
    def distance_from_incident(self, incident):
        print(f"Shortest distance from an incident: {math.sqrt((self.location[0]-incident.location[0])**2 + (self.location[1]-incident.location[1])**2)}")

    def ambulance_done(self):
        self.sort_incident()
        assert self.state == u'\U0001F914'
        for accident in self.incident:
            self.time_from_incident_happend(accident)
            self.distance_from_incident(accident)
            self.update_location(accident.location)
            assert self.state == 'hitting the road'
            accident.status = 'going for coffee'
            self.state = 'going for coffee'
            assert self.state == 'going for coffee'
            print("incident done, going for coffee \U0001f604")

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
        return isinstance(ambulance_id, int) and ambulance_id > 0

    @classmethod
    def get_instances_count(cls):
        return f"Number of working ambulances: {cls.__instances_count}"

if __name__ == "__main__":
    ambulance1 = Ambulance(
        #id=0,
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        #id=1,
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

    # ambulance1.whatever = "123"
    # print(ambulance1.whatever)

    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())