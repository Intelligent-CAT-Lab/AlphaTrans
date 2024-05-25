from __future__ import annotations

# Imports Begin
# from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatException import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoney import *
import collections
import os
import decimal
import typing
from typing import *
import io

# Imports End


class MoneyParseContext:

    # Class Fields Begin
    __locale: typing.Any = None
    __text: str = None
    __textIndex: int = None
    __textErrorIndex: int = None
    __currency: CurrencyUnit = None
    __amount: decimal.Decimal = None
    # Class Fields End

    # Class Methods Begin
    def toBigMoney(self) -> BigMoney:
        pass

    def toParsePosition(self) -> collections.namedtuple:
        pass

    def isComplete(self) -> bool:
        pass

    def isFullyParsed(self) -> bool:
        pass

    def isError(self) -> bool:
        pass

    def setAmount(self, amount: decimal.Decimal) -> None:
        pass

    def getAmount(self) -> decimal.Decimal:
        pass

    def setCurrency(self, currency: CurrencyUnit) -> None:
        pass

    def getCurrency(self) -> CurrencyUnit:
        pass

    def setError(self) -> None:
        pass

    def setErrorIndex(self, index: int) -> None:
        pass

    def getErrorIndex(self) -> int:
        pass

    def setIndex(self, index: int) -> None:
        pass

    def getIndex(self) -> int:
        pass

    def getTextSubstring(self, start: int, end: int) -> str:
        pass

    def getTextLength(self) -> int:
        pass

    def setText(self, text: str) -> None:
        pass

    def getText(self) -> str:
        pass

    def setLocale(self, locale: typing.Any) -> None:
        pass

    def getLocale(self) -> typing.Any:
        pass

    def __init__(
        self,
        constructorId: int,
        text: str,
        index: int,
        locale: typing.Any,
        amount: decimal.Decimal,
        errorIndex: int,
        currency: CurrencyUnit,
    ) -> None:
        pass

    def mergeChild(self, child: MoneyParseContext) -> None:
        pass

    def createChild(self) -> MoneyParseContext:
        pass

    # Class Methods End
