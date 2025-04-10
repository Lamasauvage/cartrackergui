import json
import uuid

from models.log_entry import LogEntry
from models.vehicle import Vehicle
from models.maintenance import Maintenance
from models.fuel import Fuel


class DataManager:
    def __init__(self):
        self.vehicles = [] # List to store Vehicle objects
        self.logs = [] # List to store Maintenance and Fuel objects

    def load_all(self, filename: str):
        with open(filename, 'r') as f:
            data = json.load(f)
            for vehicle_data in data['vehicles']:
                vehicle = Vehicle.from_dict(vehicle_data)
                self.vehicles.append(vehicle)

            for log_data in data['logs']:
                if log_data['type'] == 'maintenance':
                    log = Maintenance.from_dict(log_data)
                elif log_data['type'] == 'fuel':
                    log = Fuel.from_dict(log_data)
                else:
                    continue
                self.logs.append(log)

    def save_all(self, filename: str):
        with open(filename, 'w') as f:
            data = {
                "vehicles": [v.to_dict() for v in self.vehicles],
                "logs": [l.to_dict() for l in self.logs],
            }
            json.dump(data, f)

    def add_vehicle(self, vehicle: Vehicle):
        for v in self.vehicles:
            if v.plate_number == vehicle.plate_number:
                raise ValueError("Vehicle plate number already exists")
        self.vehicles.append(vehicle)

    def add_log(self, log: LogEntry):
        found = False
        for v in self.vehicles:
            if v.id == log.vehicle_id:
                found = True
                break
        if not found:
            raise ValueError("You must register the vehicle before adding a log.")

        self.logs.append(log)







