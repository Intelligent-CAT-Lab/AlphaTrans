from __future__ import annotations
import locale
import re
from abc import ABC
from io import IOBase
import io
import typing
from typing import *
import os
from src.main.org.joda.money.format.AmountPrinterParser import *
from src.main.org.joda.money.format.LiteralPrinterParser import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *
from src.main.org.joda.money.format.SignedPrinterParser import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.IllegalCurrencyException import *
from src.main.org.joda.money.format.MoneyParseContext import *


class SingletonPrinters(MoneyPrinter):

    LOCALIZED_SYMBOL: SingletonPrinters = None

    def toString(self) -> str:
        return "${symbolLocalized}"

    def print(
        self,
        context: MoneyPrintContext,
        appendable: typing.Union[typing.List, io.TextIOBase],
        money: BigMoney,
    ) -> None:
        appendable.append(money.getCurrencyUnit().getSymbol1(context.getLocale()))


class Singletons(MoneyParser, MoneyPrinter, ABC):

    NUMERIC_CODE: Singletons = None
    NUMERIC_3_CODE: Singletons = None
    CODE: Singletons = None
    __toString: str = ""

    @staticmethod
    def initialize_fields() -> None:
        Singletons.NUMERIC_CODE: Singletons = Singletons("${numericCode}")

        Singletons.NUMERIC_3_CODE: Singletons = Singletons("${numeric3Code}")

        Singletons.CODE: Singletons = Singletons("${code}")

    def toString(self) -> str:
        return self.__toString

    def __init__(self, toString: str) -> None:
        self.__toString = toString

    def __str__(self) -> str:
        return self.__toString

    def print(
        self, context: MoneyPrintContext, appendable: IOBase, money: BigMoney
    ) -> None:
        if self == Singletons.NUMERIC_CODE:
            appendable.write(str(money.getCurrencyUnit().getNumericCode()))
        elif self == Singletons.NUMERIC_3_CODE:
            appendable.write(money.getCurrencyUnit().getNumeric3Code())
        elif self == Singletons.CODE:
            appendable.write(money.getCurrencyUnit().getCode())

    def parse(self, context: MoneyParseContext) -> None:
        if self == Singletons.NUMERIC_CODE:
            count = 0
            for count in range(3):
                if context.getIndex() + count < context.getTextLength():
                    ch = context.getText()[context.getIndex() + count]
                    if ch < "0" or ch > "9":
                        break
                else:
                    break
            endPos = context.getIndex() + count
            code = context.getText()[context.getIndex() : endPos]
            try:
                context.setCurrency(CurrencyUnit.ofNumericCode0(code))
                context.setIndex(endPos)
            except IllegalCurrencyException:
                context.setError()
        elif self == Singletons.NUMERIC_3_CODE:
            endPos = context.getIndex() + 3
            if endPos > context.getTextLength():
                context.setError()
            else:
                code = context.getText()[context.getIndex() : endPos]
                try:
                    context.setCurrency(CurrencyUnit.ofNumericCode0(code))
                    context.setIndex(endPos)
                except IllegalCurrencyException:
                    context.setError()
        elif self == Singletons.CODE:
            endPos = context.getIndex() + 3
            if endPos > context.getTextLength():
                context.setError()
            else:
                code = context.getText()[context.getIndex() : endPos]
                try:
                    context.setCurrency(CurrencyUnit.of1(code))
                    context.setIndex(endPos)
                except IllegalCurrencyException:
                    context.setError()


