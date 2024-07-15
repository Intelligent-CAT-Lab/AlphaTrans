from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class TestCurrencyUnitExtension(unittest.TestCase):

    def test_CurrencyEURChanged(self) -> None:
        currency: CurrencyUnit = CurrencyUnit.ofCountry("HU")
        self.assertEqual(CurrencyUnit.EUR, currency)
        self.assertEqual(True, CurrencyUnit.EUR.getCountryCodes().contains("HU"))
        self.assertEqual(True, CurrencyUnit.of1("HUF").getCountryCodes().isEmpty())

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
                self.assertEqual(
                    "ETH 1.234567890000000000000000000000",
                    Money.of2(currencyUnit, 1.23456789).toString(),
                )
                break
        self.assertEqual(True, found)

    def test_CurrencyFromMoneyDataExtension(self) -> None:
        curList = CurrencyUnit.registeredCurrencies()
        found = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "BTC":
                found = True
                break
        self.assertEqual(True, found)

    def test_CurrencyFromMoneyData(self) -> None:
        curList = CurrencyUnit.registeredCurrencies()
        found = False
        for currencyUnit in curList:
            if currencyUnit.getCode() == "GBP":
                found = True
                break
        self.assertEqual(True, found)
