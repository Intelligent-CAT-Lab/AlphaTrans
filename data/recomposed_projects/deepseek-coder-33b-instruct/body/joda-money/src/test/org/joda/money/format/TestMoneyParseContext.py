from __future__ import annotations
import re
import collections
import os
import decimal
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.MoneyParseContext import *


class TestMoneyParseContext(unittest.TestCase):

    def test_getTextSubstring_afterEnd(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)

        # Assert that IndexOutOfBoundsException is raised when getTextSubstring is called with start and end indices that are out of bounds
        with self.assertRaises(IndexError):
            test.getTextSubstring(0, 8)

    def test_getTextSubstring_beforeStart(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)

        # Check if IndexOutOfBoundsException is raised when calling getTextSubstring with negative start index
        with self.assertRaises(IndexError):
            test.getTextSubstring(-1, 2)

    def test_getTextSubstring_ok(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)

        # Assert that the substring from index 0 to 2 is "GB"
        self.assertEqual(test.getTextSubstring(0, 2), "GB")

        # Assert that the substring from index 5 to 7 is "23"
        self.assertEqual(test.getTextSubstring(5, 7), "23")

    def test_toBigMoney_noAmount(self) -> None:

        # Create an instance of MoneyParseContext with no amount
        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        # Set the currency
        test.setCurrency(CurrencyUnit.GBP)

        # Expect MoneyFormatException to be raised when calling toBigMoney
        with pytest.raises(MoneyFormatException.MoneyFormatException1):
            test.toBigMoney()

    def test_toBigMoney_noCurrency(self) -> None:

        # Create an instance of MoneyParseContext with no currency
        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        # Set the amount
        test.setAmount(Decimal("10"))

        # Check that a MoneyFormatException is raised when calling toBigMoney
        with pytest.raises(MoneyFormatException.MoneyFormatException1):
            test.toBigMoney()

    def test_isComplete_noAmount(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)
        test.setCurrency(CurrencyUnit.GBP)
        self.assertEqual(False, test.isComplete())

    def test_isComplete_noCurrency(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)

        # Set the amount
        test.setAmount(decimal.Decimal(10))

        # Assert that isComplete returns False
        self.assertEqual(False, test.isComplete())

    def test_setError_withIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        test.setIndex(2)
        test.setError()
        self.assertEqual(2, test.getIndex())
        self.assertEqual(2, test.getErrorIndex())

    def test_setError(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        test.setError()
        self.assertEqual(0, test.getIndex())
        self.assertEqual(0, test.getErrorIndex())

    def test_setErrorIndex(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)

        # Assert that the error index is -1
        self.assertEqual(-1, test.getErrorIndex())

        # Set the error index to 3
        test.setErrorIndex(3)

        # Assert that the error index is now 3
        self.assertEqual(3, test.getErrorIndex())

    def test_setIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)
        self.assertEqual(0, test.getIndex())
        test.setIndex(2)
        self.assertEqual(2, test.getIndex())

    def test_initialState(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, None, None, -1, None)
        self.assertIsNone(test.getAmount())
        self.assertIsNone(test.getCurrency())
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("GBP 123", test.getText())
        self.assertEqual(7, test.getTextLength())
        self.assertFalse(test.isError())
        self.assertFalse(test.isFullyParsed())
        self.assertFalse(test.isComplete())
        pp = collections.namedtuple("ParsePosition", ["textIndex", "textErrorIndex"])
        pp = pp(0, -1)
        self.assertEqual(pp, test.toParsePosition())
