import datetime

from airnowpy.category import Category


class Observation(object):
    """
    Air Quality Observation

    A container of data representing an observation from the AirNow API
    webserivce.
    """

    def __init__(self,
            timestamp: datetime,
            reportingArea: str,
            stateCode: str,
            latitude: float,
            longitude: float,
            parameterName: float,
            aqiValue: int,
            category: Category):
        """
        Parameters:
            timestamp (datetime): The local timestamp of the observation
            reportingArea (string):	City or area name of observed data
            stateCode (string): Two-character state abbreviation
            latitude (float): Latitude in decimal degrees
            longitude (float): Longitude in decimal degrees
            parameterName (string): Name of the Air Quality parameter
            aqiValue (int): Observed Air Quality Index value
            category (Category): The corresponding Category for the AQI value
        """

        self._timestamp = timestamp
        self._reportingArea = reportingArea
        self._stateCode = stateCode
        self._latitude = latitude
        self._longitude = longitude
        self._parameterName = parameterName
        self._aqiValue = aqiValue
        self._category = category

    def getParameterName(self) -> str:
        return self._parameterName

    def getCategory(self) -> Category:
        return self._category

    def getTimestamp(self) -> datetime:
        return self._timestamp
