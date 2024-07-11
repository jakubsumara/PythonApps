from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *
import random

def run_application():
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    print(Ambulance.get_instances_count())

    queue = IncidentQueue()

    prio1 = random.randint(1,100)
    incident1 = Incident("Power outage in sector 4",(53,25),prio1, "06:00")
    prio2 = random.randint(1,100)
    incident2 = Incident("Fire alarm in building 21",(51,21),prio2,"15:00")

    queue += incident1
    queue += incident2

    print("Aktualne zgłoszenia:")
    print(queue)

    station1 = Station((51, 20), ambulance1, driver1.display_info(), employee1.display_info())
    print(f'Station one: {station1}')
    station2 = Station((51, 20), ambulance2, driver2.display_info(), employee2.display_info())
    print(f'Station one: {station2}')
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

    incident1.add_ambulance(ambulance1)
    incident2.add_ambulance(ambulance2)

    ambulance1.ambulance_done()
    ambulance2.ambulance_done()

    for i in queue:
        assert i.status == 'going for coffee'

if __name__ == "__main__":
    run_application()