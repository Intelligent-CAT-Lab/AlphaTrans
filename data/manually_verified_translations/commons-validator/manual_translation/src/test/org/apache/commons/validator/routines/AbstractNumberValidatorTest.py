from __future__ import annotations
import locale
import re
import os
from io import BytesIO
import unittest
import pytest
from abc import ABC
import io
import numbers
import pickle
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class AbstractNumberValidatorTest(unittest.TestCase, ABC):

    _localeExpected: typing.Union[int, float, numbers.Number] = None

    _testLocale: typing.Any = None

    _localePattern: str = ""

    _localeValue: str = ""

    _testStringDE: str = ""

    _testStringUS: str = ""

    _testZero: typing.Union[int, float, numbers.Number] = None

    _testNumber: typing.Union[int, float, numbers.Number] = None

    _testPattern: str = ""

    _validStrictCompare: typing.List[typing.Union[int, float, numbers.Number]] = None

    _validStrict: typing.List[typing.List[str]] = None

    _invalidStrict: typing.List[typing.List[str]] = None

    _validCompare: typing.List[typing.Union[int, float, numbers.Number]] = None

    _valid: typing.List[typing.List[str]] = None

    _invalid: typing.List[typing.List[str]] = None

    _minMinusOne: typing.Union[int, float, numbers.Number] = None

    _min: typing.Union[int, float, numbers.Number] = None

    _maxPlusOne: typing.Union[int, float, numbers.Number] = None

    _max: typing.Union[int, float, numbers.Number] = None

    _strictValidator: AbstractNumberValidator = None

    _validator: AbstractNumberValidator = None

    def tearDown(self) -> None:

        super().tearDown()
        self._validator = None
        self._strictValidator = None

    def setUp(self) -> None:
        super().setUp()
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    def testSerialization(self) -> None:

        baos = BytesIO()
        try:
            pickle.dump(self._validator, baos)
        except Exception as e:
            self.fail(f"{self._validator.__class__.__name__} error during serialization: {e}")

        result = None
        try:
            bais = BytesIO(baos.getvalue())
            result = pickle.load(bais)
        except Exception as e:
            self.fail(
                f"{self._validator.__class__.__name__} error during deserialization: {e}"
            )
        
        self.assertIsNotNone(result)

    def testRangeMinMax(self) -> None:

        number9 = int(9)
        number10 = int(10)
        number11 = int(11)
        number19 = int(19)
        number20 = int(20)
        number21 = int(21)

        self.assertFalse(
            self._strictValidator.isInRange(number9, number10, number20),
            "isInRange() < min",
        )
        self.assertTrue(
            self._strictValidator.isInRange(number10, number10, number20),
            "isInRange() = min",
        )
        self.assertTrue(
            self._strictValidator.isInRange(number11, number10, number20),
            "isInRange() in range",
        )
        self.assertTrue(
            self._strictValidator.isInRange(number20, number10, number20),
            "isInRange() = max",
        )
        self.assertFalse(
            self._strictValidator.isInRange(number21, number10, number20),
            "isInRange() > max",
        )

        self.assertFalse(
            self._strictValidator.minValue(number9, number10), "minValue() < min"
        )
        self.assertTrue(
            self._strictValidator.minValue(number10, number10), "minValue() = min"
        )
        self.assertTrue(
            self._strictValidator.minValue(number11, number10), "minValue() > min"
        )

        self.assertTrue(
            self._strictValidator.maxValue(number19, number20), "maxValue() < max"
        )
        self.assertTrue(
            self._strictValidator.maxValue(number20, number20), "maxValue() = max"
        )
        self.assertFalse(
            self._strictValidator.maxValue(number21, number20), "maxValue() > max"
        )

    def testFormat(self) -> None:

        number = Decimal("1234.5")
        self.assertEqual(
            "1,234.5",
            self._strictValidator._format2(number, 'en_US.UTF-8'),
            "US Locale, US Format"
        )
        self.assertEqual(
            "1.234,5",
            self._strictValidator._format2(number, 'de_DE.UTF-8'),
            "DE Locale, DE Format"
        )
        self.assertEqual(
            "12,34.50",
            self._strictValidator._format1(number, "#,#0.00"),
            "Pattern #,#0.00"
        )

    def testValidateLocale(self) -> None:

        self.assertEqual(
            self._testNumber,
            self._strictValidator._parse(self._testStringUS, None, "en_US.UTF-8"),
            "US Locale, US Format"
        )
        self.assertIsNone(
            self._strictValidator._parse(self._testStringDE, None, "en_US.UTF-8"),
            "US Locale, DE Format"
        )

        self.assertEqual(
            self._testNumber,
            self._strictValidator._parse(self._testStringDE, None, "de_DE.UTF-8"),
            "DE Locale, DE Format"
        )
        self.assertIsNone(
            self._strictValidator._parse(self._testStringUS, None, "de_DE.UTF-8"),
            "DE Locale, US Format"
        )

        self.assertEqual(
            self._testNumber,
            self._strictValidator._parse(self._testStringUS, None, None),
            "Default Locale, US Format"
        )
        self.assertIsNone(
            self._strictValidator._parse(self._testStringDE, None, None),
            "Default Locale, DE Format"
        )

    def testValidNotStrict(self) -> None:

        for i in range(len(self._valid)):
            text = "idx=[" + str(i) + "] value=[" + str(self._validCompare[i]) + "]"
            self.assertEqual(
                self._validCompare[i],
                self._validator._parse(self._valid[i], None, "en_US.UTF-8"),
                "(A) " + text,
            )
            self.assertTrue(
                self._validator.isValid3(self._valid[i], None, "en_US.UTF-8"), "(B) " + text
            )
            self.assertEqual(
                self._validCompare[i],
                self._validator._parse(self._valid[i], self._testPattern, None),
                "(C) " + text,
            )
            self.assertTrue(
                self._validator.isValid3(self._valid[i], self._testPattern, None),
                "(D) " + text,
            )

    def testValidStrict(self) -> None:

        for i in range(len(self._validStrict)):
            text = (
                "idx=[" + str(i) + "] value=[" + str(self._validStrictCompare[i]) + "]"
            )
            self.assertEqual(
                self._validStrictCompare[i],
                self._strictValidator._parse(self._validStrict[i], None, "en_US.UTF-8"),
                "(A) " + text
            )
            self.assertTrue(
                self._strictValidator.isValid3(self._validStrict[i], None, "en_US.UTF-8"),
                "(B) " + text
            )
            self.assertEqual(
                self._validStrictCompare[i],
                self._strictValidator._parse(
                    self._validStrict[i], self._testPattern, None
                ),
                "(C) " + text
            )
            self.assertTrue(
                self._strictValidator.isValid3(
                    self._validStrict[i], self._testPattern, None
                ),
                "(D) " + text
            )

    def testInvalidNotStrict(self) -> None:

        for i in range(len(self._invalid)):
            text = "idx=[" + str(i) + "] value=[" + str(self._invalid[i]) + "]"
            self.assertIsNone(
                self._validator._parse(self._invalid[i], None, "en_US.UTF-8"), "(A) " + text
            )
            self.assertFalse(
                self._validator.isValid3(self._invalid[i], None, "en_US.UTF-8"), "(B) " + text
            )
            self.assertIsNone(
                self._validator._parse(self._invalid[i], self._testPattern, None),
                "(C) " + text,
            )
            self.assertFalse(
                self._validator.isValid3(self._invalid[i], self._testPattern, None),
                "(D) " + text,
            )

    def testInvalidStrict(self) -> None:

        for i in range(len(self._invalidStrict)):
            text = "idx=[" + str(i) + "] value=[" + str(self._invalidStrict[i]) + "]"
            self.assertIsNone(
                self._strictValidator._parse(self._invalidStrict[i], None, "en_US.UTF-8"),
                "(A) " + text,
            )
            self.assertFalse(
                self._strictValidator.isValid3(self._invalidStrict[i], None, "en_US.UTF-8"),
                "(B) " + text,
            )
            self.assertIsNone(
                self._strictValidator._parse(
                    self._invalidStrict[i], self._testPattern, None
                ),
                "(C) " + text,
            )
            self.assertFalse(
                self._strictValidator.isValid3(
                    self._invalidStrict[i], self._testPattern, None
                ),
                "(D) " + text,
            )

    def testValidateMinMax(self) -> None:

        if self._max is not None:
            self.assertEqual(
                self._max,
                self._validator._parse(str(self._max), '#', None),
                "Test Max"
            )
            self.assertIsNone(
                self._validator._parse(str(self._maxPlusOne), '#', None),
                "Test Max + 1"
            )
            self.assertEqual(
                self._min,
                self._validator._parse(str(self._min), '#', None),
                "Test Min"
            )
            self.assertIsNone(
                self._validator._parse(str(self._minMinusOne), '#', None),
                "Test min - 1"
            )

    def testFormatType(self) -> None:
        self.assertEqual(0, self._validator.getFormatType(), "Format Type A")
        self.assertEqual(
            AbstractNumberValidator.STANDARD_FORMAT,
            self._validator.getFormatType(),
            "Format Type B",
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
