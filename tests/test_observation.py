import pytz
import unittest

from datetime import datetime

from airnowpy.category import Category
from airnowpy.observation import Observation


class ObservationTest(unittest.TestCase):
    expectedTimestampUTC = datetime(2017, 8, 21, 18, 25, 35, tzinfo=pytz.UTC)
    expectedParameterName = "ECL"
    expectedCategory = Category.GOOD
    observation = Observation(expectedTimestampUTC,
            "United State of America", "USA",
            37.583333, -89.116667,
            expectedParameterName, 161600, expectedCategory)
            
    def test_getParameterName(self):
        self.assertEqual(self.expectedParameterName, 
            self.observation.getParameterName())

    def test_getCategory(self):
        self.assertEqual(self.expectedCategory, 
            self.observation.getCategory())

    def test_getTimestampUTC(self):
        self.assertEqual(self.expectedTimestampUTC, 
            self.observation.getTimestampUTC())
