from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.ByteValidator import *


class ByteValidatorTest(AbstractNumberValidatorTest):

    __BYTE_MIN_1: str = "-129"
    __BYTE_MIN_0: str = "-128.999999999999999999999999"  # force double rounding
    __BYTE_MIN: str = "-128"
    __BYTE_MAX_1: str = "128"
    __BYTE_MAX_0: str = "127.99999999999999999999999"
    __BYTE_MAX: str = "127"
    __BYTE_MAX_VAL: int = int(127)
    __BYTE_MIN_VAL: int = -128

    def setUp(self) -> None:

        self._BYTE_MIN_1 = "-129"
        self._BYTE_MIN_0 = "-128.999999999999999999999999"  # force double rounding
        self._BYTE_MIN = "-128"
        self._BYTE_MAX_1 = "128"
        self._BYTE_MAX_0 = "127.99999999999999999999999"
        self._BYTE_MAX = "127"
        self._BYTE_MAX_VAL = int(127)
        self._BYTE_MIN_VAL = -128

        self._validator = ByteValidator(False, 0)
        self._strictValidator = ByteValidator.ByteValidator1()

        self._testPattern = "#,###"

        self._max = int(127)
        self._maxPlusOne = self._max + 1
        self._min = -128
        self._minMinusOne = self._min - 1

        self._invalidStrict = [
            None,
            "",
            "X",
            "X12",
            "12X",
            "1X2",
            "1.2",
            self._BYTE_MAX_1,
            self._BYTE_MIN_1,
            self._BYTE_MAX_0,
            self._BYTE_MIN_0,
        ]

        self._invalid = [None, "", "X", "X12", self._BYTE_MAX_1, self._BYTE_MIN_1]

        self._testNumber = int(123)
        self._testZero = int(0)
        self._validStrict = ["0", "123", ",123", self._BYTE_MAX, self._BYTE_MIN]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._BYTE_MAX_VAL,
            self._BYTE_MIN_VAL,
        ]
        self._valid = [
            "0",
            "123",
            ",123",
            ",123.5",
            "123X",
            self._BYTE_MAX,
            self._BYTE_MIN,
            self._BYTE_MAX_0,
            self._BYTE_MIN_0,
        ]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._BYTE_MAX_VAL,
            self._BYTE_MIN_VAL,
            self._BYTE_MAX_VAL,
            self._BYTE_MIN_VAL,
        ]

        self._testStringUS = ",123"
        self._testStringDE = ".123"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###"
        self._testLocale = "Germany"
        self._localeExpected = self._testNumber

    def testByteRangeMinMax(self) -> None:

        validator = ByteValidator(self._strictValidator)
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        min_ = b"10"
        max_ = b"20"

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

    def testByteValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
