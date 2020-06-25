from datetime import datetime
from unittest import TestCase

from airnowpy.category import Category
from airnowpy.observation import Observation


class ObservationTest(TestCase):
    expectedTimestamp = datetime(2017, 8, 21, 18, 25, 35)
    expectedParameterName = "ECL"
    expectedCategory = Category.GOOD
    observation = Observation(expectedTimestamp,
            "United State of America", "USA",
            37.583333, -89.116667,
            expectedParameterName, 161600, expectedCategory)
            
    def test_getParameterName(self):
        self.assertEqual(self.expectedParameterName, 
            self.observation.getParameterName())

    def test_getCategory(self):
        self.assertEqual(self.expectedCategory, 
            self.observation.getCategory())

    def test_getTimestamp(self):
        self.assertEqual(self.expectedTimestamp,
            self.observation.getTimestamp())
