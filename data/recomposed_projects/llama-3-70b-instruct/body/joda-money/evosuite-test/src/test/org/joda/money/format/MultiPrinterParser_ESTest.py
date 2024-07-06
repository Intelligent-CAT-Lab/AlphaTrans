from __future__ import annotations
import time
import locale
import re
import mock
import os
import decimal
from io import StringIO
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.AmountPrinterParser import *
from src.main.org.joda.money.format.LiteralPrinterParser import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *

# from src.test.org.joda.money.format.MultiPrinterParser_ESTest_scaffolding import *


class MultiPrinterParser_ESTest(unittest.TestCase):

    def test21(self) -> None:

        money_printer_array0 = [None]
        money_parser_array0 = [None, None]
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        locale0 = "de"
        currency_unit0 = CurrencyUnit.GBP
        big_decimal0 = 10
        money_parse_context0 = MoneyParseContext(
            8, "tRyAM_&cl9t3j", (-10), locale0, big_decimal0, (-10), currency_unit0
        )

        try:
            multi_printer_parser0.parse(money_parse_context0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.format.MultiPrinterParser", e)

    def test20(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("Bx")
        moneyPrinterArray0 = [None] * 1
        moneyPrinterArray0[0] = literalPrinterParser0
        moneyParserArray0 = [None] * 2
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        string0 = multiPrinterParser0.toString()
        self.assertIsNotNone(string0)

    def test19(self) -> None:

        money_printer_array0 = [MoneyPrinter()]
        money_formatter_builder0 = MoneyFormatterBuilder()
        money_parser_array0 = [MoneyParser(), MoneyParser()]
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        multi_printer_parser0.appendTo(money_formatter_builder0)

    def test18(self) -> None:

        money_printer_array0 = []
        money_parser_array0 = []
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        locale0 = Locale.US
        money_parser_array1 = [None] * 2
        money_parser_array1[0] = multi_printer_parser0
        money_parser_array1[1] = multi_printer_parser0
        multi_printer_parser1 = MultiPrinterParser(
            money_printer_array0, money_parser_array1
        )
        money_formatter0 = MoneyFormatter(
            1, locale0, money_parser_array0, money_printer_array0, multi_printer_parser1
        )
        money_parse_context0 = money_formatter0.parse("V$_G", 1)
        self.assertFalse(money_parse_context0.isError())

    def test17(self) -> None:

        money_printer_array0 = [None] * 1
        literal_printer_parser0 = LiteralPrinterParser("Bx")
        money_parser_array0 = [None] * 2
        money_parser_array0[0] = literal_printer_parser0
        money_parser_array0[1] = literal_printer_parser0
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        locale0 = Locale.FRENCH
        money_formatter0 = MoneyFormatter(
            (-4158),
            locale0,
            money_parser_array0,
            money_printer_array0,
            multi_printer_parser0,
        )
        money_parse_context0 = money_formatter0.parse(
            "org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001",
            1,
        )
        multi_printer_parser0.parse(money_parse_context0)
        self.assertEqual(1, money_parse_context0.getErrorIndex())
        self.assertTrue(money_parse_context0.isError())

    def test16(self) -> None:

        money_printer_array0 = [None] * 1
        literal_printer_parser0 = LiteralPrinterParser("Bx")
        money_parser_array0 = [None] * 2
        money_parser_array0[0] = literal_printer_parser0
        money_parser_array0[1] = literal_printer_parser0
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        string0 = multi_printer_parser0.toString()
        self.assertIsNotNone(string0)

    def test15(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("Bx")
        moneyPrinterArray0 = [None] * 1
        moneyPrinterArray0[0] = literalPrinterParser0
        moneyParserArray0 = [None] * 2
        moneyParserArray0[0] = literalPrinterParser0
        moneyParserArray0[1] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        string0 = multiPrinterParser0.toString()
        self.assertIsNotNone(string0)

    def test14(self) -> None:

        money_printer_array0 = [None] * 8
        money_parser_array0 = [None] * 1
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        string0 = multi_printer_parser0.toString()
        self.assertEqual("", string0)

    def test13(self) -> None:

        money_printer_array0 = [None] * 5
        money_parser_array0 = []
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        money_formatter_builder0 = MoneyFormatterBuilder()

        try:
            multi_printer_parser0.appendTo(money_formatter_builder0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "list index out of range")

    def test12(self) -> None:

        money_printer_array0 = [None]
        multi_printer_parser0 = MultiPrinterParser(money_printer_array0, None)
        money_formatter_builder0 = MoneyFormatterBuilder()

        try:
            multi_printer_parser0.appendTo(money_formatter_builder0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.format.MultiPrinterParser", e)

    def test11(self) -> None:
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        with pytest.raises(RuntimeError):
            multiPrinterParser0.isParser()

    def test10(self) -> None:
        multiPrinterParser0 = MultiPrinterParser(None, None)
        try:
            multiPrinterParser0.isPrinter()
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "")

    def test09(self) -> None:

        money_printer_array0 = [None] * 2
        money_amount_style0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        amount_printer_parser0 = AmountPrinterParser(money_amount_style0)
        money_parser_array0 = [None] * 1
        money_parser_array0[0] = amount_printer_parser0
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        big_decimal0 = decimal.Decimal(10)
        money_parse_context0 = MoneyParseContext(
            5, "£", 2304, None, big_decimal0, 2304, None
        )

        try:
            multi_printer_parser0.parse(money_parse_context0)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test08(self) -> None:

        money_printer_array0 = [None] * 1
        literal_printer_parser0 = LiteralPrinterParser("Bx")
        money_parser_array0 = [None] * 2
        money_parser_array0[0] = literal_printer_parser0
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        locale0 = "de"
        currency_unit0 = CurrencyUnit.GBP
        big_decimal0 = 10
        money_parse_context0 = MoneyParseContext(
            8, "tRyAM_&cl9t3j", -10, locale0, big_decimal0, -10, currency_unit0
        )

        try:
            multi_printer_parser0.parse(money_parse_context0)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except StringIndexOutOfBoundsException:
            pass

    def test07(self) -> None:

        money_printer_array0 = [None] * 4
        money_parser_array0 = []
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        locale0 = Locale.US
        money_print_context0 = MoneyPrintContext(locale0)
        mock_file0 = MockFile("^23s*N:l2R.#[,)K%'")
        mock_file_writer0 = MockFileWriter(mock_file0, True)

        try:
            multi_printer_parser0.print(money_print_context0, mock_file_writer0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MultiPrinterParser", e)

    def test06(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("Bx")
        moneyPrinterArray0 = [literalPrinterParser0]
        moneyParserArray0 = []
        charBuffer0 = io.StringIO("Money iterator must not contain n~ll entriQs")
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)

        try:
            multiPrinterParser0.print(None, charBuffer0, None)
            self.fail("Expecting exception: ReadOnlyBufferException")

        except Exception as e:
            self.verifyException("java.nio.CharBuffer", e)

    def test05(self) -> None:

        money_printer_array0 = [None]
        multi_printer_parser0 = MultiPrinterParser(money_printer_array0, None)

        try:
            multi_printer_parser0.toString()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("java.util.Objects", e)

    def test04(self) -> None:
        moneyParserArray0 = [None] * 3
        moneyPrinterArray0 = [None] * 7
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        boolean0 = multiPrinterParser0.isParser()
        self.assertFalse(boolean0)

    def test03(self) -> None:

        money_printer_array0 = []
        money_parser_array0 = [None] * 1
        literal_printer_parser0 = LiteralPrinterParser("")
        money_parser_array0[0] = literal_printer_parser0
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        boolean0 = multi_printer_parser0.isParser()
        self.assertTrue(boolean0)

    def test02(self) -> None:
        moneyPrinterArray0 = [None] * 3
        moneyParserArray0 = [None] * 9
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        boolean0 = multiPrinterParser0.isPrinter()
        self.assertFalse(boolean0)

    def test01(self) -> None:

        money_printer_array0 = [None] * 2
        money_amount_style0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA
        amount_printer_parser0 = AmountPrinterParser(money_amount_style0)
        money_printer_array0[0] = amount_printer_parser0
        money_printer_array0[1] = amount_printer_parser0
        money_parser_array0 = [None] * 1
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        boolean0 = multi_printer_parser0.isPrinter()
        self.assertTrue(boolean0)

    def test00(self) -> None:

        locale0 = Locale("7<9]ug;4-LO2Sd(ns")
        moneyPrintContext0 = MoneyPrintContext(locale0)
        mockFileWriter0 = MockFileWriter("7<9]ug;4-LO2Sd(ns")
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        multiPrinterParser0.print(moneyPrintContext0, mockFileWriter0, None)
