import uuid

class Vehicle:
    def __init__(self, plate_number: str, make: str, model: str, year: int, mileage: int, id: str = None):
        self.id = id if isinstance(id, uuid.UUID) else uuid.UUID(id) if id else uuid.uuid4()
        self.plate_number = plate_number
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"Vehicle({self.plate_number}, {self.make}, {self.model}, {self.year}, {self.mileage})"

    def to_dict(self):
        return {
            "id": str(self.id),
            "plate_number": self.plate_number,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            plate_number=data["plate_number"],
            make=data["make"],
            model=data["model"],
            year=data["year"],
            mileage=data["mileage"]
        )