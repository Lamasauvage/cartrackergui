import unittest
from core.data_manager import DataManager
from models.maintenance import Maintenance
from models.vehicle import Vehicle

class TestDataManager(unittest.TestCase):

    def test_add_vehicle_success(self):
        dm = DataManager()
        v = Vehicle("AA-111-AA", "Mazda", "RX-7", 1993, 123456)
        dm.add_vehicle(v)
        self.assertEqual(len(dm.vehicles), 1)
        self.assertEqual(dm.vehicles[0].plate_number, "AA-111-AA")

    # add a vehicle with the same license plate - Excepting an error
    def test_add_vehicle_duplicate(self):
        dm = DataManager()
        v1 = Vehicle("BB-222-BB", "Toyota", "Supra", 1998, 90000)
        v2 = Vehicle("BB-222-BB", "BMW", "Z4", 2004, 120000)
        dm.add_vehicle(v1)
        with self.assertRaises(ValueError):
            dm.add_vehicle(v2)

    def test_add_log_success(self):
        dm = DataManager()
        v = Vehicle("AB-123-AA", "BMW", "Z4", 2004, 120000)
        dm.add_vehicle(v)
        m = Maintenance(
            vehicle_id=v.id,
            date="2024-04-10",
            mileage=125000,
            maintenance_type="Oil Change",
            cost=89.90,
            notes="Vidange + filtre à huile"
        )
        dm.add_log(m)
        self.assertEqual(len(dm.logs), 1)
        self.assertEqual(dm.logs[0].vehicle_id, v.id)
        self.assertEqual(dm.logs[0].maintenance_type, "Oil Change")

    def test_update_mileage(self):
        dm = DataManager()
        v = Vehicle("CC-333-CC", "Honda", "Civic", 2005, 150000)
        dm.add_vehicle(v)
        m = Maintenance(
            vehicle_id=v.id,
            date="2024-04-10",
            mileage=155000,
            maintenance_type="Oil Change",
            cost=89.90,
            notes="Vidange + filtre à huile"
        )
        dm.add_log(m)
        self.assertEqual(dm.vehicles[0].mileage, 155000)

    def test_mileage_not_downgraded(self):
        dm = DataManager()
        v = Vehicle("DD-444-DD", "Ford", "Focus", 2010, 200000)
        dm.add_vehicle(v)
        m = Maintenance(
            vehicle_id=v.id,
            date="2024-04-10",
            mileage=180000,  # inférieur à 200000
            maintenance_type="Brake Pads",
            cost=120.00
        )
        dm.add_log(m)
        self.assertEqual(dm.vehicles[0].mileage, 200000)




