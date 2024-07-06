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

    _validStrict: typing.List[str] = None

    _invalidStrict: typing.List[str] = None

    _validCompare: typing.List[typing.Union[int, float, numbers.Number]] = None

    _valid: typing.List[str] = None

    _invalid: typing.List[str] = None

    _minMinusOne: typing.Union[int, float, numbers.Number] = None

    _min: typing.Union[int, float, numbers.Number] = None

    _maxPlusOne: typing.Union[int, float, numbers.Number] = None

    _max: typing.Union[int, float, numbers.Number] = None

    _strictValidator: AbstractNumberValidator = None

    _validator: AbstractNumberValidator = None

    def _tearDown(self) -> None:
        super()._tearDown()
        self._validator = None
        self._strictValidator = None

    def _setUp(self) -> None:
        super()._setUp()
        Locale.setDefault(Locale.US)

    def testSerialization(self) -> None:
        baos = io.BytesIO()
        try:
            oos = io.ObjectOutputStream(baos)
            oos.writeObject(self._validator)
            oos.flush()
            oos.close()
        except Exception as e:
            self.fail(
                self._validator.getClass().getName()
                + " error during serialization: "
                + e
            )

        result = None
        try:
            bais = io.ByteArrayInputStream(baos.toByteArray())
            ois = io.ObjectInputStream(bais)
            result = ois.readObject()
            bais.close()
        except Exception as e:
            self.fail(
                self._validator.getClass().getName()
                + " error during deserialization: "
                + e
            )
        self.assertNotNull(result)

    def testRangeMinMax(self) -> None:
        number9: typing.Union[int, float, numbers.Number] = Integer(9)
        number10: typing.Union[int, float, numbers.Number] = Integer(10)
        number11: typing.Union[int, float, numbers.Number] = Integer(11)
        number19: typing.Union[int, float, numbers.Number] = Integer(19)
        number20: typing.Union[int, float, numbers.Number] = Integer(20)
        number21: typing.Union[int, float, numbers.Number] = Integer(21)

        self.assertFalse(
            "isInRange() < min",
            self._strictValidator.isInRange(number9, number10, number20),
        )
        self.assertTrue(
            "isInRange() = min",
            self._strictValidator.isInRange(number10, number10, number20),
        )
        self.assertTrue(
            "isInRange() in range",
            self._strictValidator.isInRange(number11, number10, number20),
        )
        self.assertTrue(
            "isInRange() = max",
            self._strictValidator.isInRange(number20, number10, number20),
        )
        self.assertFalse(
            "isInRange() > max",
            self._strictValidator.isInRange(number21, number10, number20),
        )

        self.assertFalse(
            "minValue() < min", self._strictValidator.minValue(number9, number10)
        )
        self.assertTrue(
            "minValue() = min", self._strictValidator.minValue(number10, number10)
        )
        self.assertTrue(
            "minValue() > min", self._strictValidator.minValue(number11, number10)
        )

        self.assertTrue(
            "maxValue() < max", self._strictValidator.maxValue(number19, number20)
        )
        self.assertTrue(
            "maxValue() = max", self._strictValidator.maxValue(number20, number20)
        )
        self.assertFalse(
            "maxValue() > max", self._strictValidator.maxValue(number21, number20)
        )

    def testFormat(self) -> None:
        number: numbers.Number = BigDecimal("1234.5")
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
                "(A) " + text,
                self._validCompare[i],
                self._validator._parse(self._valid[i], None, Locale.US),
            )
            self.assertTrue(
                "(B) " + text, self._validator.isValid3(self._valid[i], None, Locale.US)
            )
            self.assertEqual(
                "(C) " + text,
                self._validCompare[i],
                self._validator._parse(self._valid[i], self._testPattern, None),
            )
            self.assertTrue(
                "(D) " + text,
                self._validator.isValid3(self._valid[i], self._testPattern, None),
            )

    def testValidStrict(self) -> None:
        for i in range(len(self._validStrict)):
            text = (
                "idx=[" + str(i) + "] value=[" + str(self._validStrictCompare[i]) + "]"
            )
            self.assertEqual(
                "(A) " + text,
                self._validStrictCompare[i],
                self._strictValidator.parse(self._validStrict[i], None, Locale.US),
            )
            self.assertTrue(
                "(B) " + text,
                self._strictValidator.isValid3(self._validStrict[i], None, Locale.US),
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
                "(A) " + text, self._validator._parse(self._invalid[i], None, Locale.US)
            )
            self.assertFalse(
                "(B) " + text,
                self._validator.isValid3(self._invalid[i], None, Locale.US),
            )
            self.assertIsNone(
                "(C) " + text,
                self._validator._parse(self._invalid[i], self._testPattern, None),
            )
            self.assertFalse(
                "(D) " + text,
                self._validator.isValid3(self._invalid[i], self._testPattern, None),
            )

    def testInvalidStrict(self) -> None:
        for i in range(len(self._invalidStrict)):
            text = "idx=[" + str(i) + "] value=[" + self._invalidStrict[i] + "]"
            self.assertIsNone(
                "(A) " + text,
                self._strictValidator._parse(self._invalidStrict[i], None, Locale.US),
            )
            self.assertFalse(
                "(B) " + text,
                self._strictValidator.isValid3(self._invalidStrict[i], None, Locale.US),
            )
            self.assertIsNone(
                "(C) " + text,
                self._strictValidator._parse(
                    self._invalidStrict[i], self._testPattern, None
                ),
            )
            self.assertFalse(
                "(D) " + text,
                self._strictValidator.isValid3(
                    self._invalidStrict[i], self._testPattern, None
                ),
            )

    def testValidateMinMax(self) -> None:
        fmt = DecimalFormat("#")
        if self._max is not None:
            self.assertEqual(
                self._max, self._validator.parse(fmt.format(self._max), "#", None)
            )
            self.assertIsNone(
                self._validator.parse(fmt.format(self._maxPlusOne), "#", None)
            )
            self.assertEqual(
                self._min, self._validator.parse(fmt.format(self._min), "#", None)
            )
            self.assertIsNone(
                self._validator.parse(fmt.format(self._minMinusOne), "#", None)
            )

    def testFormatType(self) -> None:
        self.assertEqual("Format Type A", 0, self._validator.getFormatType())
        self.assertEqual(
            "Format Type B",
            AbstractNumberValidator.STANDARD_FORMAT,
            self._validator.getFormatType(),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
