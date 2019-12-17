

class Observation(object):
    """
    Air Quality Observation

    A container of data representing an observation from the AirNow API
    webserivce.
    """

    def __init__(self,
            timestampUTC,
            reportingArea,
            stateCode,
            latitude,
            longitude,
            parameterName,
            aqiValue,
            category):
        """
        Parameters:
            timestampUTC (datetime): The UTC timestamp of the observation
            reportingArea (string):	City or area name of observed data
            stateCode (string): Two-character state abbreviation
            latitude (float): Latitude in decimal degrees
            longitude (float): Longitude in decimal degrees
            parameterName (string): Name of the Air Quality parameter
            aqiValue (int): Observed Air Quality Index value
            category (Category): The corresponding Category for the AQI value
        """

        self._timestampUTC = timestampUTC
        self._reportingArea = reportingArea
        self._stateCode = stateCode
        self._latitude = latitude
        self._longitude = longitude
        self._parameterName = parameterName
        self._aqiValue = aqiValue
        self._category = category

    def getParameterName(self):
        return self._parameterName

    def getCategory(self):
        return self._category

    def getTimestampUTC(self):
        return self._timestampUTC
