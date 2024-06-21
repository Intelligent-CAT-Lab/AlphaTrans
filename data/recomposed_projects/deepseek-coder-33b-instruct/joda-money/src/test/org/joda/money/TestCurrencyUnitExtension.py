from __future__ import annotations
import io
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class TestCurrencyUnitExtension:

    def test_CurrencyEURChanged(self) -> None:

        currency = CurrencyUnit.ofCountry("HU")
        assert currency == CurrencyUnit.EUR
        assert CurrencyUnit.EUR.getCountryCodes().contains("HU")
        assert CurrencyUnit.of1("HUF").getCountryCodes().isEmpty()

    def test_CurrencyMissing(self) -> None:

        for currencyUnit in CurrencyUnit.registeredCurrencies():
            if currencyUnit.getCode() == "NMC":
                self.fail("Currency NMC should not exist")

    def test_InvalidLargerDecimalPrecisionCurrencyFromMoneyDataExtension(self) -> None:

        for currencyUnit in CurrencyUnit.registeredCurrencies():
            if currencyUnit.getCode() == "XXL":
                self.fail("Currency XXL should not exist")

    def test_LargerDecimalPrecisionCurrencyFromMoneyDataExtension(self) -> None:

        curList = CurrencyUnit.registeredCurrencies()
        found = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "ETH":
                found = True
                assert (
                    Money.of2(currencyUnit, 1.23456789).toString()
                    == "ETH 1.234567890000000000000000000000"
                )
                break
        assert found == True

    def test_CurrencyFromMoneyDataExtension(self) -> None:

        curList = CurrencyUnit.registeredCurrencies()
        found = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "BTC":
                found = True
                break

        assert found == True

    def test_CurrencyFromMoneyData(self) -> None:

        curList = CurrencyUnit.registeredCurrencies()
        found = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "GBP":
                found = True
                break

        assert found == True
