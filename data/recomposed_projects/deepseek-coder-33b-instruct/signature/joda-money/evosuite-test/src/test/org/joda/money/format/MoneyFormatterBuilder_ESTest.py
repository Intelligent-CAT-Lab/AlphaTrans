from __future__ import annotations
import time
import locale
import re
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.format.LiteralPrinterParser import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.MoneyFormatterBuilder import *

# from src.test.org.joda.money.format.MoneyFormatterBuilder_ESTest_scaffolding import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *


class MoneyFormatterBuilder_ESTest(unittest.TestCase):

    def test23(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendAmountLocalized()
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test22(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatter0 = moneyFormatterBuilder0.toFormatter0()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendSigned0(
            moneyFormatter0, moneyFormatter0
        )
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test21(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencyCode()
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test20(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        try:
            moneyFormatterBuilder0.append0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)

    def test19(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendAmount0()
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test18(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencyNumericCode()
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test17(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencySymbolLocalized()
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test16(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendCurrencyNumeric3Code()
        self.assertIs(moneyFormatterBuilder1, moneyFormatterBuilder0)

    def test15(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()

        try:
            moneyFormatterBuilder0.appendAmount1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test14(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        locale0 = Locale.ROOT
        moneyParserArray0 = [None] * 6
        moneyPrinterArray0 = [None] * 1
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            690, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyFormatterBuilder1 = moneyFormatterBuilder0.append0(moneyFormatter0)
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test13(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendLiteral(None)
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test12(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        charArray0 = []
        charBuffer0 = "".join(charArray0)
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendLiteral(charBuffer0)
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test11(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        charArray0 = ["\0"]
        charBuffer0 = "".join(charArray0)
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendLiteral(charBuffer0)
        self.assertIs(moneyFormatterBuilder1, moneyFormatterBuilder0)

    def test10(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        try:
            moneyFormatterBuilder0.toFormatter1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test09(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        literalPrinterParser0 = LiteralPrinterParser(
            "org.joda.money.format.SignedPrinterParser"
        )
        moneyFormatterBuilder1 = moneyFormatterBuilder0.append1(
            literalPrinterParser0, literalPrinterParser0
        )
        self.assertIs(moneyFormatterBuilder1, moneyFormatterBuilder0)

    def test08(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()

        try:
            moneyFormatterBuilder0.appendSigned1(None, None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertEqual(str(e), "MoneyFormatter whenPositive must not be null")

    def test07(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        locale0 = ""
        moneyParserArray0 = []
        moneyPrinterArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -3822, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatterBuilder0.append0(moneyFormatter0)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "list index out of range")

    def test06(self) -> None:

        money_formatter_builder0 = MoneyFormatterBuilder()
        locale0 = Locale.ROOT
        money_parser_array0 = []
        multi_printer_parser0 = MultiPrinterParser(None, money_parser_array0)
        money_formatter0 = MoneyFormatter(
            -1550, locale0, money_parser_array0, None, multi_printer_parser0
        )

        try:
            money_formatter_builder0.append0(money_formatter0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MultiPrinterParser", e)

    def test05(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        charArray0 = ["\0"] * 5
        charBuffer0 = CharBuffer.wrap(charArray0)
        charBuffer1 = CharBuffer.wrap(charBuffer0)
        charBuffer0.compact()

        try:
            moneyFormatterBuilder0.appendLiteral(charBuffer1)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexOutOfBoundsException as e:
            verifyException("java.nio.HeapCharBuffer", e)

    def test04(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()

        try:
            moneyFormatterBuilder0.appendSigned0(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertEqual(
                str(e), "MoneyFormatter whenPositiveOrZero must not be null"
            )

    def test03(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyAmountStyle0 = MoneyAmountStyle.LOCALIZED_NO_GROUPING
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendAmount1(moneyAmountStyle0)
        self.assertIs(moneyFormatterBuilder1, moneyFormatterBuilder0)

    def test02(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        locale0 = Locale("N; y", "")
        moneyFormatter0 = moneyFormatterBuilder0.toFormatter1(locale0)
        self.assertIsNotNone(moneyFormatter0)

    def test01(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        locale0 = Locale.KOREAN
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 2
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            3, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyFormatter1 = moneyFormatter0.withLocale(locale0)
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendSigned0(
            moneyFormatter1, moneyFormatter0
        )
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)

    def test00(self) -> None:

        moneyFormatterBuilder0 = MoneyFormatterBuilder()
        moneyPrinterArray0 = []
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        locale0 = Locale.PRC
        moneyFormatter0 = MoneyFormatter(
            2303, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyFormatter1 = moneyFormatter0.withLocale(locale0)
        moneyFormatterBuilder1 = moneyFormatterBuilder0.appendSigned1(
            moneyFormatter0, moneyFormatter1, moneyFormatter1
        )
        self.assertIs(moneyFormatterBuilder0, moneyFormatterBuilder1)
