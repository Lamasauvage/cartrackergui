from models.log_entry import LogEntry

class Fuel(LogEntry):
    def __init__(self, vehicle_id: str, date: str, mileage: int, fuel_type: str, liters: float, price: float, location: str, id: str = None):
        super().__init__(vehicle_id, date, mileage, id)
        self.fuel_type = fuel_type
        self.liters = liters
        self.price = price
        self.total_cost = liters * price
        self.location = location

    def __str__(self):
        return f"Fuel({self.vehicle_id}, {self.date}, {self.mileage}, {self.fuel_type}, {self.liters}, {self.price}, {self.location})"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "fuel",
            "fuel_type": self.fuel_type,
            "liters": self.liters,
            "price": self.price,
            "total_cost": self.total_cost,
            "location": self.location
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            vehicle_id=data["vehicle_id"],
            date=data["date"],
            mileage=data["mileage"],
            fuel_type=data["fuel_type"],
            liters=data["liters"],
            price=data["price"],
            location=data["location"]
        )
