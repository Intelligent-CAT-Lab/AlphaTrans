from __future__ import annotations
from io import IOBase
import io
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *


class LiteralPrinterParser(MoneyParser, MoneyPrinter):

    __literal: str = None

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
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:

        appendable.write(self.__literal)

    def __init__(self, literal: str) -> None:

        self.__literal = literal
