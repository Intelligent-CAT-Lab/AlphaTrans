from __future__ import annotations
import locale
from decimal import Decimal
import decimal
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class BigDecimalValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:

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
        testNumber2 = Decimal(".1")
        testNumber3 = Decimal("12345.67899")
        self._testZero = Decimal("0")
        self._validStrict = ["0", "1234.5", "1,234.5", ".1", "12345.678990"]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            testNumber2,
            testNumber3,
        ]
        self._valid = ["0", "1234.5", "1,234.5", "1,234.5", "1234.5X"]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
        ]

        self._testStringUS = "1,234.5"
        self._testStringDE = "1.234,5"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###,#"
        self._testLocale = 'de_DE.UTF-8'
        self._localeExpected = self._testNumber

    def testBigDecimalRangeMinMax(self) -> None:

        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = decimal.Decimal("9")
        number10 = decimal.Decimal("10")
        number11 = decimal.Decimal("11")
        number19 = decimal.Decimal("19")
        number20 = decimal.Decimal("20")
        number21 = decimal.Decimal("21")

        min_ = 10
        max_ = 20

        self.assertFalse(validator.isInRange(number9, min_, max_), "isInRange(A) < min")
        self.assertTrue(validator.isInRange(number10, min_, max_), "isInRange(A) = min")
        self.assertTrue(
            validator.isInRange(number11, min_, max_), "isInRange(A) in range"
        )
        self.assertTrue(validator.isInRange(number20, min_, max_), "isInRange(A) = max")
        self.assertFalse(
            validator.isInRange(number21, min_, max_), "isInRange(A) > max"
        )

        self.assertFalse(validator.minValue(number9, min_), "minValue(A) < min")
        self.assertTrue(validator.minValue(number10, min_), "minValue(A) = min")
        self.assertTrue(validator.minValue(number11, min_), "minValue(A) > min")

        self.assertTrue(validator.maxValue(number19, max_), "maxValue(A) < max")
        self.assertTrue(validator.maxValue(number20, max_), "maxValue(A) = max")
        self.assertFalse(validator.maxValue(number21, max_), "maxValue(A) > max")

    def testBigDecimalValidatorMethods(self) -> None:

        locale = 'de_DE.UTF-8'
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

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
            BigDecimalValidator.getInstance().validate3(
                germanPatternVal, pattern, 'de_DE.UTF-8'
            ),
            "validate(A) both"
        )

        self.assertTrue(
            BigDecimalValidator.getInstance().isValid0(defaultVal), "isValid(A) default"
        )
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid2(localeVal, locale), "isValid(A) locale "
        )
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid1(patternVal, pattern), "isValid(A) pattern"
        )
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid3(
                germanPatternVal, pattern, 'de_DE.UTF-8'
            ),
            "isValid(A) both"
        )

        self.assertIsNone(
            BigDecimalValidator.getInstance().validate0(XXXX), "validate(B) default"
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
            BigDecimalValidator.getInstance().validate3(
                patternVal, pattern, 'de_DE.UTF-8'
            ),
            "validate(B) both"
        )

        self.assertFalse(
            BigDecimalValidator.getInstance().isValid0(XXXX), "isValid(B) default"
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
            BigDecimalValidator.getInstance().isValid3(
                patternVal, pattern, 'de_DE.UTF-8'
            ),
            "isValid(B) both"
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
