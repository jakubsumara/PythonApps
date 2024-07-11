class Station:
    __station_id = 0
    def __init__(self, location, ambulance, driver, employee):
        self.location = location 
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        self.id = Station.__station_id
        Station.__station_id += 1    

    def __str__(self):
        return f"Station {self.id}: location: {self.location}, ambulance: {self.ambulance}, driver: {self.driver}, employee: {self.employee}"
    
    def check_location(self):

        if self.location == self.ambulance.location:
            print("Ambulance is on coffee break")
        else:
            print("Ambulance hitting the road")       