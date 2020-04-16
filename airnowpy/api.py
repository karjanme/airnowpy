import json
import pytz
import requests

from datetime import date, datetime, time
from pytz import timezone

from airnowpy.observation import Observation
from airnowpy.category import Category
from airnowpy.util import Util


class API(object):
    """AirNow API"""

    _HOST = "www.airnowapi.org"
    _RETURN_FORMAT = "application/json"

    def __init__(self,
            apiKey):
        """
        Constructor for the AirNow API

        Parameters:
            apiKey (string): the key to access the api
        """
        self.apiKey = apiKey

    def getCurrentObservationByLatLon(self, 
            latitude, 
            longitude):
        """
        Retrieve the current air quality observation closest to the given
        location provided as a Latidute/Longitude pair.

        Parameters:
            latitude (float): Latitude in decimal degrees.
            longitude (float): Longitude in decimal degrees.

        Returns:
            Observation[]: An array of observation objects containing the air
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

        endpoint = "/aq/observation/latLong/current"
        distanceMiles = 0

        # Send Request and Receive Response
        requestUrl = "http://" + API._HOST + endpoint
        payload = {"latitude": latitude,
                   "longitude": longitude,
                   "distance": distanceMiles,
                   "format": API._RETURN_FORMAT,
                   "API_KEY": self.apiKey
                  }
        response = requests.get(requestUrl, params=payload)
        return self._convertResponseToObservation(response)

    def getCurrentObservationByZipCode(self, 
            zipCode):
        """
        Retrieve the current air quality observation closest to the given
        location provided as a Zip Code.

        Parameters:
            zipCode (int): Zip Code as a number.

        Returns:
            Observation[]: An array of observation objects containing the air
                quality data

        Reference:
            https://docs.airnowapi.org/CurrentObservationsByZip/docs
        """
        # Validate Arguments
        if (zipCode < 10000 or 99999 < zipCode):
            raise ValueError(
                "Zip Code must be between 10000 and 99999: " + str(zipCode))

        endpoint = "/aq/observation/zipCode/current"
        distanceMiles = 0

        # Send Request and Receive Response
        requestUrl = "http://" + API._HOST + endpoint
        payload = {"zipCode": zipCode,
                   "distance": distanceMiles,
                   "format": API._RETURN_FORMAT,
                   "API_KEY": self.apiKey
                  }
        response = requests.get(requestUrl, params=payload)
        return self._convertResponseToObservation(response)

    def _convertResponseToObservation(self,
            response):
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
