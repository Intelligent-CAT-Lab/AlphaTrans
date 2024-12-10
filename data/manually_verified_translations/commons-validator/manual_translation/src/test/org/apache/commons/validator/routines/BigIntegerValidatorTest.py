from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.BigIntegerValidator import *


class BigIntegerValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:

        super().setUp()

        self._validator = BigIntegerValidator(False, 0)
        self._strictValidator = BigIntegerValidator.BigIntegerValidator1()

        self._testPattern = "#,###"

        self._max = None
        self._maxPlusOne = None
        self._min = None
        self._minMinusOne = None

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2", "1.2"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = int("1234")
        self._testZero = int("0")
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

    def testBigIntegerRangeMinMax(self) -> None:

        validator = self._strictValidator

        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange(number21, 10, 20), "isInRange() > max")

        self.assertFalse(validator.minValue(number9, 10), "minValue() < min")
        self.assertTrue(validator.minValue(number10, 10), "minValue() = min")
        self.assertTrue(validator.minValue(number11, 10), "minValue() > min")

        self.assertTrue(validator.maxValue(number19, 20), "maxValue() < max")
        self.assertTrue(validator.maxValue(number20, 20), "maxValue() = max")
        self.assertFalse(validator.maxValue(number21, 20), "maxValue() > max")

    def testBigIntegerValidatorMethods(self) -> None:

        locale = "de_DE.UTF-8"
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = int("12345")

        self.assertEqual(
            expected,
            BigIntegerValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            BigIntegerValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale "
        )
        self.assertEqual(
            expected,
            BigIntegerValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            BigIntegerValidator.getInstance().validate3(
                germanPatternVal, pattern, "de_DE.UTF-8"
            ),
            "validate(A) both"
        )

        self.assertTrue(
            BigIntegerValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            BigIntegerValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale "
        )
        self.assertTrue(
            BigIntegerValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            BigIntegerValidator.getInstance().isValid3(
                germanPatternVal, pattern, "de_DE.UTF-8"
            ),
            "isValid(A) both"
        )

        self.assertIsNone(
            BigIntegerValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            BigIntegerValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale "
        )
        self.assertIsNone(
            BigIntegerValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            BigIntegerValidator.getInstance().validate3(
                patternVal, pattern, "de_DE.UTF-8"
            ),
            "validate(B) both"
        )

        self.assertFalse(
            BigIntegerValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            BigIntegerValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale "
        )
        self.assertFalse(
            BigIntegerValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            BigIntegerValidator.getInstance().isValid3(
                patternVal, pattern, "de_DE.UTF-8"
            ),
            "isValid(B) both"
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
