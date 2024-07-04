from __future__ import annotations
import math
import time
import locale
import re
import mock
import os
import decimal
import typing
from typing import *
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *

# from src.test.org.joda.money.BigMoney_ESTest_scaffolding import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class BigMoney_ESTest(unittest.TestCase):

    def test229(self) -> None:

        bigMoneyProviderArray0 = [None]
        currencyUnit0 = CurrencyUnit.USD

        with pytest.raises(RuntimeError):
            BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.joda.money.MoneyUtils", RuntimeError)

    def test228(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        int0 = bigMoney0.getAmountMajorInt()
        self.assertEqual(0, int0)

    def test227(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.FLOOR
        bigMoney1 = bigMoney0.multiplyRetainScale1(-3109.98526811487, roundingMode0)
        self.assertTrue(bigMoney1.equals(bigMoney0))
        self.assertIsNot(bigMoney1, bigMoney0)

    def test226(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        string0 = bigMoney0.toString()
        self.assertEqual("EUR 0", string0)

    def test225(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = bigMoney0.getAmount()
        self.assertEqual(0, bigDecimal0)

    def test224(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(10)

        try:
            BigMoney.ofScale0(currencyUnit0, bigDecimal0, -4579)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException("java.math.BigDecimal", e)

    def test223(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        int0 = bigMoney0.getMinorPart()
        self.assertEqual(0, int0)

    def test222(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)

        try:
            bigMoney0.plus1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test221(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.withAmount1(-2041.5577429803)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test220(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_UP

        try:
            bigMoney0.convertRetainScale(currencyUnit0, None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test219(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        vector0 = []
        bigMoney0 = BigMoney.total3(currencyUnit0, vector0)
        self.assertIsNotNone(bigMoney0)

    def test218(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigMoney0.hashCode()

    def test217(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        int0 = bigMoney0.getAmountMinorInt()
        self.assertEqual(0, int0)

    def test216(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        long0 = bigMoney0.getAmountMinorLong()
        self.assertEqual(0, long0)

    def test215(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        long0 = bigMoney0.getAmountMajorLong()
        self.assertEqual(1, long0)

    def test214(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.withScale0(17)
        self.assertFalse(bigMoney1.equals(bigMoney0))
        self.assertIsNot(bigMoney1, bigMoney0)

    def test213(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(7)
        bigMoney0 = BigMoney((-1785), bigDecimal0, currencyUnit0)

        try:
            bigMoney0.toMoney0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test212(self) -> None:

        bigDecimal0 = decimal.Decimal(-7)
        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = Money(0, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.withCurrencyScale0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test211(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        money0 = Money.ofMajor(currencyUnit0, 0)
        roundingMode0 = RoundingMode.DOWN
        bigMoney1 = bigMoney0.minusRetainScale0(money0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test210(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_UP
        money0 = bigMoney0.toMoney1(roundingMode0)
        self.assertIsNotNone(money0)

    def test209(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        boolean0 = bigMoney0.isPositiveOrZero()
        self.assertFalse(boolean0)

    def test208(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, 0.0)
        bigDecimal0 = decimal.Decimal(0)

        try:
            bigMoney0.convertedTo(currencyUnit0, bigDecimal0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Cannot convert to the same currency")

    def test207(self) -> None:
        bigMoneyProviderArray0 = []
        try:
            BigMoney.total0(bigMoneyProviderArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.assertEqual(str(e), "Money array must not be empty")

    def test206(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoneyProviderArray0 = [None] * 2
        bigMoneyProviderArray0[0] = bigMoney0
        # Undeclared exception in Java code
        try:
            BigMoney.total0(bigMoneyProviderArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # BigMoneyProvider must not be null
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test205(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 841)
        list0 = [bigMoney0, bigMoney0, bigMoney0, bigMoney0, bigMoney0]
        bigMoney1 = BigMoney.total1(list0)
        self.assertFalse(list0.contains(bigMoney1))

    def test204(self) -> None:
        vector0 = []
        try:
            BigMoney.total1(vector0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.assertEqual(str(e), "Money iterator must not be empty")

    def test203(self) -> None:

        try:
            BigMoney.parse(" is greater than the scale of the currency ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test202(self) -> None:

        try:
            BigMoney.parse("C1}")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Money 'C1}' cannot be parsed")

    def test201(self) -> None:

        bigMoney0 = BigMoney.parse("EUR 0")
        self.assertIsNotNone(bigMoney0)

    def test200(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = None
        try:
            bigMoney0 = BigMoney(0, None, currencyUnit0)
            self.fail("Expecting exception: AssertionError")

        except AssertionError:
            pass

    def test199(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(-2807, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.withCurrencyUnit(currencyUnit0)
            self.fail("Expecting exception: AssertionError")

        except AssertionError:
            pass

    def test198(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.withCurrencyUnit(currencyUnit0)
        self.assertIs(bigMoney1, bigMoney0)

    def test197(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = bigMoney0.isCurrencyScale()
        self.assertFalse(boolean0)

    def test196(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, 0)
        boolean0 = bigMoney0.isCurrencyScale()
        self.assertTrue(boolean0)

    def test195(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -1)
        bigMoney1 = bigMoney0.withCurrencyScale0()
        self.assertIs(bigMoney1, bigMoney0)

    def test194(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.negated()
        self.assertIs(bigMoney1, bigMoney0)

    def test193(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        boolean0 = bigMoney0.isPositive()
        self.assertFalse(boolean0)

    def test192(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.of2(currencyUnit0, 1.0)
        bigMoney0 = BigMoney.of2(money0)
        boolean0 = bigMoney0.isPositive()
        self.assertTrue(boolean0)

    def test191(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = bigMoney0.isPositiveOrZero()
        self.assertTrue(boolean0)

    def test190(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.abs()
        self.assertIs(bigMoney0, bigMoney1)

    def test189(self) -> None:

        bigDecimal0 = decimal.Decimal(10)
        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        boolean0 = bigMoney0.isNegativeOrZero()
        self.assertFalse(boolean0)

    def test188(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        boolean0 = bigMoney0.isNegativeOrZero()
        self.assertTrue(boolean0)

    def test187(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigDecimal0 = decimal.Decimal(0)
        bigMoney1 = bigMoney0.withAmount0(bigDecimal0)
        self.assertIs(bigMoney1, bigMoney0)

    def test186(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(0)
        bigMoney1 = bigMoney0.plus2(bigDecimal0)
        self.assertIs(bigMoney1, bigMoney0)

    def test185(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.plus3(0.0)
        self.assertIs(bigMoney1, bigMoney0)

    def test184(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigMoney1 = bigMoney0.plusMajor(0)
        self.assertIs(bigMoney1, bigMoney0)

    def test183(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.plusMinor(-1431655764)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test182(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigMoney1 = bigMoney0.plusMinor(0)
        self.assertIs(bigMoney1, bigMoney0)

    def test181(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        bigMoney1 = bigMoney0.plusRetainScale2(0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test180(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)
        list0 = [money0]
        bigMoney1 = bigMoney0.minus0(list0)
        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertNotEqual(bigMoney1, bigMoney0)

    def test179(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.minus3(0)
        self.assertIs(bigMoney1, bigMoney0)

    def test178(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.minusMajor(1601)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test177(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.minusMajor(0)
        self.assertEqual(bigMoney1, bigMoney0)

    def test176(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.minusMinor(-981)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test175(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        bigMoney1 = bigMoney0.minusMinor(0)
        self.assertIs(bigMoney1, bigMoney0)

    def test174(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(-3295)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        bigMoney1 = bigMoney0.minusRetainScale1(bigDecimal0, roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test173(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 1877)
        roundingMode0 = decimal.ROUND_DOWN
        bigMoney1 = bigMoney0.minusRetainScale2(1.0, roundingMode0)
        int0 = bigMoney1.compareTo(bigMoney0)
        self.assertEqual(-1, int0)

    def test172(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        roundingMode0 = decimal.ROUND_UP
        bigMoney1 = bigMoney0.minusRetainScale2(0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test171(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = bigMoney0.multipliedBy0(bigDecimal0)
        self.assertIs(bigMoney1, bigMoney0)

    def test170(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.multipliedBy1(0.0)

        self.assertIsNot(bigMoney1, bigMoney0)

    def test169(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.multipliedBy1(1.0)
        self.assertIs(bigMoney1, bigMoney0)

    def test168(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.multipliedBy2(1)
        self.assertIs(bigMoney1, bigMoney0)

    def test167(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 77, roundingMode0)
        bigDecimal1 = decimal.Decimal(1)
        bigMoney1 = bigMoney0.multiplyRetainScale0(bigDecimal1, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test166(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_UP
        bigMoney1 = bigMoney0.dividedBy0(bigDecimal0, roundingMode0)

        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertTrue(bigMoney1.equals(bigMoney0))

    def test165(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_UP
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = bigMoney0.dividedBy0(bigDecimal0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test164(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        roundingMode0 = RoundingMode.DOWN

        try:
            bigMoney0.dividedBy1(0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test163(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.of2(currencyUnit0, 1.0)
        bigMoney0 = BigMoney.of2(money0)
        roundingMode0 = RoundingMode.CEILING
        bigMoney1 = bigMoney0.dividedBy1(1.0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test162(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        with self.assertRaises(ArithmeticError):
            bigMoney0.dividedBy2(0, roundingMode0)

    def test161(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        roundingMode0 = RoundingMode.UNNECESSARY
        bigMoney1 = bigMoney0.dividedBy2(1, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test160(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        bigMoney1 = bigMoney0.rounded(-7, roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertTrue(bigMoney1.equals(bigMoney0))

    def test159(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_CEILING
        bigMoney1 = bigMoney0.rounded(10, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test158(self) -> None:

        bigDecimal0 = decimal.Decimal(-1079)
        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney(-1079, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.convertedTo(currencyUnit0, bigDecimal0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(
                str(e), "Cannot convert using a negative conversion multiplier"
            )

    def test157(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        bigMoney1 = bigMoney0.convertedTo(currencyUnit0, bigDecimal0)
        self.assertIs(bigMoney1, bigMoney0)

    def test156(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = bigMoney0.getAmountMinor()
        roundingMode0 = decimal.ROUND_HALF_UP

        try:
            bigMoney0.convertRetainScale(currencyUnit0, bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Cannot convert to the same currency
            self.verifyException("org.joda.money.BigMoney", e)

    def test155(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = Money.of0(currencyUnit0, bigDecimal0)
        currencyUnit1 = CurrencyUnit("3p", 3692, 3692)
        roundingMode0 = RoundingMode.HALF_DOWN
        bigMoney1 = bigMoney0.convertRetainScale(
            currencyUnit1, bigDecimal0, roundingMode0
        )

        try:
            bigMoney1.plus1(bigMoney0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test154(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.zero1(currencyUnit0, -5437)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = BigMoney(-5437, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.compareTo(bigMoney1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test153(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.of2(currencyUnit0, 1.0)
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = bigMoney0.isEqual(money0)
        self.assertFalse(boolean0)

    def test152(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = bigMoney0.isEqual(bigMoney0)
        self.assertTrue(boolean0)

    def test151(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, 0)
        boolean0 = bigMoney0.isGreaterThan(bigMoney0)
        self.assertFalse(boolean0)

    def test150(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -1)
        bigDecimal0 = decimal.Decimal(67)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        bigMoney1 = bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0)
        boolean0 = bigMoney1.isGreaterThan(bigMoney0)
        self.assertTrue(boolean0)

    def test149(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(10)
        roundingMode0 = decimal.ROUND_HALF_UP
        bigMoney1 = bigMoney0.minusRetainScale1(bigDecimal0, roundingMode0)
        boolean0 = bigMoney1.isGreaterThanOrEqual(bigMoney0)
        self.assertFalse(boolean0)

    def test148(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = bigMoney0.isGreaterThanOrEqual(bigMoney0)
        self.assertTrue(boolean0)

    def test147(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 16)
        boolean0 = bigMoney0.isLessThan(bigMoney0)
        self.assertFalse(boolean0)

    def test146(self) -> None:

        bigMoneyProviderArray0 = [None] * 1
        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.of1(currencyUnit0, -1290.7206734967915)
        bigMoneyProviderArray0[0] = bigMoney0
        bigMoney1 = bigMoney0.plus1(bigMoneyProviderArray0[0])
        boolean0 = bigMoney1.isLessThan(bigMoneyProviderArray0[0])
        self.assertTrue(boolean0)

    def test145(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.of2(currencyUnit0, 1.0)
        list0 = [money0, money0, money0, money0, money0, money0, money0]
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.plus0(list0)
        boolean0 = bigMoney1.isLessThanOrEqual(bigMoney0)
        self.assertFalse(boolean0)

    def test144(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        boolean0 = bigMoney0.isLessThanOrEqual(bigMoney0)
        self.assertTrue(boolean0)

    def test143(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = bigMoney0.equals(currencyUnit0)
        self.assertFalse(boolean0)

    def test142(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        roundingMode0 = decimal.ROUND_UP
        bigDecimal0 = decimal.Decimal(0)
        money0 = Money.zero(currencyUnit0)
        money1 = money0.withAmount1(bigDecimal0, roundingMode0)
        self.assertEqual(money1, money0)

    def test141(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        int0 = bigMoney0.getScale()
        self.assertEqual(0, int0)

    def test140(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney(66, bigDecimal0, currencyUnit0)
        bigMoney1 = bigMoney0.toBigMoney()
        self.assertIs(bigMoney0, bigMoney1)

    def test139(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = bigMoney0.getAmountMajor()
        self.assertEqual(0, bigDecimal0)

    def test138(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        boolean0 = bigMoney0.isSameCurrency(bigMoney0)
        self.assertTrue(boolean0)

    def test137(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(0, bigDecimal0, currencyUnit0)

    def test136(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-2379), 39)
        roundingMode0 = decimal.ROUND_HALF_UP
        bigMoney1 = bigMoney0.withScale1(39, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test135(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 775)
        roundingMode0 = RoundingMode.UNNECESSARY

        try:
            bigMoney0.withScale1(-1692, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test134(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.plus3(1.0)
        boolean0 = bigMoney1.isZero()
        self.assertFalse(boolean0)

    def test133(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        boolean0 = bigMoney0.isZero()
        self.assertTrue(boolean0)

    def test132(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 4)
        boolean0 = bigMoney0.isNegative()
        self.assertFalse(boolean0)

    def test131(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        boolean0 = bigMoney0.isNegative()
        self.assertTrue(boolean0)

    def test130(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigDecimal0 = decimal.Decimal(10)
        bigMoney1 = bigMoney0.plus2(bigDecimal0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test129(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 77, roundingMode0)
        bigMoney1 = bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test128(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(0)
        bigMoney1 = bigMoney0.minus2(bigDecimal0)
        self.assertIs(bigMoney1, bigMoney0)

    def test127(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_HALF_DOWN
        bigMoney1 = bigMoney0.minusRetainScale1(bigDecimal0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test126(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 77)
        bigMoney1 = bigMoney0.multiplyRetainScale0(bigDecimal0, roundingMode0)
        self.assertTrue(bigMoney1.equals(bigMoney0))
        self.assertIsNot(bigMoney1, bigMoney0)

    def test125(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigMoney1 = bigMoney0.negated()
        self.assertIsNot(bigMoney1, bigMoney0)

    def test124(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.of1(currencyUnit0, 0.0)
        bigDecimal0 = decimal.Decimal(0)
        currencyUnit1 = CurrencyUnit.EUR
        bigMoney1 = bigMoney0.convertedTo(currencyUnit1, bigDecimal0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test123(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        int0 = bigMoney0.compareTo(bigMoney0)
        self.assertEqual(0, int0)

    def test122(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = Money(762, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.abs()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test121(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.zero0(currencyUnit0)

        try:
            bigMoney0.compareTo(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test120(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 4)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = BigMoney(4, bigDecimal0, currencyUnit0)

        try:
            bigMoney1.compareTo(bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test119(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = decimal.Decimal(1495)

        try:
            bigMoney0.convertedTo(None, bigDecimal0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test118(self) -> None:

        bigDecimal0 = decimal.Decimal(1553.0)
        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney((-1724), bigDecimal0, currencyUnit0)

        try:
            bigMoney0.convertedTo(currencyUnit0, bigDecimal0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test117(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_HALF_UP

        try:
            bigMoney0.dividedBy0(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.DivisionByZero:
            self.verifyException("decimal.Decimal", decimal.DivisionByZero)

    def test116(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_DOWN

        try:
            bigMoney0.dividedBy0(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test115(self) -> None:

        bigDecimal0 = decimal.Decimal(1)
        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney((-2797), bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        try:
            bigMoney0.dividedBy1((-2797), roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test114(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = Money(1, bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_DOWN

        try:
            bigMoney0.dividedBy2(1591, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test113(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 530, -2398)

        try:
            bigMoney0.getAmountMajorLong()
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException("java.math.BigDecimal", e)

    def test112(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = Money(66, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.getAmountMinor()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test111(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal((-456.0))
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-971), roundingMode0)

        try:
            bigMoney0.getAmountMinorLong()
            self.fail("Expecting exception: ArithmeticException")

        except decimal.InvalidOperation as e:
            self.verifyException("decimal.Decimal", e)

    def test110(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)

        try:
            bigMoney0.isEqual(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test109(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoneyProviderArray0 = []
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        currencyUnit1 = CurrencyUnit.GBP
        roundingMode0 = RoundingMode.HALF_DOWN
        money0 = Money.of3(currencyUnit1, (-1762.110832), roundingMode0)

        try:
            bigMoney0.isLessThanOrEqual(money0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test108(self) -> None:

        bigDecimal0 = decimal.Decimal(1553.0)
        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney((-1724), bigDecimal0, currencyUnit0)

        try:
            bigMoney0.isPositive()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test107(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        bigMoney1 = BigMoney(32, bigDecimal0, currencyUnit0)

        try:
            bigMoney1.isSameCurrency(bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test106(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)

        try:
            bigMoney0.minus0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "RuntimeError")

    def test105(self) -> None:

        pass  # LLM could not translate this method

    def test104(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)

        try:
            bigMoney0.minus2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test103(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(-347, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.minus2(bigDecimal0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test102(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(3, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.minus3(3)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test101(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(-4680)
        bigMoney0 = BigMoney(3, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.minusMajor(-4680)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test100(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(1092)
        bigMoney0 = BigMoney(1092, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.minusMinor(1092)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test099(self) -> None:

        currencyUnit0 = CurrencyUnit("", -1254, -1254)
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.FLOOR

        try:
            bigMoney0.minusRetainScale1(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test098(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney(4, bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_DOWN

        try:
            bigMoney0.minusRetainScale2(-423.792, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test097(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 3715, -6)

        try:
            bigMoney0.multipliedBy0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test096(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(-2940, bigDecimal0, currencyUnit0)
        bigDecimal1 = decimal.Decimal(0)

        try:
            bigMoney0.multipliedBy0(bigDecimal1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test095(self) -> None:

        bigDecimal0 = decimal.Decimal(1553.0)
        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney((-1724), bigDecimal0, currencyUnit0)

        try:
            bigMoney0.multipliedBy2(841)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test094(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = decimal.Decimal(-1957.443)
        roundingMode0 = decimal.ROUND_UP

        try:
            bigMoney0.multiplyRetainScale0(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.InvalidOperation as e:
            self.verifyException("java.math.BigDecimal", e)

    def test093(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, -3201)
        roundingMode0 = RoundingMode.HALF_UP

        try:
            bigMoney0.multiplyRetainScale0(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test092(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1.0)
        roundingMode0 = RoundingMode.UNNECESSARY

        try:
            bigMoney0.multiplyRetainScale1(113.236137, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test091(self) -> None:

        bigDecimal0 = decimal.Decimal(1)
        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney(338, bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        try:
            bigMoney0.multiplyRetainScale1((-1345.5), roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test090(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = Money(32, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.negated()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test089(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR

        try:
            BigMoney.of0(currencyUnit0, None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            self.assertEqual(str(e), "Amount must not be null")

    def test088(self) -> None:

        try:
            BigMoney.of1(None, 650.71982050396)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Currency must not be null
            self.assertIsInstance(e, RuntimeError)

    def test087(self) -> None:

        try:
            BigMoney.of2(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test086(self) -> None:

        try:
            BigMoney.ofMajor(None, -1314)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test085(self) -> None:

        try:
            BigMoney.ofMinor(None, -742)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test084(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        # Undeclared exception
        try:
            BigMoney.ofScale0(currencyUnit0, None, 2026)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Amount must not be null
            self.assertIsInstance(e, RuntimeError)

    def test083(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(-165)
        roundingMode0 = decimal.ROUND_DOWN

        try:
            BigMoney.ofScale1(currencyUnit0, bigDecimal0, -1840, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.InvalidOperation as e:
            self.verifyException("decimal.Decimal", e)

    def test082(self) -> None:

        bigInteger0 = BigInteger.TEN
        bigDecimal0 = BigDecimal(bigInteger0)
        roundingMode0 = RoundingMode.UNNECESSARY

        with pytest.raises(RuntimeError):
            BigMoney.ofScale1(None, bigDecimal0, 540, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

    def test081(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR

        try:
            BigMoney.ofScale2(currencyUnit0, (-725), (-2146934699))
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException("java.math.BigInteger", e)

    def test080(self) -> None:

        try:
            BigMoney.ofScale2(None, 4335, 5)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test079(self) -> None:

        try:
            BigMoney.parse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Money must not be null")

    def test078(self) -> None:

        try:
            BigMoney.parse("uCs5")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Unknown currency 'uCs'
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test077(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal(-456.0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, -971, roundingMode0)

        try:
            bigMoney0.plus0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test076(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.of2(currencyUnit0, 1.0)
        list0 = [money0, money0, money0, money0, money0, money0, money0]
        currencyUnit1 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.ofMajor(currencyUnit1, 350)

        try:
            bigMoney0.plus0(list0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test074(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)

        try:
            bigMoney0.plus2(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test073(self) -> None:

        bigDecimal0 = decimal.Decimal(10)
        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney(47, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.plusMajor(-1968)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test072(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = Money.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_UP

        try:
            bigMoney0.plusRetainScale0(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test071(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.of2(currencyUnit0, 1.0)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney((-13), bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        try:
            bigMoney0.plusRetainScale0(money0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test070(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = Money.of0(currencyUnit0, bigDecimal0)
        currencyUnit1 = CurrencyUnit("3p", 3692, 3692)
        roundingMode0 = decimal.ROUND_DOWN
        bigMoney1 = Money.zero1(currencyUnit1, 3692)

        try:
            bigMoney0.plusRetainScale0(bigMoney1, roundingMode0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Currencies differ: USD/3p
            self.verifyException("org.joda.money.BigMoney", e)

    def test069(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        roundingMode0 = RoundingMode.UP
        bigMoney0 = BigMoney.zero0(currencyUnit0)

        try:
            bigMoney0.plusRetainScale1(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test068(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(7)
        roundingMode0 = decimal.ROUND_CEILING
        bigMoney0 = BigMoney(7, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test067(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_UP

        try:
            bigMoney0.plusRetainScale2(2488.8807, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.InvalidOperation as e:
            self.verifyException("java.math.BigDecimal", e)

    def test066(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney(-1527, bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_DOWN

        try:
            bigMoney0.rounded(-1527, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except decimal.InvalidOperation as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test065(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.minus3(-1828.1825955349)

        try:
            bigMoney1.toMoney0()
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test064(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(-8, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.toString()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError:
            pass

    def test063(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 33)
        bigDecimal0 = decimal.Decimal(1)
        bigMoney1 = BigMoney(33, bigDecimal0, currencyUnit0)
        bigMoneyProviderArray0 = [None] * 4
        bigMoneyProviderArray0[0] = bigMoney1
        bigMoneyProviderArray0[1] = bigMoney0

        try:
            BigMoney.total0(bigMoneyProviderArray0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test062(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoneyProviderArray0 = [None] * 5
        money0 = Money.zero(currencyUnit0)
        bigMoneyProviderArray0[0] = money0
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 2512)
        bigMoneyProviderArray0[1] = bigMoney0
        bigMoneyProviderArray0[2] = bigMoney0
        bigMoneyProviderArray0[3] = bigMoney0
        bigMoney1 = BigMoney(1140, bigDecimal0, currencyUnit0)
        bigMoneyProviderArray0[4] = bigMoney1

        try:
            BigMoney.total0(bigMoneyProviderArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Money array must not contain null entries")

    def test061(self) -> None:

        # Undeclared exception
        try:
            BigMoney.total1(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # Money iterator must not be null
            self.assertEqual(str(e), "Money iterator must not be null")

    def test060(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        try:
            BigMoney.total2(currencyUnit0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test059(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        locale0 = Locale.SIMPLIFIED_CHINESE
        currency0 = Currency.getInstance(locale0)
        currencyUnit1 = CurrencyUnit.of0(currency0)
        bigMoney0 = BigMoney.zero0(currencyUnit1)
        bigMoneyProviderArray0 = [None] * 8
        bigMoneyProviderArray0[0] = bigMoney0
        try:
            BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test058(self) -> None:

        try:
            BigMoney.total3(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test057(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        try:
            BigMoney.total3(currencyUnit0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'RuntimeError'>")

    def test056(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, 0)

        try:
            bigMoney0.withAmount0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test055(self) -> None:

        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(44, bigDecimal0, None)

        try:
            bigMoney0.withAmount0(bigDecimal0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test054(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-2379), 39)

        with self.assertRaises(ArithmeticException):
            bigMoney0.withCurrencyScale0()

    def test053(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        roundingMode0 = RoundingMode.UNNECESSARY
        bigMoney0 = BigMoney.of1(currencyUnit0, 714.1664)

        # Undeclared exception in Java code
        try:
            bigMoney0.withCurrencyScale1(roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            # Rounding necessary
            self.verifyException("java.math.BigDecimal", e)

    def test052(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(1)
        roundingMode0 = decimal.ROUND_DOWN
        bigMoney0 = Money(627, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.withCurrencyScale1(roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test051(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigInteger0 = BigInteger.ONE
        bigDecimal0 = BigDecimal(bigInteger0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)

        # Undeclared exception in Java code
        try:
            bigMoney0.withScale0(-614)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            # Rounding necessary
            self.verifyException("java.math.BigDecimal", e)

    def test050(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(477)
        bigMoney0 = BigMoney(-1723, bigDecimal0, currencyUnit0)

        try:
            bigMoney0.withScale0(-1723)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test049(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney(2, bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_UP

        try:
            bigMoney0.withScale1(0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test048(self) -> None:

        try:
            BigMoney.zero0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test047(self) -> None:

        try:
            BigMoney.zero1(None, 407)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test046(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 841)
        bigMoney1 = bigMoney0.plusMajor(814)
        int0 = bigMoney1.compareTo(bigMoney0)
        self.assertEqual(1, int0)

    def test045(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        boolean0 = bigMoney0.equals(bigMoney0)
        self.assertTrue(boolean0)

    def test044(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.of2(currencyUnit0, 1.0)
        bigMoney0 = BigMoney.of2(money0)
        bigDecimal0 = bigMoney0.getAmount()
        self.assertEqual(1, bigDecimal0)

    def test043(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = bigMoney0.getAmountMajor()
        self.assertEqual(bytearray([-9]), bigDecimal0.to_bytes(1, "big", signed=True))

    def test042(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, 0)
        bigMoney1 = bigMoney0.plusMajor(1)
        bigDecimal0 = bigMoney1.getAmountMajor()
        self.assertEqual(1, bigDecimal0)

    def test041(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0))
        int0 = bigMoney0.getAmountMajorInt()
        self.assertEqual((-1289), int0)

    def test040(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoneyProviderArray0 = []
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney1 = bigMoney0.minusRetainScale2(52.4458, roundingMode0)
        bigMoney2 = bigMoney1.abs()
        bigMoney3 = bigMoney2.minus1(bigMoney0)
        int0 = bigMoney3.getAmountMajorInt()
        self.assertIs(bigMoney3, bigMoney2)
        self.assertEqual(53, int0)

    def test039(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-3148), 0)
        long0 = bigMoney0.getAmountMajorLong()
        self.assertEqual((-3148), long0)

    def test038(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 77, roundingMode0)
        long0 = bigMoney0.getAmountMajorLong()
        self.assertEqual(0, long0)

    def test037(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.of2(currencyUnit0, 1.0)
        list0 = [money0, money0, money0, money0, money0, money0, money0]
        money1 = Money.total3(currencyUnit0, list0)
        bigMoneyProviderArray0 = [BigMoneyProvider() for _ in range(1)]
        bigMoneyProviderArray0[0] = money1
        bigMoney0 = BigMoney.total0(bigMoneyProviderArray0)
        bigDecimal0 = bigMoney0.getAmountMinor()
        self.assertEqual(700, bigDecimal0)

    def test036(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigDecimal0 = bigMoney0.getAmountMinor()
        self.assertEqual(0, bigDecimal0)

    def test035(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigMoney1 = bigMoney0.minusMinor(3630)
        int0 = bigMoney1.getAmountMinorInt()
        self.assertEqual(-3630, int0)

    def test034(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(1.0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        int0 = bigMoney0.getAmountMinorInt()
        self.assertEqual(100, int0)

    def test033(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        long0 = bigMoney0.getAmountMinorLong()
        self.assertEqual(-128900, long0)

    def test032(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        long0 = bigMoney0.getAmountMinorLong()
        self.assertEqual(1000, long0)

    def test031(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 1625)
        currencyUnit1 = bigMoney0.getCurrencyUnit()
        self.assertEqual(currencyUnit1, currencyUnit0)

    def test030(self) -> None:

        currencyUnit0 = CurrencyUnit("", -1697, 48)
        bigMoney0 = BigMoney.zero1(currencyUnit0, 48)
        currencyUnit1 = bigMoney0.getCurrencyUnit()
        self.assertEqual("", currencyUnit1.toString())

    def test029(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigMoney1 = bigMoney0.minusMinor(3630)
        int0 = bigMoney1.getMinorPart()
        self.assertEqual(-30, int0)

    def test028(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.of1(currencyUnit0, -1290.7206734967915)
        int0 = bigMoney0.getScale()
        self.assertEqual(13, int0)

    def test027(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(1.0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_HALF_UP
        currencyUnit1 = CurrencyUnit("{uCT60@GBk6", -6, -6)
        bigMoney1 = bigMoney0.convertRetainScale(
            currencyUnit1, bigDecimal0, roundingMode0
        )
        boolean0 = bigMoney1.isSameCurrency(bigMoney0)
        self.assertFalse(boolean0)

    def test026(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 1126)
        self.assertIsNotNone(bigMoney0)

    def test025(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        money0 = bigMoney0.toMoney0()
        self.assertIsNotNone(money0)

    def test024(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 44)
        roundingMode0 = RoundingMode.DOWN
        bigMoney1 = bigMoney0.withCurrencyScale1(roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test023(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_CEILING
        bigMoney1 = bigMoney0.dividedBy1(-2328.95, roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test022(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.DOWN
        bigMoney1 = bigMoney0.dividedBy2((-1586), roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test021(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoneyProviderArray0 = []
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        bigMoney1 = bigMoney0.minus3(2228.66566665)
        boolean0 = bigMoney1.isCurrencyScale()
        self.assertFalse(boolean0)

    def test020(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        boolean0 = bigMoney0.isPositive()
        self.assertFalse(boolean0)

    def test019(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        bigMoney1 = bigMoney0.plus3(2231.84)
        boolean0 = bigMoney1.isPositiveOrZero()
        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertTrue(boolean0)

    def test018(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        boolean0 = bigMoney0.isNegativeOrZero()
        self.assertTrue(boolean0)

    def test017(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.of1(currencyUnit0, 0.0)
        bigMoney1 = bigMoney0.plus3((-1834.54034602969))
        self.assertIsNot(bigMoney1, bigMoney0)

    def test016(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, -638, 48)
        bigMoney1 = bigMoney0.plusMinor(1)

        self.assertIsNot(bigMoney1, bigMoney0)

    def test015(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = RoundingMode.UP
        bigMoney2 = bigMoney0.plusRetainScale0(bigMoney1, roundingMode0)
        self.assertIs(bigMoney2, bigMoney0)

    def test014(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = decimal.Decimal(-1837)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney1 = bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test013(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoneyProviderArray0 = []
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        roundingMode0 = decimal.ROUND_FLOOR
        bigMoney1 = bigMoney0.plusRetainScale2(-2270.0, roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test012(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = decimal.Decimal(-1822)
        bigMoney1 = bigMoney0.minus2(bigDecimal0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test011(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = decimal.Decimal(10)
        bigMoney1 = bigMoney0.multipliedBy0(bigDecimal0)
        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertNotEqual(bigMoney1, bigMoney0)

    def test010(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigMoney1 = bigMoney0.multipliedBy1(7)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test009(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.multipliedBy2(-4680)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test008(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_UP
        bigMoney1 = bigMoney0.dividedBy1(927.7288717742318, roundingMode0)
        self.assertIsNot(bigMoney1, bigMoney0)

    def test007(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        roundingMode0 = RoundingMode.CEILING
        bigMoney1 = bigMoney0.rounded(0, roundingMode0)
        self.assertIs(bigMoney1, bigMoney0)

    def test006(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigDecimal0 = decimal.Decimal(10)
        roundingMode0 = decimal.ROUND_HALF_UP

        try:
            bigMoney0.convertRetainScale(currencyUnit0, bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Cannot convert to the same currency
            self.verifyException("org.joda.money.BigMoney", e)

    def test005(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 0)
        bigMoney1 = bigMoney0.minusMinor(3630)
        boolean0 = bigMoney0.isEqual(bigMoney1)
        self.assertFalse(boolean0)

    def test004(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney.of1(currencyUnit0, -1289.0)
        bigMoney1 = BigMoney.zero1(currencyUnit0, -845)
        boolean0 = bigMoney0.isGreaterThan(bigMoney1)
        self.assertFalse(bigMoney1.equals(bigMoney0))
        self.assertFalse(boolean0)

    def test003(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 1625)
        bigMoney1 = bigMoney0.multipliedBy2(841)
        boolean0 = bigMoney1.isGreaterThanOrEqual(bigMoney0)
        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertTrue(boolean0)

    def test002(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero1(currencyUnit0, 16)
        bigMoney1 = bigMoney0.plusMajor(-3334)
        boolean0 = bigMoney0.isLessThan(bigMoney1)
        self.assertIsNot(bigMoney1, bigMoney0)
        self.assertFalse(boolean0)

    def test001(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        bigMoney1 = bigMoney0.plus3(1.0)
        boolean0 = bigMoney0.isLessThanOrEqual(bigMoney1)
        self.assertTrue(boolean0)
        self.assertNotEqual(bigMoney1, bigMoney0)

    def test000(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.ofMinor(currencyUnit0, -2270)
        linkedHashSet0 = set()
        boolean0 = linkedHashSet0.add(money0)
        self.assertTrue(boolean0)
