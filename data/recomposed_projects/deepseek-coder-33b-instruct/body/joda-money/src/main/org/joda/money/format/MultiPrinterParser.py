from __future__ import annotations
import re
from io import StringIO
from io import IOBase
import io
import typing
from typing import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *


class MultiPrinterParser(MoneyParser, MoneyPrinter):

    __parsers: typing.List[MoneyParser] = None

    __printers: typing.List[MoneyPrinter] = None

    __serialVersionUID: int = 1

    def toString(self) -> str:

        buf1 = ""
        if self.isPrinter():
            for printer in self.__printers:
                buf1 += printer.__str__()

        buf2 = ""
        if self.isParser():
            for parser in self.__parsers:
                buf2 += parser.__str__()

        if self.isPrinter() and not self.isParser():
            return buf1
        elif self.isParser() and not self.isPrinter():
            return buf2
        elif buf1 == buf2:
            return buf1
        else:
            return buf1 + ":" + buf2

    def parse(self, context: MoneyParseContext) -> None:
        for parser in self.__parsers:
            parser.parse(context)
            if context.isError():
                break

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:

        if isinstance(appendable, list):
            appendable = io.StringIO()

        for printer in self.__printers:
            printer.print(context, appendable, money)

    def appendTo(self, builder: MoneyFormatterBuilder) -> None:

        for i in range(len(self.__printers)):
            builder.append1(self.__printers[i], self.__parsers[i])

    def isParser(self) -> bool:
        return all(self.__parsers)

    def isPrinter(self) -> bool:
        return None not in self.__printers

    def __init__(
        self, printers: typing.List[MoneyPrinter], parsers: typing.List[MoneyParser]
    ) -> None:
        self.__printers = printers
        self.__parsers = parsers

    def parse(self, context: MoneyParseContext) -> None:
        pass

    def print(
        self, context: MoneyPrintContext, appendable: IOBase, money: BigMoney
    ) -> None:
        pass
