from src.main.org.apache.commons.validator.routines.LongValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest
import sys


class LongValidatorTest(AbstractNumberValidatorTest):

    __LONG_MIN_VAL = -sys.maxsize - 1
    __LONG_MAX_VAL = sys.maxsize
    __LONG_MAX = str(sys.maxsize)
    __LONG_MAX_0 = str(sys.maxsize) + ".99999999999999999999999"
    __LONG_MAX_1 = str(sys.maxsize + 1)
    __LONG_MIN = str(-sys.maxsize - 1)
    __LONG_MIN_0 = str(-sys.maxsize - 1) + ".99999999999999999999999"
    __LONG_MIN_1 = str(-sys.maxsize - 1 - 1)
    __NINES = "9999999999999999999999999999999999999"

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp()

            self._validator = LongValidator(False, 0)
            self._strictValidator = LongValidator.LongValidator1()

            self._testPattern = "#,###"

            self._max = None
            self._maxPlusOne = None
            self._min = None
            self._minMinusOne = None

            self._invalidStrict = [
                None,
                "",
                "X",
                "X12",
                "12X",
                "1X2",
                "1.2",
                LongValidatorTest.__LONG_MAX_1,
                LongValidatorTest.__LONG_MIN_1,
                LongValidatorTest.__NINES
            ]

            self._invalid = [
                None,
                "",
                "X",
                "X12",
                "",
                LongValidatorTest.__LONG_MAX_1,
                LongValidatorTest.__LONG_MIN_1,
                LongValidatorTest.__NINES
            ]

            self._testNumber = 1234
            self._testZero = 0
            self._validStrict = [
                "0",
                "1234",
                "1,234",
                LongValidatorTest.__LONG_MAX,
                LongValidatorTest.__LONG_MIN
            ]
            self._validStrictCompare = [
                self._testZero,
                self._testNumber,
                self._testNumber,
                LongValidatorTest.__LONG_MAX_VAL,
                LongValidatorTest.__LONG_MIN_VAL
            ]
            self._valid = [
                "0",
                "1234",
                "1,234",
                "1,234.5",
                "1234X",
                LongValidatorTest.__LONG_MAX,
                LongValidatorTest.__LONG_MIN,
                LongValidatorTest.__LONG_MAX_0,
                LongValidatorTest.__LONG_MIN_0
            ]
            self._validCompare = [
                self._testZero,
                self._testNumber,
                self._testNumber,
                self._testNumber,
                self._testNumber,
                LongValidatorTest.__LONG_MAX_VAL,
                LongValidatorTest.__LONG_MIN_VAL,
                LongValidatorTest.__LONG_MAX_VAL,
                LongValidatorTest.__LONG_MIN_VAL
            ]

            self._testStringUS = "1,234"
            self._testStringDE = "1.234"

            self._localeValue = self._testStringDE
            self._localePattern = "#.###"
            self._testLocale = 'de_DE.UTF-8'
            self._localeExpected = self._testNumber
        except Exception as e:
            self._fail(f"An exception occurred when setting up the test: {e}")
    

    def test_LongValidatorMethods(self) -> None:
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
            LongValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            LongValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale "
        )
        self.assertEqual(
            expected,
            LongValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            LongValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "validate(A) both"
        )

        self.assertTrue(
            LongValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            LongValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale "
        )
        self.assertTrue(
            LongValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            LongValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )

        self.assertIsNone(
            LongValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            LongValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale "
        )
        self.assertIsNone(
            LongValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            LongValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )

        self.assertFalse(
            LongValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            LongValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale "
        )
        self.assertFalse(
            LongValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            LongValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )
    

    def test_LongRangeMinMax(self) -> None:
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
