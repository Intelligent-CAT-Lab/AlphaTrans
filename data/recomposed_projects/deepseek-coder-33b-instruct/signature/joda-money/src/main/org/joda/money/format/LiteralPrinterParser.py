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

    __literal: str = ""

    __serialVersionUID: int = 1

    def toString(self) -> str:
        return "'" + self.__literal + "'"

    def parse(self, context: MoneyParseContext) -> None:

        endPos = context.getIndex() + len(self.__literal)

        if (
            endPos <= context.getTextLength()
            and context.getTextSubstring(context.getIndex(), endPos) == self.__literal
        ):
            context.setIndex(endPos)
        else:
            context.setError()

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:

        if isinstance(appendable, list):
            appendable.append(self.__literal)
        elif isinstance(appendable, io.TextIOBase):
            appendable.write(self.__literal)
        else:
            raise TypeError("appendable must be a list or a TextIOBase")

    def __init__(self, literal: str) -> None:
        self.__literal = literal
