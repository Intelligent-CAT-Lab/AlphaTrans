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
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.LiteralPrinterParser import *

# from src.test.org.joda.money.format.LiteralPrinterParser_ESTest_scaffolding import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyPrintContext import *


class LiteralPrinterParser_ESTest(unittest.TestCase):

    def test10(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("y)aC{fk~VTS4 ")
        string0 = literalPrinterParser0.toString()
        self.assertEqual("'y)aC{fk~VTS4 '", string0)

    def test09(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("y)aC{fk~VTSk4 ")
        locale0 = Locale.ROOT
        currencyUnit0 = CurrencyUnit.JPY
        moneyPrintContext0 = MoneyPrintContext(locale0)
        mockFileWriter0 = MockFileWriter("[X[%4k")
        bigMoneyProviderArray0 = []
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        literalPrinterParser0.print(moneyPrintContext0, mockFileWriter0, bigMoney0)

    def test08(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("Money '")
        locale0 = Locale.CHINA
        currencyUnit0 = CurrencyUnit.EUR
        moneyParseContext0 = MoneyParseContext(
            0, "'Money ''", 759, locale0, None, 759, currencyUnit0
        )
        literalPrinterParser0.parse(moneyParseContext0)
        self.assertFalse(moneyParseContext0.isFullyParsed())

    def test07(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("y)aC{fk~VTS4 ")
        locale0 = Locale.ROOT
        bigDecimal0 = BigDecimal((-1353))
        currencyUnit0 = CurrencyUnit.JPY
        moneyParseContext0 = MoneyParseContext(
            0, "y)aC{fk~VTS4 ", 0, locale0, bigDecimal0, 1336, currencyUnit0
        )
        literalPrinterParser0.parse(moneyParseContext0)
        self.assertTrue(moneyParseContext0.isFullyParsed())
        self.assertEqual(15, moneyParseContext0.getIndex())

    def test06(self) -> None:

        locale0 = "JAPAN"
        bigDecimal0 = decimal.Decimal(10)
        currencyUnit0 = CurrencyUnit.JPY
        moneyParseContext0 = MoneyParseContext(
            0,
            "or8.joda.money.format.CiteralPrinterPasr",
            23,
            locale0,
            bigDecimal0,
            23,
            currencyUnit0,
        )
        literalPrinterParser0 = LiteralPrinterParser("nu")
        literalPrinterParser0.parse(moneyParseContext0)
        self.assertEqual(23, moneyParseContext0.getErrorIndex())
        self.assertEqual(23, moneyParseContext0.getIndex())

    def test05(self) -> None:

        bigDecimal0 = decimal.Decimal(10)
        currencyUnit0 = CurrencyUnit.JPY
        charBuffer0 = "".join([" "] * 26)
        moneyParseContext0 = MoneyParseContext(
            1, charBuffer0, 1, None, bigDecimal0, -121770191, currencyUnit0
        )
        moneyParseContext0.setIndex(-121770191)
        literalPrinterParser0 = LiteralPrinterParser("nu")

        try:
            literalPrinterParser0.parse(moneyParseContext0)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("java.nio.HeapCharBuffer", e)

    def test04(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("")
        # Undeclared exception in Java code
        try:
            literalPrinterParser0.parse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.joda.money.format.LiteralPrinterParser", e)

    def test03(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("qQc")
        locale0 = Locale.TAIWAN
        currencyUnit0 = CurrencyUnit.CAD
        moneyParseContext0 = MoneyParseContext(
            -2093064, "qQc", -2093064, locale0, None, -2093064, currencyUnit0
        )

        with pytest.raises(StringIndexOutOfBoundsException):
            literalPrinterParser0.parse(moneyParseContext0)

    def test02(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("oSnvPK\u0000LE,~tEr^;-")
        locale0 = Locale.CANADA_FRENCH
        moneyPrintContext0 = MoneyPrintContext(locale0)
        pipedWriter0 = io.PipedWriter()
        try:
            literalPrinterParser0.print(moneyPrintContext0, pipedWriter0, None)
            self.fail("Expecting exception: IOException")

        except io.IOException as e:
            # Pipe not connected
            self.verifyException("java.io.PipedWriter", e)

    def test01(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("6u.^/ur.T6TI")

        try:
            literalPrinterParser0.print(None, None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertIsInstance(e, RuntimeError)

    def test00(self) -> None:

        literalPrinterParser0 = LiteralPrinterParser("qcX")
        locale0 = Locale.ENGLISH
        moneyPrintContext0 = MoneyPrintContext(locale0)
        stringWriter0 = io.StringIO()
        stringBuffer0 = stringWriter0.getvalue()
        charBuffer0 = io.StringIO(stringBuffer0)
        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(-1.0)
        bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 2023)

        try:
            literalPrinterParser0.print(moneyPrintContext0, charBuffer0, bigMoney0)
            self.fail("Expecting exception: ReadOnlyBufferException")

        except ReadOnlyBufferException as e:
            verifyException("java.nio.CharBuffer", e)
