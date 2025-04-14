import json
import os
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
        try:
            if not os.path.exists(filename) or os.path.getsize(filename) == 0:
                print(f"[INFO] No data file found at '{filename}'. Starting with empty data.")
                return
            with open(filename, 'r', encoding='utf-8') as f:
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
                    print("[DEBUG] Logs chargés :", self.logs)


        except FileNotFoundError:
                print(f"[INFO] No data file found at '{filename}'. Starting with empty data.")
                self.vehicles = []
                self.logs = []


    def save_all(self, filename: str):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            data = {
                "vehicles": [v.to_dict() for v in self.vehicles],
                "logs": [l.to_dict() for l in self.logs],
            }
            json.dump(data, f, ensure_ascii=False, indent=4)

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

        # Update mileage if needed
        if log.mileage > v.mileage:
            v.mileage = log.mileage

        self.logs.append(log)

    def remove_vehicle(self, vehicle: Vehicle):
        for v in self.vehicles:
            if v.id == vehicle.id:
                self.vehicles.remove(v)
                self.logs = [log for log in self.logs if str(log.vehicle_id) != str(v.id)]
                break
        else:
            raise ValueError("Vehicle not found")

    def remove_log(self, log: LogEntry):
        for l in self.logs:
            if l.id == log.id:
                self.logs.remove(l)
                break
        else:
            raise ValueError("Log not found")

    def edit_vehicle(self, vehicle: Vehicle ):
        for v in self.vehicles:
            if v.id != vehicle.id and v.plate_number == vehicle.plate_number:
                raise ValueError("Vehicle plate number already exists")

        # Edit vehicle
        for v in self.vehicles:
            if v.id == vehicle.id:
                v.plate_number = vehicle.plate_number
                v.make = vehicle.make
                v.model = vehicle.model
                v.year = vehicle.year
                v.mileage = vehicle.mileage
                break
            else:
                raise ValueError("Vehicle not found")

