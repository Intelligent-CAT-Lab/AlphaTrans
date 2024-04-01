# Imports Begin
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoney import *
import unittest

# Imports End


class TestMoneyParseContext(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_getTextSubstring_afterEnd(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.getTextSubstring(0, 8)

    def test_getTextSubstring_beforeStart(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.getTextSubstring(-1, 2)

    def test_getTextSubstring_ok(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        self.assertEqual("GB", test.getTextSubstring(0, 2))
        self.assertEqual("23", test.getTextSubstring(5, 7))

    def test_toBigMoney_noAmount(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setCurrency(CurrencyUnit.GBP)
        test.toBigMoney()

    def test_toBigMoney_noCurrency(self) -> None:

        test = MoneyParseContext(1, "GBP 123", 0, Locale.FRANCE, None, 0, None)
        test.setAmount(decimal.Decimal(10))
        test.toBigMoney()

    def test_isComplete_noAmount(self) -> None:

        pass  # LLM could not translate method body

    def test_isComplete_noCurrency(self) -> None:

        pass  # LLM could not translate method body

    def test_setError_withIndex(self) -> None:

        pass  # LLM could not translate method body

    def test_setError(self) -> None:

        pass  # LLM could not translate method body

    def test_setErrorIndex(self) -> None:

        pass  # LLM could not translate method body

    def test_setIndex(self) -> None:

        pass  # LLM could not translate method body

    def test_initialState(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
