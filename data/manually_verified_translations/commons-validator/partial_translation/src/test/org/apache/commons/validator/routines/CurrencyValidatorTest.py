from __future__ import annotations
import re
import os
import decimal
import numbers
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.CurrencyValidator import *


class CurrencyValidatorTest(unittest.TestCase):

    __UK_POUND: str = ""

    __US_DOLLAR: str = ""

    __CURRENCY_SYMBOL: str = "\u00A4"

    def tearDown(self) -> None:
        super().tearDown()

    def setUp(self) -> None:

        import locale
        from decimal import Decimal, getcontext

        getcontext().prec = 4

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        self.__US_DOLLAR = Decimal("1.00").format_currency(
            locale.currency(locale.getlocale()[0])
        )

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        self.__UK_POUND = Decimal("1.00").format_currency(
            locale.currency(locale.getlocale()[0])
        )

    def testPattern(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        validator = CurrencyValidator.getInstance()
        basicPattern = self.__CURRENCY_SYMBOL + "#,##0.000"
        pattern = basicPattern + ";[" + basicPattern + "]"
        expected = decimal.Decimal("1234.567")
        negative = decimal.Decimal("-1234.567")

        self.assertEqual(
            "default",
            expected,
            validator.validate1(self.__UK_POUND + "1,234.567", pattern),
        )
        self.assertEqual(
            "negative",
            negative,
            validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
        )
        self.assertEqual(
            "no symbol +ve", expected, validator.validate1("1,234.567", pattern)
        )
        self.assertEqual(
            "no symbol -ve", negative, validator.validate1("[1,234.567]", pattern)
        )

        self.assertEqual(
            "default",
            expected,
            validator.validate3(self.__US_DOLLAR + "1,234.567", pattern, locale.US),
        )
        self.assertEqual(
            "negative",
            negative,
            validator.validate3(
                "[" + self.__US_DOLLAR + "1,234.567]", pattern, locale.US
            ),
        )
        self.assertEqual(
            "no symbol +ve",
            expected,
            validator.validate3("1,234.567", pattern, locale.US),
        )
        self.assertEqual(
            "no symbol -ve",
            negative,
            validator.validate3("[1,234.567]", pattern, locale.US),
        )

        self.assertFalse(
            "invalid symbol",
            validator.isValid1(self.__US_DOLLAR + "1,234.567", pattern),
        )
        self.assertFalse(
            "invalid symbol",
            validator.isValid3(self.__UK_POUND + "1,234.567", pattern, locale.US),
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def testIntegerInvalid(self) -> None:

        validator = CurrencyValidator(True, False)

        self.assertFalse(
            validator.isValid2(self.__UK_POUND + "1,234.56", Locale.UK), "UK positive"
        )
        self.assertFalse(
            validator.isValid2("-" + self.__UK_POUND + "1,234.56", Locale.UK),
            "UK negative",
        )

        self.assertFalse(
            validator.isValid2(self.__US_DOLLAR + "1,234.56", Locale.US), "US positive"
        )
        self.assertFalse(
            validator.isValid2("(" + self.__US_DOLLAR + "1,234.56)", Locale.US),
            "US negative",
        )

    def testIntegerValid(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        validator = CurrencyValidator.CurrencyValidator1()
        expected = decimal.Decimal("1234.00")
        negative = decimal.Decimal("-1234.00")

        self.assertEqual(
            "Default locale", expected, validator.validate0(self.__UK_POUND + "1,234")
        )

        self.assertEqual(
            "UK locale",
            expected,
            validator.validate2(self.__UK_POUND + "1,234", locale.UK),
        )
        self.assertEqual(
            "UK negative",
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234", locale.UK),
        )

        self.assertEqual(
            "US locale",
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234", locale.US),
        )
        self.assertEqual(
            "US negative",
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234)", locale.US),
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def testInvalid(self) -> None:

        validator = CurrencyValidator.getInstance()

        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")

        self.assertFalse(
            validator.isValid2(self.__US_DOLLAR + "1,234.56", Locale.UK),
            "UK wrong symbol",
        )
        self.assertFalse(
            validator.isValid2("(" + self.__UK_POUND + "1,234.56)", Locale.UK),
            "UK wrong negative",
        )

        self.assertFalse(
            validator.isValid2(self.__UK_POUND + "1,234.56", Locale.US),
            "US wrong symbol",
        )
        self.assertFalse(
            validator.isValid2("-" + self.__US_DOLLAR + "1,234.56", Locale.US),
            "US wrong negative",
        )

    def testValid(self) -> None:

        origDefault = locale.getlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.utf8")

        validator = CurrencyValidator.getInstance()
        expected = decimal.Decimal("1234.56")
        negative = decimal.Decimal("-1234.56")
        noDecimal = decimal.Decimal("1234.00")
        oneDecimal = decimal.Decimal("1234.50")

        self.assertEqual(
            "Default locale",
            expected,
            validator.validate0(self.__UK_POUND + "1,234.56"),
        )

        self.assertEqual(
            "UK locale",
            expected,
            validator.validate2(self.__UK_POUND + "1,234.56", locale.UK),
        )
        self.assertEqual(
            "UK negative",
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234.56", locale.UK),
        )
        self.assertEqual(
            "UK no decimal",
            noDecimal,
            validator.validate2(self.__UK_POUND + "1,234", locale.UK),
        )
        self.assertEqual(
            "UK 1 decimal",
            oneDecimal,
            validator.validate2(self.__UK_POUND + "1,234.5", locale.UK),
        )
        self.assertEqual(
            "UK 3 decimal",
            expected,
            validator.validate2(self.__UK_POUND + "1,234.567", locale.UK),
        )
        self.assertEqual(
            "UK no symbol", expected, validator.validate2("1,234.56", locale.UK)
        )

        self.assertEqual(
            "US locale",
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.56", locale.US),
        )
        self.assertEqual(
            "US negative",
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234.56)", locale.US),
        )
        self.assertEqual(
            "US no decimal",
            noDecimal,
            validator.validate2(self.__US_DOLLAR + "1,234", locale.US),
        )
        self.assertEqual(
            "US 1 decimal",
            oneDecimal,
            validator.validate2(self.__US_DOLLAR + "1,234.5", locale.US),
        )
        self.assertEqual(
            "US 3 decimal",
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.567", locale.US),
        )
        self.assertEqual(
            "US no symbol", expected, validator.validate2("1,234.56", locale.US)
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def testFormatType(self) -> None:
        self.assertEqual(
            1, CurrencyValidator.getInstance().getFormatType(), "Format Type A"
        )
        self.assertEqual(
            AbstractNumberValidator.CURRENCY_FORMAT,
            CurrencyValidator.getInstance().getFormatType(),
            "Format Type B",
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
