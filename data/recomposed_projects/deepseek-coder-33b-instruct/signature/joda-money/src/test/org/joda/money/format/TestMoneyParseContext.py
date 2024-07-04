from __future__ import annotations
import re
import os
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

        # Define a context manager to catch the expected exception
        with pytest.raises(IndexError):
            # Call the getTextSubstring method with start and end indices that are out of bounds
            test.getTextSubstring(0, 8)

    def test_getTextSubstring_beforeStart(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, None, None, 0, None)

        # Use a context manager to catch the exception
        with pytest.raises(IndexError):
            test.getTextSubstring(-1, 2)

    def test_getTextSubstring_ok(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual("GB", test.getTextSubstring(0, 2))
        self.assertEqual("23", test.getTextSubstring(5, 7))

    def test_toBigMoney_noAmount(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        # Set the currency
        test.setCurrency(CurrencyUnit.GBP)

        # Expect MoneyFormatException to be raised
        with pytest.raises(MoneyFormatException):
            test.toBigMoney()

    def test_toBigMoney_noCurrency(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        # Set the amount
        test.setAmount(Decimal("10"))

        # Expect a MoneyFormatException to be thrown
        with pytest.raises(MoneyFormatException):
            test.toBigMoney()

    def test_isComplete_noAmount(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setCurrency(CurrencyUnit.GBP)
        self.assertEqual(False, test.isComplete())

    def test_isComplete_noCurrency(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setAmount(Decimal(10))
        self.assertEqual(False, test.isComplete())

    def test_setError_withIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        test.setIndex(2)
        test.setError()
        self.assertEqual(2, test.getIndex())
        self.assertEqual(2, test.getErrorIndex())

    def test_setError(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, None, None, -1, None)
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        test.setError()
        self.assertEqual(0, test.getIndex())
        self.assertEqual(0, test.getErrorIndex())

    def test_setErrorIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual(-1, test.getErrorIndex())
        test.setErrorIndex(3)
        self.assertEqual(3, test.getErrorIndex())

    def test_setIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual(0, test.getIndex())
        test.setIndex(2)
        self.assertEqual(2, test.getIndex())

    def test_initialState(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        self.assertEqual(None, test.getAmount())
        self.assertEqual(None, test.getCurrency())
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("GBP 123", test.getText())
        self.assertEqual(7, test.getTextLength())
        self.assertEqual(False, test.isError())
        self.assertEqual(False, test.isFullyParsed())
        self.assertEqual(False, test.isComplete())

        pp = ParsePosition(0)
        pp.setErrorIndex(-1)
        self.assertEqual(pp, test.toParsePosition())
