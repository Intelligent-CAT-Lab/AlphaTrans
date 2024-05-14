# Imports Begin
from src.main.org.joda.money.CurrencyUnit import *
from abc import ABC

# Imports End


class CurrencyUnitDataProvider(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _registerCountry(self, countryCode: str, currencyCode: str) -> None:
        pass

    def _registerCurrency(
        self, currencyCode: str, numericCurrencyCode: int, decimalPlaces: int
    ) -> None:
        pass

    def _registerCurrencies(self) -> None:
        pass

    # Class Methods End
