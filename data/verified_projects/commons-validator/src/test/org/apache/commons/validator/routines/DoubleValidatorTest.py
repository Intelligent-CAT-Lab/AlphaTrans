from src.main.org.apache.commons.validator.routines.DoubleValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest


class DoubleValidatorTest(AbstractNumberValidatorTest):

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp(
                validator = DoubleValidator(False, 0),
                strictValidator = DoubleValidator.DoubleValidator1(),
                testPattern = "#,###.#",
                _max = None,
                maxPlusOne = None,
                _min = None,
                minMinusOne = None,
                invalidStrict = [None, "", "X", "X12", "12X", "1X2"],
                invalid = [None, "", "X", "X12"],
                testNumber = 1234.5,
                testZero = 0,
                validStrict = ["0", "1234.5", "1,234.5"],
                validStrictCompare = [0, 1234.5, 1,234.5],
                valid = [
                    "0",
                    "1234.5",
                    "1,234.5",
                    "1,234.5",
                    "1234.5X"
                ],
                validCompare = [
                    0,
                    1234.5,
                    1234.5,
                    1234.5,
                    1234.5
                ],
                testStringUS = "1,234.5",
                testStringDE = "1.234,5",
                localeValue = "1.234,5",
                localePattern = "#.###,#",
                testLocale = 'de_DE.UTF-8',
                localeExpected = 1234.5
            )
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    def test_DoubleValidatorMethods(self) -> None:
        locale = 'de_DE.UTF-8'
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = 12345
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale "
        )
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "validate(A) both"
        )

        self.assertTrue(
            DoubleValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            DoubleValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale "
        )
        self.assertTrue(
            DoubleValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            DoubleValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )

        self.assertIsNone(
            DoubleValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            DoubleValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale "
        )
        self.assertIsNone(
            DoubleValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            DoubleValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )

        self.assertFalse(
            DoubleValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            DoubleValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale "
        )
        self.assertFalse(
            DoubleValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            DoubleValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )

    
    def test_DoubleRangeMinMax(self) -> None:
        validator = self._strictValidator
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange1(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange1(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange1(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange1(number21, 10, 20), "isInRange() > max")

        self.assertFalse(validator.minValue1(number9, 10), "minValue() < min")
        self.assertTrue(validator.minValue1(number10, 10), "minValue() = min")
        self.assertTrue(validator.minValue1(number11, 10), "minValue() > min")

        self.assertTrue(validator.maxValue1(number19, 20), "maxValue() < max")
        self.assertTrue(validator.maxValue1(number20, 20), "maxValue() = max")
        self.assertFalse(validator.maxValue1(number21, 20), "maxValue() > max")
