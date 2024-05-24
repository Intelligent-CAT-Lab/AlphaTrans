from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatException import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import typing
from typing import *
import io
from io import IOBase

# Imports End


class IOAppendable(io.TextIOBase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def append2(self, csq: str) -> io.TextIOBase:
        pass

    def append1(self, c: str) -> io.TextIOBase:
        pass

    def append0(self, csq: str, start: int, end: int) -> io.TextIOBase:
        pass

    # Class Methods End


class MoneyParser:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    # Class Methods End


class MoneyPrinter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    # Class Methods End


class TestMoneyFormatter:

    # Class Fields Begin
    __cCachedLocale: typing.Any = None
    __TEST_GB_LOCALE: typing.Any = None
    __TEST_FR_LOCALE: typing.Any = None
    __MONEY_GBP_12_34: Money = None
    __iPrintTest: MoneyFormatter = None
    __iCannotPrint: MoneyFormatter = None
    __iParseTest: MoneyFormatter = None
    __iCannotParse: MoneyFormatter = None
    # Class Fields End

    # Class Methods Begin
    def test_toString_differentPrinterParser(self) -> None:
        pass

    def test_toString(self) -> None:
        pass

    def test_parse_notFullyParsed(self) -> None:
        pass

    def test_parseBigMoney_noAmount(self) -> None:
        pass

    def test_parseBigMoney_notFullyParsed(self) -> None:
        pass

    def test_parseMoney_noAmount(self) -> None:
        pass

    def test_parseMoney_notFullyParsed(self) -> None:
        pass

    def test_printParse_zeroChar(self) -> None:
        pass

    def test_parse_CharSequenceInt_startIndexTooBig(self) -> None:
        pass

    def test_parse_CharSequenceInt_startIndexTooSmall(self) -> None:
        pass

    def test_parse_CharSequenceInt_nullCharSequence(self) -> None:
        pass

    def test_parse_CharSequenceInt_cannotParse(self) -> None:
        pass

    def test_parse_CharSequenceInt_continueAfterDoubleComma(self) -> None:
        pass

    def test_parse_CharSequenceInt_continueAfterSingleComma(self) -> None:
        pass

    def test_parse_CharSequenceInt_continueAfterDoubleDecimal(self) -> None:
        pass

    def test_parse_CharSequenceInt_incomplete(self) -> None:
        pass

    def test_parse_CharSequenceInt(
        self,
        str: str,
        amount: decimal.Decimal,
        currency: CurrencyUnit,
        index: int,
        errorIndex: int,
        error: bool,
        fullyParsed: bool,
        complete: bool,
    ) -> None:
        pass

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:
        pass

    def test_parseMoney_CharSequence_nullCharSequence(self) -> None:
        pass

    def test_parseMoney_CharSequence_cannotParse(self) -> None:
        pass

    def test_parseMoney_CharSequence_incomplete(self) -> None:
        pass

    def test_parseMoney_CharSequence_notFullyParsed(self) -> None:
        pass

    def test_parseMoney_CharSequence_invalidCurrency(self) -> None:
        pass

    def test_parseMoney_CharSequence(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_nullCharSequence(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_cannotParse(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_missingCurrency(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_incompleteEmptyParser(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_incompleteLongText(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_incomplete(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_notFullyParsed(self) -> None:
        pass

    def test_parseBigMoney_CharSequence_invalidCurrency(self) -> None:
        pass

    def test_parseBigMoney_CharSequence(self) -> None:
        pass

    def test_printIO_AppendableBigMoneyProvider_nullBigMoneyProvider(self) -> None:
        pass

    def test_printIO_AppendableBigMoneyProvider_nullAppendable(self) -> None:
        pass

    def test_printIO_AppendableBigMoneyProvider_cannotPrint(self) -> None:
        pass

    def test_printIO_AppendableBigMoneyProvider_IOException(self) -> None:
        pass

    def test_printIO_AppendableBigMoneyProvider(self) -> None:
        pass

    def test_print_AppendableBigMoneyProvider_nullBigMoneyProvider(self) -> None:
        pass

    def test_print_AppendableBigMoneyProvider_nullAppendable(self) -> None:
        pass

    def test_print_AppendableBigMoneyProvider_cannotPrint(self) -> None:
        pass

    def test_print_AppendableBigMoneyProvider_IOException(self) -> None:
        pass

    def test_print_AppendableBigMoneyProvider(self) -> None:
        pass

    def test_print_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        pass

    def test_print_BigMoneyProvider_cannotPrint(self) -> None:
        pass

    def test_print_BigMoneyProvider(self) -> None:
        pass

    def test_withLocale_nullLocale(self) -> None:
        pass

    def test_withLocale(self) -> None:
        pass

    def test_getLocale(self) -> None:
        pass

    def test_serialization(self) -> None:
        pass

    def afterMethod(self) -> None:
        pass

    def beforeMethod(self) -> None:
        pass

    # Class Methods End
