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
        super().tearDown()
        self._validator = None

    def setUp(self) -> None:
        super().setUp()
        self._validator = PercentValidator.PercentValidator1()

    def testInvalid(self) -> None:
        validator: BigDecimalValidator = PercentValidator.getInstance()

        self.assertFalse("isValid() Null Value", validator.isValid0(None))
        self.assertFalse("isValid() Empty Value", validator.isValid0(""))
        self.assertIsNone("validate() Null Value", validator.validate0(None))
        self.assertIsNone("validate() Empty Value", validator.validate0(""))

        self.assertFalse("UK wrong symbol", validator.isValid2("12@", Locale.UK))  # ???
        self.assertFalse("UK wrong negative", validator.isValid2("(12%)", Locale.UK))

        self.assertFalse("US wrong symbol", validator.isValid2("12@", Locale.US))  # ???
        self.assertFalse("US wrong negative", validator.isValid2("(12%)", Locale.US))

    def testValid(self) -> None:
        origDefault: Locale = Locale.getDefault()
        Locale.setDefault(Locale.UK)

        validator: BigDecimalValidator = PercentValidator.getInstance()
        expected: decimal.Decimal = decimal.Decimal("0.12")
        negative: decimal.Decimal = decimal.Decimal("-0.12")
        hundred: decimal.Decimal = decimal.Decimal("1.00")

        self.assertEqual("Default locale", expected, validator.validate0("12%"))
        self.assertEqual("Default negtve", negative, validator.validate0("-12%"))

        self.assertEqual("UK locale", expected, validator.validate2("12%", Locale.UK))
        self.assertEqual(
            "UK negative", negative, validator.validate2("-12%", Locale.UK)
        )
        self.assertEqual("UK No symbol", expected, validator.validate2("12", Locale.UK))

        self.assertEqual("US locale", expected, validator.validate2("12%", Locale.US))
        self.assertEqual(
            "US negative", negative, validator.validate2("-12%", Locale.US)
        )
        self.assertEqual("US No symbol", expected, validator.validate2("12", Locale.US))

        self.assertEqual("100%", hundred, validator.validate0("100%"))

        Locale.setDefault(origDefault)

    def testFormatType(self) -> None:
        self.assertEqual(
            "Format Type A", 2, PercentValidator.getInstance().getFormatType()
        )
        self.assertEqual(
            "Format Type B",
            AbstractNumberValidator.PERCENT_FORMAT,
            PercentValidator.getInstance().getFormatType(),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
