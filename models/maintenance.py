from models.log_entry import LogEntry

class Maintenance(LogEntry):
    def __init__(self, vehicle_id: str, date: str, mileage: int, maintenance_type: str, cost: float, notes="", id: str = None):
        super().__init__(vehicle_id, date, mileage, id)
        self.maintenance_type = maintenance_type
        self.cost = cost
        self.notes = notes

    def __str__(self):
        return f"Maintenance({self.vehicle_id}, {self.date}, {self.mileage}, {self.maintenance_type}, {self.cost}, {self.notes})"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "maintenance",
            "maintenance_type": str(self.maintenance_type),
            "cost": self.cost,
            "notes": self.notes
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            vehicle_id=data["vehicle_id"],
            date=data["date"],
            mileage=data["mileage"],
            maintenance_type=data["maintenance_type"],
            cost=data["cost"],
            notes=data.get("notes", "")
        )