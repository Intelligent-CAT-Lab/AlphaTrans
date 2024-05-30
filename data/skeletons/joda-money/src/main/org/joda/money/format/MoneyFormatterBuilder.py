from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.IllegalCurrencyException import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.format.SignedPrinterParser import *
from src.main.org.joda.money.format.MultiPrinterParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.LiteralPrinterParser import *
from src.main.org.joda.money.format.AmountPrinterParser import *
import os
import typing
from typing import *
import io
from io import IOBase
from abc import ABC

# Imports End


class SingletonPrinters(MoneyPrinter):

    # Class Fields Begin
    LOCALIZED_SYMBOL: SingletonPrinters = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def print(
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:
        pass

    # Class Methods End


class Singletons(MoneyParser, MoneyPrinter, ABC):

    # Class Fields Begin
    CODE: Singletons = None
    NUMERIC_3_CODE: Singletons = None
    NUMERIC_CODE: Singletons = None
    __toString: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def __init__(self, toString: str) -> None:
        pass

    # Class Methods End


class MoneyFormatterBuilder:

    # Class Fields Begin
    __printers: typing.List[MoneyPrinter] = None
    __parsers: typing.List[MoneyParser] = None
    # Class Fields End

    # Class Methods Begin
    def toFormatter1(self, locale: typing.Any) -> MoneyFormatter:
        pass

    def toFormatter0(self) -> MoneyFormatter:
        pass

    def appendSigned1(
        self,
        whenPositive: MoneyFormatter,
        whenZero: MoneyFormatter,
        whenNegative: MoneyFormatter,
    ) -> MoneyFormatterBuilder:
        pass

    def appendSigned0(
        self, whenPositiveOrZero: MoneyFormatter, whenNegative: MoneyFormatter
    ) -> MoneyFormatterBuilder:
        pass

    def append1(
        self, printer: MoneyPrinter, parser: MoneyParser
    ) -> MoneyFormatterBuilder:
        pass

    def append0(self, formatter: MoneyFormatter) -> MoneyFormatterBuilder:
        pass

    def appendLiteral(self, literal: str) -> MoneyFormatterBuilder:
        pass

    def appendCurrencySymbolLocalized(self) -> MoneyFormatterBuilder:
        pass

    def appendCurrencyNumericCode(self) -> MoneyFormatterBuilder:
        pass

    def appendCurrencyNumeric3Code(self) -> MoneyFormatterBuilder:
        pass

    def appendCurrencyCode(self) -> MoneyFormatterBuilder:
        pass

    def appendAmount1(self, style: MoneyAmountStyle) -> MoneyFormatterBuilder:
        pass

    def appendAmountLocalized(self) -> MoneyFormatterBuilder:
        pass

    def appendAmount0(self) -> MoneyFormatterBuilder:
        pass

    def __init__(self) -> None:
        pass

    def __appendInternal(
        self, printer: MoneyPrinter, parser: MoneyParser
    ) -> MoneyFormatterBuilder:
        pass

    # Class Methods End
