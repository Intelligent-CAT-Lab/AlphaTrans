from __future__ import annotations
from abc import ABC
from io import IOBase
import io
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.MoneyPrintContext import *


class MoneyPrinter(ABC):

    def print(
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:

        pass
