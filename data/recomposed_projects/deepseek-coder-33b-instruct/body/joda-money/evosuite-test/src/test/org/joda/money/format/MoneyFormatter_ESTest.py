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
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.format.AmountPrinterParser import *
from src.main.org.joda.money.format.LiteralPrinterParser import *
from src.main.org.joda.money.format.MoneyAmountStyle import *
from src.main.org.joda.money.format.MoneyFormatter import *

# from src.test.org.joda.money.format.MoneyFormatter_ESTest_scaffolding import *
from src.main.org.joda.money.format.MoneyParseContext import *
from src.main.org.joda.money.format.MoneyParser import *
from src.main.org.joda.money.format.MoneyPrinter import *
from src.main.org.joda.money.format.MultiPrinterParser import *
from src.main.org.joda.money.format.SignedPrinterParser import *


class MoneyFormatter_ESTest(unittest.TestCase):

    def test53(self) -> None:

        locale0 = Locale.FRENCH
        moneyPrinterArray0 = []
        moneyParserArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyParserArray0[0] = signedPrinterParser0
        # Undeclared exception in Java code
        try:
            moneyFormatter0.parseBigMoney("T8")
            self.fail("Expecting exception: StackOverflowError")

        except StackOverflowError:
            # no message in exception (getMessage() returned null)
            pass

    def test52(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 6
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        boolean0 = moneyFormatter0.isPrinter()
        self.assertFalse(boolean0)

    def test51(self) -> None:

        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 7
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        locale0 = "CANADA"
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 360)

        try:
            moneyFormatter0.print0(bigMoney0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test50(self) -> None:

        locale0 = Locale.FRENCH
        moneyPrinterArray0 = []
        moneyParserArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            1, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyFormatter1 = moneyFormatter0.withLocale(locale0)
        self.assertIsNot(moneyFormatter1, moneyFormatter0)

    def test49(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 9
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        locale1 = moneyFormatter0.getLocale()
        self.assertEqual("deu", locale1.getISO3Language())

    def test48(self) -> None:

        money_printer_array0 = []
        money_parser_array0 = []
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        locale0 = Locale.JAPANESE
        money_formatter0 = MoneyFormatter(
            0, locale0, money_parser_array0, money_printer_array0, multi_printer_parser0
        )
        string0 = money_formatter0.toString()
        self.assertEqual("", string0)

    def test47(self) -> None:

        locale0 = Locale.ITALY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 18
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parse(None, -2593)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test46(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = None
        try:
            moneyFormatter0 = MoneyFormatter(
                0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Printers and parsers must match
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test45(self) -> None:

        locale0 = Locale.ITALY
        moneyParserArray0 = [None] * 1
        literalPrinterParser0 = LiteralPrinterParser(")")
        moneyParserArray0[0] = literalPrinterParser0
        moneyPrinterArray0 = [None] * 7
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            (-1585), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseMoney(
                "org.joda.money.format.LiteralPrinterParser@0000000001"
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)

    def test44(self) -> None:

        locale0 = Locale.FRENCH
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 7
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        charBuffer0 = CharBuffer.allocate(360)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseBigMoney(charBuffer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)

    def test43(self) -> None:

        locale0 = Locale.TRADITIONAL_CHINESE
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -1, locale0, moneyParserArray0, None, multiPrinterParser0
        )

        try:
            moneyFormatter0.parse("T8", -1)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException as e:
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test42(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 8
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            345, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parse("iP-Xow", 345)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test41(self) -> None:

        locale0 = Locale.ENGLISH
        moneyParserArray0 = [None] * 1
        moneyPrinterArray0 = [None] * 9
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            347, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        with pytest.raises(NotImplementedError):
            moneyFormatter0.parseMoney("")
            self.fail("Expecting exception: NotImplementedError")

    def test40(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 8
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            345, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        charArrayWriter0 = io.StringIO()
        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, 345)

        try:
            moneyFormatter0.print1(charArrayWriter0, bigMoney0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test39(self) -> None:

        locale0 = Locale.KOREA
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        moneyFormatter0 = MoneyFormatter(
            64, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.isParser()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test38(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 9
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        writer0 = io.StringIO()
        currencyUnit0 = CurrencyUnit.of2(locale0)
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, 988)

        try:
            moneyFormatter0.printIO(writer0, bigMoney0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test37(self) -> None:

        locale0 = Locale.ENGLISH
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 3
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseBigMoney("")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)

    def test36(self) -> None:

        locale0 = Locale.JAPAN
        moneyParserArray0 = [None] * 3
        literalPrinterParser0 = LiteralPrinterParser(
            "Parsing did not find both currency and amount: "
        )
        moneyParserArray0[0] = literalPrinterParser0
        moneyParserArray0[1] = literalPrinterParser0
        moneyPrinterArray0 = [None] * 3
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyParserArray0[2] = multiPrinterParser0
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseBigMoney(
                "Parsing did not find both currency and amount: "
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)

    def test35(self) -> None:

        locale0 = Locale("Mt0K")
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        moneyFormatter0 = MoneyFormatter(
            -701, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parse("Mt0K", 1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test34(self) -> None:

        locale0 = Locale.JAPAN
        moneyParserArray0 = [None] * 3
        moneyPrinterArray0 = [None] * 3
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parse("Parsing did not find both currency and amount: ", 0)
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test33(self) -> None:

        moneyPrinterArray0 = []
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        locale0 = Locale.KOREAN
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyParseContext0 = moneyFormatter0.parse("", 0)
        self.assertFalse(moneyParseContext0.isError())
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test32(self) -> None:

        locale0 = Locale.US
        moneyFormatter0 = None
        try:
            moneyFormatter0 = MoneyFormatter(-248, locale0, None, None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # PrinterParser must not be null
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test31(self) -> None:
        with pytest.raises(ValueError) as e:
            MoneyFormatter.checkNotNull(None, "00")
        assert str(e.value) == "Expecting exception: RuntimeError"

    def test30(self) -> None:

        locale0 = Locale.ITALY
        moneyParserArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -1585, locale0, moneyParserArray0, None, multiPrinterParser0
        )

        try:
            moneyFormatter0.isPrinter()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test29(self) -> None:

        locale0 = Locale.ENGLISH
        moneyParserArray0 = []
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            362, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseBigMoney(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test28(self) -> None:

        locale0 = Locale.GERMAN
        multiPrinterParser0 = MultiPrinterParser(None, None)
        moneyFormatter0 = MoneyFormatter(45, locale0, None, None, multiPrinterParser0)

        try:
            moneyFormatter0.parseBigMoney(
                "MoneyFormatter whenNegative must not be null"
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test27(self) -> None:

        locale0 = Locale.TAIWAN
        moneyParserArray0 = [None] * 1
        moneyPrinterArray0 = [None] * 3
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseBigMoney("")
            self.fail("Expecting exception: NotImplementedError")

        except NotImplementedError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test26(self) -> None:

        locale0 = Locale.CHINA
        moneyParserArray0 = [None] * 1
        moneyPrinterArray0 = [None] * 9
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            (-491), locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseMoney(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test25(self) -> None:

        locale0 = Locale.GERMANY
        moneyPrinterArray0 = [None] * 2
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        moneyFormatter0 = MoneyFormatter(
            15, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )

        try:
            moneyFormatter0.parseMoney("^tB>YZKnrW_8bt+}=P")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test24(self) -> None:

        locale0 = Locale.CHINESE
        moneyParserArray0 = [None] * 2
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            44, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyParserArray0[0] = signedPrinterParser0
        moneyAmountStyle0 = MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_SPACE
        amountPrinterParser0 = AmountPrinterParser(moneyAmountStyle0)
        moneyParserArray0[1] = amountPrinterParser0

        try:
            moneyFormatter0.parseMoney("0Z0")
            self.fail("Expecting exception: StackOverflowError")
        except StackOverflowError:
            pass

    def test23(self) -> None:

        locale0 = Locale.US
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -1545, locale0, moneyParserArray0, None, multiPrinterParser0
        )

        try:
            moneyFormatter0.print0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test22(self) -> None:

        locale0 = Locale.CANADA
        moneyParserArray0 = [None] * 5
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -1510, locale0, moneyParserArray0, None, multiPrinterParser0
        )
        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.ofMinor(currencyUnit0, -1510)

        try:
            moneyFormatter0.print0(money0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test21(self) -> None:

        money_printer_array0 = [None] * 1
        locale0 = Locale.JAPAN
        money_parser_array0 = [None] * 8
        multi_printer_parser0 = MultiPrinterParser(
            money_printer_array0, money_parser_array0
        )
        money_formatter0 = MoneyFormatter(
            67,
            locale0,
            money_parser_array0,
            money_printer_array0,
            multi_printer_parser0,
        )
        signed_printer_parser0 = SignedPrinterParser(
            money_formatter0, money_formatter0, money_formatter0
        )
        money_printer_array0[0] = signed_printer_parser0
        currency_unit0 = CurrencyUnit.EUR
        big_money0 = BigMoney.ofScale2(currency_unit0, 67, 3696)

        try:
            money_formatter0.print0(big_money0)
            self.fail("Expecting exception: StackOverflowError")
        except StackOverflowError:
            pass

    def test20(self) -> None:

        locale0 = Locale.ITALY
        moneyParserArray0 = [None] * 1
        moneyPrinterArray0 = [None] * 2
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyPrinterArray0[0] = multiPrinterParser0
        moneyFormatter0 = MoneyFormatter(
            -1585, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        signedPrinterParser0 = SignedPrinterParser(
            moneyFormatter0, moneyFormatter0, moneyFormatter0
        )
        moneyPrinterArray0[1] = signedPrinterParser0
        currencyUnit0 = CurrencyUnit.of2(locale0)
        bigMoney0 = BigMoney.zero0(currencyUnit0)

        try:
            moneyFormatter0.print0(bigMoney0)
            self.fail("Expecting exception: StackOverflowError")
        except StackOverflowError:
            pass

    def test19(self) -> None:

        locale0 = Locale.TRADITIONAL_CHINESE
        moneyParserArray0 = []
        moneyPrinterArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            347, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        charArray0 = []
        charBuffer0 = CharBuffer.wrap(charArray0)

        try:
            moneyFormatter0.print1(charBuffer0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test18(self) -> None:

        locale0 = "JAPAN"
        moneyParserArray0 = [None] * 3
        literalPrinterParser0 = LiteralPrinterParser(
            "Parsing did not find both currency and amount: "
        )
        moneyPrinterArray0 = [None] * 3
        moneyPrinterArray0[0] = literalPrinterParser0
        moneyPrinterArray0[1] = literalPrinterParser0
        moneyPrinterArray0[2] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        currencyUnit0 = CurrencyUnit.EUR
        pipedWriter0 = io.StringIO()
        bigDecimal0 = decimal.Decimal(10)
        roundingMode0 = decimal.ROUND_CEILING
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 0, roundingMode0)

        try:
            moneyFormatter0.print1(pipedWriter0, bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test17(self) -> None:

        locale0 = Locale.FRENCH
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 7
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            360, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        charBuffer0 = CharBuffer.allocate(360)

        try:
            moneyFormatter0.printIO(charBuffer0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test16(self) -> None:

        locale0 = Locale.FRENCH
        moneyParserArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            3282, locale0, moneyParserArray0, None, multiPrinterParser0
        )
        mockPrintStream0 = MockPrintStream("/N:#WZU4w,}}ag")
        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -1)

        try:
            moneyFormatter0.printIO(mockPrintStream0, bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test15(self) -> None:

        multiPrinterParser0 = MultiPrinterParser(None, None)
        locale0 = Locale.ROOT
        moneyFormatter0 = MoneyFormatter(525, locale0, None, None, multiPrinterParser0)

        try:
            moneyFormatter0.toString()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test14(self) -> None:

        locale0 = Locale.ITALY
        moneyParserArray0 = [None]
        multiPrinterParser0 = MultiPrinterParser(None, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -3557, locale0, moneyParserArray0, None, multiPrinterParser0
        )

        try:
            moneyFormatter0.withLocale(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test13(self) -> None:

        locale0 = Locale.JAPAN
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        moneyFormatter0 = MoneyFormatter(
            1805, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        multiPrinterParser1 = moneyFormatter0.getPrinterParser()
        self.assertIs(multiPrinterParser0, multiPrinterParser1)

    def test12(self) -> None:

        locale0 = Locale.PRC
        moneyPrinterArray0 = [None] * 1
        moneyParserArray0 = [None] * 10
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            535, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        boolean0 = moneyFormatter0.isParser()
        self.assertFalse(boolean0)

    def test11(self) -> None:

        locale0 = Locale.PRC
        moneyPrinterArray0 = [None] * 1
        moneyParserArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            535, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        boolean0 = moneyFormatter0.isParser()
        self.assertTrue(boolean0)

    def test10(self) -> None:

        locale0 = Locale.JAPANESE
        moneyParserArray0 = [None] * 1
        amountPrinterParser0 = AmountPrinterParser(None)
        moneyPrinterArray0 = [None] * 2
        moneyPrinterArray0[0] = amountPrinterParser0
        moneyPrinterArray0[1] = amountPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            274, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        boolean0 = moneyFormatter0.isPrinter()
        self.assertTrue(boolean0)

    def test09(self) -> None:

        locale0 = Locale.JAPAN
        moneyParserArray0 = [None] * 3
        literalPrinterParser0 = LiteralPrinterParser(
            "Parsing did not find both currency and amount: "
        )
        moneyParserArray0[0] = literalPrinterParser0
        moneyParserArray0[1] = literalPrinterParser0
        moneyPrinterArray0 = [None] * 3
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyParserArray0[2] = multiPrinterParser0
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyParseContext0 = moneyFormatter0.parse(
            "Parsing did not find both currency and amount: ", 0
        )
        self.assertEqual(47, moneyParseContext0.getErrorIndex())

    def test08(self) -> None:

        locale0 = Locale.CHINA
        moneyParserArray0 = [None] * 1
        literalPrinterParser0 = LiteralPrinterParser(
            "Cannot convert using a negative conversion multiplier"
        )
        moneyParserArray0[0] = literalPrinterParser0
        moneyPrinterArray0 = [None] * 9
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            3531, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        moneyParseContext0 = moneyFormatter0.parse(
            "org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001org.joda.money.format.LiteralPrinterParser@0000000001:org.joda.money.format.LiteralPrinterParser@0000000001",
            0,
        )
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test07(self) -> None:

        locale0 = "ko_KR"
        moneyPrinterArray0 = []
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, None)
        moneyFormatter0 = MoneyFormatter(
            2041, locale0, None, moneyPrinterArray0, multiPrinterParser0
        )
        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.ofMinor(currencyUnit0, -795)
        string0 = moneyFormatter0.print0(money0)
        self.assertEqual("", string0)

    def test06(self) -> None:

        locale0 = Locale.JAPAN
        moneyParserArray0 = [None] * 3
        literalPrinterParser0 = LiteralPrinterParser(
            "Parsing did not find both currency and amount: "
        )
        moneyPrinterArray0 = [None] * 3
        moneyPrinterArray0[0] = literalPrinterParser0
        moneyPrinterArray0[1] = literalPrinterParser0
        moneyPrinterArray0[2] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        currencyUnit0 = CurrencyUnit.of2(locale0)
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, (-3667))
        string0 = moneyFormatter0.print0(bigMoney0)
        self.assertEqual(
            "Parsing did not find both currency and amount: Parsing did not find both currency and amount: Parsing did not find both currency and amount: ",
            string0,
        )

    def test05(self) -> None:

        locale0 = Locale.ITALY
        moneyParserArray0 = [None] * 1
        literalPrinterParser0 = LiteralPrinterParser(")")
        moneyParserArray0[0] = literalPrinterParser0
        moneyPrinterArray0 = [None] * 7
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            -1585, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        string0 = moneyFormatter0.toString()
        self.assertIsNotNone(string0)

    def test04(self) -> None:
        MoneyFormatter.checkNotNull("00", "00")

    def test03(self) -> None:

        locale0 = Locale.JAPANESE
        moneyParserArray0 = [None] * 7
        literalPrinterParser0 = LiteralPrinterParser(
            "Parsing did not find both currency and amount: "
        )
        moneyPrinterArray0 = [None] * 2
        moneyPrinterArray0[0] = literalPrinterParser0
        moneyPrinterArray0[1] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            30, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        writer0 = io.StringIO()
        mockPrintWriter0 = MockPrintWriter(writer0, True)
        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        moneyFormatter0.print1(mockPrintWriter0, bigMoney0)

    def test02(self) -> None:

        locale0 = Locale.JAPAN
        moneyParserArray0 = [None] * 3
        literalPrinterParser0 = LiteralPrinterParser(
            "Parsing did not find both currency and amount: "
        )
        moneyPrinterArray0 = [None] * 3
        moneyPrinterArray0[0] = literalPrinterParser0
        moneyPrinterArray0[1] = literalPrinterParser0
        moneyPrinterArray0[2] = literalPrinterParser0
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        currencyUnit0 = CurrencyUnit.of2(locale0)
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -3667)
        mockPrintWriter0 = MockPrintWriter("Money amount '")
        moneyFormatter0.printIO(mockPrintWriter0, bigMoney0)

    def test01(self) -> None:

        locale0 = Locale.ROOT
        moneyParserArray0 = [None] * 7
        moneyPrinterArray0 = [None] * 6
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = None
        try:
            moneyFormatter0 = MoneyFormatter(
                0, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Printers and parsers must match
            self.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test00(self) -> None:

        locale0 = Locale.GERMANY
        moneyParserArray0 = []
        moneyPrinterArray0 = [None] * 8
        multiPrinterParser0 = MultiPrinterParser(moneyPrinterArray0, moneyParserArray0)
        moneyFormatter0 = MoneyFormatter(
            345, locale0, moneyParserArray0, moneyPrinterArray0, multiPrinterParser0
        )
        charBuffer0 = CharBuffer.allocate(64)
        try:
            moneyFormatter0.parseBigMoney(charBuffer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)
