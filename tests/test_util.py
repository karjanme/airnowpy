import unittest

from pytz import timezone

from airnowpy.util import Util


class UtilTest(unittest.TestCase):

    def test_lookupTimezone(self):
        tzString = "PST"
        expectedTz = timezone("America/Los_Angeles")
        actualTz = Util.lookupTimezone(tzString)
        self.assertEqual(expectedTz, actualTz)

    def test_lookupTimezone_exception(self):
        tzString = "NO_TIMEZONE"
        expectedMsg = "Timezone not supported: " + tzString
        with self.assertRaises(LookupError) as context:
            Util.lookupTimezone(tzString)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
