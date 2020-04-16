import pytz
import requests
import unittest

from datetime import datetime

from airnowpy.api import API
from airnowpy.category import Category
from airnowpy.observation import Observation


class APITest(unittest.TestCase):
    api = API('TEST_KEY')

    @classmethod
    def setUpClass(cls):
        def mock_requestsGet(*args, **kwargs):
            response = type('Response', (object,), {})
            response.headers = {}
            response.status_code = 200
            with open('./tests/sample_observation.json', 'r') as fixture:
                response.text = fixture.read()
            return response

        cls.request_get = requests.get
        requests.get = mock_requestsGet

    @classmethod
    def tearDownClass(cls):
        requests.get = cls.request_get

    def test_getCurrentObservationByLatLon_badLatitudeLower(self):
        self._checkBadLatitude(-90.001)

    def test_getCurrentObservationByLatLon_badLatitudeUpper(self):
        self._checkBadLatitude(90.001)

    def _checkBadLatitude(self, lat):
        expectedMsg = "Latitude must be between -90 and 90: " + str(lat)
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByLatLon(lat, 0)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_getCurrentObservationByLatLon_badLongitudeLower(self):
        self._checkBadLongitude(-180.001)

    def test_getCurrentObservationByLatLon_badLongitudeUpper(self):
        self._checkBadLongitude(180.001)

    def _checkBadLongitude(self, lon):
        expectedMsg = "Longitude must be between -180 and 180: " + str(lon)
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByLatLon(0, lon)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_getCurrentObservationByLatLon(self):
        latitude = 47.562
        longitude = -122.3405
        observations = self.api.getCurrentObservationByLatLon(latitude, longitude)
        self.assertIsInstance(observations, list)
        self.assertIsInstance(observations[0], Observation)
        self._assertObservations(observations)

    def test_getCurrentObservationByZipCode_badZipCodeLower(self):
        self._checkBadZipCode(9999)

    def test_getCurrentObservationByZipCode_badZipCodeUpper(self):
        self._checkBadZipCode(100000)

    def _checkBadZipCode(self, zipCode):
        expectedMsg = "Zip Code must be between 10000 and 99999: " + str(zipCode)
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByZipCode(zipCode)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_getCurrentObservationByZipCode(self):
        zipCode = 98195
        observations = self.api.getCurrentObservationByZipCode(zipCode)
        self.assertIsInstance(observations, list)
        self.assertIsInstance(observations[0], Observation)
        self._assertObservations(observations)

    def _assertObservations(self, observations):
        # Spot check a few attributes on the sample observations
        expectedTimestampUTC = datetime(2019, 8, 1, 8, 0, tzinfo=pytz.UTC)
        self.assertEqual(expectedTimestampUTC, observations[0].getTimestampUTC())
        self.assertEqual("O3", observations[0].getParameterName())
        self.assertEqual("PM2.5", observations[1].getParameterName())
        self.assertEqual(Category.GOOD, observations[1].getCategory())
