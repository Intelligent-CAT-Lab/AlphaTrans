import unittest
from decimal import Decimal
from src.main.org.apache.commons.validator.routines.PercentValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from locale import getlocale, setlocale, LC_NUMERIC
class PercentValidatorTest(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self._validator = None

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._validator = PercentValidator.PercentValidator1()
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")


    def tearDown(self) -> None:
        try:    
            super().tearDown()
            self._validator = None
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")

    
    def testFormatType(self) -> None:
        self.assertEqual(
            2,
            PercentValidator.getInstance().getFormatType(),
            "Format Type A"
        )
        self.assertEqual(
            AbstractNumberValidator.PERCENT_FORMAT,
            PercentValidator.getInstance().getFormatType(),
            "Format Type B"
        )

    
    def testValid(self) -> None:
        origDefault = getlocale(LC_NUMERIC)
        setlocale(LC_NUMERIC, 'en_GB.UTF-8')

        validator = PercentValidator.getInstance()
        expected = Decimal("0.12")
        negative = Decimal("-0.12")
        hundred = Decimal("1.00")

        self.assertEqual(
            expected,
            validator.validate0("12%"),
            "Default locale"
        )
        self.assertEqual(
            negative,
            validator.validate0("-12%"),
            "Default negative"
        )

        self.assertEqual(
            expected,
            validator.validate2("12%", 'en_GB.UTF-8'),
            "UK locale"
        )
        self.assertEqual(
            negative,
            validator.validate2("-12%", 'en_GB.UTF-8'),
            "UK negative"
        )
        self.assertEqual(
            expected,
            validator.validate2("12", 'en_GB.UTF-8'),
            "UK No symbol"
        )

        self.assertEqual(
            expected,
            validator.validate2("12%", 'en_US.UTF-8'),
            "US locale"
        )
        self.assertEqual(
            negative,
            validator.validate2("-12%", 'en_US.UTF-8'),
            "US negative"
        )
        self.assertEqual(
            expected,
            validator.validate2("12", 'en_US.UTF-8'),
            "US No symbol"
        )

        self.assertEqual(
            hundred,
            validator.validate0("100%"),
            "100%"
        )

        setlocale(LC_NUMERIC, origDefault)

    
    def testInvalid(self) -> None:
        validator = PercentValidator.getInstance()

        self.assertFalse(
            validator.isValid0(None),
            "isValid() Null Value"
        )
        self.assertFalse(
            validator.isValid0(""),
            "isValid() Empty Value"
        )
        self.assertIsNone(
            validator.validate0(None),
            "validate() Null Value"
        )
        self.assertIsNone(
            validator.validate0(""),
            "validate() Empty Value"
        )

        self.assertFalse(
            validator.isValid2("12@", 'en_GB.UTF-8'),
            "UK wrong symbol"
        )
        self.assertFalse(
            validator.isValid2("(12%)", 'en_GB.UTF-8'),
            "UK wrong negative"
        )

        self.assertFalse(
            validator.isValid2("12@", 'en_US.UTF-8'),
            "US wrong symbol"
        )
        self.assertFalse(
            validator.isValid2("(12%)", 'en_US.UTF-8'),
            "US wrong negative"
        )
