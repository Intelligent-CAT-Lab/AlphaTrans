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

        self._validator = ByteValidator(False, 0)
        self._strictValidator = ByteValidator.ByteValidator1()

        self._testPattern = "#,###"

        self._max = Byte.valueOf(127)
        self._maxPlusOne = Long.valueOf(self._max.longValue() + 1)
        self._min = Byte.valueOf(-128)
        self._minMinusOne = Long.valueOf(self._min.longValue() - 1)

        self._invalidStrict = [
            None,
            "",
            "X",
            "X12",
            "12X",
            "1X2",
            "1.2",
            self.__BYTE_MAX_1,
            self.__BYTE_MIN_1,
            self.__BYTE_MAX_0,
            self.__BYTE_MIN_0,
        ]

        self._invalid = [None, "", "X", "X12", self.__BYTE_MAX_1, self.__BYTE_MIN_1]

        self._testNumber = Byte.valueOf(123)
        self._testZero = Byte.valueOf(0)
        self._validStrict = ["0", "123", ",123", self.__BYTE_MAX, self.__BYTE_MIN]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self.__BYTE_MAX_VAL,
            self.__BYTE_MIN_VAL,
        ]
        self._valid = [
            "0",
            "123",
            ",123",
            ",123.5",
            "123X",
            self.__BYTE_MAX,
            self.__BYTE_MIN,
            self.__BYTE_MAX_0,
            self.__BYTE_MIN_0,
        ]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self.__BYTE_MAX_VAL,
            self.__BYTE_MIN_VAL,
            self.__BYTE_MAX_VAL,
            self.__BYTE_MIN_VAL,
        ]

        self._testStringUS = ",123"
        self._testStringDE = ".123"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###"
        self._testLocale = Locale.GERMANY
        self._localeExpected = self._testNumber

    def testByteRangeMinMax(self) -> None:

        validator = ByteValidator()
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        min_byte = b"\n"
        max_byte = b"\x14"

        assert not validator.isInRange1(
            number9, min_byte, max_byte
        ), "isInRange() < min"
        assert validator.isInRange1(number10, min_byte, max_byte), "isInRange() = min"
        assert validator.isInRange1(
            number11, min_byte, max_byte
        ), "isInRange() in range"
        assert validator.isInRange1(number20, min_byte, max_byte), "isInRange() = max"
        assert not validator.isInRange1(
            number21, min_byte, max_byte
        ), "isInRange() > max"

        assert not validator.minValue1(number9, min_byte), "minValue() < min"
        assert validator.minValue1(number10, min_byte), "minValue() = min"
        assert validator.minValue1(number11, min_byte), "minValue() > min"

        assert validator.maxValue1(number19, max_byte), "maxValue() < max"
        assert validator.maxValue1(number20, max_byte), "maxValue() = max"
        assert not validator.maxValue1(number21, max_byte), "maxValue() > max"

    def testByteValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
