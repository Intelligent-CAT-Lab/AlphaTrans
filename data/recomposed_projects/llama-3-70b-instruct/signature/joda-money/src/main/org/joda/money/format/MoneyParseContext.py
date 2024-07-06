from __future__ import annotations
import locale
import re
import io
import typing
from typing import *
import decimal
import os
import collections
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.MoneyFormatException import *
from src.main.org.joda.money.format.MoneyFormatter import *


class MoneyParseContext:

    def toBigMoney(self) -> BigMoney:
         if self.__currency == None:
             raise MoneyFormatException.MoneyFormatException1(
                 "Cannot convert to BigMoney as no currency found")
         if self.__amount == None:
             raise MoneyFormatException.MoneyFormatException1(
                 "Cannot convert to BigMoney as no amount found")
         return BigMoney.of0(self.__currency, self.__amount)
    def toParsePosition(self) -> collections.namedtuple:
         pp = collections.namedtuple('ParsePosition', ['index', 'errorIndex'])
         pp = pp(self.__textIndex, self.__textErrorIndex)
         return pp
    def isComplete(self) -> bool:
         return self.__currency is not None and self.__amount is not None
    def isFullyParsed(self) -> bool:
         return self.__textIndex == self.getTextLength()
    def isError(self) -> bool:
         return self.__textErrorIndex >= 0
    def setAmount(self, amount: decimal.Decimal) -> None:
         self.__amount = amount
    def getAmount(self) -> decimal.Decimal:
         return self.__amount
    def setCurrency(self, currency: CurrencyUnit) -> None:
         self.__currency = currency
    def getCurrency(self) -> CurrencyUnit:
         return self.__currency
    def setError(self) -> None:
         self.__textErrorIndex = self.__textIndex
    def setErrorIndex(self, index: int) -> None:
         self.__textErrorIndex = index
    def getErrorIndex(self) -> int:
         return self.__textErrorIndex
    def setIndex(self, index: int) -> None:
         self.__textIndex = index
    def getIndex(self) -> int:
         return self.__textIndex
    def getTextSubstring(self, start: int, end: int) -> str:
         return self.__text[start:end]
    def getTextLength(self) -> int:
         return len(self.__text)
    def setText(self, text: str) -> None:
         MoneyFormatter.checkNotNull(text, "Text must not be null")
         self.__text = text
    def getText(self) -> str:
         return self.__text
    def setLocale(self, locale: typing.Any) -> None:
         MoneyFormatter.checkNotNull(locale, "Locale must not be null")
         self.__locale = locale
    def getLocale(self) -> typing.Any:
         return self.__locale

    def __init__(self, constructorId: int, text: str, index: int, locale: typing.Any, amount: decimal.Decimal, errorIndex: int, currency: CurrencyUnit) -> None:

         self.__locale: typing.Any = None
         self.__text: str = ''
         self.__textIndex: int = 0
         self.__textErrorIndex: int = -1
         self.__currency: CurrencyUnit = None
         self.__amount: decimal.Decimal = None
        pass # LLM could not translate this method


    def mergeChild(self, child: MoneyParseContext) -> None:
         self.setLocale(child.getLocale())
         self.setText(child.getText())
         self.setIndex(child.getIndex())
         self.setErrorIndex(child.getErrorIndex())
         self.setCurrency(child.getCurrency())
         self.setAmount(child.getAmount())
    def createChild(self) -> MoneyParseContext:
         return MoneyParseContext(0, self.__text, self.__textIndex, self.__locale, self.__amount, self.__textErrorIndex, self.__currency)
