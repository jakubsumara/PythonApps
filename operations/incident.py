# incident.py

from logger_config import logger

class Incident:
    def __init__(self, id, location, severity):
        self.id = id
        self.location = location
        self.severity = severity
        logger.info(f'Incident {self.id} reported at location {self.location} with severity {self.severity}')

    def update_severity(self, new_severity):
        if not (0 <= new_severity <= 10):
            logger.error(f'Invalid severity: {new_severity}')
            raise ValueError('Invalid severity value')
        self.severity = new_severity
        logger.info(f'Incident {self.id} severity updated to {self.severity}')
    
    def __eq__(self, other):
        if not isinstance(other, Incident):
            return NotImplemented
        return self.id == other.id
    
    def __str__(self):
        return f"Incident ID: {self.id}, Location: {self.location}, Severity: {self.severity}"
    
    @staticmethod
    def validate_id(incident_id):
        valid = isinstance(incident_id, int) and incident_id > 0
        logger.info(f'Validating incident ID {incident_id}: {valid}')
        return valid

    @classmethod
    def get_instances_count(cls):
        count_info = f"Number of reported incidents: {cls.__instances_count}"
        logger.info(count_info)
        return count_info

if __name__ == "__main__":
    incident1 = Incident(1, (50.095340, 19.920282), 5)
    incident2 = Incident(2, (51.095340, 20.920282), 7)

    print(incident1 == incident2)
    print(incident1)

    print(Incident.validate_id(1))
    print(Incident.validate_id("1"))

    print(Incident.get_instances_count())
