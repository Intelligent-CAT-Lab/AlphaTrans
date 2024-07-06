from __future__ import annotations
import locale
import re
from io import StringIO
from io import IOBase
import io
import typing
from typing import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.format.MoneyFormatException import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *


class MoneyFormatter:

    __printerParser: MultiPrinterParser = None

    __locale: typing.Any = None

    serialVersionUID: int = 2385346258

    def toString(self) -> str:
        buf1 = ""
        if self.isPrinter():
            for printer in self.__printers:
                buf1 += printer.toString()
        buf2 = ""
        if self.isParser():
            for parser in self.__parsers:
                buf2 += parser.toString()
        str1 = buf1
        str2 = buf2
        if self.isPrinter() and not self.isParser():
            return str1
        elif self.isParser() and not self.isPrinter():
            return str2
        elif str1 == str2:
            return str1
        else:
            return str1 + ":" + str2

    def parse(self, text: str, startIndex: int) -> MoneyParseContext:
        self.checkNotNull(text, "Text must not be null")
        if startIndex < 0 or startIndex > len(text):
            raise StringIndexOutOfBoundsException("Invalid start index: " + startIndex)
        if self.isParser() == False:
            raise NotImplementedError(
                "MoneyFomatter has not been configured to be able to parse"
            )
        context = MoneyParseContext(1, text, startIndex, self.__locale, None, 0, None)
        self.__printerParser.parse(context)
        return context

    def parseMoney(self, text: str) -> Money:
        return self.parseBigMoney(text).toMoney0()

    def parseBigMoney(self, text: str) -> BigMoney:
        self.checkNotNull(text, "Text must not be null")
        result = self.parse(text, 0)
        if (
            result.isError()
            or result.isFullyParsed() == False
            or result.isComplete() == False
        ):
            str = text[0:64] + "..." if len(text) > 64 else text
            if result.isError():
                raise MoneyFormatException.MoneyFormatException1(
                    "Text could not be parsed at index "
                    + result.getErrorIndex()
                    + ": "
                    + str
                )
            elif result.isFullyParsed() == False:
                raise MoneyFormatException.MoneyFormatException1(
                    "Unparsed text found at index " + result.getIndex() + ": " + str
                )
            else:
                raise MoneyFormatException.MoneyFormatException1(
                    "Parsing did not find both currency and amount: " + str
                )
        return result.toBigMoney()

    def printIO(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        moneyProvider: BigMoneyProvider,
    ) -> None:
        MoneyUtils.checkNotNull(moneyProvider, "BigMoneyProvider must not be null")
        if self.isPrinter() == False:
            raise NotImplementedError(
                "MoneyFomatter has not been configured to be able to print"
            )

        money: BigMoney = BigMoney.of2(moneyProvider)
        context: MoneyPrintContext = MoneyPrintContext(self.__locale)
        self.__printerParser.print(context, appendable, money)

    def print1(
        self,
        appendable: typing.Union[typing.List, io.TextIOBase],
        moneyProvider: BigMoneyProvider,
    ) -> None:
        try:
            self.printIO(appendable, moneyProvider)
        except IOException as ex:
            raise MoneyFormatException(ex.getMessage(), ex)

    def print0(self, moneyProvider: BigMoneyProvider) -> str:
        buf = io.StringIO()
        self.print1(buf, moneyProvider)
        return buf.getvalue()

    def isParser(self) -> bool:
        return self.__printerParser.isParser()

    def isPrinter(self) -> bool:
        return self.__printerParser.isPrinter()

    def withLocale(self, locale: typing.Any) -> MoneyFormatter:
        MoneyFormatter.checkNotNull(locale, "Locale must not be null")
        return MoneyFormatter(1, locale, None, None, self.__printerParser)

    def getLocale(self) -> typing.Any:
        return self.__locale

    def __init__(
        self,
        constructorId: int,
        locale: typing.Any,
        parsers: typing.List[MoneyParser],
        printers: typing.List[MoneyPrinter],
        printerParser: MultiPrinterParser,
    ) -> None:
        if constructorId == 0:
            MoneyFormatter.checkNotNull(locale, "Locale must not be null")
            MoneyFormatter.checkNotNull(printers, "Printers must not be null")
            MoneyFormatter.checkNotNull(parsers, "Parsers must not be null")
            if len(printers) != len(parsers):
                raise ValueError("Printers and parsers must match")
            self.__locale = locale
            self.__printerParser = MultiPrinterParser(printers, parsers)
        else:
            MoneyFormatter.checkNotNull(locale, "Locale must not be null")
            MoneyFormatter.checkNotNull(printerParser, "PrinterParser must not be null")
            self.__locale = locale
            self.__printerParser = printerParser

    @staticmethod
    def checkNotNull(object: typing.Any, message: str) -> None:
        if object is None:
            raise NullPointerException(message)

    def getPrinterParser(self) -> MultiPrinterParser:
        return self.__printerParser
