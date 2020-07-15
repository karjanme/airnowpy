from datetime import datetime
from unittest import TestCase

from airnowpy.category import Category
from airnowpy.observation import Observation


class ObservationTest(TestCase):
    expectedTimestamp = datetime(2017, 8, 21, 18, 25, 35)
    expectedReportingArea = "United States of America"
    expectedStateCode = "USA"
    expectedLatitude = 37.583333
    expectedLongitude = -89.116667
    expectedParameterName = "ECL"
    expectedAqiValue = 161600
    expectedCategory = Category.GOOD
    observation = Observation(expectedTimestamp,
            expectedReportingArea, expectedStateCode,
            expectedLatitude, expectedLongitude,
            expectedParameterName, expectedAqiValue, expectedCategory)

    def test_timestamp(self):
        self.assertEqual(self.expectedTimestamp,
            self.observation.timestamp)

    def test_reportingArea(self):
        self.assertEqual(self.expectedReportingArea,
            self.observation.reportingArea)

    def test_stateCode(self):
        self.assertEqual(self.expectedStateCode,
            self.observation.stateCode)

    def test_latitude(self):
        self.assertEqual(self.expectedLatitude,
            self.observation.latitude)

    def test_longitude(self):
        self.assertEqual(self.expectedLongitude,
            self.observation.longitude)

    def test_parameterName(self):
        self.assertEqual(self.expectedParameterName,
            self.observation.parameterName)

    def test_aqiValue(self):
        self.assertEqual(self.expectedAqiValue,
            self.observation.aqiValue)

    def test_category(self):
        self.assertEqual(self.expectedCategory,
            self.observation.category)


