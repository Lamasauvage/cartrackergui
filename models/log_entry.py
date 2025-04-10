import uuid

class LogEntry:
    def __init__(self, vehicle_id: str, date: str, mileage: int, id: str = None):
        self.id = uuid.UUID(id) if id else uuid.uuid4()
        self.vehicle_id = vehicle_id
        self.date = date
        self.mileage = mileage

    def __str__(self):
        return f"LogEntry({self.vehicle_id}, {self.date}, {self.mileage})"

    def to_dict(self):
        return {
            "id": str(self.id),
            "vehicle_id": self.vehicle_id,
            "date": self.date,
            "mileage": self.mileage
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            vehicle_id=data["vehicle_id"],
            date=data["date"],
            mileage=data["mileage"]
        )