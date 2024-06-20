from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MultiPrinterParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyFormatException import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import typing
from typing import *
import io
from io import IOBase

# Imports End


class MoneyFormatter:

    # Class Fields Begin
    __serialVersionUID: int = None
    __locale: typing.Any = None
    __printerParser: MultiPrinterParser = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def parse(self, text: str, startIndex: int) -> MoneyParseContext:
        pass

    def parseMoney(self, text: str) -> Money:
        pass

    def parseBigMoney(self, text: str) -> BigMoney:
        pass

    def printIO(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        moneyProvider: BigMoneyProvider,
    ) -> None:
        pass

    def print1(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        moneyProvider: BigMoneyProvider,
    ) -> None:
        pass

    def print0(self, moneyProvider: BigMoneyProvider) -> str:
        pass

    def isParser(self) -> bool:
        pass

    def isPrinter(self) -> bool:
        pass

    def withLocale(self, locale: typing.Any) -> MoneyFormatter:
        pass

    def getLocale(self) -> typing.Any:
        pass

    def __init__(
        self,
        constructorId: int,
        locale: typing.Any,
        parsers: typing.List[MoneyParser],
        printers: typing.List[MoneyPrinter],
        printerParser: MultiPrinterParser,
    ) -> None:
        pass

    @staticmethod
    def checkNotNull(object: typing.Any, message: str) -> None:
        pass

    def getPrinterParser(self) -> MultiPrinterParser:
        pass

    # Class Methods End
