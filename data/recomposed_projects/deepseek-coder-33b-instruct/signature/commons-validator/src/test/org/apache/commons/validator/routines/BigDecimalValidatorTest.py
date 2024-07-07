from __future__ import annotations
import locale
import re
import decimal
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class BigDecimalValidatorTest(AbstractNumberValidatorTest):

    def setUp(self) -> None:

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
        testNumber2 = Decimal(".1")
        testNumber3 = Decimal("12345.67899")
        self._testZero = Decimal("0")
        self._validStrict = ["0", "1234.5", "1,234.5", ".1", "12345.678990"]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            testNumber2,
            testNumber3,
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
        number9 = decimal.Decimal("9")
        number10 = decimal.Decimal("10")
        number11 = decimal.Decimal("11")
        number19 = decimal.Decimal("19")
        number20 = decimal.Decimal("20")
        number21 = decimal.Decimal("21")

        min = 10
        max = 20

        assert not validator.isInRange(number9, min, max), "isInRange(A) < min"
        assert validator.isInRange(number10, min, max), "isInRange(A) = min"
        assert validator.isInRange(number11, min, max), "isInRange(A) in range"
        assert validator.isInRange(number20, min, max), "isInRange(A) = max"
        assert not validator.isInRange(number21, min, max), "isInRange(A) > max"

        assert not validator.minValue(number9, min), "minValue(A) < min"
        assert validator.minValue(number10, min), "minValue(A) = min"
        assert validator.minValue(number11, min), "minValue(A) > min"

        assert validator.maxValue(number19, max), "maxValue(A) < max"
        assert validator.maxValue(number20, max), "maxValue(A) = max"
        assert not validator.maxValue(number21, max), "maxValue(A) > max"

    def testBigDecimalValidatorMethods(self) -> None:

        pass  # LLM could not translate this method

    def __init__(self, name: str) -> None:
        super().__init__(name)
