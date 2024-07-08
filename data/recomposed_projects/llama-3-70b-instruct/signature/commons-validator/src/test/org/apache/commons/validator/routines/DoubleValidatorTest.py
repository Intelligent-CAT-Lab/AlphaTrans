from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.DoubleValidator import *


class DoubleValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:
        super().setUp()

        self._validator = DoubleValidator(False, 0)
        self._strictValidator = DoubleValidator.DoubleValidator1()

        self._testPattern = "#,###.#"

        self._max = None
        self._maxPlusOne = None
        self._min = None
        self._minMinusOne = None

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = 1234.5
        self._testZero = 0
        self._validStrict = ["0", "1234.5", "1,234.5"]
        self._validStrictCompare = [self._testZero, self._testNumber, self._testNumber]
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

    def testDoubleRangeMinMax(self) -> None:
        validator = DoubleValidator()
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")

        self.assertFalse("isInRange() < min", validator.isInRange1(number9, 10, 20))
        self.assertTrue("isInRange() = min", validator.isInRange1(number10, 10, 20))
        self.assertTrue("isInRange() in range", validator.isInRange1(number11, 10, 20))
        self.assertTrue("isInRange() = max", validator.isInRange1(number20, 10, 20))
        self.assertFalse("isInRange() > max", validator.isInRange1(number21, 10, 20))

        self.assertFalse("minValue() < min", validator.minValue1(number9, 10))
        self.assertTrue("minValue() = min", validator.minValue1(number10, 10))
        self.assertTrue("minValue() > min", validator.minValue1(number11, 10))

        self.assertTrue("maxValue() < max", validator.maxValue1(number19, 20))
        self.assertTrue("maxValue() = max", validator.maxValue1(number20, 20))
        self.assertFalse("maxValue() > max", validator.maxValue1(number21, 20))

    def testDoubleValidatorMethods(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = Double.valueOf(12345)
        self.assertEqual(
            "validate(A) default",
            expected,
            DoubleValidator.getInstance().validate0(defaultVal),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            DoubleValidator.getInstance().validate2(localeVal, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            DoubleValidator.getInstance().validate1(patternVal, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            DoubleValidator.getInstance().validate3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertTrue(
            "isValid(A) default", DoubleValidator.getInstance().isValid0(defaultVal)
        )
        self.assertTrue(
            "isValid(A) locale ",
            DoubleValidator.getInstance().isValid2(localeVal, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            DoubleValidator.getInstance().isValid1(patternVal, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            DoubleValidator.getInstance().isValid3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertIsNone(
            "validate(B) default", DoubleValidator.getInstance().validate0(XXXX)
        )
        self.assertIsNone(
            "validate(B) locale ", DoubleValidator.getInstance().validate2(XXXX, locale)
        )
        self.assertIsNone(
            "validate(B) pattern",
            DoubleValidator.getInstance().validate1(XXXX, pattern),
        )
        self.assertIsNone(
            "validate(B) both",
            DoubleValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN),
        )

        self.assertFalse(
            "isValid(B) default", DoubleValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ", DoubleValidator.getInstance().isValid2(XXXX, locale)
        )
        self.assertFalse(
            "isValid(B) pattern", DoubleValidator.getInstance().isValid1(XXXX, pattern)
        )
        self.assertFalse(
            "isValid(B) both",
            DoubleValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
