from __future__ import annotations
import time
import traceback
import locale
import re
import sys
import os
import io
import typing
from typing import *
import decimal
import pickle
# import security error


# from src.main.org.joda.convert.FromString import *
# from src.main.org.joda.convert.ToString import *
from src.main.org.joda.money.CurrencyUnitDataProvider import *
from src.main.org.joda.money.DefaultCurrencyUnitDataProvider import *
from src.main.org.joda.money.IllegalCurrencyException import *
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.Ser import *


class CurrencyUnit:

    CAD: CurrencyUnit = None
    AUD: CurrencyUnit = None
    CHF: CurrencyUnit = None
    GBP: CurrencyUnit = None
    JPY: CurrencyUnit = None
    EUR: CurrencyUnit = None
    USD: CurrencyUnit = None
    __decimalPlaces: int = 0

    __numericCode: int = 0

    __code: str = ""

    __currenciesByCountry: typing.Dict[str, CurrencyUnit] = {}
    __currenciesByNumericCode: typing.Dict[int, CurrencyUnit] = {}
    __currenciesByCode: typing.Dict[str, CurrencyUnit] = {}
    __CODE: re.Pattern = re.compile("[A-Z][A-Z][A-Z]")
    __serialVersionUID: int = 327835287287

    @staticmethod
    def initialize_fields() -> None:
        CurrencyUnit.CAD: CurrencyUnit = CurrencyUnit.of1("CAD")

        CurrencyUnit.AUD: CurrencyUnit = CurrencyUnit.of1("AUD")

        CurrencyUnit.CHF: CurrencyUnit = CurrencyUnit.of1("CHF")

        CurrencyUnit.GBP: CurrencyUnit = CurrencyUnit.of1("GBP")

        CurrencyUnit.JPY: CurrencyUnit = CurrencyUnit.of1("JPY")

        CurrencyUnit.EUR: CurrencyUnit = CurrencyUnit.of1("EUR")

        CurrencyUnit.USD: CurrencyUnit = CurrencyUnit.of1("USD")

    @staticmethod
    def run_static_init():

        # try:
        #     try:
        #         clsName = os.getenv(
        #             "org.joda.money.CurrencyUnitDataProvider",
        #             "org.joda.money.DefaultCurrencyUnitDataProvider",
        #         )
        #         cls = (
        #             CurrencyUnit.__class__.getClassLoader()
        #             .loadClass(clsName)
        #             .asSubclass(CurrencyUnitDataProvider)
        #         )
        #         cls.getDeclaredConstructor().newInstance().registerCurrencies()
        #     except SecurityException as ex:
        #         DefaultCurrencyUnitDataProvider().registerCurrencies()
        # except RuntimeError as ex:
        #     print("ERROR: " + str(ex), file=sys.stderr)
        #     traceback.print_exc()
        #     raise ex
        # except Exception as ex:
        #     print("ERROR: " + str(ex), file=sys.stderr)
        #     traceback.print_exc()
        #     raise RuntimeError(str(ex), ex)

        try:
            cls_name = sys.modules.get('org.joda.money.CurrencyUnitDataProvider', 'org.joda.money.DefaultCurrencyUnitDataProvider')
            cls = getattr(__import__(cls_name, fromlist=['']), cls_name)
            cls().register_currencies()
        except Exception:
            DefaultCurrencyUnitDataProvider()._registerCurrencies()
        except RuntimeError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            raise
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            raise RuntimeError(str(e)) from e

    def toString(self) -> str:
        return self.__code

    def hashCode(self) -> int:
        return hash(self.__code)

    def equals(self, obj: typing.Any) -> bool:
        if obj == self:
            return True
        if isinstance(obj, CurrencyUnit):
            return self.__code == obj.__code
        return False

    def compareTo(self, other: CurrencyUnit) -> int:
        return (self.__code > other.__code) - (self.__code < other.__code)

    @staticmethod
    def of1(currencyCode: str) -> CurrencyUnit:

        MoneyUtils.checkNotNull(currencyCode, "Currency code must not be null")
        currency = CurrencyUnit.__currenciesByCode.get(currencyCode)
        if currency is None:
            raise IllegalCurrencyException("Unknown currency '" + currencyCode + "'")
        return currency

    def toCurrency(self) -> typing.Any:

        # Assuming that the Currency class is available in the same module
        from .Currency import Currency

        return Currency.getInstance(self.__code)

    def getSymbol1(self, locale: typing.Any) -> str:

        MoneyUtils.checkNotNull(locale, "Locale must not be null")
        try:
            return Currency.getInstance(self.__code).getSymbol(locale)
        except ValueError:
            return self.__code

    def getSymbol0(self) -> str:

        try:
            return Currency.getInstance(self.__code).getSymbol()
        except ValueError:
            return self.__code

    def isPseudoCurrency(self) -> bool:
        return self.__decimalPlaces < 0

    def getDecimalPlaces(self) -> int:
        return self.__decimalPlaces if self.__decimalPlaces >= 0 else 0

    def getCountryCodes(self) -> typing.Set[str]:

        countryCodes: typing.Set[str] = set()
        for entry in self.__currenciesByCountry.items():
            if self.equals(entry[1]):
                countryCodes.add(entry[0])
        return countryCodes

    def getNumeric3Code(self) -> str:

        if self.__numericCode < 0:
            return ""

        str_numericCode = str(self.__numericCode)

        if len(str_numericCode) == 1:
            return "00" + str_numericCode

        if len(str_numericCode) == 2:
            return "0" + str_numericCode

        return str_numericCode

    def getNumericCode(self) -> int:
        return self.__numericCode

    def getCode(self) -> str:
        return self.__code

    @staticmethod
    def ofCountry(countryCode: str) -> CurrencyUnit:

        MoneyUtils.checkNotNull(countryCode, "Country code must not be null")
        currency = CurrencyUnit.__currenciesByCountry.get(countryCode)
        if currency is None:
            raise IllegalCurrencyException(
                "No currency found for country '" + countryCode + "'"
            )
        return currency

    @staticmethod
    def of2(locale: typing.Any) -> CurrencyUnit:

        MoneyUtils.checkNotNull(locale, "Locale must not be null")
        currency = CurrencyUnit.__currenciesByCountry.get(locale.getCountry())
        if currency is None:
            raise IllegalCurrencyException(
                "No currency found for locale '" + str(locale) + "'"
            )
        return currency

    @staticmethod
    def ofNumericCode1(numericCurrencyCode: int) -> CurrencyUnit:

        currency = CurrencyUnit.__currenciesByNumericCode.get(numericCurrencyCode)
        if currency is None:
            raise IllegalCurrencyException(
                "Unknown currency '" + str(numericCurrencyCode) + "'"
            )
        return currency

    @staticmethod
    def ofNumericCode0(numericCurrencyCode: str) -> CurrencyUnit:

        MoneyUtils.checkNotNull(numericCurrencyCode, "Currency code must not be null")

        match len(numericCurrencyCode):
            case 1:
                return CurrencyUnit.ofNumericCode1(int(numericCurrencyCode[0]))
            case 2:
                return CurrencyUnit.ofNumericCode1(
                    (int(numericCurrencyCode[0]) * 10) + int(numericCurrencyCode[1])
                )
            case 3:
                return CurrencyUnit.ofNumericCode1(
                    (int(numericCurrencyCode[0]) * 100)
                    + (int(numericCurrencyCode[1]) * 10)
                    + int(numericCurrencyCode[2])
                )
            case _:
                raise IllegalCurrencyException(
                    "Unknown currency '" + numericCurrencyCode + "'"
                )

    @staticmethod
    def of0(currency: typing.Any) -> CurrencyUnit:
        MoneyUtils.checkNotNull(currency, "Currency must not be null")
        return CurrencyUnit.of1(currency.getCurrencyCode())

    @staticmethod
    def registeredCountries() -> typing.List[str]:
        return list(CurrencyUnit.__currenciesByCountry.keys())

    @staticmethod
    def registeredCurrencies() -> typing.List[CurrencyUnit]:
        return list(CurrencyUnit.__currenciesByCode.values())

    @staticmethod
    def registerCountry(countryCode: str, currency: CurrencyUnit) -> None:
        CurrencyUnit.__currenciesByCountry[countryCode] = currency

    @staticmethod
    def registerCurrency2(
        currencyCode: str, numericCurrencyCode: int, decimalPlaces: int, force: bool
    ) -> CurrencyUnit:

        countryCodes = []
        return CurrencyUnit.registerCurrency1(
            currencyCode, numericCurrencyCode, decimalPlaces, countryCodes, force
        )

    @staticmethod
    def registerCurrency1(
        currencyCode: str,
        numericCurrencyCode: int,
        decimalPlaces: int,
        countryCodes: typing.List[str],
        force: bool,
    ) -> CurrencyUnit:

        MoneyUtils.checkNotNull(currencyCode, "Currency code must not be null")
        if len(currencyCode) != 3:
            raise ValueError("Invalid string code, must be length 3")
        if not CurrencyUnit.__CODE.match(currencyCode):
            raise ValueError("Invalid string code, must be ASCII upper-case letters")
        if numericCurrencyCode < -1 or numericCurrencyCode > 999:
            raise ValueError("Invalid numeric code")
        if decimalPlaces < -1 or decimalPlaces > 30:
            raise ValueError("Invalid number of decimal places")
        MoneyUtils.checkNotNull(countryCodes, "Country codes must not be null")

        currency = CurrencyUnit(currencyCode, numericCurrencyCode, decimalPlaces)
        if force:
            CurrencyUnit.__currenciesByCode.pop(currencyCode, None)
            CurrencyUnit.__currenciesByNumericCode.pop(numericCurrencyCode, None)
            for countryCode in countryCodes:
                CurrencyUnit.__currenciesByCountry.pop(countryCode, None)
        else:
            if (
                currencyCode in CurrencyUnit.__currenciesByCode
                or numericCurrencyCode in CurrencyUnit.__currenciesByNumericCode
            ):
                raise ValueError("Currency already registered: " + currencyCode)
            for countryCode in countryCodes:
                if countryCode in CurrencyUnit.__currenciesByCountry:
                    raise ValueError(
                        "Currency already registered for country: " + countryCode
                    )

        CurrencyUnit.__currenciesByCode[currencyCode] = currency
        if numericCurrencyCode >= 0:
            CurrencyUnit.__currenciesByNumericCode[numericCurrencyCode] = currency
        for countryCode in countryCodes:
            CurrencyUnit.registerCountry(countryCode, currency)
        return CurrencyUnit.__currenciesByCode.get(currencyCode)

    @staticmethod
    def registerCurrency0(
        currencyCode: str,
        numericCurrencyCode: int,
        decimalPlaces: int,
        countryCodes: typing.List[str],
    ) -> CurrencyUnit:

        return CurrencyUnit.registerCurrency1(
            currencyCode, numericCurrencyCode, decimalPlaces, countryCodes, False
        )

    def __writeReplace(self) -> typing.Any:
        return Ser(0, self, Ser.CURRENCY_UNIT)

    def __readObject(self, ois: pickle.Unpickler) -> None:
        raise pickle.UnpicklingError("Serialization delegate required")

    def __init__(self, code: str, numericCode: int, decimalPlaces: int) -> None:

        assert code is not None, "Joda-Money bug: Currency code must not be null"
        self.__code = code
        self.__numericCode = numericCode
        self.__decimalPlaces = decimalPlaces


CurrencyUnit.run_static_init()

CurrencyUnit.initialize_fields()

