from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.BigMoney import *
import typing
from typing import *
import io
from io import IOBase

# Imports End


class MultiPrinterParser(MoneyParser, MoneyPrinter):

    # Class Fields Begin
    __serialVersionUID: int = None
    __printers: typing.List[MoneyPrinter] = None
    __parsers: typing.List[MoneyParser] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def parse(self, context: MoneyParseContext) -> None:
        pass

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:
        pass

    def appendTo(self, builder: MoneyFormatterBuilder) -> None:
        pass

    def isParser(self) -> bool:
        pass

    def isPrinter(self) -> bool:
        pass

    def __init__(
        self, printers: typing.List[MoneyPrinter], parsers: typing.List[MoneyParser]
    ) -> None:
        pass

    # Class Methods End
