# incident_queue.py

from logger_config import logger

class IncidentQueue:
    def __init__(self):
        self.queue = []
        logger.info('IncidentQueue created')

    def add_incident(self, incident):
        self.queue.append(incident)
        logger.info(f'Incident {incident.id} added to the queue')

    def get_next_incident(self):
        if not self.queue:
            logger.warning('No incidents in the queue')
            return None
        incident = self.queue.pop(0)
        logger.info(f'Incident {incident.id} retrieved from the queue')
        return incident
    
    def __len__(self):
        queue_length = len(self.queue)
        logger.info(f'IncidentQueue length: {queue_length}')
        return queue_length

    def __str__(self):
        return f"IncidentQueue with {len(self.queue)} incidents"

if __name__ == "__main__":
    from incident import Incident

    incident1 = Incident(1, (50.095340, 19.920282), 5)
    incident2 = Incident(2, (51.095340, 20.920282), 7)
    
    queue = IncidentQueue()
    queue.add_incident(incident1)
    queue.add_incident(incident2)
    
    print(queue.get_next_incident())
    print(queue)
    print(len(queue))
