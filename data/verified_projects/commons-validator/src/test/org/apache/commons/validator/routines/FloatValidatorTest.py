import pytest

from src.main.org.apache.commons.validator.routines.FloatValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest
import sys


class FloatValidatorTest(AbstractNumberValidatorTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._validator = FloatValidator(False, 0)
            self._strictValidator = FloatValidator.FloatValidator1()
            self._testPattern = "#,###.#"
            self._max = float(sys.float_info.max)
            self._maxPlusOne = float(float(sys.float_info.max) * 10)
            self._min = float(sys.float_info.max * -1)
            self._minMinusOne = float(float(sys.float_info.max * -1) * 10)
            self._invalidStrict = [None, "", "X", "X12", "12X", "1X2"]
            self._invalid = [None, "", "X", "X12"]
            self._testNumber = float(1234.5)
            self._testZero = float(0)
            self._validStrict = ["0", "1234.5", "1,234.5"]
            self._validStrictCompare = [
                float(0),
                float(1234.5),
                float(1234.5)
            ]
            self._valid = [
                "0",
                "1234.5",
                "1,234.5",
                "1,234.5",
                "1234.5X"
            ]
            self._validCompare = [
                float(0),
                float(1234.5),
                float(1234.5),
                float(1234.5),
                float(1234.5)
            ]
            self._testStringUS = "1,234.5"
            self._testStringDE = "1.234,5"
            self._localeValue = "1.234,5"
            self._localePattern = "#.###,#"
            self._testLocale = 'de_DE.UTF-8'
            self._localeExpected = float(1234.5)
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    @pytest.mark.test
    def testFloatValidatorMethods(self) -> None:
        locale = 'de_DE.UTF-8'
        pattern = "0,00,00"
        patternVal = "1,23,45"
        localeVal = "12.345"
        germanPatternVal = "1.23.45"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = float(12345)
        self.assertEqual(
            FloatValidator.getInstance().validate0(defaultVal),
            expected,
            "validate(A) default"
        )
        self.assertEqual(
            FloatValidator.getInstance().validate2(localeVal, locale),
            expected,
            "validate(A) locale"
        )
        self.assertEqual(
            FloatValidator.getInstance().validate1(patternVal, pattern),
            expected,
            "validate(A) pattern"
        )
        self.assertEqual(
            FloatValidator.getInstance().validate3(germanPatternVal, pattern, locale),
            expected,
            "validate(A) both"
        )

        self.assertTrue(
            FloatValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            FloatValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale"
        )
        self.assertTrue(
            FloatValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            FloatValidator.getInstance().isValid3(germanPatternVal, pattern, locale),
            "isValid(A) both"
        )

        self.assertIsNone(
            FloatValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            FloatValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale"
        )
        self.assertIsNone(
            FloatValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            FloatValidator.getInstance().validate3(XXXX, pattern, locale),
            "validate(B) both"
        )

        self.assertFalse(
            FloatValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            FloatValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale"
        )
        self.assertFalse(
            FloatValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            FloatValidator.getInstance().isValid3(XXXX, pattern, locale),
            "isValid(B) both"
        )


    @pytest.mark.test
    def testFloatSmallestValues(self) -> None:
        pattern = "#.#################################################################"
        precision = max(len(pattern.split('.')[1]), 500)

        smallestPositive = sys.float_info.min
        strSmallestPositive = f"{smallestPositive:.{precision}f}".rstrip('0')
        self.assertEqual(
            FloatValidator.getInstance().validate1(strSmallestPositive, pattern),
            smallestPositive,
            "Smallest +ve"
        )

        smallestNegative = float(sys.float_info.min * -1)
        strSmallestNegative = f"{smallestNegative:.{precision}f}".rstrip('0')
        self.assertEqual(
            FloatValidator.getInstance().validate1(strSmallestNegative, pattern),
            smallestNegative,
            "Smallest -ve"
        )

        tooSmallPositive = sys.float_info.min / float(10)
        strTooSmallPositive = f"{tooSmallPositive:.{precision}f}".rstrip('0')
        self.assertFalse(
            FloatValidator.getInstance().isValid1(strTooSmallPositive, pattern),
            "Too small +ve"
        )

        tooSmallNegative = float(tooSmallPositive * -1)
        strTooSmallNegative = f"{tooSmallNegative:.{precision}f}".rstrip('0')
        self.assertFalse(
            FloatValidator.getInstance().isValid1(strTooSmallNegative, pattern),
            "Too small -ve"
        )
    

    @pytest.mark.test
    def testFloatRangeMinMax(self) -> None:
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
