from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.GroupingStyle import *
from src.main.org.joda.money.BigMoney import *
import os
import io
from io import IOBase

# Imports End


class AmountPrinterParser(MoneyParser, MoneyPrinter):

    # Class Fields Begin
    __serialVersionUID: int = None
    __style: MoneyAmountStyle = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def parse(self, context: MoneyParseContext) -> None:
        pass

    def print(
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:
        pass

    def __isPostGroupingPoint(
        self, i: int, post: int, groupingSize: int, extendedGroupingSize: int
    ) -> bool:
        pass

    def __isPreGroupingPoint(
        self, remaining: int, groupingSize: int, extendedGroupingSize: int
    ) -> bool:
        pass

    def __init__(self, style: MoneyAmountStyle) -> None:
        pass

    # Class Methods End
