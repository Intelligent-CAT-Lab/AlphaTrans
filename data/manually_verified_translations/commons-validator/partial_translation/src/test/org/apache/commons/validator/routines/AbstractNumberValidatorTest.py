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

        baos = io.BytesIO()
        try:
            oos = io.BufferedWriter(baos)
            oos.write(str(self._validator).encode())
            oos.flush()
            oos.close()
        except Exception as e:
            pytest.fail(
                self._validator.__class__.__name__
                + " error during serialization: "
                + str(e)
            )

        result = None
        try:
            bais = io.BytesIO(baos.getvalue())
            ois = io.BufferedReader(bais)
            result = ois.read()
            bais.close()
        except Exception as e:
            pytest.fail(
                self._validator.__class__.__name__
                + " error during deserialization: "
                + str(e)
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
            "US Locale, US Format",
            "1,234.5",
            self._strictValidator.format2(number, Locale.US),
        )
        self.assertEqual(
            "DE Locale, DE Format",
            "1.234,5",
            self._strictValidator.format2(number, Locale.GERMAN),
        )
        self.assertEqual(
            "Pattern #,#0.00",
            "12,34.50",
            self._strictValidator.format1(number, "#,#0.00"),
        )

    def testValidateLocale(self) -> None:

        self.assertEqual(
            "US Locale, US Format",
            self._testNumber,
            self._strictValidator.parse(self._testStringUS, None, Locale.US),
        )
        self.assertIsNone(
            "US Locale, DE Format",
            self._strictValidator.parse(self._testStringDE, None, Locale.US),
        )

        self.assertEqual(
            "DE Locale, DE Format",
            self._testNumber,
            self._strictValidator.parse(self._testStringDE, None, Locale.GERMAN),
        )
        self.assertIsNone(
            "DE Locale, US Format",
            self._strictValidator.parse(self._testStringUS, None, Locale.GERMAN),
        )

        self.assertEqual(
            "Default Locale, US Format",
            self._testNumber,
            self._strictValidator.parse(self._testStringUS, None, None),
        )
        self.assertIsNone(
            "Default Locale, DE Format",
            self._strictValidator.parse(self._testStringDE, None, None),
        )

    def testValidNotStrict(self) -> None:

        for i in range(len(self._valid)):
            text = "idx=[" + str(i) + "] value=[" + str(self._validCompare[i]) + "]"
            self.assertEqual(
                self._validCompare[i],
                self._validator.parse(self._valid[i], None, "US"),
                "(A) " + text,
            )
            self.assertTrue(
                self._validator.isValid3(self._valid[i], None, "US"), "(B) " + text
            )
            self.assertEqual(
                self._validCompare[i],
                self._validator.parse(self._valid[i], self._testPattern, None),
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
                "(A) " + text,
                self._validStrictCompare[i],
                self._strictValidator.parse(self._validStrict[i], None, "US"),
            )
            self.assertTrue(
                "(B) " + text,
                self._strictValidator.isValid3(self._validStrict[i], None, "US"),
            )
            self.assertEqual(
                "(C) " + text,
                self._validStrictCompare[i],
                self._strictValidator.parse(
                    self._validStrict[i], self._testPattern, None
                ),
            )
            self.assertTrue(
                "(D) " + text,
                self._strictValidator.isValid3(
                    self._validStrict[i], self._testPattern, None
                ),
            )

    def testInvalidNotStrict(self) -> None:

        for i in range(len(self._invalid)):
            text = "idx=[" + str(i) + "] value=[" + self._invalid[i] + "]"
            self.assertIsNone(
                self._validator.parse(self._invalid[i], None, "US"), "(A) " + text
            )
            self.assertFalse(
                self._validator.isValid3(self._invalid[i], None, "US"), "(B) " + text
            )
            self.assertIsNone(
                self._validator.parse(self._invalid[i], self._testPattern, None),
                "(C) " + text,
            )
            self.assertFalse(
                self._validator.isValid3(self._invalid[i], self._testPattern, None),
                "(D) " + text,
            )

    def testInvalidStrict(self) -> None:

        for i in range(len(self._invalidStrict)):
            text = "idx=[" + str(i) + "] value=[" + self._invalidStrict[i] + "]"
            self.assertIsNone(
                self._strictValidator.parse(self._invalidStrict[i], None, "US"),
                "(A) " + text,
            )
            self.assertFalse(
                self._strictValidator.isValid3(self._invalidStrict[i], None, "US"),
                "(B) " + text,
            )
            self.assertIsNone(
                self._strictValidator.parse(
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

        fmt = DecimalFormat("#")
        if self._max is not None:
            self.assertEqual(
                self._max,
                self._validator.parse(fmt.format(self._max), "#", None),
                "Test Max",
            )
            self.assertIsNone(
                self._validator.parse(fmt.format(self._maxPlusOne), "#", None),
                "Test Max + 1",
            )
            self.assertEqual(
                self._min,
                self._validator.parse(fmt.format(self._min), "#", None),
                "Test Min",
            )
            self.assertIsNone(
                self._validator.parse(fmt.format(self._minMinusOne), "#", None),
                "Test min - 1",
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
