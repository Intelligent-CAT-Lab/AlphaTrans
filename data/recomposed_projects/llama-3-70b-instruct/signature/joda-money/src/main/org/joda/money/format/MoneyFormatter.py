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


class MoneyFormatter():

    serialVersionUID: int = 2385346258
    def toString(self) -> str:
         return self.__printerParser.toString()
    def parse(self, text: str, startIndex: int) -> MoneyParseContext:
         self.checkNotNull(text, "Text must not be null")
         if startIndex < 0 or startIndex > len(text):
             raise StringIndexOutOfBoundsException("Invalid start index: " + startIndex)
         if self.isParser() == False:
             raise NotImplementedError(
                     "MoneyFomatter has not been configured to be able to parse")
         context = MoneyParseContext(1, text, startIndex, self.locale, None, 0, None)
         self.printerParser.parse(context)
         return context
    def parseMoney(self, text: str) -> Money:
         return self.parseBigMoney(text).toMoney0()

    def parseBigMoney(self, text: str) -> BigMoney:

        pass # LLM could not translate this method


    def printIO(self, appendable: typing.Union[typing.List, io.TextIOBase], moneyProvider: BigMoneyProvider) -> None:
         MoneyFormatter.checkNotNull(moneyProvider, "BigMoneyProvider must not be null")
         if self.isPrinter() == False:
             raise NotImplementedError(
                 "MoneyFomatter has not been configured to be able to print")
         money: BigMoney = BigMoney.of2(moneyProvider)
         context: MoneyPrintContext = MoneyPrintContext(self.__locale)
         self.__printerParser.print(context, appendable, money)

    def print1(self, appendable: typing.Union[typing.List, io.TextIOBase], moneyProvider: BigMoneyProvider) -> None:

        pass # LLM could not translate this method


    def print0(self, moneyProvider: BigMoneyProvider) -> str:
         buf = io.StringIO()
         self.print1(buf, moneyProvider)
         return buf.getvalue()
    def isParser(self) -> bool:
         return self.__printerParser.isParser()
    def isPrinter(self) -> bool:
         return self.__printerParser.isPrinter()
    def withLocale(self, locale: typing.Any) -> MoneyFormatter:
         self.checkNotNull(locale, "Locale must not be null")
         return MoneyFormatter(1, locale, None, None, self.__printerParser)
    def getLocale(self) -> typing.Any:
         return self.__locale

    def __init__(self, constructorId: int, locale: typing.Any, parsers: typing.List[MoneyParser], printers: typing.List[MoneyPrinter], printerParser: MultiPrinterParser) -> None:

         self.__locale: typing.Any = None
         self.__printerParser: MultiPrinterParser = None
        pass # LLM could not translate this method


    @staticmethod
    def checkNotNull(object: typing.Any, message: str) -> None:
         if object is None:
             raise NullPointerException(message)
    def getPrinterParser(self) -> MultiPrinterParser:
         return self.__printerParser