class MoneyFormatterBuilder:

    __parsers: typing.List[MoneyParser] = []

    __printers: typing.List[MoneyPrinter] = []

    def toFormatter1(self, locale: typing.Any) -> MoneyFormatter:

        MoneyFormatter.checkNotNull(locale, "Locale must not be null")
        printersCopy = [printer for printer in self.__printers]
        parsersCopy = [parser for parser in self.__parsers]
        return MoneyFormatter(0, locale, parsersCopy, printersCopy, None)

    def toFormatter0(self) -> MoneyFormatter:

        locale = Locale.getDefault()
        printersCopy = [printer for printer in self.__printers]
        parsersCopy = [parser for parser in self.__parsers]
        return MoneyFormatter(0, locale, parsersCopy, printersCopy, None)

    def appendSigned1(
        self,
        whenPositive: MoneyFormatter,
        whenZero: MoneyFormatter,
        whenNegative: MoneyFormatter,
    ) -> MoneyFormatterBuilder:

        MoneyFormatter.checkNotNull(
            whenPositive, "MoneyFormatter whenPositive must not be null"
        )
        MoneyFormatter.checkNotNull(
            whenZero, "MoneyFormatter whenZero must not be null"
        )
        MoneyFormatter.checkNotNull(
            whenNegative, "MoneyFormatter whenNegative must not be null"
        )
        pp = SignedPrinterParser(whenPositive, whenZero, whenNegative)
        return self.__appendInternal(pp, pp)

    def appendSigned0(
        self, whenPositiveOrZero: MoneyFormatter, whenNegative: MoneyFormatter
    ) -> MoneyFormatterBuilder:

        MoneyFormatter.checkNotNull(
            whenPositiveOrZero, "MoneyFormatter whenPositiveOrZero must not be null"
        )
        MoneyFormatter.checkNotNull(
            whenNegative, "MoneyFormatter whenNegative must not be null"
        )
        pp = SignedPrinterParser(whenPositiveOrZero, whenPositiveOrZero, whenNegative)
        return self.__appendInternal(pp, pp)

    def append1(
        self, printer: MoneyPrinter, parser: MoneyParser
    ) -> MoneyFormatterBuilder:

        return self.__appendInternal(printer, parser)

    def append0(self, formatter: MoneyFormatter) -> MoneyFormatterBuilder:

        MoneyFormatter.checkNotNull(formatter, "MoneyFormatter must not be null")
        formatter.getPrinterParser().appendTo(self)
        return self

    def appendLiteral(self, literal: str) -> MoneyFormatterBuilder:

        if literal is None or len(literal) == 0:
            return self

        pp = LiteralPrinterParser(literal)
        return self.__appendInternal(pp, pp)

    def appendCurrencySymbolLocalized(self) -> MoneyFormatterBuilder:
        return self.__appendInternal(SingletonPrinters.LOCALIZED_SYMBOL, None)

    def appendCurrencyNumericCode(self) -> MoneyFormatterBuilder:
        return self.__appendInternal(
            SingletonPrinters.NUMERIC_CODE, Singletons.NUMERIC_CODE
        )

    def appendCurrencyNumeric3Code(self) -> MoneyFormatterBuilder:
        return self.__appendInternal(
            SingletonPrinters.NUMERIC_3_CODE, Singletons.NUMERIC_3_CODE
        )

    def appendCurrencyCode(self) -> MoneyFormatterBuilder:
        return self.__appendInternal(SingletonPrinters.CODE, Singletons.CODE)

    def appendAmount1(self, style: MoneyAmountStyle) -> MoneyFormatterBuilder:

        MoneyFormatter.checkNotNull(style, "MoneyAmountStyle must not be null")
        pp = AmountPrinterParser(style)
        return self.__appendInternal(pp, pp)

    def appendAmountLocalized(self) -> MoneyFormatterBuilder:
        pp = AmountPrinterParser(MoneyAmountStyle.LOCALIZED_GROUPING)
        return self.__appendInternal(pp, pp)

    def appendAmount0(self) -> MoneyFormatterBuilder:
        pp = AmountPrinterParser(MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA)
        return self.__appendInternal(pp, pp)

    def __init__(self) -> None:

        self.__parsers: typing.List[MoneyParser] = []
        self.__printers: typing.List[MoneyPrinter] = []

    def __appendInternal(
        self, printer: MoneyPrinter, parser: MoneyParser
    ) -> MoneyFormatterBuilder:

        self.__printers.append(printer)
        self.__parsers.append(parser)
        return self


Singletons.initialize_fields()
