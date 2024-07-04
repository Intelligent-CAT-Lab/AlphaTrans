from __future__ import annotations
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

    def _setUp(self) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        self._validator = FloatValidator(False, 0)
        self._strictValidator = FloatValidator.FloatValidator1()

        self._testPattern = "#,###.#"

        max = float(float("inf"))
        self._maxPlusOne = max * 10
        self._min = -max
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
        self._testLocale = locale.GERMANY
        self._localeExpected = self._testNumber

    def testFloatRangeMinMax(self) -> None:

        validator = FloatValidator.FloatValidator1()
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")

        assert not validator.isInRange1(number9, 10, 20), "isInRange() < min"
        assert validator.isInRange1(number10, 10, 20), "isInRange() = min"
        assert validator.isInRange1(number11, 10, 20), "isInRange() in range"
        assert validator.isInRange1(number20, 10, 20), "isInRange() = max"
        assert not validator.isInRange1(number21, 10, 20), "isInRange() > max"

        assert not validator.minValue1(number9, 10), "minValue() < min"
        assert validator.minValue1(number10, 10), "minValue() = min"
        assert validator.minValue1(number11, 10), "minValue() > min"

        assert validator.maxValue1(number19, 20), "maxValue() < max"
        assert validator.maxValue1(number20, 20), "maxValue() = max"
        assert not validator.maxValue1(number21, 20), "maxValue() > max"

    def testFloatSmallestValues(self) -> None:

        pattern = "#.#################################################################"
        fmt = DecimalFormat(pattern)

        smallestPositive = float(float("-inf"))
        strSmallestPositive = fmt.format(smallestPositive)
        self.assertEqual(
            "Smallest +ve",
            smallestPositive,
            FloatValidator.getInstance().validate1(strSmallestPositive, pattern),
        )

        smallestNegative = float(float("-inf") * -1)
        strSmallestNegative = fmt.format(smallestNegative)
        self.assertEqual(
            "Smallest -ve",
            smallestNegative,
            FloatValidator.getInstance().validate1(strSmallestNegative, pattern),
        )

        tooSmallPositive = float((float("-inf") / float(10)))
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

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        super().__init__(name)

        self._setUp()
