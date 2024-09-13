from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.ShortValidator import *


class ShortValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:

        super().setUp()

        self._validator = ShortValidator(False, 0)
        self._strictValidator = ShortValidator.ShortValidator1()

        self._testPattern = "#,###"

        max_ = int(32767)
        self._maxPlusOne = int(max_ + 1)
        min_ = int(-32768)
        self._minMinusOne = int(min_ - 1)

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2", "1.2"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = int(1234)
        self._testZero = int(0)
        self._validStrict = ["0", "1234", "1,234"]
        self._validStrictCompare = [self._testZero, self._testNumber, self._testNumber]
        self._valid = ["0", "1234", "1,234", "1,234.5", "1234X"]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
        ]

        self._testStringUS = "1,234"
        self._testStringDE = "1.234"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###"
        self._testLocale = "de_DE.UTF-8"
        self._localeExpected = self._testNumber

    def testShortRangeMinMax(self) -> None:

        validator = self._strictValidator
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        min_ = int(10)
        max_ = int(20)

        self.assertFalse(validator.isInRange1(number9, min_, max_), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, min_, max_), "isInRange() = min")
        self.assertTrue(
            validator.isInRange1(number11, min_, max_), "isInRange() in range"
        )
        self.assertTrue(validator.isInRange1(number20, min_, max_), "isInRange() = max")
        self.assertFalse(
            validator.isInRange1(number21, min_, max_), "isInRange() > max"
        )

        self.assertFalse(validator.minValue1(number9, min_), "minValue() < min")
        self.assertTrue(validator.minValue1(number10, min_), "minValue() = min")
        self.assertTrue(validator.minValue1(number11, min_), "minValue() > min")

        self.assertTrue(validator.maxValue1(number19, max_), "maxValue() < max")
        self.assertTrue(validator.maxValue1(number20, max_), "maxValue() = max")
        self.assertFalse(validator.maxValue1(number21, max_), "maxValue() > max")

    def testShortValidatorMethods(self) -> None:

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
            ShortValidator.getInstance().validate0(defaultVal), 
            "validate(A) default"
        )
        self.assertEqual(
            expected, 
            ShortValidator.getInstance().validate2(localeVal, locale), 
            "validate(A) locale "
        )
        self.assertEqual(
            expected, 
            ShortValidator.getInstance().validate1(patternVal, pattern), 
            "validate(A) pattern"
        )
        self.assertEqual(
            expected, 
            ShortValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'), 
            "validate(A) both"
        )

        self.assertTrue(
            ShortValidator.getInstance().isValid0(defaultVal), 
            "isValid(A) default"
        )
        self.assertTrue(
            ShortValidator.getInstance().isValid2(localeVal, locale), 
            "isValid(A) locale "
        )
        self.assertTrue(
            ShortValidator.getInstance().isValid1(patternVal, pattern), 
            "isValid(A) pattern"
        )
        self.assertTrue(
            ShortValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'), 
            "isValid(A) both"
        )

        self.assertIsNone(
            ShortValidator.getInstance().validate0(XXXX), 
            "validate(B) default"
        )
        self.assertIsNone(
            ShortValidator.getInstance().validate2(XXXX, locale), 
            "validate(B) locale "
        )
        self.assertIsNone(
            ShortValidator.getInstance().validate1(XXXX, pattern), 
            "validate(B) pattern"
        )
        self.assertIsNone(
            ShortValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'), 
            "validate(B) both"
        )

        self.assertFalse(
            ShortValidator.getInstance().isValid0(XXXX), 
            "isValid(B) default"
        )
        self.assertFalse(
            ShortValidator.getInstance().isValid2(XXXX, locale), 
            "isValid(B) locale "
        )
        self.assertFalse(
            ShortValidator.getInstance().isValid1(XXXX, pattern), 
            "isValid(B) pattern"
        )
        self.assertFalse(
            ShortValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'), 
            "isValid(B) both"
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
