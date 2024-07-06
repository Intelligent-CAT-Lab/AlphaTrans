from __future__ import annotations
import locale
import re
import io
import typing
from typing import *
from src.main.org.joda.money.format.MoneyFormatter import *


class MoneyPrintContext:

    def setLocale(self, locale: typing.Any) -> None:
        MoneyFormatter.checkNotNull(locale, "Locale must not be null")
        self.__locale = locale

    def getLocale(self) -> typing.Any:
        return self.__locale

    def __init__(self, locale: typing.Any) -> None:
        self.__locale: typing.Any = None
        MoneyFormatter.checkNotNull(locale, "Locale must not be null")
        self.__locale = locale
