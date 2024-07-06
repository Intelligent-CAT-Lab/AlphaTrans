from __future__ import annotations
import locale
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

    def _tearDown(self) -> None:
        super().tearDown()

    def _setUp(self) -> None:
        self.__US_DOLLAR = (DecimalFormatSymbols(Locale.US)).getCurrencySymbol()
        self.__UK_POUND = (DecimalFormatSymbols(Locale.UK)).getCurrencySymbol()

    def testPattern(self) -> None:
        origDefault: Locale = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        validator: BigDecimalValidator = CurrencyValidator.getInstance()
        basicPattern: str = CURRENCY_SYMBOL + "#,##0.000"
        pattern: str = basicPattern + ";[" + basicPattern + "]"
        expected: BigDecimal = BigDecimal("1234.567")
        negative: BigDecimal = BigDecimal("-1234.567")

        self.assertEqual(
            "default", expected, validator.validate1(UK_POUND + "1,234.567", pattern)
        )
        self.assertEqual(
            "negative",
            negative,
            validator.validate1("[" + UK_POUND + "1,234.567]", pattern),
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
            validator.validate3(US_DOLLAR + "1,234.567", pattern, Locale.US),
        )
        self.assertEqual(
            "negative",
            negative,
            validator.validate3("[" + US_DOLLAR + "1,234.567]", pattern, Locale.US),
        )
        self.assertEqual(
            "no symbol +ve",
            expected,
            validator.validate3("1,234.567", pattern, Locale.US),
        )
        self.assertEqual(
            "no symbol -ve",
            negative,
            validator.validate3("[1,234.567]", pattern, Locale.US),
        )

        self.assertFalse(
            "invalid symbol", validator.isValid1(US_DOLLAR + "1,234.567", pattern)
        )
        self.assertFalse(
            "invalid symbol",
            validator.isValid3(UK_POUND + "1,234.567", pattern, Locale.US),
        )

        Locale.setDefault(origDefault)

    def testIntegerInvalid(self) -> None:
        validator = CurrencyValidator(True, False)

        self.assertFalse(
            "UK positive", validator.isValid2(UK_POUND + "1,234.56", Locale.UK)
        )
        self.assertFalse(
            "UK negative", validator.isValid2("-" + UK_POUND + "1,234.56", Locale.UK)
        )

        self.assertFalse(
            "US positive", validator.isValid2(US_DOLLAR + "1,234.56", Locale.US)
        )
        self.assertFalse(
            "US negative", validator.isValid2("(" + US_DOLLAR + "1,234.56)", Locale.US)
        )

    def testIntegerValid(self) -> None:
        origDefault = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        validator = CurrencyValidator.CurrencyValidator1()
        expected = BigDecimal("1234.00")
        negative = BigDecimal("-1234.00")

        self.assertEqual(
            "Default locale", expected, validator.validate0(UK_POUND + "1,234")
        )

        self.assertEqual(
            "UK locale", expected, validator.validate2(UK_POUND + "1,234", Locale.UK)
        )
        self.assertEqual(
            "UK negative",
            negative,
            validator.validate2("-" + UK_POUND + "1,234", Locale.UK),
        )

        self.assertEqual(
            "US locale", expected, validator.validate2(US_DOLLAR + "1,234", Locale.US)
        )
        self.assertEqual(
            "US negative",
            negative,
            validator.validate2("(" + US_DOLLAR + "1,234)", Locale.US),
        )

        Locale.setDefault(origDefault)

    def testInvalid(self) -> None:
        validator = CurrencyValidator.getInstance()

        self.assertFalse("isValid() Null Value", validator.isValid0(None))
        self.assertFalse("isValid() Empty Value", validator.isValid0(""))
        self.assertIsNone("validate() Null Value", validator.validate0(None))
        self.assertIsNone("validate() Empty Value", validator.validate0(""))

        self.assertFalse(
            "UK wrong symbol", validator.isValid2(US_DOLLAR + "1,234.56", Locale.UK)
        )
        self.assertFalse(
            "UK wrong negative",
            validator.isValid2("(" + UK_POUND + "1,234.56)", Locale.UK),
        )

        self.assertFalse(
            "US wrong symbol", validator.isValid2(UK_POUND + "1,234.56", Locale.US)
        )
        self.assertFalse(
            "US wrong negative",
            validator.isValid2("-" + US_DOLLAR + "1,234.56", Locale.US),
        )

    def testValid(self) -> None:
        origDefault: Locale = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        validator: BigDecimalValidator = CurrencyValidator.getInstance()
        expected: BigDecimal = BigDecimal("1234.56")
        negative: BigDecimal = BigDecimal("-1234.56")
        noDecimal: BigDecimal = BigDecimal("1234.00")
        oneDecimal: BigDecimal = BigDecimal("1234.50")

        self.assertEqual(
            "Default locale", expected, validator.validate0(UK_POUND + "1,234.56")
        )

        self.assertEqual(
            "UK locale", expected, validator.validate2(UK_POUND + "1,234.56", Locale.UK)
        )
        self.assertEqual(
            "UK negative",
            negative,
            validator.validate2("-" + UK_POUND + "1,234.56", Locale.UK),
        )
        self.assertEqual(
            "UK no decimal",
            noDecimal,
            validator.validate2(UK_POUND + "1,234", Locale.UK),
        )
        self.assertEqual(
            "UK 1 decimal",
            oneDecimal,
            validator.validate2(UK_POUND + "1,234.5", Locale.UK),
        )
        self.assertEqual(
            "UK 3 decimal",
            expected,
            validator.validate2(UK_POUND + "1,234.567", Locale.UK),
        )
        self.assertEqual(
            "UK no symbol", expected, validator.validate2("1,234.56", Locale.UK)
        )

        self.assertEqual(
            "US locale",
            expected,
            validator.validate2(US_DOLLAR + "1,234.56", Locale.US),
        )
        self.assertEqual(
            "US negative",
            negative,
            validator.validate2("(" + US_DOLLAR + "1,234.56)", Locale.US),
        )
        self.assertEqual(
            "US no decimal",
            noDecimal,
            validator.validate2(US_DOLLAR + "1,234", Locale.US),
        )
        self.assertEqual(
            "US 1 decimal",
            oneDecimal,
            validator.validate2(US_DOLLAR + "1,234.5", Locale.US),
        )
        self.assertEqual(
            "US 3 decimal",
            expected,
            validator.validate2(US_DOLLAR + "1,234.567", Locale.US),
        )
        self.assertEqual(
            "US no symbol", expected, validator.validate2("1,234.56", Locale.US)
        )

        Locale.setDefault(origDefault)

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
