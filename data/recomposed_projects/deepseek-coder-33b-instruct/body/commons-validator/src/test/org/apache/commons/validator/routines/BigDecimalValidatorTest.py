from __future__ import annotations
import re
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class BigDecimalValidatorTest(AbstractNumberValidatorTest):

    def _setUp(self) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        self._validator = BigDecimalValidator.BigDecimalValidator1(False)
        self._strictValidator = BigDecimalValidator.BigDecimalValidator2()

        self._testPattern = "#,###.###"

        self._max = None
        self._maxPlusOne = None
        self._min = None
        self._minMinusOne = None

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2", "1.234X"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = Decimal("1234.5")
        self._testNumber2 = Decimal(".1")
        self._testNumber3 = Decimal("12345.67899")
        self._testZero = Decimal("0")
        self._validStrict = ["0", "1234.5", "1,234.5", ".1", "12345.678990"]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber2,
            self._testNumber3,
        ]
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

    def testBigDecimalRangeMinMax(self) -> None:

        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = Decimal("9")
        number10 = Decimal("10")
        number11 = Decimal("11")
        number19 = Decimal("19")
        number20 = Decimal("20")
        number21 = Decimal("21")

        min = 10
        max = 20

        self.assertFalse(validator.isInRange(number9, min, max), "isInRange(A) < min")
        self.assertTrue(validator.isInRange(number10, min, max), "isInRange(A) = min")
        self.assertTrue(
            validator.isInRange(number11, min, max), "isInRange(A) in range"
        )
        self.assertTrue(validator.isInRange(number20, min, max), "isInRange(A) = max")
        self.assertFalse(validator.isInRange(number21, min, max), "isInRange(A) > max")

        self.assertFalse(validator.minValue(number9, min), "minValue(A) < min")
        self.assertTrue(validator.minValue(number10, min), "minValue(A) = min")
        self.assertTrue(validator.minValue(number11, min), "minValue(A) > min")

        self.assertTrue(validator.maxValue(number19, max), "maxValue(A) < max")
        self.assertTrue(validator.maxValue(number20, max), "maxValue(A) = max")
        self.assertFalse(validator.maxValue(number21, max), "maxValue(A) > max")

    def testBigDecimalValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:

        import locale

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

        super().__init__(name)

        self._setUp()
