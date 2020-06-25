from unittest import TestCase

from airnowpy.category import Category


class CategoryTest(TestCase):

    def test_lookupByLabel(self):
        labelToLookup = "Unavailable"
        expectedCategory = Category.UNAVAILABLE
        actualCategory = Category.lookupByLabel(labelToLookup)
        self.assertEqual(expectedCategory, actualCategory)

    def test_lookupByLabel_exception(self):
        labelToLookup = "NO_LABEL"
        expectedMsg = "No matching Category found for label: " + labelToLookup
        with self.assertRaises(LookupError) as context:
            Category.lookupByLabel(labelToLookup)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)

    def test_lookupByValue(self):
        valueToLookup = 7
        expectedCategory = Category.UNAVAILABLE
        actualCategory = Category.lookupByValue(valueToLookup)
        self.assertEqual(expectedCategory, actualCategory)

    def test_lookupByValue_exception(self):
        valueToLookup = 8
        expectedMsg = "No matching Category found for value: " + str(valueToLookup)
        with self.assertRaises(LookupError) as context:
            Category.lookupByValue(valueToLookup)
            ex = context.exception
            actualMsg = ex.msg
            self.assertEquals(expectedMsg, actualMsg)
