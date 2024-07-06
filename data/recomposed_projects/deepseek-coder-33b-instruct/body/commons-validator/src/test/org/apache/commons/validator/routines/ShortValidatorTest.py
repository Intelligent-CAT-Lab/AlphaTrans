from __future__ import annotations
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

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        self._validator = ShortValidator(False, 0)
        self._strictValidator = ShortValidator.ShortValidator1()

        self._testPattern = "#,###"

        max_ = Short.valueOf(Short.MAX_VALUE)
        self._maxPlusOne = Long.valueOf(max_.longValue() + 1)
        min_ = Short.valueOf(Short.MIN_VALUE)
        self._minMinusOne = Long.valueOf(min_.longValue() - 1)

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2", "1.2"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = Short.valueOf(1234)
        self._testZero = Short.valueOf(0)
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
        self._testLocale = Locale.GERMANY
        self._localeExpected = self._testNumber

    def testShortRangeMinMax(self) -> None:

        validator = ShortValidator.ShortValidator1()
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        min_ = 10
        max_ = 20

        assert not validator.isInRange1(number9, min_, max_), "isInRange() < min"
        assert validator.isInRange1(number10, min_, max_), "isInRange() = min"
        assert validator.isInRange1(number11, min_, max_), "isInRange() in range"
        assert validator.isInRange1(number20, min_, max_), "isInRange() = max"
        assert not validator.isInRange1(number21, min_, max_), "isInRange() > max"

        assert not validator.minValue1(number9, min_), "minValue() < min"
        assert validator.minValue1(number10, min_), "minValue() = min"
        assert validator.minValue1(number11, min_), "minValue() > min"

        assert validator.maxValue1(number19, max_), "maxValue() < max"
        assert validator.maxValue1(number20, max_), "maxValue() = max"
        assert not validator.maxValue1(number21, max_), "maxValue() > max"

    def testShortValidatorMethods(self) -> None:

        pass  # LLM could not translate this method
