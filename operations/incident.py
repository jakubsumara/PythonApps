class Incident:
    __max_id = 0
    def __init__(self, description, location, priority, time):
        self.id = Incident.__max_id
        self.description = description
        self.location = location
        self.priority = priority
        self.time = time
        self.status = "Dead or not? We don't know yet"
        Incident.__max_id += 1

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r}, location{self.location}, priority={self.priority}, hour={self.time}, status={self.status})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}, location: {self.location}, priority: {self.priority}, hour: {self.time}, status: {self.status}"
    
    def add_ambulance(self, ambulance):
        self.ambulance = ambulance
        ambulance.add_incident(self)
        print(f'Ambulance{self.ambulance.id} was added to incident{self.id}')