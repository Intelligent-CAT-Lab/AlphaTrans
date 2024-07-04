from __future__ import annotations
import time
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
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.MoneyUtils import *

# from src.test.org.joda.money.MoneyUtils_ESTest_scaffolding import *


class MoneyUtils_ESTest(unittest.TestCase):

    def test70(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -393)
        money1 = Money(-2428, bigMoney0)

        try:
            MoneyUtils.min0(money0, money1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test69(self) -> None:
        boolean0 = MoneyUtils.isZero(None)
        self.assertTrue(boolean0)

    def test68(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -1139)
        boolean0 = MoneyUtils.isZero(bigMoney0)
        self.assertTrue(boolean0)

    def test67(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -1)
        boolean0 = MoneyUtils.isZero(bigMoney0)
        self.assertFalse(boolean0)

    def test66(self) -> None:
        boolean0 = MoneyUtils.isPositive(None)
        self.assertFalse(boolean0)

    def test65(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.zero(currencyUnit0)
        boolean0 = MoneyUtils.isPositive(money0)
        self.assertFalse(boolean0)

    def test64(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(10)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        boolean0 = MoneyUtils.isPositive(money0)
        self.assertTrue(boolean0)

    def test63(self) -> None:
        boolean0 = MoneyUtils.isPositiveOrZero(None)
        self.assertTrue(boolean0)

    def test62(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.ofMinor(currencyUnit0, 0)
        boolean0 = MoneyUtils.isPositiveOrZero(money0)
        self.assertTrue(boolean0)

    def test61(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.ofMinor(currencyUnit0, -1011)
        boolean0 = MoneyUtils.isPositiveOrZero(money0)
        self.assertFalse(boolean0)

    def test60(self) -> None:
        boolean0 = MoneyUtils.isNegative(None)
        self.assertFalse(boolean0)

    def test59(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -1139)
        boolean0 = MoneyUtils.isNegative(bigMoney0)
        self.assertFalse(boolean0)

    def test58(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, -1)
        boolean0 = MoneyUtils.isNegative(bigMoney0)
        self.assertTrue(boolean0)

    def test57(self) -> None:
        boolean0 = MoneyUtils.isNegativeOrZero(None)
        self.assertTrue(boolean0)

    def test56(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        boolean0 = MoneyUtils.isNegativeOrZero(money0)
        self.assertTrue(boolean0)

    def test55(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(1.0)
        bigMoney1 = bigMoney0.withAmount0(bigDecimal0)
        money0 = Money.of4(bigMoney1)
        boolean0 = MoneyUtils.isNegativeOrZero(money0)
        self.assertFalse(boolean0)

    def test54(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        list0 = []
        money0 = Money.total3(currencyUnit0, list0)
        money1 = MoneyUtils.max0(money0, None)
        self.assertFalse(list0.contains(money1))

    def test53(self) -> None:
        money0 = MoneyUtils.max0(None, None)
        self.assertIsNone(money0)

    def test52(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.ofMajor(currencyUnit0, -1)
        money1 = MoneyUtils.max0(money0, money0)
        self.assertIs(money0, money1)

    def test51(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.ofMajor(currencyUnit0, -1)
        moneyArray0 = [money0, money0, money0]
        money1 = Money.total2(currencyUnit0, moneyArray0)
        money2 = MoneyUtils.max0(money0, money1)
        self.assertIsNot(money2, money1)

    def test50(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        roundingMode0 = RoundingMode.DOWN
        money0 = Money.of3(currencyUnit0, (-2687.757945337272), roundingMode0)
        money1 = MoneyUtils.min0(None, money0)
        self.assertIs(money1, money0)

    def test49(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        money1 = MoneyUtils.min0(money0, None)
        self.assertIs(money1, money0)

    def test48(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -1139, -1139)
        roundingMode0 = RoundingMode.DOWN
        money0 = bigMoney0.toMoney1(roundingMode0)
        money1 = MoneyUtils.min0(money0, money0)
        self.assertIs(money1, money0)

    def test47(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.ofMinor(currencyUnit0, -1)
        money1 = MoneyUtils.add0(money0, money0)
        money2 = MoneyUtils.min0(money1, money0)
        self.assertIsNot(money2, money0)

    def test46(self) -> None:
        money0 = MoneyUtils.add0(None, None)
        self.assertIsNone(money0)

    def test45(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        money1 = MoneyUtils.add0(money0, None)
        self.assertIs(money1, money0)

    def test44(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.of2(currencyUnit0, 0)
        money1 = MoneyUtils.subtract0(None, money0)
        self.assertEqual(money0, money1)

    def test43(self) -> None:
        money0 = MoneyUtils.subtract0(None, None)
        self.assertIsNone(money0)

    def test42(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        money0 = Money(0, bigMoney0)

        try:
            MoneyUtils.subtract0(money0, money0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.Money", e)

    def test41(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -1139, -1139)
        bigMoney1 = MoneyUtils.max1(bigMoney0, bigMoney0)
        self.assertIs(bigMoney1, bigMoney0)

    def test40(self) -> None:
        bigMoney0 = MoneyUtils.max1(None, None)
        self.assertIsNone(bigMoney0)

    def test39(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = MoneyUtils.max1(bigMoney0, None)
        self.assertIs(bigMoney1, bigMoney0)

    def test38(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -498)
        bigMoney1 = MoneyUtils.subtract1(bigMoney0, bigMoney0)
        bigMoney2 = MoneyUtils.max1(bigMoney1, bigMoney0)
        self.assertIsNot(bigMoney2, bigMoney0)

    def test37(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -1139, -1139)
        bigMoney1 = MoneyUtils.min1(bigMoney0, bigMoney0)
        self.assertIs(bigMoney0, bigMoney1)

    def test36(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -1139)
        bigMoney1 = MoneyUtils.min1(None, bigMoney0)
        self.assertIs(bigMoney1, bigMoney0)

    def test35(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 1, 0)
        bigMoney1 = MoneyUtils.min1(bigMoney0, None)
        self.assertEqual(bigMoney1, bigMoney0)

    def test34(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -1139, -1139)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = BigMoney.of0(currencyUnit0, bigDecimal0)
        bigMoney2 = MoneyUtils.min1(bigMoney0, bigMoney1)

        self.assertIsNot(bigMoney2, bigMoney1)

    def test33(self) -> None:
        bigMoney0 = MoneyUtils.add1(None, None)
        self.assertIsNone(bigMoney0)

    def test32(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -84)
        bigMoney1 = MoneyUtils.add1(bigMoney0, None)
        self.assertEqual(bigMoney0, bigMoney1)

    def test31(self) -> None:

        bigMoney0 = MoneyUtils.subtract1(None, None)
        self.assertIsNone(bigMoney0)

    def test30(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 1, 0)
        bigMoney1 = MoneyUtils.subtract1(None, bigMoney0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test29(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -208)
        bigDecimal0 = decimal.Decimal(-1962.0)
        bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 92)
        money1 = Money(92, bigMoney0)

        try:
            MoneyUtils.add0(money0, money1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test28(self) -> None:

        money0 = Money(832, None)

        try:
            MoneyUtils.add0(money0, money0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test27(self) -> None:

        bigDecimal0 = decimal.Decimal(0)
        currencyUnit0 = CurrencyUnit(
            "Invalid string code, must be ASCII upper-case letters", 1464, 1464
        )
        bigMoney0 = BigMoney(1, bigDecimal0, currencyUnit0)

        try:
            MoneyUtils.add1(bigMoney0, bigMoney0)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test26(self) -> None:
        with pytest.raises(ValueError) as e:
            MoneyUtils.checkNotNull(None, "yicM=6Mo4ibkj")
        assert str(e.value) == "yicM=6Mo4ibkj"

    def test25(self) -> None:

        money0 = Money(100, None)

        try:
            MoneyUtils.isNegative(money0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test24(self) -> None:

        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney(-66, bigDecimal0, None)

        try:
            MoneyUtils.isPositive(bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test22(self) -> None:

        bigDecimal0 = decimal.Decimal(1)
        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney((-749), bigDecimal0, currencyUnit0)

        try:
            MoneyUtils.max1(bigMoney0, bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test21(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -1139)
        currencyUnit1 = CurrencyUnit.EUR
        bigMoneyProviderArray0 = []
        bigMoney1 = BigMoney.total2(currencyUnit1, bigMoneyProviderArray0)

        try:
            MoneyUtils.max1(bigMoney1, bigMoney0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test20(self) -> None:

        money0 = Money(832, None)

        try:
            MoneyUtils.min0(money0, money0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Joda-Money bug: BigMoney must not be null")

    def test19(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        currencyUnit1 = CurrencyUnit.JPY
        money1 = Money.ofMajor(currencyUnit1, -340)

        try:
            MoneyUtils.min0(money0, money1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test18(self) -> None:

        bigDecimal0 = decimal.Decimal(-1)
        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney(-1, bigDecimal0, currencyUnit0)

        try:
            MoneyUtils.min1(bigMoney0, bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test17(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = Money.of0(currencyUnit0, bigDecimal0)
        currencyUnit1 = CurrencyUnit.CHF
        bigMoney1 = Money.ofScale2(currencyUnit1, 59, 0)

        # Undeclared exception in Java code
        try:
            MoneyUtils.min1(bigMoney1, bigMoney0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Currencies differ: CHF/USD
            self.verifyException("org.joda.money.BigMoney", e)

    def test16(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        money1 = Money((-1), None)

        try:
            MoneyUtils.subtract0(money0, money1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            # BigMoneyProvider must not return null
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test15(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney(1755, None, currencyUnit0)

        try:
            MoneyUtils.subtract1(bigMoney0, bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test14(self) -> None:
        money0 = MoneyUtils.min0(None, None)
        self.assertIsNone(money0)

    def test13(self) -> None:
        bigMoney0 = MoneyUtils.min1(None, None)
        self.assertIsNone(bigMoney0)

    def test12(self) -> None:
        object0 = object()
        MoneyUtils.checkNotNull(object0, "")

    def test11(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        money1 = MoneyUtils.max0(None, money0)
        self.assertIs(money1, money0)

    def test10(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        roundingMode0 = RoundingMode.CEILING
        money0 = Money.of3(currencyUnit0, 514.0, roundingMode0)
        money1 = money0.multipliedBy1((-1713.181969), roundingMode0)
        money2 = MoneyUtils.max0(money1, money0)
        self.assertIs(money2, money0)

    def test09(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.UNNECESSARY
        money1 = Money.of3(currencyUnit0, (-1), roundingMode0)
        money2 = MoneyUtils.min0(money0, money1)
        self.assertIs(money2, money1)

    def test08(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 1510)
        money0 = bigMoney0.toMoney0()
        money1 = MoneyUtils.add0(None, money0)
        self.assertEqual(money0, money1)

    def test07(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -1139, -1139)
        roundingMode0 = RoundingMode.DOWN
        money0 = bigMoney0.toMoney1(roundingMode0)
        money1 = MoneyUtils.subtract0(money0, None)
        self.assertIs(money1, money0)

    def test06(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 0)
        bigMoney1 = MoneyUtils.max1(None, bigMoney0)
        self.assertIs(bigMoney1, bigMoney0)

    def test05(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -1139, -1139)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = BigMoney.of0(currencyUnit0, bigDecimal0)
        bigMoney2 = MoneyUtils.max1(bigMoney0, bigMoney1)

        self.assertIs(bigMoney2, bigMoney1)

    def test04(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -84)
        bigMoney1 = bigMoney0.multipliedBy2(-84)
        bigMoney2 = MoneyUtils.min1(bigMoney1, bigMoney0)
        self.assertIsNot(bigMoney2, bigMoney1)

    def test03(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = MoneyUtils.add1(None, bigMoney0)
        self.assertIs(bigMoney0, bigMoney1)

    def test02(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(1)
        roundingMode0 = decimal.ROUND_DOWN
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, -1, roundingMode0)
        bigMoney1 = bigMoney0.plusMajor(-1)
        bigMoney2 = bigMoney1.negated()
        bigMoney3 = MoneyUtils.add1(bigMoney0, bigMoney2)
        self.assertTrue(bigMoney3.equals(bigMoney2))

    def test01(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 0)
        bigMoney1 = MoneyUtils.subtract1(bigMoney0, None)
        self.assertEqual(bigMoney1, bigMoney0)

    def test00(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(1)
        roundingMode0 = decimal.ROUND_DOWN
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, -1, roundingMode0)
        bigMoney1 = bigMoney0.plus2(bigDecimal0)
        bigMoney2 = MoneyUtils.subtract1(bigMoney0, bigMoney1)
        self.assertIsNot(bigMoney2, bigMoney0)
        self.assertNotEqual(bigMoney2, bigMoney0)
