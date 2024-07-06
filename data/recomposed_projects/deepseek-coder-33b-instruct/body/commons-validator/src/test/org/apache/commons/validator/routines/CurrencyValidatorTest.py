from __future__ import annotations
import re
import os
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
        import decimal

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        self.__US_DOLLAR = decimal.Decimal("1.00").format_money(
            locale.currency(1234567.89)
        )

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        self.__UK_POUND = decimal.Decimal("1.00").format_money(
            locale.currency(1234567.89)
        )

    def testPattern(self) -> None:

        pass  # LLM could not translate this method

    def testIntegerInvalid(self) -> None:

        validator = CurrencyValidator(True, False)

        self.assertFalse(
            "UK positive", validator.isValid2(self.__UK_POUND + "1,234.56", Locale.UK)
        )
        self.assertFalse(
            "UK negative",
            validator.isValid2("-" + self.__UK_POUND + "1,234.56", Locale.UK),
        )

        self.assertFalse(
            "US positive", validator.isValid2(self.__US_DOLLAR + "1,234.56", Locale.US)
        )
        self.assertFalse(
            "US negative",
            validator.isValid2("(" + self.__US_DOLLAR + "1,234.56)", Locale.US),
        )

    def testIntegerValid(self) -> None:

        import locale
        import decimal

        origDefault = locale.getlocale()
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        US_DOLLAR = decimal.Decimal("1.00").format_money(locale.currency(1234567.89))

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        UK_POUND = decimal.Decimal("1.00").format_money(locale.currency(1234567.89))

        validator = CurrencyValidator.CurrencyValidator1()
        expected = decimal.Decimal("1234.00")
        negative = decimal.Decimal("-1234.00")

        self.assertEqual(
            "Default locale", expected, validator.validate0(UK_POUND + "1,234")
        )

        self.assertEqual(
            "UK locale", expected, validator.validate2(UK_POUND + "1,234", locale.UK)
        )
        self.assertEqual(
            "UK negative",
            negative,
            validator.validate2("-" + UK_POUND + "1,234", locale.UK),
        )

        self.assertEqual(
            "US locale", expected, validator.validate2(US_DOLLAR + "1,234", locale.US)
        )
        self.assertEqual(
            "US negative",
            negative,
            validator.validate2("(" + US_DOLLAR + "1,234)", locale.US),
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def testInvalid(self) -> None:

        validator = CurrencyValidator.getInstance()

        self.assertFalse("isValid() Null Value", validator.isValid0(None))
        self.assertFalse("isValid() Empty Value", validator.isValid0(""))
        self.assertIsNone("validate() Null Value", validator.validate0(None))
        self.assertIsNone("validate() Empty Value", validator.validate0(""))

        self.assertFalse(
            "UK wrong symbol",
            validator.isValid2(self.__US_DOLLAR + "1,234.56", "en_GB"),
        )
        self.assertFalse(
            "UK wrong negative",
            validator.isValid2("(" + self.__UK_POUND + "1,234.56)", "en_GB"),
        )

        self.assertFalse(
            "US wrong symbol", validator.isValid2(self.__UK_POUND + "1,234.56", "en_US")
        )
        self.assertFalse(
            "US wrong negative",
            validator.isValid2("-" + self.__US_DOLLAR + "1,234.56", "en_US"),
        )

    def testValid(self) -> None:

        import locale
        import decimal

        origDefault = locale.getlocale()
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        US_DOLLAR = decimal.Decimal("1.00").format_money(locale.currency(1234567.89))

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        UK_POUND = decimal.Decimal("1.00").format_money(locale.currency(1234567.89))

        validator = CurrencyValidator.getInstance()
        expected = decimal.Decimal("1234.56")
        negative = decimal.Decimal("-1234.56")
        noDecimal = decimal.Decimal("1234.00")
        oneDecimal = decimal.Decimal("1234.50")

        self.assertEqual(
            "Default locale", expected, validator.validate0(UK_POUND + "1,234.56")
        )

        self.assertEqual(
            "UK locale", expected, validator.validate2(UK_POUND + "1,234.56", locale.UK)
        )
        self.assertEqual(
            "UK negative",
            negative,
            validator.validate2("-" + UK_POUND + "1,234.56", locale.UK),
        )
        self.assertEqual(
            "UK no decimal",
            noDecimal,
            validator.validate2(UK_POUND + "1,234", locale.UK),
        )
        self.assertEqual(
            "UK 1 decimal",
            oneDecimal,
            validator.validate2(UK_POUND + "1,234.5", locale.UK),
        )
        self.assertEqual(
            "UK 3 decimal",
            expected,
            validator.validate2(UK_POUND + "1,234.567", locale.UK),
        )
        self.assertEqual(
            "UK no symbol", expected, validator.validate2("1,234.56", locale.UK)
        )

        self.assertEqual(
            "US locale",
            expected,
            validator.validate2(US_DOLLAR + "1,234.56", locale.US),
        )
        self.assertEqual(
            "US negative",
            negative,
            validator.validate2("(" + US_DOLLAR + "1,234.56)", locale.US),
        )
        self.assertEqual(
            "US no decimal",
            noDecimal,
            validator.validate2(US_DOLLAR + "1,234", locale.US),
        )
        self.assertEqual(
            "US 1 decimal",
            oneDecimal,
            validator.validate2(US_DOLLAR + "1,234.5", locale.US),
        )
        self.assertEqual(
            "US 3 decimal",
            expected,
            validator.validate2(US_DOLLAR + "1,234.567", locale.US),
        )
        self.assertEqual(
            "US no symbol", expected, validator.validate2("1,234.56", locale.US)
        )

        locale.setlocale(locale.LC_ALL, origDefault)

    def testFormatType(self) -> None:

        self.assertEqual(
            "Format Type A", 1, CurrencyValidator.getInstance().getFormatType()
        )
        self.assertEqual(
            "Format Type B",
            AbstractNumberValidator.CURRENCY_FORMAT,
            CurrencyValidator.getInstance().getFormatType(),
        )

    def __init__(self, name: str) -> None:

        super().__init__(name)

        import locale
        import decimal

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        self.__US_DOLLAR = decimal.Decimal("1.00").format_money(
            locale.currency(1234567.89)
        )

        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        self.__UK_POUND = decimal.Decimal("1.00").format_money(
            locale.currency(1234567.89)
        )
