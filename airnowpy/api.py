import json
import pytz
import requests

from datetime import date, datetime, time
from typing import List

from airnowpy.observation import Observation
from airnowpy.category import Category
from airnowpy.util import Util


class API(object):
    """AirNow API"""

    _HOST = "www.airnowapi.org"
    _ENDPOINT_OBSERVATION_BY_LATLON = "/aq/observation/latLong/current"
    _ENDPOINT_OBSERVATION_BY_ZIPCODE = "/aq/observation/zipCode/current"
    _RETURN_FORMAT = "application/json"

    def __init__(self,
            apiKey: str):
        """
        Constructor for the AirNow API

        Parameters:
            apiKey (string): the key to access the api
        """
        self.apiKey = apiKey

    def getCurrentObservationByLatLon(self,
            latitude: float,
            longitude: float,
            distanceMiles: int = 0) -> List[Observation]:
        """
        Retrieve the current air quality observation closest to the given
        location provided as a Latidute/Longitude pair.

        Parameters:
            latitude (float): Latitude in decimal degrees.
            longitude (float): Longitude in decimal degrees.
            [distanceMiles] (int): Distance in miles.

        Returns:
            Observation[]: A list of observation objects containing the air
                quality data

        Reference:
            https://docs.airnowapi.org/CurrentObservationsByLatLon/docs
        """
        # Validate Arguments
        if (latitude < -90 or 90 < latitude):
            raise ValueError(
                "Latitude must be between -90 and 90: " + str(latitude))
        if (longitude < -180 or 180 < longitude):
            raise ValueError(
                "Longitude must be between -180 and 180: " + str(longitude))
        if (distanceMiles < 0):
            raise ValueError(
                "Distance must be a positive integer: " + str(distanceMiles))

        # Send Request and Receive Response
        requestUrl = "http://" + API._HOST + API._ENDPOINT_OBSERVATION_BY_LATLON
        payload = {}
        payload["latitude"] = latitude
        payload["longitude"] = longitude
        payload["format"] = API._RETURN_FORMAT
        payload["API_KEY"] = self.apiKey
        if (distanceMiles is not 0):
            payload["distance"] = distanceMiles

        response = requests.get(requestUrl, params=payload)
        return self._convertResponseToObservation(response)

    def getCurrentObservationByZipCode(self,
            zipCode: int,
            distanceMiles: int = 0) -> List[Observation]:
        """
        Retrieve the current air quality observation closest to the given
        location provided as a Zip Code.

        Parameters:
            zipCode (int): Zip Code as a number.
            [distanceMiles] (int): Distance in miles.

        Returns:
            Observation[]: A list of observation objects containing the air
                quality data

        Reference:
            https://docs.airnowapi.org/CurrentObservationsByZip/docs
        """
        # Validate Arguments
        if (zipCode < 10000 or 99999 < zipCode):
            raise ValueError(
                "Zip Code must be between 10000 and 99999: " + str(zipCode))
        if (distanceMiles < 0):
            raise ValueError(
                "Distance must be a positive integer: " + str(distanceMiles))

        # Send Request and Receive Response
        requestUrl = "http://" + API._HOST + API._ENDPOINT_OBSERVATION_BY_ZIPCODE
        payload = {}
        payload["zipCode"] = zipCode
        payload["format"] = API._RETURN_FORMAT
        payload["API_KEY"] = self.apiKey
        if (distanceMiles is not 0):
            payload["distance"] = distanceMiles

        response = requests.get(requestUrl, params=payload)
        return self._convertResponseToObservation(response)

    def _convertResponseToObservation(self,
            response: requests.Response) -> List[Observation]:
        rawObservations = json.loads(response.text)
        observations = []
        for jsonObservation in rawObservations:
            datetimeObservedStr = (jsonObservation["DateObserved"]
                + str(jsonObservation["HourObserved"]))
            datetimeObservedObj = datetime.strptime(datetimeObservedStr,
                "%Y-%m-%d %H")
            localTimezone = Util.lookupTimezone(
                jsonObservation["LocalTimeZone"]
            )
            timestampLocal = localTimezone.localize(datetimeObservedObj)
            timestampUTC = timestampLocal.astimezone(pytz.UTC)
            category = Category.lookupByValue(
                jsonObservation["Category"]["Number"]
            )
            observation = Observation(timestampUTC,
                                      jsonObservation["ReportingArea"],
                                      jsonObservation["StateCode"],
                                      jsonObservation["Latitude"],
                                      jsonObservation["Longitude"],
                                      jsonObservation["ParameterName"],
                                      jsonObservation["AQI"],
                                      category)
            observations.append(observation)
        return observations
