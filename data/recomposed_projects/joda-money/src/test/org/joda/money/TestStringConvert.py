# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.convert.StringConvert import *
import unittest

# Imports End


class TestStringConvert(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_CurrencyUnit(self) -> None:

        test = CurrencyUnit.CHF
        str = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str, "CHF")
        self.assertEqual(
            test, StringConvert.INSTANCE.convertFromString(CurrencyUnit, str)
        )

    def test_Money(self) -> None:

        test = Money.of2(CurrencyUnit.CHF, 1234.56)
        str = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str, "CHF 1234.56")
        self.assertEqual(test, StringConvert.INSTANCE.convertFromString(Money, str))

    def test_BigMoney(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
