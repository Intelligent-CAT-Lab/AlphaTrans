import pytest

from decimal import Decimal
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class BigDecimalValidatorTest(AbstractNumberValidatorTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            testNumber2 = Decimal(".1")
            testNumber3 = Decimal("12345.67899")

            super().setUp()
            self._validator = BigDecimalValidator.BigDecimalValidator1(False)
            self._strictValidator = BigDecimalValidator.BigDecimalValidator2()
            self._testPattern = "#,###.###"
            self._max = None
            self._maxPlusOne = None
            self._min = None
            self._minMinusOne = None
            self._invalidStrict = [None, "", "X", "X12", "12X", "1X2", "1.234X"]
            self._invalid = [None, "", "X", "X12"]
            self._testNumber = Decimal("1234.5")
            self._testZero = Decimal("0")
            self._validStrict = ["0", "1234.5", "1,234.5", ".1", "12345.678990"]
            self._validStrictCompare = [
                Decimal("0"),
                Decimal("1234.5"),
                Decimal("1234.5"),
                testNumber2,
                testNumber3
            ]
            self._valid = ["0", "1234.5", "1,234.5", "1,234.5", "1234.5X"]
            self._validCompare = [
                Decimal("0"),
                Decimal("1234.5"),
                Decimal("1234.5"),
                Decimal("1234.5"),
                Decimal("1234.5")
            ]
            self._testStringUS = "1,234.5"
            self._testStringDE = "1.234,5"
            self._localeValue = "1.234,5"
            self._localePattern = "#.###,#"
            self._testLocale = 'de_DE.UTF-8'
            self._localeExpected = Decimal("1234.5")
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    @pytest.mark.test
    def testBigDecimalValidatorMethods(self) -> None:
        locale = 'de_DE.UTF-8'
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = Decimal(12345)
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale "
        )
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "validate(A) both"
        )

        self.assertTrue(
            BigDecimalValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale "
        )
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )

        self.assertIsNone(
            BigDecimalValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale "
        )
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )

        self.assertFalse(
            BigDecimalValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            BigDecimalValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale "
        )
        self.assertFalse(
            BigDecimalValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            BigDecimalValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )

    
    @pytest.mark.test
    def testBigDecimalRangeMinMax(self) -> None:
        validator = BigDecimalValidator(True, AbstractNumberValidator.STANDARD_FORMAT, True)
        number9 = Decimal("9")
        number10 = Decimal("10")
        number11 = Decimal("11")
        number19 = Decimal("19")
        number20 = Decimal("20")
        number21 = Decimal("21")

        minVal = 10
        maxVal = 20

        self.assertFalse(validator.isInRange(number9, minVal, maxVal), "isInRange(A) < min")
        self.assertTrue(validator.isInRange(number10, minVal, maxVal), "isInRange(A) = min")
        self.assertTrue(validator.isInRange(number11, minVal, maxVal), "isInRange(A) in range")
        self.assertTrue(validator.isInRange(number20, minVal, maxVal), "isInRange(A) = max")
        self.assertFalse(validator.isInRange(number21, minVal, maxVal), "isInRange(A) > max")

        self.assertFalse(validator.minValue(number9, minVal), "minValue(A) < min")
        self.assertTrue(validator.minValue(number10, minVal), "minValue(A) = min")
        self.assertTrue(validator.minValue(number11, minVal), "minValue(A) > min")

        self.assertTrue(validator.maxValue(number19, maxVal), "maxValue(A) < max")
        self.assertTrue(validator.maxValue(number20, maxVal), "maxValue(A) = max")
        self.assertFalse(validator.maxValue(number21, maxVal), "maxValue(A) > max")
    
