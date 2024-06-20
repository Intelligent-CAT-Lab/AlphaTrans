from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.BigMoney import *
import typing
from typing import *
import io
from io import IOBase

# Imports End


class LiteralPrinterParser(MoneyParser, MoneyPrinter):

    # Class Fields Begin
    __serialVersionUID: int = None
    __literal: str = None
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

    def __init__(self, literal: str) -> None:
        pass

    # Class Methods End
