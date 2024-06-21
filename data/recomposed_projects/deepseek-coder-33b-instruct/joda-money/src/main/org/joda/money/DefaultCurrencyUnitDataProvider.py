from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.money.CurrencyUnitDataProvider import *


class DefaultCurrencyUnitDataProvider(CurrencyUnitDataProvider):

    __COUNTRY_REGEX_LINE: re.Pattern = re.compile("([A-Z]{2}),([A-Z]{3}) *(#.*)?")

    __CURRENCY_REGEX_LINE: re.Pattern = re.compile(
        "([A-Z]{3}),(-1|[0-9]{1,3}),(-1|[0-9]|[1-2][0-9]|30) *(#.*)?"
    )

    def _registerCurrencies(self) -> None:

        self.__parseCurrencies(self.__loadFromFile("/org/joda/money/CurrencyData.csv"))
        self.__parseCountries(self.__loadFromFile("/org/joda/money/CountryData.csv"))
        self.__parseCurrencies(
            self.__loadFromFiles("META-INF/org/joda/money/CurrencyDataExtension.csv")
        )
        self.__parseCountries(
            self.__loadFromFiles("META-INF/org/joda/money/CountryDataExtension.csv")
        )

    def __parseCountries(self, content: typing.List[str]) -> None:

        for line in content:
            matcher = self.__COUNTRY_REGEX_LINE.match(line)
            if matcher:
                countryCode = matcher.group(1)
                currencyCode = matcher.group(2)
                self.registerCountry(countryCode, currencyCode)

    def __parseCurrencies(self, content: typing.List[str]) -> None:

        for line in content:
            matcher = self.__CURRENCY_REGEX_LINE.match(line)
            if matcher:
                currencyCode = matcher.group(1)
                numericCode = int(matcher.group(2))
                digits = int(matcher.group(3))
                self.registerCurrency(currencyCode, numericCode, digits)

    def __loadFromFiles(self, fileName: str) -> typing.List[str]:

        content = []
        en = self.__class__.__class__.getClassLoader().getResources(fileName)
        while en.hasMoreElements():
            url = en.nextElement()
            with io.open(url.openStream(), "r", encoding="utf-8") as reader:
                for line in reader:
                    content.append(line)
        return content

    def __loadFromFile(self, fileName: str) -> typing.List[str]:

        try:
            with open(fileName, "r", encoding="utf-8") as reader:
                content = []
                for line in reader:
                    content.append(line)
                return content
        except FileNotFoundError:
            raise Exception("Data file " + fileName + " not found")
