from __future__ import annotations
import locale
import re
import os
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.FloatValidator import *


class FloatValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:

        super().setUp()

        self._validator = FloatValidator(False, 0)
        self._strictValidator = FloatValidator.FloatValidator1()

        self._testPattern = "#,###.#"

        max_ = float(float("inf"))
        self._maxPlusOne = max_ * 10
        self._min = max_ * -1
        self._minMinusOne = self._min * 10

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = float(1234.5)
        self._testZero = float(0)
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
        self._testLocale = "Germany"
        self._localeExpected = self._testNumber

    def testFloatRangeMinMax(self) -> None:

        validator = FloatValidator()
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

    def testFloatSmallestValues(self) -> None:

        pattern = "#.#################################################################"
        fmt = DecimalFormat(pattern)

        smallestPositive = float(float(Float.MIN_VALUE))
        strSmallestPositive = fmt.format(smallestPositive)
        self.assertEqual(
            "Smallest +ve",
            smallestPositive,
            FloatValidator.getInstance().validate1(strSmallestPositive, pattern),
        )

        smallestNegative = float(float(Float.MIN_VALUE * -1))
        strSmallestNegative = fmt.format(smallestNegative)
        self.assertEqual(
            "Smallest -ve",
            smallestNegative,
            FloatValidator.getInstance().validate1(strSmallestNegative, pattern),
        )

        tooSmallPositive = float((float(Float.MIN_VALUE) / float(10)))
        strTooSmallPositive = fmt.format(tooSmallPositive)
        self.assertFalse(
            "Too small +ve",
            FloatValidator.getInstance().isValid1(strTooSmallPositive, pattern),
        )

        tooSmallNegative = float(tooSmallPositive * -1)
        strTooSmallNegative = fmt.format(tooSmallNegative)
        self.assertFalse(
            "Too small -ve",
            FloatValidator.getInstance().isValid1(strTooSmallNegative, pattern),
        )

    def testFloatValidatorMethods(self) -> None:

        locale = Locale.GERMAN
        pattern = "0,00,00"
        patternVal = "1,23,45"
        localeVal = "12.345"
        germanPatternVal = "1.23.45"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = float(12345)

        self.assertEqual(
            "validate(A) default",
            expected,
            FloatValidator.getInstance().validate0(defaultVal),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            FloatValidator.getInstance().validate2(localeVal, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            FloatValidator.getInstance().validate1(patternVal, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            FloatValidator.getInstance().validate3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertTrue(
            "isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal)
        )
        self.assertTrue(
            "isValid(A) locale ",
            FloatValidator.getInstance().isValid2(localeVal, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            FloatValidator.getInstance().isValid1(patternVal, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            FloatValidator.getInstance().isValid3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertIsNone(
            "validate(B) default", FloatValidator.getInstance().validate0(XXXX)
        )
        self.assertIsNone(
            "validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale)
        )
        self.assertIsNone(
            "validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern)
        )
        self.assertIsNone(
            "validate(B) both",
            FloatValidator.getInstance().validate3(XXXX, pattern, Locale.GERMAN),
        )

        self.assertFalse(
            "isValid(B) default", FloatValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale)
        )
        self.assertFalse(
            "isValid(B) pattern", FloatValidator.getInstance().isValid1(XXXX, pattern)
        )
        self.assertFalse(
            "isValid(B) both",
            FloatValidator.getInstance().isValid3(XXXX, pattern, Locale.GERMAN),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
