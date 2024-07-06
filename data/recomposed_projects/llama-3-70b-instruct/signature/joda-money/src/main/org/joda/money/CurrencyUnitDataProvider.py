from __future__ import annotations
import re
from abc import ABC
import io
import decimal
from src.main.org.joda.money.CurrencyUnit import *


class CurrencyUnitDataProvider(ABC):

    def _registerCountry(self, countryCode: str, currencyCode: str) -> None:
        CurrencyUnit.registerCountry(countryCode, CurrencyUnit.of1(currencyCode))

    def _registerCurrency(
        self, currencyCode: str, numericCurrencyCode: int, decimalPlaces: int
    ) -> None:
        CurrencyUnit.registerCurrency2(
            currencyCode, numericCurrencyCode, decimalPlaces, True
        )

    def _registerCurrencies(self) -> None:
        pass
