from __future__ import annotations
import re
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
            matcher = self.__COUNTRY_REGEX_LINE.matcher(line)
            if matcher.matches():
                countryCode = matcher.group(1)
                currencyCode = matcher.group(2)
                self._registerCountry(countryCode, currencyCode)

    def __parseCurrencies(self, content: typing.List[str]) -> None:
        for line in content:
            matcher = self.__CURRENCY_REGEX_LINE.match(line)
            if matcher:
                currencyCode = matcher.group(1)
                numericCode = int(matcher.group(2))
                digits = int(matcher.group(3))
                self._registerCurrency(currencyCode, numericCode, digits)

    def __loadFromFiles(self, fileName: str) -> typing.List[str]:
        content: typing.List[str] = []
        en = self.__class__.get_class_loader().get_resources(fileName)
        while en.has_more_elements():
            url = en.next_element()
            with url.open_stream() as in_:
                with io.BufferedReader(io.InputStreamReader(in_, "UTF-8")) as reader:
                    line: str
                    while (line := reader.read_line()) is not None:
                        content.append(line)
        return content

    def __loadFromFile(self, fileName: str) -> typing.List[str]:
        with io.open(fileName, "r", encoding="UTF-8") as f:
            content = f.readlines()
            return content
