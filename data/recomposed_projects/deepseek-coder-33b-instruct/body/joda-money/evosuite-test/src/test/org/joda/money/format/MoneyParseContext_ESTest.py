from __future__ import annotations
import time
import locale
import re
import os
import decimal
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.format.MoneyParseContext import *

# from src.test.org.joda.money.format.MoneyParseContext_ESTest_scaffolding import *


class MoneyParseContext_ESTest(unittest.TestCase):

    def test55(self) -> None:

        bigDecimal0 = decimal.Decimal(0)
        moneyParseContext0 = MoneyParseContext(
            0, None, -2177, None, bigDecimal0, -2177, None
        )

        try:
            moneyParseContext0.setLocale(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test54(self) -> None:

        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(-1374.11854808)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0
        )
        moneyParseContext0.getAmount()
        self.assertEqual(2, moneyParseContext0.getIndex())
        self.assertEqual(2, moneyParseContext0.getErrorIndex())

    def test53(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        currencyUnit0 = CurrencyUnit.GBP
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, currencyUnit0
        )
        moneyParseContext0.setAmount(bigDecimal0)
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertEqual(5763, moneyParseContext0.getIndex())

    def test52(self) -> None:

        locale0 = Locale.CHINESE
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            956, None, 956, locale0, bigDecimal0, 956, None
        )

        try:
            moneyParseContext0.mergeChild(moneyParseContext0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test51(self) -> None:

        locale0 = "it_IT"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.EUR
        moneyParseContext0 = MoneyParseContext(
            0, "", 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        moneyParseContext0.setCurrency(currencyUnit0)

        try:
            moneyParseContext0.toBigMoney()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)

    def test50(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            2591, "Canada", 5763, locale0, bigDecimal0, 772, currencyUnit0
        )
        int0 = moneyParseContext0.getIndex()
        self.assertEqual(5763, int0)
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())

    def test49(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())

        moneyParseContext0.setError()
        self.assertEqual(5763, moneyParseContext0.getErrorIndex())

    def test48(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )

        try:
            moneyParseContext0.getTextLength()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyParseContext", e)

    def test47(self) -> None:

        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(-1374.11854808)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0
        )
        self.assertEqual(moneyParseContext0.getCurrency(), currencyUnit0)
        self.assertEqual(moneyParseContext0.getErrorIndex(), 2)
        self.assertEqual(moneyParseContext0.getIndex(), 2)

    def test46(self) -> None:

        locale0 = Locale.FRANCE
        bigDecimal0 = Decimal("10")
        moneyParseContext0 = MoneyParseContext(
            0, None, -2177, locale0, bigDecimal0, -2177, None
        )
        parsePosition0 = moneyParseContext0.toParsePosition()
        self.assertEqual(
            "java.text.ParsePosition[index=-2177,errorIndex=-1]", str(parsePosition0)
        )

    def test45(self) -> None:

        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(-1374.11854808)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0
        )

        with self.assertRaises(StringIndexOutOfBoundsException):
            moneyParseContext0.getTextSubstring(881, 134)

    def test44(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 22, locale0, None, 30, currencyUnit0
        )
        int0 = moneyParseContext0.getErrorIndex()
        self.assertEqual(22, moneyParseContext0.getIndex())
        self.assertEqual(30, int0)

    def test43(self) -> None:

        locale0 = Locale.TAIWAN
        bigDecimal0 = BigDecimal((-1374.11854808))
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0
        )
        moneyParseContext0.setErrorIndex((-3511))
        self.assertEqual((-3511), moneyParseContext0.getErrorIndex())

    def test42(self) -> None:

        locale0 = "CANADA_FRENCH"
        bigDecimal0 = decimal.Decimal(10)
        currencyUnit0 = CurrencyUnit.GBP
        moneyParseContext0 = MoneyParseContext(
            0, "", 5763, locale0, bigDecimal0, 5763, currencyUnit0
        )
        boolean0 = moneyParseContext0.isError()
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertFalse(boolean0)
        self.assertEqual(5763, moneyParseContext0.getIndex())

    def test41(self) -> None:

        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(-1374.11854808)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "iclboP6c>aTp{R`8", 2, locale0, bigDecimal0, 2, currencyUnit0
        )
        boolean0 = moneyParseContext0.isError()
        self.assertEqual(2, moneyParseContext0.getIndex())
        self.assertEqual(2, moneyParseContext0.getErrorIndex())
        self.assertTrue(boolean0)

    def test40(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 22, locale0, None, 30, currencyUnit0
        )
        boolean0 = moneyParseContext0.isFullyParsed()
        self.assertEqual(30, moneyParseContext0.getErrorIndex())
        self.assertFalse(boolean0)
        self.assertEqual(22, moneyParseContext0.getIndex())

    def test39(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        boolean0 = moneyParseContext0.isFullyParsed()
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertTrue(boolean0)

    def test38(self) -> None:

        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal("-1374.11854808")
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            2, "Taiwan", -3511, locale0, bigDecimal0, 0, currencyUnit0
        )
        boolean0 = moneyParseContext0.isComplete()
        self.assertEqual(-3511, moneyParseContext0.getIndex())
        self.assertFalse(boolean0)
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())

    def test37(self) -> None:

        charArray0 = [""] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        boolean0 = moneyParseContext0.isComplete()
        self.assertTrue(boolean0)
        self.assertTrue(moneyParseContext0.isFullyParsed())
        self.assertEqual(0, moneyParseContext0.getErrorIndex())

    def test36(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 22, locale0, None, 30, currencyUnit0
        )
        boolean0 = moneyParseContext0.isComplete()
        self.assertFalse(boolean0)
        self.assertEqual(30, moneyParseContext0.getErrorIndex())
        self.assertEqual(22, moneyParseContext0.getIndex())

    def test35(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        bigDecimal0 = decimal.Decimal(0)
        locale0 = 'RA4h@"7qvZz#.Kh<'
        currencyUnit0 = CurrencyUnit.JPY
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 855, currencyUnit0
        )
        moneyParseContext0.toBigMoney()
        self.assertEqual(855, moneyParseContext0.getErrorIndex())
        self.assertTrue(moneyParseContext0.isFullyParsed())

    def test34(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )

        try:
            moneyParseContext0.toBigMoney()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.format.MoneyFormatException", e)

    def test33(self) -> None:

        charArray0 = [""] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        self.assertTrue(moneyParseContext0.isFullyParsed())

        moneyParseContext0.setText("Taiwan")
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test32(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )
        self.assertEqual(locale0, moneyParseContext0.getLocale())
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertEqual(5763, moneyParseContext0.getIndex())

    def test31(self) -> None:

        locale0 = "ja_JP"
        bigDecimal0 = decimal.Decimal(10)
        charBuffer0 = " " * 1686
        moneyParseContext0 = MoneyParseContext(
            685, charBuffer0, 1686, locale0, bigDecimal0, 1686, None
        )

        try:
            moneyParseContext0.getTextSubstring(1686, -1051)
            self.fail("Expecting exception: IndexOutOfBoundsException")

        except IndexError as e:
            self.verifyException("java.nio.HeapCharBuffer", e)

    def test30(self) -> None:

        locale0 = Locale.FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )

        try:
            moneyParseContext0.getTextSubstring(5763, 5763)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyParseContext", e)

    def test29(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )

        try:
            moneyParseContext0.isFullyParsed()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyParseContext", e)

    def test28(self) -> None:

        locale0 = Locale.ITALY
        bigDecimal0 = BigDecimal.ONE
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            2649, None, 2649, locale0, bigDecimal0, 64, currencyUnit0
        )

        try:
            moneyParseContext0.mergeChild(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyParseContext", e)

    def test27(self) -> None:

        locale0 = Locale.KOREA
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            171, None, 171, locale0, bigDecimal0, 171, None
        )

        try:
            moneyParseContext0.setText(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.format.MoneyFormatter", e)

    def test26(self) -> None:

        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal(0.0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "Taiwan", 1776, locale0, bigDecimal0, 1278, currencyUnit0
        )
        moneyParseContext1 = moneyParseContext0.createChild()
        self.assertEqual(1776, moneyParseContext1.getIndex())
        self.assertEqual(1278, moneyParseContext1.getErrorIndex())
        self.assertTrue(moneyParseContext0.isError())
        self.assertEqual(1776, moneyParseContext0.getIndex())

    def test25(self) -> None:

        charArray0 = [""] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        moneyParseContext1 = moneyParseContext0.createChild()
        self.assertTrue(moneyParseContext1.isFullyParsed())
        self.assertEqual(0, moneyParseContext1.getErrorIndex())

    def test24(self) -> None:

        locale0 = "zh_CN"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CAD
        moneyParseContext0 = MoneyParseContext(
            0, None, -990, locale0, bigDecimal0, 77, currencyUnit0
        )
        moneyParseContext1 = moneyParseContext0.createChild()
        self.assertEqual(-1, moneyParseContext1.getErrorIndex())
        self.assertEqual(-990, moneyParseContext1.getIndex())

    def test23(self) -> None:

        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal("-472.55137")
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "Taiwan", 1, locale0, bigDecimal0, -1172, currencyUnit0
        )
        moneyParseContext0.getAmount()
        self.assertEqual(-1172, moneyParseContext0.getErrorIndex())
        self.assertEqual(1, moneyParseContext0.getIndex())

    def test22(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        moneyParseContext0.getAmount()
        self.assertEqual(0, moneyParseContext0.getErrorIndex())
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test21(self) -> None:

        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal(1)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "Taiwan", 0, locale0, bigDecimal0, 2, currencyUnit0
        )
        moneyParseContext0.getAmount()
        self.assertEqual(2, moneyParseContext0.getErrorIndex())
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test20(self) -> None:

        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal((-472.55137))
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            12, "Taiwan", 1, locale0, bigDecimal0, (-1172), currencyUnit0
        )
        moneyParseContext0.getAmount()
        self.assertEqual((-1), moneyParseContext0.getErrorIndex())
        self.assertEqual(1, moneyParseContext0.getIndex())

    def test19(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        bigDecimal0 = decimal.Decimal(0)
        locale0 = 'RA4h@"7qvZz#.Kh<'
        currencyUnit0 = CurrencyUnit.JPY
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 855, currencyUnit0
        )
        self.assertEqual(moneyParseContext0.getCurrency(), currencyUnit0)
        self.assertEqual(855, moneyParseContext0.getErrorIndex())
        self.assertTrue(moneyParseContext0.isFullyParsed())

    def test18(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )
        moneyParseContext0.getCurrency()
        self.assertEqual(5763, moneyParseContext0.getIndex())
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())

    def test17(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            2591, "Canada", 5763, locale0, bigDecimal0, 772, currencyUnit0
        )
        int0 = moneyParseContext0.getErrorIndex()
        self.assertEqual((-1), int0)
        self.assertEqual(5763, moneyParseContext0.getIndex())

    def test16(self) -> None:

        charArray0 = ["\0"] * 8
        charBuffer0 = "".join(charArray0)
        locale0 = "zh-Hant"
        bigDecimal0 = decimal.Decimal(1)
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, None
        )
        int0 = moneyParseContext0.getErrorIndex()
        self.assertEqual(0, moneyParseContext0.getIndex())
        self.assertEqual(0, int0)

    def test15(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        locale0 = Locale.UK
        bigDecimal0 = Decimal(2979)
        moneyParseContext0 = MoneyParseContext(
            2821, "", (-1172), locale0, bigDecimal0, 0, currencyUnit0
        )
        int0 = moneyParseContext0.getIndex()
        self.assertEqual((-1172), int0)
        self.assertEqual((-1), moneyParseContext0.getErrorIndex())

    def test14(self) -> None:

        charBuffer0 = ""
        locale0 = "zh_CN"
        bigDecimal0 = decimal.Decimal(1)
        currencyUnit0 = CurrencyUnit.AUD
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        int0 = moneyParseContext0.getIndex()
        self.assertEqual(0, moneyParseContext0.getErrorIndex())
        self.assertEqual(0, int0)

    def test13(self) -> None:

        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            999, "Taiwan", 0, None, bigDecimal0, 0, currencyUnit0
        )
        self.assertEqual(moneyParseContext0.getLocale(), None)
        self.assertEqual(moneyParseContext0.getIndex(), 0)
        self.assertEqual(moneyParseContext0.getErrorIndex(), -1)

    def test12(self) -> None:

        locale0 = "Taiwan"
        bigDecimal0 = decimal.Decimal(0.0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, "Taiwan", 1776, locale0, bigDecimal0, 1278, currencyUnit0
        )
        moneyParseContext0.getText()
        self.assertEqual(1278, moneyParseContext0.getErrorIndex())
        self.assertEqual(1776, moneyParseContext0.getIndex())

    def test11(self) -> None:

        locale0 = "zh"
        bigDecimal0 = decimal.Decimal(0.0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            810, "", (-1), locale0, bigDecimal0, (-2142), currencyUnit0
        )
        moneyParseContext0.getText()
        self.assertEqual((-1), moneyParseContext0.getErrorIndex())
        self.assertEqual((-1), moneyParseContext0.getIndex())

    def test10(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        moneyParseContext0 = MoneyParseContext(
            5763, None, 5763, locale0, bigDecimal0, 5763, None
        )
        moneyParseContext0.getText()
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertEqual(5763, moneyParseContext0.getIndex())

    def test09(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = Decimal(5763)
        moneyParseContext0 = MoneyParseContext(
            0, "Canada", 10, locale0, bigDecimal0, 222, None
        )
        moneyParseContext0.getTextLength()
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertEqual(10, moneyParseContext0.getIndex())

    def test08(self) -> None:

        charBuffer0 = ""
        locale0 = "zh_CN"
        bigDecimal0 = decimal.Decimal(1)
        currencyUnit0 = CurrencyUnit.AUD
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        moneyParseContext0.getTextLength()
        self.assertEqual(0, moneyParseContext0.getErrorIndex())
        self.assertTrue(moneyParseContext0.isFullyParsed())

    def test07(self) -> None:

        charArray0 = [""] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        moneyParseContext0.getTextSubstring(0, 0)
        self.assertEqual(0, moneyParseContext0.getErrorIndex())
        self.assertTrue(moneyParseContext0.isFullyParsed())

    def test06(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = BigDecimal.TEN
        charBuffer0 = CharBuffer.allocate(6)
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 1359, locale0, bigDecimal0, (-2447), None
        )
        string0 = moneyParseContext0.getTextSubstring(0, 6)
        self.assertEqual(1359, moneyParseContext0.getIndex())
        self.assertEqual(-1, moneyParseContext0.getErrorIndex())
        self.assertEqual("\u0000\u0000\u0000\u0000\u0000\u0000", string0)

    def test05(self) -> None:

        charArray0 = [""] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "Taiwan"
        currencyUnit0 = CurrencyUnit.GBP
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 22, locale0, None, 30, currencyUnit0
        )
        parsePosition0 = moneyParseContext0.toParsePosition()
        self.assertEqual(
            "java.text.ParsePosition[index=22,errorIndex=30]", str(parsePosition0)
        )

    def test04(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        parsePosition0 = moneyParseContext0.toParsePosition()
        self.assertEqual(
            "java.text.ParsePosition[index=0,errorIndex=0]", str(parsePosition0)
        )

    def test03(self) -> None:

        charArray0 = [""] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        moneyParseContext0.setLocale(locale0)
        self.assertEqual(0, moneyParseContext0.getErrorIndex())
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test02(self) -> None:

        charArray0 = ["\0"] * 5
        charBuffer0 = "".join(charArray0)
        locale0 = "taiwan"
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, bigDecimal0, 0, currencyUnit0
        )
        boolean0 = moneyParseContext0.isError()
        self.assertEqual(0, moneyParseContext0.getErrorIndex())
        self.assertTrue(boolean0)
        self.assertEqual(0, moneyParseContext0.getIndex())

    def test01(self) -> None:

        locale0 = Locale.CANADA_FRENCH
        bigDecimal0 = Decimal(5763)
        moneyParseContext0 = MoneyParseContext(
            0, "Canada", -2728, locale0, bigDecimal0, 222, None
        )
        moneyParseContext0.setIndex(-62)
        boolean0 = moneyParseContext0.isFullyParsed()
        self.assertEqual(-62, moneyParseContext0.getIndex())
        self.assertFalse(boolean0)

    def test00(self) -> None:

        charBuffer0 = ""
        locale0 = "en_US"
        currencyUnit0 = CurrencyUnit.CHF
        moneyParseContext0 = MoneyParseContext(
            0, charBuffer0, 0, locale0, None, -3019, currencyUnit0
        )
        moneyParseContext1 = moneyParseContext0.createChild()
        moneyParseContext1.mergeChild(moneyParseContext0)
        self.assertEqual(-3019, moneyParseContext1.getErrorIndex())
        self.assertEqual(0, moneyParseContext1.getIndex())
