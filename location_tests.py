# Melissa Melton
# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        loc2 = Location('SLO', 35.3, -120.7)
        loc3 = Location('Liverpool', 53.4084, 2.9916)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc), repr(loc2))
        self.assertEqual(repr(loc3), "Location('Liverpool', 53.4084, 2.9916)")

    def test_init(self) -> None:
        loc = Location('Cairo', 30.03, 31.234)
        self.assertEqual(loc.name, 'Cairo')
        self.assertEqual(loc.lat, 30.03)
        self.assertEqual(loc.lon, 31.234)

    def test_eq(self):
        loc1 = Location('Brooklyn', 40.6782, 73.9442)
        loc2 = Location('Brooklyn', 40.6782, 73.9440)
        loc3 = Location('Brooklyn', 40.6782, 73.9442)
        loc4 = Location('Alternative Brooklyn', 40.6782, 73.9442)
        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc4)
        self.assertTrue(loc1==loc3)
        self.assertEqual(loc1, loc3)
        self.assertTrue(loc1.__eq__(loc3))

if __name__ == "__main__":
        unittest.main()
