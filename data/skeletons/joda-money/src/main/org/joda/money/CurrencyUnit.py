from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.Ser import *
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.IllegalCurrencyException import *
from src.main.org.joda.money.DefaultCurrencyUnitDataProvider import *
from src.main.org.joda.money.CurrencyUnitDataProvider import *
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import pickle
import typing
from typing import *
import io

# Imports End


class CurrencyUnit:

    # Class Fields Begin
    EUR: CurrencyUnit = None
    JPY: CurrencyUnit = None
    GBP: CurrencyUnit = None
    CHF: CurrencyUnit = None
    AUD: CurrencyUnit = None
    CAD: CurrencyUnit = None
    __code: str = None
    __numericCode: int = None
    __decimalPlaces: int = None
    __serialVersionUID: int = None
    __CODE: re.Pattern = None
    __currenciesByCode: typing.Dict[str, CurrencyUnit] = None
    __currenciesByNumericCode: typing.Dict[int, CurrencyUnit] = None
    __currenciesByCountry: typing.Dict[str, CurrencyUnit] = None
    USD: CurrencyUnit = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def compareTo(self, other: CurrencyUnit) -> int:
        pass

    @staticmethod
    def of1(currencyCode: str) -> CurrencyUnit:
        pass

    def toCurrency(self) -> typing.Any:
        pass

    def getSymbol1(self, locale: typing.Any) -> str:
        pass

    def getSymbol0(self) -> str:
        pass

    def isPseudoCurrency(self) -> bool:
        pass

    def getDecimalPlaces(self) -> int:
        pass

    def getCountryCodes(self) -> typing.Set[str]:
        pass

    def getNumeric3Code(self) -> str:
        pass

    def getNumericCode(self) -> int:
        pass

    def getCode(self) -> str:
        pass

    @staticmethod
    def ofCountry(countryCode: str) -> CurrencyUnit:
        pass

    @staticmethod
    def of2(locale: typing.Any) -> CurrencyUnit:
        pass

    @staticmethod
    def ofNumericCode1(numericCurrencyCode: int) -> CurrencyUnit:
        pass

    @staticmethod
    def ofNumericCode0(numericCurrencyCode: str) -> CurrencyUnit:
        pass

    @staticmethod
    def of0(currency: typing.Any) -> CurrencyUnit:
        pass

    @staticmethod
    def registeredCountries() -> typing.List[str]:
        pass

    @staticmethod
    def registeredCurrencies() -> typing.List[CurrencyUnit]:
        pass

    @staticmethod
    def registerCountry(countryCode: str, currency: CurrencyUnit) -> None:
        pass

    @staticmethod
    def registerCurrency2(
        currencyCode: str, numericCurrencyCode: int, decimalPlaces: int, force: bool
    ) -> CurrencyUnit:
        pass

    @staticmethod
    def registerCurrency1(
        currencyCode: str,
        numericCurrencyCode: int,
        decimalPlaces: int,
        countryCodes: typing.List[str],
        force: bool,
    ) -> CurrencyUnit:
        pass

    @staticmethod
    def registerCurrency0(
        currencyCode: str,
        numericCurrencyCode: int,
        decimalPlaces: int,
        countryCodes: typing.List[str],
    ) -> CurrencyUnit:
        pass

    def __writeReplace(self) -> typing.Any:
        pass

    def __readObject(self, ois: pickle.Unpickler) -> None:
        pass

    def __init__(self, code: str, numericCode: int, decimalPlaces: int) -> None:
        pass

    # Class Methods End
