from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.DoubleValidator import *


class DoubleValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:

        super().setUp()

        self._validator = DoubleValidator(False, 0)
        self._strictValidator = DoubleValidator.DoubleValidator1()

        self._testPattern = "#,###.#"

        self._max = None
        self._maxPlusOne = None
        self._min = None
        self._minMinusOne = None

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
        self._testLocale = Locale.GERMANY
        self._localeExpected = self._testNumber

    def testDoubleRangeMinMax(self) -> None:

        validator = DoubleValidator()
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

    def testDoubleValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
