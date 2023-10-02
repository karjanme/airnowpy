import requests

from datetime import datetime, tzinfo
from pytz import timezone
from typing import List
from unittest import TestCase
from unittest.mock import patch

from airnowpy.api import API
from airnowpy.category import Category
from airnowpy.observation import Observation


class APITest(TestCase):
    api_key = "TEST_KEY"
    api = API(api_key)

    def _mock_response(self):
            response = type('Response', (object,), {})
            response.headers = {}
            response.status_code = 200
            with open('./tests/sample_observation.json', 'r') as fixture:
                response.text = fixture.read()
            return response

    def test_getCurrentObservationByLatLon_badLatitudeLower(self):
        self._checkBadLatitude(-90.001)

    def test_getCurrentObservationByLatLon_badLatitudeUpper(self):
        self._checkBadLatitude(90.001)

    def _checkBadLatitude(self, lat: float) -> None:
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

    def _checkBadLongitude(self, lon: float) -> None:
        expectedMsg = "Longitude must be between -180 and 180: " + str(lon)
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByLatLon(0, lon)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_getCurrentObservationByLatLon_noDistance(self):
        self.executeGetCurrentObservationByLatLongTest(False)

    def test_getCurrentObservationByLatLon_withGoodDistance(self):
        self.executeGetCurrentObservationByLatLongTest(True)

    def test_getCurrentObservationByLatLon_withBadDistance(self):
        badDistance = -1
        expectedMsg = "Distance must be a positive integer: " + str(badDistance)
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByLatLon(0, 0, badDistance)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def executeGetCurrentObservationByLatLongTest(self, useDistance: bool) -> None:
        latitude = 47.562
        longitude = -122.3405
        distance = 10

        expected_url = "http://" + API._HOST + API._ENDPOINT_OBSERVATION_BY_LATLON
        expected_payload = {}
        expected_payload["latitude"] = latitude
        expected_payload["longitude"] = longitude
        expected_payload["format"] = API._RETURN_FORMAT
        expected_payload["API_KEY"] = self.api_key
        if (useDistance):
            expected_payload["distance"] = 10

        with patch.object(requests, 'get', return_value=self._mock_response()) as mock_requestsGet:
            if (useDistance):
                observations = self.api.getCurrentObservationByLatLon(latitude, longitude, distance)
            else:
                observations = self.api.getCurrentObservationByLatLon(latitude, longitude)

            mock_requestsGet.assert_called_once_with(expected_url, params=expected_payload)
            self.assertIsInstance(observations, list)
            self.assertIsInstance(observations[0], Observation)
            self._assertObservations(observations)

    def test_getCurrentObservationByZipCode_badZipCodeLower(self):
        self._checkBadZipCode("9999")

    def test_getCurrentObservationByZipCode_badZipCodeUpper(self):
        self._checkBadZipCode("100000")

    def _checkBadZipCode(self, zipCode: str) -> None:
        expectedMsg = "Zip Code must be a 5-digit string: " + zipCode
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByZipCode(zipCode)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_getCurrentObservationByZipCode_noDistance(self):
        self.executeGetCurrentObservationByZipCodeTest(False)

    def test_getCurrentObservationByZipCode_withGoodDistance(self):
        self.executeGetCurrentObservationByZipCodeTest(True)

    def test_getCurrentObservationByZipCode_withBadDistance(self):
        badDistance = -1
        expectedMsg = "Distance must be a positive integer: " + str(badDistance)
        with self.assertRaises(ValueError) as context:
            self.api.getCurrentObservationByZipCode("01234", badDistance)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_getCurrentObservationByZipCode_ZeroZipCode(self):
        self.executeGetCurrentObservationByZipCodeTest(True, "01234")

    def executeGetCurrentObservationByZipCodeTest(self,
            useDistance: bool,
            zipCode: str = "98185") -> None:
        distance = 10

        expected_url = "http://" + API._HOST + API._ENDPOINT_OBSERVATION_BY_ZIPCODE
        expected_payload = {}
        expected_payload["zipCode"] = zipCode
        expected_payload["format"] = API._RETURN_FORMAT
        expected_payload["API_KEY"] = self.api_key
        if (useDistance):
            expected_payload["distance"] = 10

        with patch.object(requests, 'get', return_value=self._mock_response()) as mock_requestsGet:
            if (useDistance):
                observations = self.api.getCurrentObservationByZipCode(zipCode, distance)
            else:
                observations = self.api.getCurrentObservationByZipCode(zipCode)

            mock_requestsGet.assert_called_once_with(expected_url, params=expected_payload)
            self.assertIsInstance(observations, list)
            self.assertIsInstance(observations[0], Observation)
            self._assertObservations(observations)

    def _assertObservations(self, observations: List[Observation]) -> None:
        expectedTimestamp = datetime(2019, 8, 1, 1, 0, tzinfo=API.convertLocalTimeZone("PST"))
        self.assertEqual(2, len(observations))
        self.assertEqual(expectedTimestamp, observations[0].timestamp)
        self.assertEqual("O3", observations[0].parameterName)
        self.assertEqual(Category.GOOD, observations[0].category)
        self.assertEqual(expectedTimestamp, observations[1].timestamp)
        self.assertEqual("PM2.5", observations[1].parameterName)
        self.assertEqual(Category.GOOD, observations[1].category)

    def test_convertLocalTimeZone_withGoodTimeZoneString(self):
        self.executeConvertLocalTimeZoneTest("EST", timezone("Etc/GMT+5"))
        self.executeConvertLocalTimeZoneTest("CST", timezone("Etc/GMT+6"))
        self.executeConvertLocalTimeZoneTest("MST", timezone("Etc/GMT+7"))
        self.executeConvertLocalTimeZoneTest("PST", timezone("Etc/GMT+8"))

    def test_convertLocalTimeZone_withBadTimeZoneString(self):
        badTimeZoneStr = "PDT"
        expectedMsg = "Local Time Zone '" + badTimeZoneStr + "' is not supported."
        with self.assertRaises(LookupError) as context:
            API.convertLocalTimeZone(badTimeZoneStr)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def executeConvertLocalTimeZoneTest(self, timeZoneStr: str, expectedTZ: tzinfo):
        actualTZ = API.convertLocalTimeZone(timeZoneStr)
        self.assertEqual(expectedTZ, actualTZ)
