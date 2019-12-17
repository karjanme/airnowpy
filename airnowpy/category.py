from enum import Enum, unique


@unique
class Category(Enum):
    """
    AQI Category

    An indicator for the level of health concerns based on the Air Quality
    Index value.
    """

    GOOD = ("Good", 1)
    MODERATE = ("Moderate", 2)
    UNHEALTHY_FOR_SENSITIVE_GROUPS = ("Unhealthy for Sensitive Groups", 3)
    UNHEALTHY = ("Unhealthy", 4)
    VERY_UNHEALTHY = ("Very Unhealthy", 5)
    HAZARDOUS = ("Hazardous", 6)
    UNAVAILABLE = ("Unavailable", 7)

    def __init__(self, label, value):
        self._label = label
        self._value_ = value

    @staticmethod
    def lookupByLabel(label):
        for name, member in Category.__members__.items():
            if label == member.getLabel():
                return member
        raise LookupError("No matching Category found for label: " + label)

    @staticmethod
    def lookupByValue(value):
        for name, member in Category.__members__.items():
            if value == member.getValue():
                return member
        raise LookupError("No matching Category found for value: " + str(value))
    
    def getLabel(self):
        return self._label

    def getValue(self):
        return self._value_
