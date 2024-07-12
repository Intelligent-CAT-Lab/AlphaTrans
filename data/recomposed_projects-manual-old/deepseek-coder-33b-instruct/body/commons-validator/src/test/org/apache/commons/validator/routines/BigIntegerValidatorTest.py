from __future__ import annotations
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

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

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
        self._testLocale = locale.setlocale(locale.LC_ALL, 'de_DE')
        self._localeExpected = self._testNumber

    def testBigIntegerRangeMinMax(self) -> None:

        validator = BigIntegerValidator.BigIntegerValidator1()
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")

        assert not validator.isInRange(number9, 10, 20), "isInRange() < min"
        assert validator.isInRange(number10, 10, 20), "isInRange() = min"
        assert validator.isInRange(number11, 10, 20), "isInRange() in range"
        assert validator.isInRange(number20, 10, 20), "isInRange() = max"
        assert not validator.isInRange(number21, 10, 20), "isInRange() > max"

        assert not validator.minValue(number9, 10), "minValue() < min"
        assert validator.minValue(number10, 10), "minValue() = min"
        assert validator.minValue(number11, 10), "minValue() > min"

        assert validator.maxValue(number19, 20), "maxValue() < max"
        assert validator.maxValue(number20, 20), "maxValue() = max"
        assert not validator.maxValue(number21, 20), "maxValue() > max"

    def testBigIntegerValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        super().__init__(name)

        self.setUp()
