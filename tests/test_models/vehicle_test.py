import unittest
from models.vehicle import Vehicle

class TestVehicle(unittest.TestCase):
    def test_creation(self):
        v = Vehicle("AB-123-CD", "Mazda", "RX-7", 1999, 123456)
        self.assertEqual(v.plate_number, "AB-123-CD")
        self.assertEqual(v.make, "Mazda")
        self.assertEqual(v.model, "RX-7")
        self.assertEqual(v.year, 1999)
        self.assertEqual(v.mileage, 123456)
        self.assertIsNotNone(v.id)

    def test_str(self):
        v = Vehicle("ZZ-999-ZZ", "BMW", "Z4", 2004, 54321)
        self.assertIn("BMW", str(v))
        self.assertIn("Z4", str(v))
        self.assertIn("2004", str(v))

    def test_to_from_dict(self):
        v = Vehicle("AA-321-AA", "Toyota", "Supra", 1998, 100000)
        d = v.to_dict()
        v2 = Vehicle.from_dict(d)
        self.assertEqual(v.plate_number, v2.plate_number)
        self.assertEqual(v.make, v2.make)
        self.assertEqual(str(v.id), str(v2.id))

if __name__ == '__main__':
    unittest.main()
