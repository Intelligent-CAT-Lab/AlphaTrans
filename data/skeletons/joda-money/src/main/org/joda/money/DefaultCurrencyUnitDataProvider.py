# Imports Begin
from src.main.org.joda.money.CurrencyUnitDataProvider import *
import typing

# Imports End


class DefaultCurrencyUnitDataProvider(CurrencyUnitDataProvider):

    # Class Fields Begin
    __CURRENCY_REGEX_LINE: re.Pattern = None
    __COUNTRY_REGEX_LINE: re.Pattern = None
    # Class Fields End

    # Class Methods Begin
    def _registerCurrencies(self) -> None:
        pass

    def __parseCountries(self, content: typing.List[str]) -> None:
        pass

    def __parseCurrencies(self, content: typing.List[str]) -> None:
        pass

    def __loadFromFiles(self, fileName: str) -> typing.List[str]:
        pass

    def __loadFromFile(self, fileName: str) -> typing.List[str]:
        pass

    # Class Methods End
