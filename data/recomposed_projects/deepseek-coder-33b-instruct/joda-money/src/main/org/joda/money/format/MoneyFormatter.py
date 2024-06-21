from __future__ import annotations
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

    __serialVersionUID: int = 2385346258

    def toString(self) -> str:

        if self.__printerParser is not None:
            return self.__printerParser.toString()
        else:
            return ""

    def parse(self, text: str, startIndex: int) -> MoneyParseContext:

        self.checkNotNull(text, "Text must not be null")
        if startIndex < 0 or startIndex > len(text):
            raise IndexError("Invalid start index: " + str(startIndex))
        if self.isParser() == False:
            raise Exception("MoneyFomatter has not been configured to be able to parse")
        context = MoneyParseContext(1, text, startIndex, self.__locale, None, 0, None)
        self.__printerParser.parse(context)
        return context

    def parseMoney(self, text: str) -> Money:

        # Assuming that parseBigMoney method is defined somewhere else in the class
        # and it returns a BigMoney object
        big_money = self.parseBigMoney(text)

        # Calling the toMoney0 method on the BigMoney object
        return big_money.toMoney0()

    def parseBigMoney(self, text: str) -> BigMoney:

        self.checkNotNull(text, "Text must not be null")
        result = self.parse(text, 0)
        if (
            result.isError()
            or result.isFullyParsed() == False
            or result.isComplete() == False
        ):
            str = text[:64] + "..." if len(text) > 64 else text
            if result.isError():
                raise MoneyFormatException.MoneyFormatException1(
                    "Text could not be parsed at index "
                    + str(result.getErrorIndex())
                    + ": "
                    + str
                )
            elif result.isFullyParsed() == False:
                raise MoneyFormatException.MoneyFormatException1(
                    "Unparsed text found at index "
                    + str(result.getIndex())
                    + ": "
                    + str
                )
            else:
                raise MoneyFormatException.MoneyFormatException1(
                    "Parsing did not find both currency and amount: " + str
                )
        return result.toBigMoney()

    def printIO(
        self, appendable: io.TextIOBase, moneyProvider: BigMoneyProvider
    ) -> None:

        if self.isPrinter() == False:
            raise NotImplementedError(
                "MoneyFomatter has not been configured to be able to print"
            )

        self.checkNotNull(moneyProvider, "BigMoneyProvider must not be null")

        money = BigMoney.of2(moneyProvider)
        context = MoneyPrintContext(self.__locale)
        self.__printerParser.print(context, appendable, money)

    def print1(
        self, appendable: io.TextIOBase, moneyProvider: BigMoneyProvider
    ) -> None:

        try:
            self.printIO(appendable, moneyProvider)
        except IOError as ex:
            raise MoneyFormatException(ex.args[0], ex)

    def print0(self, moneyProvider: BigMoneyProvider) -> str:

        buf = io.StringIO()
        self.print1(buf, moneyProvider)
        return buf.getvalue()

    def isParser(self) -> bool:

        return self.__printerParser.isParser()

    def isPrinter(self) -> bool:

        if self.__printerParser is not None:
            return self.__printerParser.isPrinter()
        else:
            raise ValueError("printerParser is not initialized")

    def withLocale(self, locale: typing.Any) -> MoneyFormatter:

        self.checkNotNull(locale, "Locale must not be null")
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

            self.checkNotNull(locale, "Locale must not be null")
            self.checkNotNull(printers, "Printers must not be null")
            self.checkNotNull(parsers, "Parsers must not be null")
            if len(printers) != len(parsers):
                raise ValueError("Printers and parsers must match")
            self.__locale = locale
            self.__printerParser = MultiPrinterParser(printers, parsers)
        else:

            self.checkNotNull(locale, "Locale must not be null")
            self.checkNotNull(printerParser, "PrinterParser must not be null")
            self.__locale = locale
            self.__printerParser = printerParser

    @staticmethod
    def checkNotNull(object: typing.Any, message: str) -> None:

        if object is None:
            raise NullPointerException(message)

    def getPrinterParser(self) -> MultiPrinterParser:

        return self.__printerParser
