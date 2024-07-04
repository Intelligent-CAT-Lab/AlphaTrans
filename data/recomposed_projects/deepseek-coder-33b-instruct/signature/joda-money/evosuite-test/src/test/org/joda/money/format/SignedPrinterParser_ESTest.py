from __future__ import annotations
import math
import time
import locale
import re
import os
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
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *
from src.main.org.joda.money.format.SignedPrinterParser import *

# from src.test.org.joda.money.format.SignedPrinterParser_ESTest_scaffolding import *


class SignedPrinterParser_ESTest(unittest.TestCase):

    def test14(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = [None] * 0
        moneyPrinterArray0 = [None] * 0
        moneyParserArray1 = [None] * 5
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        string0 = signedPrinterParser0.toString()
        self.assertEqual("PositiveZeroNegative(,,)", string0)

    def test13(self) -> None:

        locale0 = Locale.US
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 8
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            13, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyPrintContext0 = MoneyPrintContext(locale0)
        charArrayWriter0 = io.StringIO()
        currencyUnit0 = CurrencyUnit.USD
        priorityQueue0 = []
        bigMoney0 = BigMoney.total3(currencyUnit0, priorityQueue0)
        bigMoney1 = bigMoney0.plus3(-336)

        try:
            signedPrinterParser0.print(moneyPrintContext0, charArrayWriter0, bigMoney1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test12(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tH&'pPq)pA6s")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            (-2321), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter0, moneyFormatter1
        )
        moneyParseContext0 = moneyFormatter0.parse("h&5'pP)A6s", 2)
        signedPrinterParser0.parse(moneyParseContext0)
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertFalse(moneyParseContext0.isError())
        self.assertEqual((-1), moneyParseContext0.getErrorIndex())

    def test11(self) -> None:

        locale0 = Locale.US
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 8
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyParseContext0 = moneyFormatter0.parse("B&OcG@", 1)
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertFalse(moneyParseContext0.isComplete())

    def test10(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tOH&['pPq)pAhs")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            -1696, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter1, moneyFormatter0
        )
        moneyParseContext0 = moneyFormatter0.parse("eF^~)9H3THVdSR", 2)

        try:
            signedPrinterParser0.parse(moneyParseContext0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.money.format.SignedPrinterParser", e)

    def test09(self) -> None:

        locale0 = Locale.CANADA
        moneyParserArray0 = [None] * 6
        literalPrinterParser0 = LiteralPrinterParser(
            "Money array must not contain null entries"
        )
        moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_COMMA_NO_GROUPING
        amountPrinterParser0 = AmountPrinterParser(moneyAmountStyle0)
        moneyPrinterArray0 = []
        moneyParserArray1 = [None] * 7
        moneyParserArray1[0] = literalPrinterParser0
        moneyParserArray1[1] = literalPrinterParser0
        moneyParserArray1[2] = literalPrinterParser0
        moneyParserArray1[3] = amountPrinterParser0
        moneyParserArray1[4] = literalPrinterParser0
        moneyParserArray1[5] = amountPrinterParser0
        moneyParserArray1[6] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter0 = MoneyFormatter(
            10, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyParseContext0 = moneyFormatter0.parse("jrtc?4Wx']L{T4", 10)
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertFalse(moneyParseContext0.isFullyParsed())

    def test08(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tH&'pPq)pA6s")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            (-2321), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter0, moneyFormatter1
        )
        moneyParseContext0 = moneyFormatter0.parse("h&5'pP)A6s", 2)
        bigDecimal0 = BigDecimal.ONE
        moneyParseContext0.setAmount(bigDecimal0)
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertFalse(moneyParseContext0.isError())
        self.assertEqual((-1), moneyParseContext0.getErrorIndex())

    def test07(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tOH&['pPq)pAhs")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            -1696, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter1, moneyFormatter0
        )
        moneyParseContext0 = moneyFormatter0.parse("eF^~)9H3THVdSR", 2)
        bigDecimal0 = BigDecimal.ONE
        moneyParseContext0.setAmount(bigDecimal0)
        signedPrinterParser0.parse(moneyParseContext0)
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertFalse(moneyParseContext0.isError())

    def test06(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        moneyParserArray0 = [None] * 3
        moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_NO_GROUPING
        amountPrinterParser0 = AmountPrinterParser(moneyAmountStyle0)
        moneyParserArray0[0] = amountPrinterParser0
        moneyPrinterArray0 = [None] * 6
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            88, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        bigDecimal0 = BigDecimal.ONE
        currencyUnit0 = CurrencyUnit.EUR
        moneyParseContext0 = MoneyParseContext(
            88,
            "org.joda.money.format.MoneyPrintContext",
            88,
            locale0,
            bigDecimal0,
            (-1081),
            currencyUnit0,
        )

        try:
            signedPrinterParser0.parse(moneyParseContext0)
            self.fail("Expecting exception: NegativeArraySizeException")

        except NegativeArraySizeException as e:
            verifyException("org.joda.money.format.AmountPrinterParser", e)

    def test05(self) -> None:

        locale0 = Locale.GERMANY
        moneyPrinterArray0 = [MoneyPrinter()]
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            3, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        mathContext0 = MathContext.DECIMAL64
        bigDecimal0 = BigDecimal((-2042), mathContext0)
        currencyUnit0 = CurrencyUnit.of2(locale0)
        moneyParseContext0 = MoneyParseContext(
            3, None, (-2042), locale0, bigDecimal0, 88, currencyUnit0
        )

        try:
            signedPrinterParser0.parse(moneyParseContext0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test04(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = [None]
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tH&'pPq)pA6s")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1720, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            2, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter0, moneyFormatter1
        )
        moneyParseContext0 = moneyFormatter0.parse("tH&'pPq)pA6s", 2)
        moneyParseContext0.setIndex(-4962)

        try:
            signedPrinterParser0.parse(moneyParseContext0)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")
        except StringIndexOutOfBoundsException:
            pass

    def test03(self) -> None:

        locale0 = Locale.TAIWAN
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            999, locale0, moneyParserArray0, None, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )

        try:
            signedPrinterParser0.toString()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test02(self) -> None:

        locale0 = Locale.CANADA
        moneyParserArray0 = [None] * 6
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            10, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyPrintContext0 = MoneyPrintContext(locale0)
        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -417)
        signedPrinterParser0.print(moneyPrintContext0, None, bigMoney0)

    def test01(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tH&'pPq)pA6s")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1691, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            (-2321), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        moneyParseContext0 = moneyFormatter0.parse("h&5'pP)A6s", 2)
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter0, moneyFormatter0
        )
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertFalse(moneyParseContext0.isError())
        self.assertEqual((-1), moneyParseContext0.getErrorIndex())

    def test00(self) -> None:

        locale0 = Locale.KOREAN
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 14
        moneyParserArray1 = [None] * 5
        literalPrinterParser0 = LiteralPrinterParser("tH&-pPq)pA6s")
        moneyParserArray1[0] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1743, locale0, moneyParserArray1, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray1)
        moneyFormatter1 = MoneyFormatter(
            11, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser1
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter1, moneyFormatter0, moneyFormatter1
        )
        moneyParseContext0 = moneyFormatter0.parse("tH&-pPq)pA6s", 11)
        byteArray0 = bytearray(6)
        byteArray0[0] = -1
        bigInteger0 = BigInteger(byteArray0)
        bigDecimal0 = BigDecimal(bigInteger0)
        moneyParseContext0.setAmount(bigDecimal0)
        signedPrinterParser0.parse(moneyParseContext0)
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertFalse(moneyParseContext0.isError())
