from __future__ import annotations
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
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:

        appendable.write(money.getCurrencyUnit().getSymbol1(context.getLocale()))


class Singletons(MoneyParser, MoneyPrinter, ABC):

    NUMERIC_CODE: Singletons = Singletons("${numericCode}")

    NUMERIC_3_CODE: Singletons = Singletons("${numeric3Code}")
    CODE: Singletons = None  # LLM could not translate this field
    __toString: str = None

    def toString(self) -> str:

        return self.__toString

    def __init__(self, toString: str) -> None:

        self.__toString = toString


class MoneyFormatterBuilder:

    __parsers: typing.List[MoneyParser] = []

    __printers: typing.List[MoneyPrinter] = []

    def toFormatter1(self, locale: typing.Any) -> MoneyFormatter:

        MoneyFormatter.checkNotNull(locale, "Locale must not be null")
        printersCopy = [printer for printer in self.__printers]
        parsersCopy = [parser for parser in self.__parsers]
        return MoneyFormatter(0, locale, parsersCopy, printersCopy, None)

    def toFormatter0(self) -> MoneyFormatter:

        return self.toFormatter1(Locale.getDefault())

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

        return self.appendSigned1(whenPositiveOrZero, whenPositiveOrZero, whenNegative)

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

        return self.__appendInternal(Singletons.NUMERIC_CODE, Singletons.NUMERIC_CODE)

    def appendCurrencyNumeric3Code(self) -> MoneyFormatterBuilder:

        return self.__appendInternal(
            Singletons.NUMERIC_3_CODE, Singletons.NUMERIC_3_CODE
        )

    def appendCurrencyCode(self) -> MoneyFormatterBuilder:

        return self.__appendInternal(Singletons.CODE, Singletons.CODE)

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

        pass

    def __appendInternal(
        self, printer: MoneyPrinter, parser: MoneyParser
    ) -> MoneyFormatterBuilder:

        self.__printers.append(printer)
        self.__parsers.append(parser)
        return self
