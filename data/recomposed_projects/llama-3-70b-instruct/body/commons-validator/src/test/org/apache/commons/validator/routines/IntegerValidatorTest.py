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
    __INT_MAX_VAL: int = 2147483647
    __INT_MIN_VAL: int = -2147483648

    def _setUp(self) -> None:
        super()._setUp()
        self._validator = IntegerValidator(False, 0)
        self._strictValidator = IntegerValidator.IntegerValidator1()
        self._testPattern = "#,###"
        self._max = Integer.valueOf(Integer.MAX_VALUE)
        self._maxPlusOne = Long.valueOf(self._max.longValue() + 1)
        self._min = Integer.valueOf(Integer.MIN_VALUE)
        self._minMinusOne = Long.valueOf(self._min.longValue() - 1)
        self._invalidStrict = [
            None,
            "",
            "X",
            "X12",
            "12X",
            "1X2",
            "1.2",
            self.__INT_MAX_1,
            self.__INT_MIN_1,
        ]
        self._invalid = [None, "", "X", "X12", self.__INT_MAX_1, self.__INT_MIN_1]
        self._testNumber = Integer.valueOf(1234)
        self._testZero = Integer.valueOf(0)
        self._validStrict = ["0", "1234", "1,234", self.__INT_MAX, self.__INT_MIN]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self.__INT_MAX_VAL,
            self.__INT_MIN_VAL,
        ]
        self._valid = [
            "0",
            "1234",
            "1,234",
            "1,234.5",
            "1234X",
            self.__INT_MAX,
            self.__INT_MIN,
            self.__INT_MAX_0,
            self.__INT_MIN_0,
        ]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self.__INT_MAX_VAL,
            self.__INT_MIN_VAL,
            self.__INT_MAX_VAL,
            self.__INT_MIN_VAL,
        ]
        self._testStringUS = "1,234"
        self._testStringDE = "1.234"
        self._localeValue = self._testStringDE
        self._localePattern = "#.###"
        self._testLocale = Locale.GERMANY
        self._localeExpected = self._testNumber

    def testMinMaxValues(self) -> None:
        assertTrue("2147483647 is max integer", validator.isValid0("2147483647"))
        assertFalse("2147483648 > max integer", validator.isValid0("2147483648"))
        assertTrue("-2147483648 is min integer", validator.isValid0("-2147483648"))
        assertFalse("-2147483649 < min integer", validator.isValid0("-2147483649"))

    def testIntegerRangeMinMax(self) -> None:
        validator: IntegerValidator = IntegerValidator()
        number9: int = validator.validate1("9", "#")
        number10: int = validator.validate1("10", "#")
        number11: int = validator.validate1("11", "#")
        number19: int = validator.validate1("19", "#")
        number20: int = validator.validate1("20", "#")
        number21: int = validator.validate1("21", "#")

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
