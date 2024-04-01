# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
import unittest

# Imports End


class TestCurrencyUnitExtension(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_CurrencyEURChanged(self) -> None:

        pass  # LLM could not translate method body

    def test_CurrencyMissing(self) -> None:

        for currency_unit in CurrencyUnit.registered_currencies():
            if currency_unit.get_code() == "NMC":
                self.fail("Currency NMC should not exist")

    def test_InvalidLargerDecimalPrecisionCurrencyFromMoneyDataExtension(self) -> None:

        for currency_unit in CurrencyUnit.registered_currencies():
            if currency_unit.get_code() == "XXL":
                self.fail("Currency XXL should not exist")

    def test_LargerDecimalPrecisionCurrencyFromMoneyDataExtension(self) -> None:

        cur_list = CurrencyUnit.registered_currencies()
        found = False
        for currency in cur_list:
            if currency.get_code() == "ETH":
                found = True
                self.assertEqual(
                    "ETH 1.234567890000000000000000000000",
                    Money.of2(currency, 1.23456789).to_string(),
                )
                break
        self.assertEqual(True, found)

    def test_CurrencyFromMoneyDataExtension(self) -> None:

        pass  # LLM could not translate method body

    def test_CurrencyFromMoneyData(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
