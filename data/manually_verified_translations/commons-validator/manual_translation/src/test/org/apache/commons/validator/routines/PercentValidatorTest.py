from __future__ import annotations
import locale
import re
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
from src.main.org.apache.commons.validator.routines.PercentValidator import *


class PercentValidatorTest(unittest.TestCase):

    _validator: PercentValidator = None

    def tearDown(self) -> None:
        self._validator = None

    def setUp(self) -> None:
        self._validator = PercentValidator.PercentValidator1()

    def testInvalid(self) -> None:

        validator = PercentValidator.getInstance()

        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")

        self.assertFalse(validator.isValid2("12@", "en_GB.UTF-8"), "UK wrong symbol")
        self.assertFalse(validator.isValid2("(12%)", "en_GB.UTF-8"), "UK wrong negative")

        self.assertFalse(validator.isValid2("12@", "en_US.UTF-8"), "US wrong symbol")
        self.assertFalse(validator.isValid2("(12%)", "en_US.UTF-8"), "US wrong negative")

    def testValid(self) -> None:

        origDefault = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")

        validator = PercentValidator.getInstance()
        expected = decimal.Decimal("0.12")
        negative = decimal.Decimal("-0.12")
        hundred = decimal.Decimal("1.00")

        self.assertEqual(expected, validator.validate0("12%"), "Default locale")
        self.assertEqual(negative, validator.validate0("-12%"), "Default negative")

        self.assertEqual(expected, validator.validate2("12%", "en_GB.UTF-8"), "UK locale")
        self.assertEqual(
            negative, validator.validate2("-12%", "en_GB.UTF-8"), "UK negative"
        )
        self.assertEqual(expected, validator.validate2("12", "en_GB.UTF-8"), "UK No symbol")

        self.assertEqual(expected, validator.validate2("12%", "en_US.UTF-8"), "US locale")
        self.assertEqual(
            negative, validator.validate2("-12%", "en_US.UTF-8"), "US negative"
        )
        self.assertEqual(expected, validator.validate2("12", "en_US.UTF-8"), "US No symbol")

        self.assertEqual(hundred, validator.validate0("100%"), "100%")

        locale.setlocale(locale.LC_ALL, origDefault)

    def testFormatType(self) -> None:
        self.assertEqual(
            2, PercentValidator.getInstance().getFormatType(), "Format Type A"
        )
        self.assertEqual(
            AbstractNumberValidator.PERCENT_FORMAT,
            PercentValidator.getInstance().getFormatType(),
            "Format Type B"
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
