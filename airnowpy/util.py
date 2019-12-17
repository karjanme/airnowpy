from pytz import timezone


class Util(object):
    """General Helper Utility Class"""

    # AirNow API webservice appears very simple with respect to time zones.
    # (e.g. not support for Daylight Saving Time)
    TZ_MAP = {
        "EST": timezone("America/New_York"),
        "CST": timezone("America/Chicago"),
        "MST": timezone("America/Denver"),
        "PST": timezone("America/Los_Angeles")
    }

    @staticmethod
    def lookupTimezone(timezoneString):
        """
        Lookup a given timezone string in the map of supported timezones.

        Parameters:
            timezoneString (string): The timezone identifier

        Returns:
            timezone: The corresponding timezone object
        """

        if timezoneString in Util.TZ_MAP:
            return Util.TZ_MAP.get(timezoneString)
        raise LookupError("Timezone not supported: " + timezoneString)
