from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MultiPrinterParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.BigMoney import *
import os
import io
from io import IOBase

# Imports End


class SignedPrinterParser(MoneyParser, MoneyPrinter):

    # Class Fields Begin
    __serialVersionUID: int = None
    __whenPositive: MoneyFormatter = None
    __whenZero: MoneyFormatter = None
    __whenNegative: MoneyFormatter = None
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

    def __init__(
        self,
        whenPositive: MoneyFormatter,
        whenZero: MoneyFormatter,
        whenNegative: MoneyFormatter,
    ) -> None:
        pass

    # Class Methods End
