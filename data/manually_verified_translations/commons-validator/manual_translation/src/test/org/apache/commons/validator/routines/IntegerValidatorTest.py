from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.IntegerValidator import *


class IntegerValidatorTest(AbstractNumberValidatorTest):

    __INT_MIN_1: str = "-2147483649"
    __INT_MIN_0: str = "-2147483648.99999999999999999999999"
    __INT_MIN: str = "-2147483648"
    __INT_MAX_1: str = "2147483648"
    __INT_MAX_0: str = "2147483647.99999999999999999999999"
    __INT_MAX: str = "2147483647"
    __INT_MAX_VAL: int = int(2147483647)
    __INT_MIN_VAL: int = -2147483648

    def setUp(self) -> None:

        self._INT_MIN_1 = "-2147483649"
        self._INT_MIN_0 = "-2147483648.99999999999999999999999"
        self._INT_MIN = "-2147483648"
        self._INT_MAX_1 = "2147483648"
        self._INT_MAX_0 = "2147483647.99999999999999999999999"
        self._INT_MAX = "2147483647"
        self._INT_MAX_VAL = int(2147483647)
        self._INT_MIN_VAL = -2147483648

        self._validator = IntegerValidator(False, 0)
        self._strictValidator = IntegerValidator.IntegerValidator1()

        self._testPattern = "#,###"

        self._max = int(2147483647)
        self._maxPlusOne = self._max + 1
        self._min = int(-2147483648)
        self._minMinusOne = self._min - 1

        self._invalidStrict = [
            None,
            "",
            "X",
            "X12",
            "12X",
            "1X2",
            "1.2",
            self._INT_MAX_1,
            self._INT_MIN_1,
        ]

        self._invalid = [None, "", "X", "X12", self._INT_MAX_1, self._INT_MIN_1]

        self._testNumber = int(1234)
        self._testZero = int(0)
        self._validStrict = ["0", "1234", "1,234", self._INT_MAX, self._INT_MIN]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._INT_MAX_VAL,
            self._INT_MIN_VAL,
        ]
        self._valid = [
            "0",
            "1234",
            "1,234",
            "1,234.5",
            "1234X",
            self._INT_MAX,
            self._INT_MIN,
            self._INT_MAX_0,
            self._INT_MIN_0,
        ]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._INT_MAX_VAL,
            self._INT_MIN_VAL,
            self._INT_MAX_VAL,
            self._INT_MIN_VAL,
        ]

        self._testStringUS = "1,234"
        self._testStringDE = "1.234"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###"
        self._testLocale = "de_DE.UTF-8"
        self._localeExpected = self._testNumber

    def testMinMaxValues(self) -> None:

        self.assertTrue(
            self._validator.isValid0("2147483647"), "2147483647 is max integer"
        )
        self.assertFalse(
            self._validator.isValid0("2147483648"), "2147483648 > max integer"
        )
        self.assertTrue(
            self._validator.isValid0("-2147483648"), "-2147483648 is min integer"
        )
        self.assertFalse(
            self._validator.isValid0("-2147483649"), "-2147483649 < min integer"
        )

    def testIntegerRangeMinMax(self) -> None:

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

    def testIntegerValidatorMethods(self) -> None:

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
            IntegerValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale"
        )
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "validate(A) both"
        )

        self.assertTrue(
            IntegerValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            IntegerValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale"
        )
        self.assertTrue(
            IntegerValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )

        self.assertIsNone(
            IntegerValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            IntegerValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale"
        )
        self.assertIsNone(
            IntegerValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            IntegerValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )

        self.assertFalse(
            IntegerValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            IntegerValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale"
        )
        self.assertFalse(
            IntegerValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            IntegerValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
