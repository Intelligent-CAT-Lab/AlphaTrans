from __future__ import annotations
import re
from abc import ABC
from io import IOBase
import io
import typing
from typing import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.MoneyPrintContext import *


class MoneyPrinter(ABC):

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:
        appendable.append(money.toString())
