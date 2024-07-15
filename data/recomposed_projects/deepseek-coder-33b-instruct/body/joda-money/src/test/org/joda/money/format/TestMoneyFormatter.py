from __future__ import annotations
import locale
import re
import collections
import os
from io import BytesIO
from io import StringIO
import unittest
import pytest
from io import IOBase
import io
import typing
from typing import *
import decimal
import unittest
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatException import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MoneyPrintContext import *


class IOAppendable:

    def append2(self, csq: str) -> typing.Union[typing.List, io.TextIOBase]:

        # If the IOAppendable is a list, append the CharSequence to the list
        if isinstance(self, list):
            self.append(csq)
            return self

        # If the IOAppendable is a TextIOBase, append the CharSequence to the TextIOBase
        elif isinstance(self, io.TextIOBase):
            self.write(csq)
            return self

        # If the IOAppendable is neither a list nor a TextIOBase, raise an exception
        else:
            raise TypeError("IOAppendable must be a list or a TextIOBase")

    def append1(self, c: str) -> typing.Union[typing.List, io.TextIOBase]:

        # Check if the object is a list
        if isinstance(self, list):
            self.append(c)
            return self

        # Check if the object is a TextIOBase
        elif isinstance(self, io.TextIOBase):
            self.write(c)
            return self

        # If the object is neither a list nor a TextIOBase, raise an error
        else:
            raise TypeError("Object must be a list or a TextIOBase")

    def append0(
        self, csq: str, start: int, end: int
    ) -> typing.Union[typing.List, io.TextIOBase]:

        # Check if the IOAppendable object is a list
        if isinstance(self, list):
            return self.append(csq[start:end])

        # Check if the IOAppendable object is a TextIOBase
        elif isinstance(self, io.TextIOBase):
            self.write(csq[start:end])
            return self

        # If the IOAppendable object is neither a list nor a TextIOBase, raise an exception
        else:
            raise TypeError("IOAppendable object must be a list or a TextIOBase")


