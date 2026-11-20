
class Spacecraft:
    def __init__(self, name):
        self.name = name
        self.status = "INITIALIZING"
        self.power = 100.0
        self.temperature = 20.0
        self.distance_from_earth = 0.0

    def initialize(self):
        self.status = "OPERATIONAL"
        print(f"{self.name} initialized successfully!")

    def get_telemetry(self):
        return {
            "name": self.name,
            "status": self.status,
            "power": self.power,
            "temperature": self.temperature,
            "distance_from_earth": self.distance_from_earth
        }
