from __future__ import annotations
import locale
import re
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

        self._testNumber = BigDecimal("1234.5")
        testNumber2 = BigDecimal(".1")
        testNumber3 = BigDecimal("12345.67899")
        self._testZero = BigDecimal("0")
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
        self._testLocale = Locale.GERMANY
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

        locale = Locale.GERMAN
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        self.assertEqual(
            "validate(A) default",
            expected,
            BigDecimalValidator.getInstance().validate0(defaultVal),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            BigDecimalValidator.getInstance().validate2(localeVal, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            BigDecimalValidator.getInstance().validate1(patternVal, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            BigDecimalValidator.getInstance().validate3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertTrue(
            "isValid(A) default", BigDecimalValidator.getInstance().isValid0(defaultVal)
        )
        self.assertTrue(
            "isValid(A) locale ",
            BigDecimalValidator.getInstance().isValid2(localeVal, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            BigDecimalValidator.getInstance().isValid1(patternVal, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            BigDecimalValidator.getInstance().isValid3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertIsNone(
            "validate(B) default", BigDecimalValidator.getInstance().validate0(XXXX)
        )
        self.assertIsNone(
            "validate(B) locale ",
            BigDecimalValidator.getInstance().validate2(XXXX, locale),
        )
        self.assertIsNone(
            "validate(B) pattern",
            BigDecimalValidator.getInstance().validate1(XXXX, pattern),
        )
        self.assertIsNone(
            "validate(B) both",
            BigDecimalValidator.getInstance().validate3(
                patternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertFalse(
            "isValid(B) default", BigDecimalValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ",
            BigDecimalValidator.getInstance().isValid2(XXXX, locale),
        )
        self.assertFalse(
            "isValid(B) pattern",
            BigDecimalValidator.getInstance().isValid1(XXXX, pattern),
        )
        self.assertFalse(
            "isValid(B) both",
            BigDecimalValidator.getInstance().isValid3(
                patternVal, pattern, Locale.GERMAN
            ),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
