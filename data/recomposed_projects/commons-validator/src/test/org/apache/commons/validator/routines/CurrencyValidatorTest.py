# Imports Begin
from src.main.org.apache.commons.validator.routines.CurrencyValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import unittest
import os
import typing
from typing import *

# Imports End


class CurrencyValidatorTest(unittest.TestCase, TestCase):

    # Class Fields Begin
    __CURRENCY_SYMBOL: str = "\u00A4"
    __US_DOLLAR: str = None
    __UK_POUND: str = None
    # Class Fields End

    # Class Methods Begin
    def _tearDown(self) -> None:

        pass  # LLM could not translate method body

    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testPattern(self) -> None:

        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()
        basic_pattern = CURRENCY_SYMBOL + "#,##0.000"
        pattern = basic_pattern + ";[" + basic_pattern + "]"
        expected = decimal.Decimal("1234.567")
        negative = decimal.Decimal("-1234.567")
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
        Locale.setDefault(orig_default)

    def testIntegerInvalid(self) -> None:

        validator = CurrencyValidator(strict=True, allowFractions=False)
        self.assertFalse(
            "UK positive",
            validator.isValid2(f"{self.__UK_POUND}1,234.56", locale=Locale.UK),
        )
        self.assertFalse(
            "UK negative",
            validator.isValid2(f"-{self.__UK_POUND}1,234.56", locale=Locale.UK),
        )
        self.assertFalse(
            "US positive",
            validator.isValid2(f"{self.__US_DOLLAR}1,234.56", locale=Locale.US),
        )
        self.assertFalse(
            "US negative",
            validator.isValid2(f"({self.__US_DOLLAR}1,234.56)", locale=Locale.US),
        )

    def testIntegerValid(self) -> None:

        pass  # LLM could not translate method body

    def testInvalid(self) -> None:

        pass  # LLM could not translate method body

    def testValid(self) -> None:

        pass  # LLM could not translate method body

    def testFormatType(self) -> None:

        pass  # LLM could not translate method body

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
