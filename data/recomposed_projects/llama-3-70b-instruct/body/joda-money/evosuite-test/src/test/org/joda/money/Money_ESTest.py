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
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *

# from src.test.org.joda.money.Money_ESTest_scaffolding import *


class Money_ESTest(unittest.TestCase):

    def test193(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        money1 = money0.negated()
        int0 = money1.getAmountMajorInt()
        self.assertEqual(29, int0)

    def test192(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        money0.hashCode()

    def test191(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)

        try:
            money0.minus2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test190(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(2407.165)

        with pytest.raises(ArithmeticException):
            money0.plus2(bigDecimal0)

    def test189(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(10)
        roundingMode0 = decimal.ROUND_CEILING

        try:
            money0.convertedTo(currencyUnit0, bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Cannot convert to the same currency
            self.verifyException("org.joda.money.BigMoney", e)

    def test188(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, -27)
        money0 = Money.ofMinor(currencyUnit0, -27)
        boolean0 = money0.isSameCurrency(bigMoney0)
        self.assertTrue(boolean0)

    def test187(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)

        try:
            money0.isLessThanOrEqual(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test186(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        boolean0 = money0.isEqual(money0)
        self.assertTrue(boolean0)

    def test185(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 158)
        money0 = bigMoney0.toMoney0()
        moneyArray0 = [None] * 5
        moneyArray0[0] = money0

        try:
            Money.total0(moneyArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test184(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -27)
        bigDecimal0 = decimal.Decimal(10)
        money1 = money0.withAmount0(bigDecimal0)
        bigDecimal1 = money1.getAmountMinor()
        self.assertEqual(
            bytearray([-24]), bigDecimal1.to_bytes(1, byteorder="big", signed=True)
        )

    def test183(self) -> None:

        money0 = Money(0, BigMoney(CurrencyUnit.USD, 105))

        try:
            money0.plusMinor(-105)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test182(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_UP

        try:
            money0.multipliedBy0(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test181(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -27)
        int0 = money0.getScale()
        self.assertEqual(2, int0)

    def test180(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.DOWN
        money1 = money0.multipliedBy1((-1852.818531), roundingMode0)
        self.assertIs(money1, money0)

    def test179(self) -> None:

        currencyUnit0 = CurrencyUnit("", -466, 42)
        money0 = Money.of2(currencyUnit0, -466)
        string0 = money0.toString()
        self.assertEqual(" -466.000000000000000000000000000000000000000000", string0)

    def test178(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        int0 = money0.getAmountMinorInt()
        self.assertEqual(0, int0)

    def test177(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        money1 = money0.minusMinor(-1223)
        self.assertIsNot(money1, money0)

    def test176(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMinor(currencyUnit0, 0)
        currencyUnit1 = money0.getCurrencyUnit()
        self.assertEqual(2, currencyUnit1.getDecimalPlaces())

    def test175(self) -> None:

        currencyUnit0 = CurrencyUnit("FJ(-/|N@o]HC4", 31, -1)
        bigDecimal0 = decimal.Decimal(-106)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        bigDecimal1 = money0.getAmount()
        self.assertEqual(short(-106), bigDecimal1.to_integral_value())

    def test174(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = decimal.ROUND_UNNECESSARY

        try:
            money0.dividedBy0(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except decimal.InvalidOperation as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test173(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMajor(currencyUnit0, -1803)
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = money0.isGreaterThanOrEqual(bigMoney0)
        self.assertFalse(boolean0)

    def test172(self) -> None:

        # Undeclared exception
        try:
            Money.parse("o9H4")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Unknown currency 'o9H'
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test171(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        moneyArray0 = [None] * 2
        money0 = Money.of2(currencyUnit0, 918)
        moneyArray0[0] = money0
        moneyArray0[1] = moneyArray0[0]
        boolean0 = moneyArray0[1].isPositive()
        self.assertTrue(boolean0)

    def test170(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        money1 = money0.minus4(-2984)
        int0 = money1.getAmountMinorInt()
        self.assertEqual(295416, int0)

    def test169(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        boolean0 = money0.isGreaterThan(money0)
        self.assertFalse(boolean0)

    def test168(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 48)
        money0 = Money(48, bigMoney0)

        try:
            money0.getAmountMinorLong()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test167(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        roundingMode0 = RoundingMode.UNNECESSARY
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 918)
        money0 = bigMoney0.toMoney1(roundingMode0)

        # Undeclared exception handling
        try:
            money0.rounded(-200, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            # Rounding necessary
            self.verifyException("java.math.BigDecimal", e)

    def test166(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        money1 = money0.plus4(0.0)
        self.assertIs(money1, money0)

    def test165(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMajor(currencyUnit0, -1803)

        try:
            money0.withAmount2(1050.52909262545)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            verifyException("java.math.BigDecimal", e)

    def test164(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        money1 = money0.multipliedBy2(2113)
        self.assertIs(money1, money0)

    def test163(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        money1 = money0.plusMajor(-476)
        self.assertIsNot(money1, money0)

    def test162(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 158)
        money0 = bigMoney0.toMoney0()
        list0 = [money0, money0, money0, money0, money0, money0, money0, money0]
        money1 = money0.minus0(list0)
        self.assertFalse(list0.contains(money1))

    def test161(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 3529)
        money0 = Money(0, bigMoney0)

        try:
            money0.abs()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Joda-Money bug: BigMoney must not be null")

    def test160(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.DOWN

        try:
            money0.dividedBy1(0.0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test159(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.ofMinor(currencyUnit0, 1071)
        bigDecimal0 = money0.getAmountMajor()
        self.assertEqual(10, bigDecimal0)

    def test158(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMinor(currencyUnit0, 0)
        money1 = money0.withCurrencyUnit0(currencyUnit0)
        self.assertIs(money1, money0)

    def test157(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        roundingMode0 = RoundingMode.DOWN
        money1 = money0.dividedBy2(-1181, roundingMode0)
        self.assertIsNot(money1, money0)

    def test156(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -27)
        bigDecimal0 = money0.getAmountMinor()
        self.assertEqual(short(-27), bigDecimal0.shortValue())

    def test155(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.of1(currencyUnit0, 1.0)
        money0 = Money.of4(bigMoney0)
        boolean0 = money0.isPositiveOrZero()
        self.assertTrue(boolean0)

    def test154(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        vector0 = []
        bigMoney0 = Money.total3(currencyUnit0, vector0)
        money0 = Money(999, bigMoney0)

        with pytest.raises(RuntimeError):
            money0.minusMajor(0)
            self.fail("Expecting exception: RuntimeError")

    def test153(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        moneyArray0 = []
        money0 = Money.total2(currencyUnit0, moneyArray0)
        self.assertIsNotNone(money0)

    def test152(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        int0 = money0.getMinorPart()
        self.assertEqual(0, int0)

    def test151(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigDecimal0 = decimal.Decimal(10)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        boolean0 = money0.isZero()
        self.assertFalse(boolean0)

    def test150(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        long0 = money0.getAmountMajorLong()
        self.assertEqual(0, long0)

    def test149(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.ofMajor(currencyUnit0, 0)
        boolean0 = money0.isNegativeOrZero()
        self.assertTrue(boolean0)

    def test148(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, (-27))
        int0 = money0.getAmountMajorInt()
        self.assertEqual(0, int0)

    def test147(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.ofMajor(currencyUnit0, -764)
        boolean0 = money0.isLessThan(money0)
        self.assertFalse(boolean0)

    def test146(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal("2199.516458641819")

        with pytest.raises(ArithmeticError) as e:
            Money.of0(currencyUnit0, bigDecimal0)

        assert (
            str(e.value)
            == "Scale of amount 2199.516458641819 is greater than the scale of the currency JPY"
        )

    def test145(self) -> None:
        moneyArray0 = []
        try:
            Money.total0(moneyArray0)
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            self.assertEqual(str(e), "Money array must not be empty")

    def test144(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        moneyArray0 = [None] * 1
        bigDecimal0 = decimal.Decimal(10)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        moneyArray0[0] = money0
        money1 = Money.total0(moneyArray0)
        self.assertIs(money1, money0)

    def test143(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        list0 = [
            money0,
            money0,
            money0,
            money0,
            money0,
            money0,
            money0,
            money0,
            money0,
            money0,
        ]
        money1 = Money.total1(list0)
        self.assertIs(money1, money0)

    def test142(self) -> None:

        treeSet0 = TreeSet()
        priorityQueue0 = PriorityQueue(treeSet0)

        try:
            Money.total1(priorityQueue0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Money iterator must not be empty")

    def test141(self) -> None:

        money0 = None
        try:
            money0 = Money(0, None)
            self.fail("Expecting exception: AssertionError")

        except AssertionError:
            # Joda-Money bug: BigMoney must not be null
            pass

    def test140(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        mathContext0 = decimal.Context(prec=999_999)
        bigDecimal0 = decimal.Decimal(0, context=mathContext0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        money0 = None
        try:
            money0 = Money(0, bigMoney0)
            self.fail("Expecting exception: AssertionError")

        except AssertionError:
            #
            # Joda-Money bug: Only currency scale is valid for Money
            #
            pass

    def test139(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        money1 = money0.abs()
        self.assertIs(money1, money0)

    def test138(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.ofMajor(currencyUnit0, -1)
        money1 = money0.abs()
        self.assertIsNot(money1, money0)

    def test137(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        boolean0 = money0.equals(currencyUnit0)
        self.assertFalse(boolean0)

    def test136(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(-1819)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_DOWN
        money0 = bigMoney0.toMoney1(roundingMode0)
        boolean0 = money0.equals(money0)
        self.assertTrue(boolean0)

    def test135(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 0)
        roundingMode0 = RoundingMode.HALF_EVEN
        money0 = bigMoney0.toMoney1(roundingMode0)
        money1 = Money.of5(money0, roundingMode0)
        boolean0 = money0.equals(money1)
        self.assertTrue(boolean0)

    def test134(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        try:
            money0.plus3(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)

    def test133(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.zero(currencyUnit0)

        try:
            money0.plus0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test132(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.UNNECESSARY

        try:
            money0.minus3(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test131(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        money1 = money0.withAmount3(0.0, roundingMode0)
        self.assertIsNot(money1, money0)

    def test130(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        roundingMode0 = RoundingMode.FLOOR

        try:
            Money.of1(currencyUnit0, None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Amount must not be null
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test129(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.UNNECESSARY

        try:
            money0.minus5(1222.1105, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test128(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        boolean0 = money0.isNegative()
        self.assertTrue(boolean0)

    def test127(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)

        try:
            money0.plus1(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test126(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_DOWN
        money1 = money0.plus5((-783.40558289), roundingMode0)
        self.assertIsNot(money1, money0)

    def test125(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.UP

        try:
            money0.withAmount1(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test124(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_DOWN

        try:
            money0.withCurrencyUnit1(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test123(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        bigMoneyProviderArray0 = [BigMoneyProvider() for _ in range(2)]
        bigMoneyProviderArray0[0] = money0
        bigMoneyProviderArray0[1] = money0
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        money1 = Money(0, bigMoney0)
        self.assertTrue(money1.equals(money0))

    def test122(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.CEILING

        try:
            money0.convertedTo(currencyUnit0, None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test121(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(0)
        roundingMode0 = decimal.ROUND_HALF_UP

        try:
            money0.dividedBy0(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.DivisionByZero:
            #
            # / by zero
            #
            self.verifyException("decimal.Decimal", decimal.DivisionByZero)

    def test120(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigMoney0 = BigMoney.zero1(currencyUnit0, -88)
        money0 = Money(-1238, bigMoney0)
        roundingMode0 = decimal.ROUND_UNNECESSARY

        try:
            money0.dividedBy0(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except decimal.InvalidOperation as e:
            self.verifyException("org.joda.money.Money", e)

    def test119(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        roundingMode0 = RoundingMode.FLOOR
        bigMoney0 = BigMoney.zero1(currencyUnit0, -1566)
        money0 = Money(2, bigMoney0)

        try:
            money0.dividedBy1(2, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test118(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_EVEN

        try:
            money0.dividedBy2(0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException("java.math.BigDecimal", e)

    def test117(self) -> None:

        bigDecimal0 = decimal.Decimal(67)
        currencyUnit0 = CurrencyUnit.USD
        bigMoney0 = BigMoney(198, bigDecimal0, currencyUnit0)
        money0 = Money(0, bigMoney0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        with self.assertRaises(RuntimeError):
            money0.dividedBy2(67, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

    def test116(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 41)
        money0 = Money(41, bigMoney0)

        with pytest.raises(RuntimeError):
            money0.getAmount()
            pytest.fail("Expecting exception: RuntimeError")

    def test115(self) -> None:

        money0 = Money(109, None)

        try:
            money0.getAmountMajor()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test114(self) -> None:

        money0 = Money(7, None)
        try:
            money0.getAmountMajorInt()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test113(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(30)
        bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 0)
        money0 = Money(0, bigMoney0)

        try:
            money0.getAmountMinor()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Joda-Money bug: BigMoney must not be null")

    def test112(self) -> None:

        money0 = Money(39, None)
        try:
            money0.getCurrencyUnit()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test111(self) -> None:

        money0 = Money(0, BigMoney(CurrencyUnit.USD, 1))
        try:
            money0.getMinorPart()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test110(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)

        try:
            money0.isEqual(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            # BigMoneyProvider must not be null
            self.assertTrue("org.joda.money.MoneyUtils" in str(e))

    def test109(self) -> None:

        currencyUnit0 = CurrencyUnit("", 2052, 2052)
        money0 = Money.zero(currencyUnit0)

        try:
            money0.isGreaterThanOrEqual(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, TypeError)
            self.assertEqual(str(e), "BigMoneyProvider must not be null")

    def test108(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        currencyUnit1 = CurrencyUnit.JPY
        money1 = Money.ofMajor(currencyUnit1, -1)

        try:
            money0.isGreaterThanOrEqual(money1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test107(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)

        with pytest.raises(RuntimeError):
            money0.isLessThan(None)

    def test106(self) -> None:

        money0 = Money(39, None)
        try:
            money0.isLessThan(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test105(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.ofMajor(currencyUnit0, -764)
        currencyUnit1 = CurrencyUnit.CHF
        money1 = Money.ofMinor(currencyUnit1, -764)

        try:
            money1.isLessThan(money0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test104(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        moneyArray0 = [None] * 6
        bigDecimal0 = decimal.Decimal(-1166)
        roundingMode0 = decimal.ROUND_CEILING
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 9, roundingMode0)
        money0 = Money(0, bigMoney0)

        try:
            money0.isLessThanOrEqual(moneyArray0[0])
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test103(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        currencyUnit1 = CurrencyUnit("6OZbmjCl+", 1713, -1)
        money1 = Money.zero(currencyUnit1)

        try:
            money0.isLessThanOrEqual(money1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Currencies differ: JPY/6OZbmjCl+
            self.verifyException("org.joda.money.BigMoney", e)

    def test102(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        byteArray0 = bytearray(4)
        bigInteger0 = int.from_bytes(byteArray0, byteorder="big", signed=True)
        bigDecimal0 = decimal.Decimal(bigInteger0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        money0 = Money(59, bigMoney0)

        try:
            money0.isNegativeOrZero()
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.Money", e)

    def test101(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)

        try:
            money0.isSameCurrency(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "BigMoneyProvider must not be null")

    def test100(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 48)
        money0 = Money(0, bigMoney0)

        try:
            money0.isSameCurrency(bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.Money", e)

    def test099(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 158)
        money0 = bigMoney0.toMoney0()
        money1 = Money(179, bigMoney0)
        list0 = [money0, money0, money0, money0, money0, money1, money1, money0]

        try:
            money0.minus0(list0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test098(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)

        try:
            money0.minus0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test097(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 41)
        money0 = Money(41, bigMoney0)

        try:
            money0.minus1(money0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test096(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(480.4741)

        try:
            money0.minus2(bigDecimal0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            verifyException("java.math.BigDecimal", e)

    def test095(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)

        try:
            money0.minus4(1170.9922759)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            verifyException("java.math.BigDecimal", e)

    def test094(self) -> None:

        roundingMode0 = RoundingMode.DOWN
        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        money0 = Money(1773, bigMoney0)

        try:
            money0.minus5(-2063.71797904411, roundingMode0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test093(self) -> None:

        bigDecimal0 = decimal.Decimal(10)
        money0 = Money(0, BigMoney.of(CurrencyUnit.USD, bigDecimal0))
        roundingMode0 = RoundingMode.HALF_DOWN

        try:
            money0.multipliedBy0(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test092(self) -> None:

        money0 = Money(-105, None)
        roundingMode0 = RoundingMode.UNNECESSARY

        try:
            money0.multipliedBy1(2463.196, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test091(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 0)
        money0 = Money(10, bigMoney0)

        try:
            money0.negated()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test090(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY

        try:
            Money.of0(currencyUnit0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test089(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(-1580.97)
        roundingMode0 = decimal.ROUND_UP

        try:
            Money.of1(currencyUnit0, bigDecimal0, roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.InvalidOperation as e:
            self.verifyException("decimal.Decimal", e)

    def test088(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        try:
            Money.of2(currencyUnit0, 3051.54465)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            verifyException("org.joda.money.Money", e)

    def test087(self) -> None:

        try:
            Money.of2(None, -4123.2)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test086(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        roundingMode0 = decimal.ROUND_UP
        # Undeclared exception in Python
        try:
            Money.of3(currencyUnit0, (-3397.933944487), roundingMode0)
            self.fail("Expecting exception: ArithmeticException")

        except decimal.InvalidOperation as e:
            # Rounding necessary
            self.assertIsInstance(e, decimal.InvalidOperation)

    def test085(self) -> None:

        roundingMode0 = decimal.ROUND_HALF_UP
        try:
            Money.of3(None, -1.0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            #
            # CurrencyUnit must not be null
            #
            self.assertTrue("org.joda.money.MoneyUtils" in str(e))

    def test084(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.of1(currencyUnit0, 4109.10315908)

        # Undeclared exception in Java code
        try:
            Money.of4(bigMoney0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            # Rounding necessary
            self.verifyException("java.math.BigDecimal", e)

    def test083(self) -> None:

        # Undeclared exception
        try:
            Money.of4(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # BigMoneyProvider must not be null
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test082(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(10)
        bigMoney0 = BigMoney((-596), bigDecimal0, currencyUnit0)

        with pytest.raises(RuntimeError):
            Money.of4(bigMoney0)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.joda.money.BigMoney", e)

    def test081(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0.0)
        roundingMode0 = decimal.ROUND_DOWN
        bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, -3576, roundingMode0)
        bigMoney1 = bigMoney0.minus3(2234.132755916115)

        with self.assertRaises(ArithmeticException):
            Money.of5(bigMoney1, roundingMode0)

    def test080(self) -> None:
        roundingMode0 = RoundingMode.UP
        try:
            Money.of5(None, roundingMode0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            MoneyUtils.verifyException("org.joda.money.MoneyUtils", e)

    def test079(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal((-642.011708682762))
        bigMoney0 = BigMoney(41, bigDecimal0, currencyUnit0)
        roundingMode0 = decimal.ROUND_HALF_EVEN

        with self.assertRaises(RuntimeError):
            Money.of5(bigMoney0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

    def test078(self) -> None:

        try:
            Money.ofMajor(None, 1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # CurrencyUnit must not be null
            verifyException("org.joda.money.MoneyUtils", e)

    def test077(self) -> None:

        try:
            Money.ofMinor(None, 0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # CurrencyUnit must not be null
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test076(self) -> None:

        try:
            Money.parse("")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test075(self) -> None:

        # Undeclared exception
        try:
            Money.parse(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Money must not be null
            verifyException("org.joda.money.MoneyUtils", e)

    def test074(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)
        locale0 = Locale.CANADA
        currency0 = Currency.getInstance(locale0)
        currencyUnit1 = CurrencyUnit.of0(currency0)
        roundingMode0 = RoundingMode.UP
        money1 = Money.of3(currencyUnit1, 1516.0, roundingMode0)
        hashSet0.add(money1)

        with self.assertRaises(ValueError):
            money0.plus0(hashSet0)

    def test073(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        currencyUnit1 = CurrencyUnit.CHF
        money0 = Money.of0(currencyUnit1, bigDecimal0)
        roundingMode0 = decimal.ROUND_UP
        money1 = Money.of1(currencyUnit0, bigDecimal0, roundingMode0)

        try:
            money0.plus1(money1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Currencies differ: CHF/JPY
            self.verifyException("org.joda.money.BigMoney", e)

    def test072(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)

        try:
            money0.plus2(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test071(self) -> None:

        money0 = Money(1344, None)
        bigDecimal0 = decimal.Decimal(1344)
        roundingMode0 = decimal.ROUND_FLOOR

        with self.assertRaises(RuntimeError):
            money0.plus3(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

    def test070(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)

        try:
            money0.plus4(1380.474300713)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            self.verifyException("java.math.BigDecimal", e)

    def test069(self) -> None:

        money0 = Money(4674, None)
        roundingMode0 = RoundingMode.UNNECESSARY

        with self.assertRaises(RuntimeError):
            money0.rounded(-1457, roundingMode0)

    def test068(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        comparator0 = mock(Comparator, new_callable=ViolatedAssumptionAnswer)
        priorityQueue0 = PriorityQueue(77, comparator0)
        bigMoney0 = BigMoney.total3(currencyUnit0, priorityQueue0)
        money0 = Money(-950, bigMoney0)

        try:
            money0.toString()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError:
            pass

    def test067(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        moneyArray0 = [None] * 2
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        money0 = Money(10, bigMoney0)
        moneyArray0[0] = money0

        try:
            Money.total0(moneyArray0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test066(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        moneyArray0 = [None] * 5
        moneyArray0[0] = money0
        moneyArray0[1] = money0
        moneyArray0[2] = money0
        moneyArray0[3] = money0
        currencyUnit1 = CurrencyUnit.JPY
        money1 = Money.zero(currencyUnit1)
        moneyArray0[4] = money1

        try:
            Money.total0(moneyArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Money array must not contain null entries")

    def test065(self) -> None:
        try:
            Money.total1(None)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test064(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal(0)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        money0 = Money(-2115, bigMoney0)
        list0 = [money0, money0, money0, money0, money0, money0, money0, money0, money0]

        try:
            Money.total1(list0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.Money", e)

    def test063(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        currencyUnit1 = CurrencyUnit.USD
        roundingMode0 = RoundingMode.HALF_DOWN
        money1 = Money.of3(currencyUnit1, (-19.7157), roundingMode0)
        list0 = [
            money0,
            money0,
            money0,
            money0,
            money0,
            money1,
            money0,
            money0,
            money0,
            money0,
        ]

        try:
            Money.total1(list0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test062(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        moneyArray0 = [None]

        with pytest.raises(RuntimeError):
            Money.total2(currencyUnit0, moneyArray0)

        verifyException("org.joda.money.MoneyUtils", RuntimeError)

    def test061(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        try:
            Money.total2(currencyUnit0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test060(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        currencyUnit1 = CurrencyUnit.EUR
        money0 = Money.ofMinor(currencyUnit1, 0)
        moneyArray0 = [money0]
        try:
            Money.total2(currencyUnit0, moneyArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.joda.money.BigMoney", e)

    def test059(self) -> None:

        try:
            Money.total3(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test058(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        try:
            Money.total3(currencyUnit0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.joda.money.BigMoney", e)

    def test057(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        bigDecimal0 = decimal.Decimal(1)
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        money0 = Money.of5(bigMoney0, roundingMode0)
        locale0 = Locale.GERMANY
        currency0 = Currency.getInstance(locale0)
        currencyUnit1 = CurrencyUnit.of0(currency0)
        list0 = [money0]

        try:
            Money.total3(currencyUnit1, list0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.money.BigMoney", e)

    def test056(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal((-4822.40255964))

        try:
            money0.withAmount0(bigDecimal0)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticException as e:
            verifyException("java.math.BigDecimal", e)

    def test055(self) -> None:

        locale0 = Locale.PRC
        currencyUnit0 = CurrencyUnit.of2(locale0)
        money0 = Money.zero(currencyUnit0)

        try:
            money0.withAmount0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.MoneyUtils", e)

    def test054(self) -> None:

        money0 = Money(0, None)
        bigDecimal0 = decimal.Decimal(3095)
        roundingMode0 = RoundingMode.DOWN

        try:
            money0.withAmount1(bigDecimal0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test053(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.zero1(currencyUnit0, -3628)
        money0 = Money(-3628, bigMoney0)

        try:
            money0.withAmount2(-3297.9804510482063)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test052(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigMoney0 = BigMoney.ofMajor(currencyUnit0, 14)
        money0 = Money(14, bigMoney0)
        roundingMode0 = RoundingMode.FLOOR

        try:
            money0.withAmount3(14, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.joda.money.Money", e)

    def test051(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        bigDecimal0 = decimal.Decimal(0)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        bigMoneyProviderArray0 = [BigMoneyProvider() for _ in range(6)]
        for i in range(6):
            bigMoneyProviderArray0[i] = money0
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        roundingMode0 = decimal.ROUND_DOWN
        money1 = Money(1, bigMoney0)

        try:
            money1.withCurrencyUnit1(currencyUnit0, roundingMode0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.joda.money.Money", e)

    def test050(self) -> None:

        try:
            Money.zero(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Currency must not be null
            verifyException("org.joda.money.MoneyUtils", e)

    def test049(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        money1 = Money.ofMinor(currencyUnit0, -241)
        int0 = money1.compareTo(money0)
        self.assertEqual(-1, int0)

    def test048(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMinor(currencyUnit0, 0)
        bigDecimal0 = decimal.Decimal(-1002)
        money1 = money0.plus2(bigDecimal0)
        int0 = money0.compareTo(money1)
        self.assertEqual(1, int0)

    def test047(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        int0 = money0.compareTo(money0)
        self.assertEqual(0, int0)

    def test046(self) -> None:

        currencyUnit0 = CurrencyUnit.GBP
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(1)
        roundingMode0 = decimal.ROUND_FLOOR
        money1 = money0.convertedTo(currencyUnit0, bigDecimal0, roundingMode0)
        self.assertIs(money1, money0)

    def test045(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoneyProviderArray0 = []
        bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0)
        bigDecimal0 = decimal.Decimal(10)
        roundingMode0 = decimal.ROUND_DOWN
        money0 = bigMoney0.toMoney1(roundingMode0)
        money1 = money0.dividedBy0(bigDecimal0, roundingMode0)
        self.assertIs(money1, money0)

    def test044(self) -> None:

        currencyUnit0 = CurrencyUnit("Country codes must not be null", 18, 18)
        money0 = Money.of2(currencyUnit0, -208.88629475)
        roundingMode0 = RoundingMode.HALF_EVEN
        money1 = money0.dividedBy1(-208.88629475, roundingMode0)
        self.assertNotEqual(money1, money0)

    def test043(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        bigDecimal1 = money0.getAmount()
        self.assertEqual(1, bigDecimal1)

    def test042(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = money0.getAmount()
        self.assertEqual(0, bigDecimal0)

    def test041(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.ofMinor(currencyUnit0, -1050)
        bigDecimal0 = money0.getAmountMajor()
        self.assertEqual(-10, bigDecimal0)

    def test040(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = money0.getAmountMajor()

        self.assertEqual(0, bigDecimal0)

    def test039(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, (-3135))
        int0 = money0.getAmountMajorInt()
        self.assertEqual((-31), int0)

    def test038(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        roundingMode0 = decimal.ROUND_UP
        money0 = Money.of3(currencyUnit0, (-1.0), roundingMode0)
        long0 = money0.getAmountMajorLong()
        self.assertEqual((-1), long0)

    def test037(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        long0 = money0.getAmountMajorLong()
        self.assertEqual(1, long0)

    def test036(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.of1(currencyUnit0, 1.0)
        roundingMode0 = RoundingMode.HALF_UP
        bigMoney1 = bigMoney0.plusRetainScale2((-3186.0), roundingMode0)
        bigMoney2 = bigMoney1.withCurrencyScale1(roundingMode0)
        bigMoney3 = bigMoney2.negated()
        money0 = Money.of4(bigMoney3)
        bigDecimal0 = money0.getAmountMinor()
        self.assertEqual((short)(-9180), bigDecimal0.shortValue())

    def test035(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = money0.getAmountMinor()

        self.assertEqual(0, bigDecimal0)

    def test034(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        int0 = money0.getAmountMinorInt()
        self.assertEqual(-2984, int0)

    def test033(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMajor(currencyUnit0, -1)
        long0 = money0.getAmountMinorLong()
        self.assertEqual(-100, long0)

    def test032(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        long0 = money0.getAmountMinorLong()
        self.assertEqual(100, long0)

    def test031(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.ofMinor(currencyUnit0, 0)
        long0 = money0.getAmountMinorLong()
        self.assertEqual(0, long0)

    def test030(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        currencyUnit1 = money0.getCurrencyUnit()
        self.assertEqual(currencyUnit0, currencyUnit1)

    def test029(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        int0 = money0.getMinorPart()
        self.assertEqual(-84, int0)

    def test028(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        money1 = money0.negated()
        int0 = money1.getMinorPart()
        self.assertEqual(84, int0)

    def test027(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        int0 = money0.getScale()
        self.assertEqual(0, int0)

    def test026(self) -> None:

        currencyUnit0 = CurrencyUnit("", 286, 1285)
        bigMoney0 = BigMoney.of1(currencyUnit0, 286)
        roundingMode0 = RoundingMode.FLOOR
        bigMoney1 = bigMoney0.plusRetainScale0(bigMoney0, roundingMode0)
        money0 = bigMoney1.toMoney1(roundingMode0)
        boolean0 = money0.isEqual(bigMoney0)
        self.assertFalse(boolean0)

    def test025(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        money1 = money0.minus4(-2984)
        boolean0 = money1.isGreaterThan(money0)
        self.assertTrue(boolean0)

    def test024(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0, -783)
        boolean0 = money0.isGreaterThanOrEqual(bigMoney0)
        self.assertTrue(boolean0)

    def test023(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        bigMoney0 = BigMoney.ofMinor(currencyUnit0, 1)
        boolean0 = money0.isLessThan(bigMoney0)
        self.assertTrue(boolean0)

    def test022(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.ofMinor(currencyUnit0, -2984)
        money1 = money0.negated()
        boolean0 = money1.isLessThanOrEqual(money0)
        self.assertFalse(boolean0)

    def test021(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        bigMoney0 = BigMoney.zero0(currencyUnit0)
        boolean0 = money0.isLessThanOrEqual(bigMoney0)
        self.assertTrue(boolean0)

    def test020(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)
        boolean0 = money0.isNegative()
        self.assertFalse(boolean0)

    def test019(self) -> None:

        currencyUnit0 = CurrencyUnit("Country codes must not be null", 2599, 2599)
        money0 = Money.ofMajor(currencyUnit0, 2599)
        boolean0 = money0.isNegativeOrZero()
        self.assertFalse(boolean0)

    def test018(self) -> None:

        currencyUnit0 = CurrencyUnit("", -466, 42)
        money0 = Money.of2(currencyUnit0, -466)
        boolean0 = money0.isPositive()
        self.assertFalse(boolean0)

    def test017(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        bigDecimal0 = decimal.Decimal((-1819))
        bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_DOWN
        money0 = bigMoney0.toMoney1(roundingMode0)
        boolean0 = money0.isPositiveOrZero()
        self.assertFalse(boolean0)

    def test016(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)
        boolean0 = money0.isZero()
        self.assertTrue(boolean0)

    def test015(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(0)
        money1 = money0.minus2(bigDecimal0)
        self.assertIs(money1, money0)

    def test014(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.ofMajor(currencyUnit0, 0)
        bigDecimal0 = decimal.Decimal(-1)
        roundingMode0 = decimal.ROUND_DOWN
        money1 = money0.minus3(bigDecimal0, roundingMode0)
        self.assertIsNot(money1, money0)

    def test013(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        money1 = money0.minus5(-366.326589124059, roundingMode0)
        self.assertIsNot(money1, money0)

    def test012(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        money0 = Money.zero(currencyUnit0)
        money1 = money0.minusMajor(-645)
        self.assertIsNot(money1, money0)

    def test011(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(10)
        roundingMode0 = decimal.ROUND_HALF_DOWN
        money1 = money0.multipliedBy0(bigDecimal0, roundingMode0)
        self.assertIs(money1, money0)

    def test010(self) -> None:
        money0 = Money.parse("CHF 0.00")
        self.assertIsNotNone(money0)

    def test008(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        hashSet0 = set()
        money0 = Money.total3(currencyUnit0, hashSet0)
        money1 = money0.plus1(money0)
        self.assertIs(money1, money0)

    def test007(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        bigMoney0 = BigMoney.of1(currencyUnit0, 1.0)
        roundingMode0 = RoundingMode.HALF_UP
        money0 = Money.of4(bigMoney0)
        bigInteger0 = BigInteger.ZERO
        bigDecimal0 = BigDecimal(bigInteger0, (-2559))
        money1 = money0.plus3(bigDecimal0, roundingMode0)
        self.assertIs(money1, money0)

    def test006(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        money1 = money0.plusMinor(-2918)
        self.assertIsNot(money1, money0)

    def test005(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.zero(currencyUnit0)
        roundingMode0 = RoundingMode.HALF_DOWN
        money1 = money0.rounded(1827, roundingMode0)
        self.assertIs(money1, money0)

    def test004(self) -> None:

        currencyUnit0 = CurrencyUnit.USD
        money0 = Money.zero(currencyUnit0)
        bigMoney0 = money0.toBigMoney()
        self.assertIsNotNone(bigMoney0)

    def test003(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        bigDecimal0 = decimal.Decimal(1)
        money0 = Money.of0(currencyUnit0, bigDecimal0)
        roundingMode0 = decimal.ROUND_HALF_EVEN
        money1 = money0.withAmount1(bigDecimal0, roundingMode0)
        self.assertIs(money1, money0)

    def test002(self) -> None:

        currencyUnit0 = CurrencyUnit.CHF
        money0 = Money.zero(currencyUnit0)
        money1 = money0.withAmount2(-1.0)
        self.assertIsNot(money1, money0)

    def test001(self) -> None:

        currencyUnit0 = CurrencyUnit.AUD
        bigMoney0 = BigMoney.of1(currencyUnit0, 0.0)
        money0 = bigMoney0.toMoney0()
        roundingMode0 = decimal.ROUND_HALF_EVEN
        money1 = money0.withCurrencyUnit1(currencyUnit0, roundingMode0)
        self.assertIs(money1, money0)

    def test000(self) -> None:

        currencyUnit0 = CurrencyUnit.JPY
        money0 = Money.zero(currencyUnit0)
        bigDecimal0 = decimal.Decimal(1)
        money1 = Money.of0(currencyUnit0, bigDecimal0)
        money2 = money0.minus1(money1)
        self.assertIsNot(money2, money0)
        self.assertFalse(money1.equals(money0))
