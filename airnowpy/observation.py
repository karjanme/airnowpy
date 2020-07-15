from dataclasses import dataclass
from datetime import datetime

from airnowpy.category import Category


@dataclass(frozen=True)
class Observation():
    """
    A container of data representing an observation from the AirNow API
    webserivce.

    Fields:
        timestamp (datetime): The local timestamp of the observation
        reportingArea (string):	City or area name of observed data
        stateCode (string): Two-character state abbreviation
        latitude (float): Latitude in decimal degrees
        longitude (float): Longitude in decimal degrees
        parameterName (string): Name of the Air Quality parameter
        aqiValue (int): Observed Air Quality Index value
        category (Category): The corresponding Category for the AQI value
    """

    timestamp: datetime
    reportingArea: str
    stateCode: str
    latitude: float
    longitude: float
    parameterName: float
    aqiValue: int
    category: Category
