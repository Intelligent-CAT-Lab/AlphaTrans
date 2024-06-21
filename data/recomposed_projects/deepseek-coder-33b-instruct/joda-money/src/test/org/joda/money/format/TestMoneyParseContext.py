from __future__ import annotations
import io
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.MoneyParseContext import *


class TestMoneyParseContext:

    def test_getTextSubstring_afterEnd(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.getTextSubstring(0, 8)

    def test_getTextSubstring_beforeStart(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        # Call the getTextSubstring method
        test.getTextSubstring(-1, 2)

    def test_getTextSubstring_ok(self) -> None:

        # Create an instance of MoneyParseContext
        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)

        # Test the getTextSubstring method
        assert test.getTextSubstring(0, 2) == "GB"
        assert test.getTextSubstring(5, 7) == "23"

    def test_toBigMoney_noAmount(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setCurrency(CurrencyUnit.GBP)
        test.toBigMoney()

    def test_toBigMoney_noCurrency(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setAmount(BigDecimal.TEN)
        test.toBigMoney()

    def test_isComplete_noAmount(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setCurrency(CurrencyUnit.GBP)
        self.assertEqual(False, test.isComplete())

    def test_isComplete_noCurrency(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setAmount(BigDecimal.TEN)
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

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        test.setError()
        self.assertEqual(0, test.getIndex())
        self.assertEqual(0, test.getErrorIndex())

    def test_setErrorIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        assert -1 == test.getErrorIndex()
        test.setErrorIndex(3)
        assert 3 == test.getErrorIndex()

    def test_setIndex(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        assert 0 == test.getIndex()
        test.setIndex(2)
        assert 2 == test.getIndex()

    def test_initialState(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual(None, test.getAmount())
        self.assertEqual(None, test.getCurrency())
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("GBP 123", test.getText().toString())
        self.assertEqual(7, test.getTextLength())
        self.assertEqual(False, test.isError())
        self.assertEqual(False, test.isFullyParsed())
        self.assertEqual(False, test.isComplete())
        pp = ParsePosition(0)
        pp.setErrorIndex(-1)
        self.assertEqual(pp, test.toParsePosition())
