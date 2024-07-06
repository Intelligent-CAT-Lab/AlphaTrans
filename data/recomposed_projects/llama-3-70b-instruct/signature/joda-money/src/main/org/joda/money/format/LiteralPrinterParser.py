from __future__ import annotations
import re
import os
from io import IOBase
import io
import typing
from typing import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *


class LiteralPrinterParser(MoneyParser, MoneyPrinter):

    __serialVersionUID: int = 1

    def toString(self) -> str:
        return "'" + self.__literal + "'"

    def parse(self, context: MoneyParseContext) -> None:
        end_pos = context.getIndex() + len(self.__literal)
        if (
            end_pos <= context.getTextLength()
            and context.getTextSubstring(context.getIndex(), end_pos) == self.__literal
        ):
            context.setIndex(end_pos)
        else:
            context.setError()

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:
        appendable.append(self.__literal)

    def __init__(self, literal: str) -> None:
        self.__literal: str = ""
        self.__literal = literal
