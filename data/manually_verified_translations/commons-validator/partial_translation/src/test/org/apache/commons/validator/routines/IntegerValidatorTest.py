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
        self._testLocale = Locale.GERMANY
        self._localeExpected = self._testNumber

    def testMinMaxValues(self) -> None:

        # Assuming validator is an instance of IntegerValidator
        self.validator = IntegerValidator()

        self.assertTrue(
            self.validator.isValid0("2147483647"), "2147483647 is max integer"
        )
        self.assertFalse(
            self.validator.isValid0("2147483648"), "2147483648 > max integer"
        )
        self.assertTrue(
            self.validator.isValid0("-2147483648"), "-2147483648 is min integer"
        )
        self.assertFalse(
            self.validator.isValid0("-2147483649"), "-2147483649 < min integer"
        )

    def testIntegerRangeMinMax(self) -> None:

        validator = IntegerValidator()
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

        locale = Locale.GERMAN
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = Integer.valueOf(12345)

        self.assertEqual(
            "validate(A) default",
            expected,
            IntegerValidator.getInstance().validate0(defaultVal),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            IntegerValidator.getInstance().validate2(localeVal, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            IntegerValidator.getInstance().validate1(patternVal, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            IntegerValidator.getInstance().validate3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertTrue(
            "isValid(A) default", IntegerValidator.getInstance().isValid0(defaultVal)
        )
        self.assertTrue(
            "isValid(A) locale ",
            IntegerValidator.getInstance().isValid2(localeVal, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            IntegerValidator.getInstance().isValid1(patternVal, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            IntegerValidator.getInstance().isValid3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertIsNone(
            "validate(B) default", IntegerValidator.getInstance().validate0(XXXX)
        )
        self.assertIsNone(
            "validate(B) locale ",
            IntegerValidator.getInstance().validate2(XXXX, locale),
        )
        self.assertIsNone(
            "validate(B) pattern",
            IntegerValidator.getInstance().validate1(XXXX, pattern),
        )
        self.assertIsNone(
            "validate(B) both",
            IntegerValidator.getInstance().validate3(
                patternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertFalse(
            "isValid(B) default", IntegerValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ", IntegerValidator.getInstance().isValid2(XXXX, locale)
        )
        self.assertFalse(
            "isValid(B) pattern", IntegerValidator.getInstance().isValid1(XXXX, pattern)
        )
        self.assertFalse(
            "isValid(B) both",
            IntegerValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