class TestMoneyFormatter(unittest.TestCase):

    __iCannotParse: MoneyFormatter = None

    __iParseTest: MoneyFormatter = None

    __iCannotPrint: MoneyFormatter = None

    __iPrintTest: MoneyFormatter = None

    __MONEY_GBP_12_34: Money = Money.parse("GBP 12.34")
    __TEST_FR_LOCALE: typing.Any = Locale("fr", "FR", "TEST")
    __TEST_GB_LOCALE: typing.Any = Locale("en", "GB", "TEST")
    __cCachedLocale: typing.Any = Locale.getDefault()

    def test_toString_differentPrinterParser(self) -> None:

        printer = MoneyPrinter()
        parser = MoneyParser()

        class TestPrinter(MoneyPrinter):
            def print(
                self,
                context: MoneyPrintContext,
                appendable: IOAppendable,
                money: BigMoney,
            ) -> None:
                pass

            def toString(self) -> str:
                return "A"

        class TestParser(MoneyParser):
            def parse(self, context: MoneyParseContext) -> None:
                pass

            def toString(self) -> str:
                return "B"

        printer = TestPrinter()
        parser = TestParser()

        f = MoneyFormatterBuilder().append1(printer, parser).toFormatter0()
        self.assertEqual("A:B", f.toString())

    def test_toString(self) -> None:

        self.assertEqual("${code}' hello'", self.__iPrintTest.toString())

    def test_parse_notFullyParsed(self) -> None:

        with pytest.raises(MoneyFormatException):
            context = self.__iParseTest.parse("GBP hello notfullyparsed", 1)
            context.toBigMoney()

    def test_parseBigMoney_noAmount(self) -> None:

        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseBigMoney("GBP hello")

    def test_parseBigMoney_notFullyParsed(self) -> None:

        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseBigMoney("GBP hello notfullyparsed")

    def test_parseMoney_noAmount(self) -> None:
        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseMoney("GBP hello")

    def test_parseMoney_notFullyParsed(self) -> None:
        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseMoney("GBP hello notfullyparsed")

    def test_printParse_zeroChar(self) -> None:

        style = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA.withZeroCharacter("A")
        f = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" ")
            .appendAmount1(style)
            .toFormatter0()
        )
        self.assertEqual("GBP BC.DE", f.print0(self.__MONEY_GBP_12_34))
        self.assertEqual(self.__MONEY_GBP_12_34, f.parseMoney("GBP BC.DE"))

    def test_parse_CharSequenceInt_startIndexTooBig(self) -> None:

        with pytest.raises(IndexError):
            self.__iParseTest.parse("", 1)

    def test_parse_CharSequenceInt_startIndexTooSmall(self) -> None:

        with pytest.raises(IndexError):
            self.__iParseTest.parse("", -1)

    def test_parse_CharSequenceInt_nullCharSequence(self) -> None:

        with pytest.raises(Exception):
            self.__iParseTest.parse(None, 0)

    def test_parse_CharSequenceInt_cannotParse(self) -> None:

        with pytest.raises(NotImplementedError):
            self.__iCannotParse.parse(StringBuilder(), 0)

    def test_parse_CharSequenceInt_continueAfterDoubleComma(self) -> None:

        f = (
            MoneyFormatterBuilder()
            .appendAmountLocalized()
            .appendLiteral(",,")
            .appendCurrencyCode()
            .toFormatter0()
        )
        test = f.parse("12,,GBP", 0)
        self.assertEqual(decimal.Decimal(12), test.getAmount())
        self.assertEqual(CurrencyUnit.of1("GBP"), test.getCurrency())
        self.assertEqual(7, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("12,,GBP", test.getText())
        self.assertEqual(7, len(test.getText()))
        self.assertEqual(False, test.isError())
        self.assertEqual(True, test.isFullyParsed())
        self.assertEqual(True, test.isComplete())

    def test_parse_CharSequenceInt_continueAfterSingleComma(self) -> None:

        f = (
            MoneyFormatterBuilder()
            .appendAmountLocalized()
            .appendLiteral(",")
            .appendCurrencyCode()
            .toFormatter0()
        )
        test = f.parse("12,GBP", 0)
        self.assertEqual(decimal.Decimal(12), test.getAmount())
        self.assertEqual(CurrencyUnit.of1("GBP"), test.getCurrency())
        self.assertEqual(6, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("12,GBP", test.getText())
        self.assertEqual(6, len(test.getText()))
        self.assertEqual(False, test.isError())
        self.assertEqual(True, test.isFullyParsed())
        self.assertEqual(True, test.isComplete())

    def test_parse_CharSequenceInt_continueAfterDoubleDecimal(self) -> None:

        f = (
            MoneyFormatterBuilder()
            .appendAmountLocalized()
            .appendLiteral(".")
            .appendCurrencyCode()
            .toFormatter0()
        )
        test = f.parse("12..GBP", 0)
        self.assertEqual(decimal.Decimal(12), test.getAmount())
        self.assertEqual(CurrencyUnit.of1("GBP"), test.getCurrency())
        self.assertEqual(7, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("12..GBP", test.getText())
        self.assertEqual(7, len(test.getText()))
        self.assertEqual(False, test.isError())
        self.assertEqual(True, test.isFullyParsed())
        self.assertEqual(True, test.isComplete())

    def test_parse_CharSequenceInt_incomplete(self) -> None:

        test = self.__iCannotPrint.parse("12.34 GBP", 0)
        self.assertEqual(None, test.getAmount())
        self.assertEqual(None, test.getCurrency())
        self.assertEqual(0, test.getIndex())
        self.assertEqual(-1, test.getErrorIndex())
        self.assertEqual("12.34 GBP", test.getText())
        self.assertEqual(9, test.getTextLength())
        self.assertEqual(False, test.isError())
        self.assertEqual(False, test.isFullyParsed())
        self.assertEqual(False, test.isComplete())

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

        input = str
        test = self.__iParseTest.parse(input, 0)
        assert amount == test.getAmount()
        assert currency == test.getCurrency()
        assert index == test.getIndex()
        assert errorIndex == test.getErrorIndex()
        assert str == test.getText()
        assert len(str) == test.getTextLength()
        assert error == test.isError()
        assert fullyParsed == test.isFullyParsed()
        assert complete == test.isComplete()
        pp = collections.namedtuple("ParsePosition", ["textIndex", "textErrorIndex"])
        pp = pp(test.getIndex(), test.getErrorIndex())
        assert pp == test.toParsePosition()

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:

        MONEY_GBP_12_34 = Money.parse("GBP 12.34")
        TEST_FR_LOCALE = Locale("fr", "FR", "TEST")
        TEST_GB_LOCALE = Locale("en", "GB", "TEST")
        cCachedLocale = Locale.getDefault()

        return [
            [
                "12.34 GBP",
                MONEY_GBP_12_34.getAmount(),
                MONEY_GBP_12_34.getCurrencyUnit(),
                9,
                -1,
                False,
                True,
                True,
            ],
            [
                "1,2.34 GBP",
                MONEY_GBP_12_34.getAmount(),
                MONEY_GBP_12_34.getCurrencyUnit(),
                10,
                -1,
                False,
                True,
                True,
            ],
            [
                "12,.34 GBP",
                MONEY_GBP_12_34.getAmount(),
                MONEY_GBP_12_34.getCurrencyUnit(),
                10,
                -1,
                False,
                True,
                True,
            ],
            [
                "12.,34 GBP",
                MONEY_GBP_12_34.getAmount(),
                MONEY_GBP_12_34.getCurrencyUnit(),
                10,
                -1,
                False,
                True,
                True,
            ],
            [
                "12.3,4 GBP",
                MONEY_GBP_12_34.getAmount(),
                MONEY_GBP_12_34.getCurrencyUnit(),
                10,
                -1,
                False,
                True,
                True,
            ],
            [
                ".12 GBP",
                BigDecimal.valueOf(12, 2),
                MONEY_GBP_12_34.getCurrencyUnit(),
                7,
                -1,
                False,
                True,
                True,
            ],
            [
                "12. GBP",
                BigDecimal.valueOf(12),
                MONEY_GBP_12_34.getCurrencyUnit(),
                7,
                -1,
                False,
                True,
                True,
            ],
            [
                "12,34 GBP",
                BigDecimal.valueOf(1234),
                MONEY_GBP_12_34.getCurrencyUnit(),
                9,
                -1,
                False,
                True,
                True,
            ],
            [
                "-12.34 GBP",
                BigDecimal.valueOf(-1234, 2),
                CurrencyUnit.GBP,
                10,
                -1,
                False,
                True,
                True,
            ],
            [
                "+12.34 GBP",
                BigDecimal.valueOf(1234, 2),
                CurrencyUnit.GBP,
                10,
                -1,
                False,
                True,
                True,
            ],
            ["12.34 GB", BigDecimal.valueOf(1234, 2), None, 6, 6, True, False, False],
            [",12.34 GBP", None, None, 0, 0, True, False, False],
            ["12..34 GBP", BigDecimal.valueOf(12), None, 3, 3, True, False, False],
            ["12,,34 GBP", BigDecimal.valueOf(12), None, 2, 2, True, False, False],
            ["12.34 GBX", MONEY_GBP_12_34.getAmount(), None, 6, 6, True, False, False],
            [
                "12.34 GBPX",
                MONEY_GBP_12_34.getAmount(),
                MONEY_GBP_12_34.getCurrencyUnit(),
                9,
                -1,
                False,
                False,
                True,
            ],
        ]

    def test_parseMoney_CharSequence_nullCharSequence(self) -> None:
        with pytest.raises(RuntimeError):
            self.__iParseTest.parseMoney(None)

    def test_parseMoney_CharSequence_cannotParse(self) -> None:
        with pytest.raises(NotImplementedError):
            self.__iCannotParse.parseMoney(StringBuilder())

    def test_parseMoney_CharSequence_incomplete(self) -> None:
        with pytest.raises(MoneyFormatException):
            self.__iCannotPrint.parseMoney("12.34 GBP")

    def test_parseMoney_CharSequence_notFullyParsed(self) -> None:
        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseMoney("12.34 GBP X")

    def test_parseMoney_CharSequence_invalidCurrency(self) -> None:
        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseMoney("12.34 GBX")

    def test_parseMoney_CharSequence(self) -> None:

        input = "12.34 GBP"
        test = self.__iParseTest.parseMoney(input)
        self.assertEqual(self.__MONEY_GBP_12_34, test)

    def test_parseBigMoney_CharSequence_nullCharSequence(self) -> None:

        with pytest.raises(RuntimeError):
            self.__iParseTest.parseBigMoney(None)

    def test_parseBigMoney_CharSequence_cannotParse(self) -> None:

        with pytest.raises(NotImplementedError):
            self.__iCannotParse.parseBigMoney(StringBuilder())

    def test_parseBigMoney_CharSequence_missingCurrency(self) -> None:

        f = MoneyFormatterBuilder().appendAmount0().toFormatter0()
        with pytest.raises(MoneyFormatException):
            f.parseBigMoney("12.34")

    def test_parseBigMoney_CharSequence_incompleteEmptyParser(self) -> None:

        with pytest.raises(MoneyFormatException):
            self.__iCannotPrint.parseBigMoney("12.34 GBP")

    def test_parseBigMoney_CharSequence_incompleteLongText(self) -> None:

        text = (
            "12.34 GBP"
            + "ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB"
        )
        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseBigMoney(text)

    def test_parseBigMoney_CharSequence_incomplete(self) -> None:

        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseBigMoney("12.34 GBP ")

    def test_parseBigMoney_CharSequence_notFullyParsed(self) -> None:

        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseBigMoney("12.34 GBP X")

    def test_parseBigMoney_CharSequence_invalidCurrency(self) -> None:

        with pytest.raises(MoneyFormatException):
            self.__iParseTest.parseBigMoney("12.34 GBX")

    def test_parseBigMoney_CharSequence(self) -> None:

        input: str = "12.34 GBP"
        test: BigMoney = self.__iParseTest.parseBigMoney(input)
        self.assertEqual(self.__MONEY_GBP_12_34.toBigMoney(), test)

    def test_printIO_AppendableBigMoneyProvider_nullBigMoneyProvider(self) -> None:

        with pytest.raises(RuntimeError):
            self.__iPrintTest.printIO(io.StringIO(), None)

    def test_printIO_AppendableBigMoneyProvider_nullAppendable(self) -> None:

        with pytest.raises(RuntimeError):
            self.__iPrintTest.printIO(None, self.__MONEY_GBP_12_34)

    def test_printIO_AppendableBigMoneyProvider_cannotPrint(self) -> None:

        with pytest.raises(NotImplementedError):
            self.__iCannotPrint.printIO(io.StringIO(), BigMoneyProvider())

    def test_printIO_AppendableBigMoneyProvider_IOException(self) -> None:

        appendable = IOAppendable()

        with pytest.raises(IOException):
            self.__iPrintTest.printIO(appendable, self.__MONEY_GBP_12_34)

    def test_printIO_AppendableBigMoneyProvider(self) -> None:

        buf = io.StringIO()
        self.__iPrintTest.printIO(buf, BigMoney.of2(Money.parse("GBP 12.34")))
        self.assertEqual("GBP hello", buf.getvalue())

    def test_print_AppendableBigMoneyProvider_nullBigMoneyProvider(self) -> None:

        with pytest.raises(RuntimeError):
            self.__iPrintTest.print1(StringIO(), None)

    def test_print_AppendableBigMoneyProvider_nullAppendable(self) -> None:

        with pytest.raises(RuntimeError):
            self.__iPrintTest.print1(None, self.__MONEY_GBP_12_34)

    def test_print_AppendableBigMoneyProvider_cannotPrint(self) -> None:

        with pytest.raises(NotImplementedError):
            self.__iCannotPrint.print1(io.StringIO(), BigMoneyProvider())

    def test_print_AppendableBigMoneyProvider_IOException(self) -> None:

        appendable = IOAppendable()
        try:
            self.__iPrintTest.print1(appendable, self.__MONEY_GBP_12_34)
        except MoneyFormatException as ex:
            self.assertEqual(IOException, type(ex.__cause__))
            raise ex

    def test_print_AppendableBigMoneyProvider(self) -> None:

        buf = io.StringIO()
        self.__iPrintTest.print1(buf, BigMoneyProvider(MONEY_GBP_12_34))
        self.assertEqual("GBP hello", buf.getvalue())

    def test_print_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

        with pytest.raises(RuntimeError):
            self.__iPrintTest.print0(None)

    def test_print_BigMoneyProvider_cannotPrint(self) -> None:

        with pytest.raises(NotImplementedError):
            self.__iCannotPrint.print0(self.__MONEY_GBP_12_34)

    def test_print_BigMoneyProvider(self) -> None:

        # Create a BigMoneyProvider instance
        moneyProvider = BigMoneyProvider()

        # Call the print0 method and compare the result
        self.assertEqual("GBP hello", self.__iPrintTest.print0(moneyProvider))

    def test_withLocale_nullLocale(self) -> None:
        with pytest.raises(RuntimeError):
            self.__iPrintTest.withLocale(None)

    def test_withLocale(self) -> None:

        test = self.__iPrintTest.withLocale(self.__TEST_FR_LOCALE)
        self.assertEqual(self.__TEST_GB_LOCALE, self.__iPrintTest.getLocale())
        self.assertEqual(self.__TEST_FR_LOCALE, test.getLocale())

    def test_getLocale(self) -> None:
        self.assertEqual(self.__TEST_GB_LOCALE, self.__iPrintTest.getLocale())

    def test_serialization(self) -> None:

        a = self.__iPrintTest
        baos = io.BytesIO()
        try:
            with io.BufferedWriter(baos) as bw:
                with ObjectOutputStream(bw) as oos:
                    oos.writeObject(a)
                    oos.close()
                    ois = ObjectInputStream(
                        io.BufferedReader(io.BytesIO(baos.getvalue()))
                    )
                    input = cast(MoneyFormatter, ois.readObject())
                    value = self.__MONEY_GBP_12_34
                    self.assertEqual(a.print0(value), input.print0(value))
        except Exception as e:
            print(f"Exception occurred: {e}")

    def afterMethod(self) -> None:

        # Set the default locale back to the cached locale
        Locale.setDefault(self.__cCachedLocale)

        # Set iPrintTest to None
        self.__iPrintTest = None

    def beforeMethod(self) -> None:

        Locale.setDefault(self.__TEST_GB_LOCALE)
        self.__iPrintTest = (
            MoneyFormatterBuilder()
            .appendCurrencyCode()
            .appendLiteral(" hello")
            .toFormatter0()
        )
        self.__iCannotPrint = (
            MoneyFormatterBuilder().append1(None, MoneyParser()).toFormatter0()
        )
        self.__iParseTest = (
            MoneyFormatterBuilder()
            .appendAmountLocalized()
            .appendLiteral(" ")
            .appendCurrencyCode()
            .toFormatter0()
        )
        self.__iCannotParse = (
            MoneyFormatterBuilder().append1(MoneyPrinter(), None).toFormatter0()
        )
