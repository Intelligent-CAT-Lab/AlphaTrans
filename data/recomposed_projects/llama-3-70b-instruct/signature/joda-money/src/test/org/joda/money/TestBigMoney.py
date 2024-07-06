from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import decimal
import os
import unittest
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class TestBigMoney(unittest.TestCase):

    __GBP_INT_MAX_PLUS1: BigMoney = None  # LLM could not translate this field

    __GBP_M5_78: BigMoney = BigMoney.parse("GBP -5.78")
    __GBP_M1_23: BigMoney = BigMoney.parse("GBP -1.23")
    __GBP_5_78: BigMoney = BigMoney.parse("GBP 5.78")
    __GBP_2_36: BigMoney = BigMoney.parse("GBP 2.36")
    __GBP_2_35: BigMoney = BigMoney.parse("GBP 2.35")
    __GBP_2_34: BigMoney = BigMoney.parse("GBP 2.34")
    __GBP_2_33: BigMoney = BigMoney.parse("GBP 2.33")
    __GBP_1_23: BigMoney = BigMoney.parse("GBP 1.23")
    __GBP_0_00: BigMoney = BigMoney.parse("GBP 0.00")
    __BIGDEC_M5_78: decimal.Decimal = decimal.Decimal("-5.78")
    __BIGDEC_2_345: decimal.Decimal = decimal.Decimal("2.345")
    __BIGDEC_2_34: decimal.Decimal = decimal.Decimal("2.34")
    __JPY: CurrencyUnit = CurrencyUnit.of1("JPY")
    __USD: CurrencyUnit = CurrencyUnit.of1("USD")
    __EUR: CurrencyUnit = CurrencyUnit.of1("EUR")
    __GBP: CurrencyUnit = CurrencyUnit.of1("GBP")
    __BAD_PROVIDER: BigMoneyProvider = BigMoneyProvider()
    __USD_2_35: BigMoney = BigMoney.parse("USD 2.35")
    __USD_2_34: BigMoney = BigMoney.parse("USD 2.34")
    __USD_1_23: BigMoney = BigMoney.parse("USD 1.23")
    __JPY_423: BigMoney = BigMoney.parse("JPY 423")
    __GBP_LONG_MIN_MAJOR_MINUS1: BigMoney = BigMoney.of0(
        __GBP,
        decimal.Decimal(Long.MIN_VALUE)
        .subtract(decimal.Decimal(1))
        .multiply(decimal.Decimal(100)),
    )
    __GBP_LONG_MAX_MAJOR_PLUS1: BigMoney = BigMoney.of0(
        __GBP,
        decimal.Decimal(Long.MAX_VALUE)
        .add(decimal.Decimal(1))
        .multiply(decimal.Decimal(100)),
    )
    __GBP_LONG_MIN_MINUS1: BigMoney = BigMoney.of0(
        __GBP, BigDecimal.valueOf(Long.MIN_VALUE).subtract(BigDecimal.ONE)
    )
    __GBP_LONG_MAX_PLUS1: BigMoney = BigMoney.of0(
        __GBP, BigDecimal.valueOf(Long.MAX_VALUE).add(BigDecimal.ONE)
    )

    def test_toString_negative(self) -> None:
        test: BigMoney = BigMoney.of0(self.__EUR, self.__BIGDEC_M5_78)
        self.assertEqual("EUR -5.78", test.toString())

    def test_toString_positive(self) -> None:
        test: BigMoney = BigMoney.of0(self.__GBP, self.__BIGDEC_2_34)
        self.assertEqual("GBP 2.34", test.toString())

    def test_equals_false(self) -> None:
        a: BigMoney = self.__GBP_2_34
        self.assertEqual(False, a.equals(None))
        self.assertEqual(False, a.equals(Object()))

    def test_equals_hashCode_positive(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_34
        c: BigMoney = self.__GBP_2_35
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, c.equals(c))

        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

        self.assertEqual(False, a.equals(c))
        self.assertEqual(False, b.equals(c))

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__USD_2_35
        a.isLessThanOrEqual(b)

    def test_isLessThanOrEqual(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_35
        c: BigMoney = self.__GBP_2_36
        self.assertEqual(True, a.isLessThanOrEqual(a))
        self.assertEqual(True, a.isLessThanOrEqual(b))
        self.assertEqual(True, a.isLessThanOrEqual(c))

        self.assertEqual(False, b.isLessThanOrEqual(a))
        self.assertEqual(True, b.isLessThanOrEqual(b))
        self.assertEqual(True, b.isLessThanOrEqual(c))

        self.assertEqual(False, c.isLessThanOrEqual(a))
        self.assertEqual(False, c.isLessThanOrEqual(b))
        self.assertEqual(True, c.isLessThanOrEqual(c))

    def test_isLessThan_currenciesDiffer(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__USD_2_35
        a.isLessThan(b)

    def test_isLessThan(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_35
        c: BigMoney = self.__GBP_2_36
        self.assertEqual(False, a.isLessThan(a))
        self.assertEqual(True, a.isLessThan(b))
        self.assertEqual(True, a.isLessThan(c))

        self.assertEqual(False, b.isLessThan(a))
        self.assertEqual(False, b.isLessThan(b))
        self.assertEqual(True, b.isLessThan(c))

        self.assertEqual(False, c.isLessThan(a))
        self.assertEqual(False, c.isLessThan(b))
        self.assertEqual(False, c.isLessThan(c))

    def test_isGreaterThanOrEqual_currenciesDiffer(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__USD_2_35
        with self.assertRaises(CurrencyMismatchException):
            a.isGreaterThanOrEqual(b)

    def test_isGreaterThanOrEqual(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_35
        c: BigMoney = self.__GBP_2_36
        self.assertEqual(True, a.isGreaterThanOrEqual(a))
        self.assertEqual(False, a.isGreaterThanOrEqual(b))
        self.assertEqual(False, a.isGreaterThanOrEqual(c))

        self.assertEqual(True, b.isGreaterThanOrEqual(a))
        self.assertEqual(True, b.isGreaterThanOrEqual(b))
        self.assertEqual(False, b.isGreaterThanOrEqual(c))

        self.assertEqual(True, c.isGreaterThanOrEqual(a))
        self.assertEqual(True, c.isGreaterThanOrEqual(b))
        self.assertEqual(True, c.isGreaterThanOrEqual(c))

    def test_isGreaterThan_currenciesDiffer(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__USD_2_35
        a.isGreaterThan(b)

    def test_isGreaterThan(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_35
        c: BigMoney = self.__GBP_2_36
        self.assertEqual(False, a.isGreaterThan(a))
        self.assertEqual(False, a.isGreaterThan(b))
        self.assertEqual(False, a.isGreaterThan(c))

        self.assertEqual(True, b.isGreaterThan(a))
        self.assertEqual(False, b.isGreaterThan(b))
        self.assertEqual(False, b.isGreaterThan(c))

        self.assertEqual(True, c.isGreaterThan(a))
        self.assertEqual(True, c.isGreaterThan(b))
        self.assertEqual(False, c.isGreaterThan(c))

    def test_isEqual_currenciesDiffer(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__USD_2_35
        a.isEqual(b)

    def test_isEqual_Money(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: Money = Money.ofMinor(self.__GBP, 234)
        self.assertEqual(True, a.isEqual(b))

    def test_isEqual(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_35
        c: BigMoney = self.__GBP_2_36
        self.assertEqual(True, a.isEqual(a))
        self.assertEqual(True, b.isEqual(b))
        self.assertEqual(True, c.isEqual(c))

        self.assertEqual(False, a.isEqual(b))
        self.assertEqual(False, b.isEqual(a))

        self.assertEqual(False, a.isEqual(c))
        self.assertEqual(False, c.isEqual(a))

        self.assertEqual(False, b.isEqual(c))
        self.assertEqual(False, c.isEqual(b))

    def test_compareTo_wrongType(self) -> None:
        a: Comparable = self.__GBP_2_34
        a.compareTo("NotRightType")

    def test_compareTo_currenciesDiffer(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__USD_2_35
        a.compareTo(b)

    def test_compareTo_Money(self) -> None:
        t: BigMoney = self.__GBP_2_35
        a: Money = Money.ofMinor(self.__GBP, 234)
        b: Money = Money.ofMinor(self.__GBP, 235)
        c: Money = Money.ofMinor(self.__GBP, 236)
        self.assertEqual(1, t.compareTo(a))
        self.assertEqual(0, t.compareTo(b))
        self.assertEqual(-1, t.compareTo(c))

    def test_compareTo_BigMoney(self) -> None:
        a: BigMoney = self.__GBP_2_34
        b: BigMoney = self.__GBP_2_35
        c: BigMoney = self.__GBP_2_36
        self.assertEqual(0, a.compareTo(a))
        self.assertEqual(0, b.compareTo(b))
        self.assertEqual(0, c.compareTo(c))

        self.assertEqual(-1, a.compareTo(b))
        self.assertEqual(1, b.compareTo(a))

        self.assertEqual(-1, a.compareTo(c))
        self.assertEqual(1, c.compareTo(a))

        self.assertEqual(-1, b.compareTo(c))
        self.assertEqual(1, c.compareTo(b))

    def test_isSameCurrency_Money_nullMoney(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_2_34.isSameCurrency(None)

    def test_isSameCurrency_Money_different(self) -> None:
        self.assertEqual(False, self.__GBP_2_34.isSameCurrency(Money.parse("USD 2")))

    def test_isSameCurrency_Money_same(self) -> None:
        self.assertEqual(True, self.__GBP_2_34.isSameCurrency(Money.parse("GBP 2")))

    def test_isSameCurrency_BigMoney_different(self) -> None:
        self.assertEqual(False, self.__GBP_2_34.isSameCurrency(self.__USD_2_34))

    def test_isSameCurrency_BigMoney_same(self) -> None:
        self.assertEqual(True, self.__GBP_2_34.isSameCurrency(self.__GBP_2_35))

    def test_toMoney_RoundingMode_round(self) -> None:
        money: BigMoney = BigMoney.parse("GBP 2.355")
        self.assertEqual(
            Money.parse("GBP 2.36"), money.toMoney1(RoundingMode.HALF_EVEN)
        )

    def test_toMoney_RoundingMode(self) -> None:
        self.assertEqual(
            Money.parse("GBP 2.34"), self.__GBP_2_34.toMoney1(RoundingMode.HALF_EVEN)
        )

    def test_toMoney(self) -> None:
        self.assertEqual(
            Money.of0(self.__GBP, self.__BIGDEC_2_34), self.__GBP_2_34.toMoney0()
        )

    def test_toBigMoney(self) -> None:
        assert self.__GBP_2_34 == self.__GBP_2_34.toBigMoney()

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullRoundingMode(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.convertRetainScale(self.__EUR, self.__bd("2"), None)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullBigDecimal(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.convertRetainScale(self.__EUR, None, RoundingMode.DOWN)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullCurrency(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.convertRetainScale(None, self.__bd("2"), RoundingMode.DOWN)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_sameCurrency(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            self.__GBP_2_33.convertRetainScale(
                self.__GBP, self.__bd("2.5"), RoundingMode.DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_negative(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            self.__GBP_2_33.convertRetainScale(
                self.__EUR, self.__bd("-2.5"), RoundingMode.DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_roundHalfUp(
        self,
    ) -> None:
        test = BigMoney.parse("GBP 2.21").convertRetainScale(
            self.__EUR, self.__bd("2.5"), RoundingMode.HALF_UP
        )
        self.assertEqual("EUR 5.53", test.toString())

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_positive(
        self,
    ) -> None:
        test = BigMoney.parse("GBP 2.2").convertRetainScale(
            self.__EUR, self.__bd("2.5"), RoundingMode.DOWN
        )
        self.assertEqual("EUR 5.5", test.toString())

    def test_convertedTo_CurrencyUnit_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.convertedTo(self.__EUR, None)

    def test_convertedTo_CurrencyUnit_BigDecimal_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.convertedTo(None, self.__bd("2"))

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyWrongFactor(self) -> None:
        with self.assertRaises(ValueError):
            self.__GBP_2_33.convertedTo(self.__GBP, self.__bd("2.5"))

    def test_convertedTo_CurrencyUnit_BigDecimal_negative(self) -> None:
        with self.assertRaises(ValueError):
            self.__GBP_2_33.convertedTo(self.__EUR, self.__bd("-2.5"))

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyCorrectFactor(
        self,
    ) -> None:
        test: BigMoney = self.__GBP_2_33.convertedTo(self.__GBP, self.__bd("1.00000"))
        self.assertEqual(self.__GBP_2_33, test)

    def test_convertedTo_CurrencyUnit_BigDecimal_positive(self) -> None:
        test: BigMoney = self.__GBP_2_33.convertedTo(self.__EUR, self.__bd("2.5"))
        self.assertEqual("EUR 5.825", test.toString())

    def test_round_3(self) -> None:
        test = self.__GBP_2_34.rounded(3, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_round_M1up(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 432.34").rounded(-1, RoundingMode.UP)
        self.assertEqual("GBP 440.00", test.toString())

    def test_round_M1down(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 432.34").rounded(-1, RoundingMode.DOWN)
        self.assertEqual("GBP 430.00", test.toString())

    def test_round_0up(self) -> None:
        test: BigMoney = self.__GBP_2_34.rounded(0, RoundingMode.UP)
        self.assertEqual("GBP 3.00", test.toString())

    def test_round_0down(self) -> None:
        test: BigMoney = self.__GBP_2_34.rounded(0, RoundingMode.DOWN)
        self.assertEqual("GBP 2.00", test.toString())

    def test_round_1up(self) -> None:
        test: BigMoney = self.__GBP_2_34.rounded(1, RoundingMode.UP)
        self.assertEqual("GBP 2.40", test.toString())

    def test_round_1down(self) -> None:
        test: BigMoney = self.__GBP_2_34.rounded(1, RoundingMode.DOWN)
        self.assertEqual("GBP 2.30", test.toString())

    def test_round_2up(self) -> None:
        test = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_round_2down(self) -> None:
        test = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_abs_negative(self) -> None:
        test: BigMoney = BigMoney.parse("GBP -2.34").abs()
        self.assertEqual("GBP 2.34", test.toString())

    def test_abs_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.abs()
        assertSame(self.__GBP_2_34, test)

    def test_negated_negative(self) -> None:
        test: BigMoney = BigMoney.parse("GBP -2.34").negated()
        self.assertEqual("GBP 2.34", test.toString())

    def test_negated_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.negated()
        self.assertEqual("GBP -2.34", test.toString())

    def test_negated_zero(self) -> None:
        test: BigMoney = self.__GBP_0_00.negated()
        assert self.__GBP_0_00 == test

    def test_dividedBy_long_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy2(-3, RoundingMode.DOWN)
        self.assertEqual("GBP -0.78", test.toString())

    def test_dividedBy_long_positive_roundUp(self) -> None:
        test: BigMoney = self.__GBP_2_35.dividedBy2(3, RoundingMode.UP)
        self.assertEqual("GBP 0.79", test.toString())

    def test_dividedBy_long_positive_roundDown(self) -> None:
        test: BigMoney = self.__GBP_2_35.dividedBy2(3, RoundingMode.DOWN)
        self.assertEqual("GBP 0.78", test.toString())

    def test_dividedBy_long_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy2(3, RoundingMode.DOWN)
        self.assertEqual("GBP 0.78", test.toString())

    def test_dividedBy_long_one(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy2(1, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.dividedBy1(2.5, None)

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy1(2.5, RoundingMode.HALF_UP)
        self.assertEqual("GBP 0.94", test.toString())

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:
        test = self.__GBP_2_34.dividedBy1(2.5, RoundingMode.DOWN)
        self.assertEqual("GBP 0.93", test.toString())

    def test_dividedBy_doubleRoundingMode_one(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.dividedBy0(self.__bd("2.5"), None)

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.dividedBy0(None, RoundingMode.DOWN)

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy0(
            self.__bd("-2.5"), RoundingMode.FLOOR
        )
        self.assertEqual("GBP -0.94", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy0(
            self.__bd("2.5"), RoundingMode.HALF_UP
        )
        self.assertEqual("GBP 0.94", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy0(self.__bd("2.5"), RoundingMode.DOWN)
        self.assertEqual("GBP 0.93", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:
        test: BigMoney = self.__GBP_2_34.dividedBy0(
            decimal.Decimal(1), RoundingMode.DOWN
        )
        assert test == self.__GBP_2_34

    def test_multiplyRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.multiplyRetainScale1(2.5, None)

    def test_multiplyRetainScale_doubleRoundingMode_negative(self) -> None:
        test: BigMoney = self.__GBP_2_33.multiplyRetainScale1(-2.5, RoundingMode.FLOOR)
        self.assertEqual("GBP -5.83", test.toString())

    def test_multiplyRetainScale_doubleRoundingMode_positive_halfUp(self) -> None:
        test: BigMoney = self.__GBP_2_33.multiplyRetainScale1(2.5, RoundingMode.HALF_UP)
        self.assertEqual("GBP 5.83", test.toString())

    def test_multiplyRetainScale_doubleRoundingMode_positive(self) -> None:
        test: BigMoney = self.__GBP_2_33.multiplyRetainScale1(2.5, RoundingMode.DOWN)
        self.assertEqual("GBP 5.82", test.toString())

    def test_multiplyRetainScale_doubleRoundingMode_one(self) -> None:
        test: BigMoney = self.__GBP_2_34.multiplyRetainScale1(1, RoundingMode.DOWN)
        assert self.__GBP_2_34 == test

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.multiplyRetainScale0(self.__bd("2.5"), None)

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_multiplyRetainScale_BigDecimalRoundingMode_negative(self) -> None:
        test = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("-2.5"), RoundingMode.FLOOR
        )
        self.assertEqual("GBP -5.83", test.toString())

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        test: BigMoney = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("2.5"), RoundingMode.HALF_UP
        )
        self.assertEqual("GBP 5.83", test.toString())

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive(self) -> None:
        test = self.__GBP_2_33.multiplyRetainScale0(self.__bd("2.5"), RoundingMode.DOWN)
        self.assertEqual("GBP 5.82", test.toString())

    def test_multiplyRetainScale_BigDecimalRoundingMode_one(self) -> None:
        test = self.__GBP_2_34.multiplyRetainScale0(
            decimal.Decimal(1), RoundingMode.DOWN
        )
        assert test == self.__GBP_2_34

    def test_multipliedBy_long_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.multipliedBy2(-3)
        self.assertEqual("GBP -7.02", test.toString())
        self.assertEqual(2, test.getScale())

    def test_multipliedBy_long_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.multipliedBy2(3)
        self.assertEqual("GBP 7.02", test.toString())
        self.assertEqual(2, test.getScale())

    def test_multipliedBy_long_one(self) -> None:
        test: BigMoney = self.__GBP_2_34.multipliedBy2(1)
        assert test == self.__GBP_2_34

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:
        test: BigMoney = self.__GBP_2_33.multipliedBy1(-2.5)
        self.assertEqual("GBP -5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:
        test: BigMoney = self.__GBP_2_33.multipliedBy1(2.5)
        self.assertEqual("GBP 5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:
        test: BigMoney = self.__GBP_2_34.multipliedBy1(1)
        assert test == self.__GBP_2_34

    def test_multipliedBy_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_5_78.multipliedBy0(None)

    def test_multipliedBy_BigDecimal_negative(self) -> None:
        test: BigMoney = self.__GBP_2_33.multipliedBy0(self.__bd("-2.5"))
        self.assertEqual("GBP -5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_BigDecimal_positive(self) -> None:
        test: BigMoney = self.__GBP_2_33.multipliedBy0(self.__bd("2.5"))
        self.assertEqual("GBP 5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_BigDecimal_one(self) -> None:
        test: BigMoney = self.__GBP_2_34.multipliedBy0(decimal.Decimal(1))
        assert test == self.__GBP_2_34

    def test_minusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.minusRetainScale2(2.34, None)

    def test_minusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

        pass  # LLM could not translate this method

    def test_minusRetainScale_doubleRoundingMode_roundDown(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusRetainScale2(1.235, RoundingMode.DOWN)
        self.assertEqual("GBP 1.10", test.toString())

    def test_minusRetainScale_doubleRoundingMode_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusRetainScale2(
            -1.23, RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_doubleRoundingMode_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusRetainScale2(
            1.23, RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusRetainScale_doubleRoundingMode_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusRetainScale2(
            0.0, RoundingMode.UNNECESSARY
        )
        assert test == self.__GBP_2_34

    def test_minusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.minusRetainScale1(self.__BIGDEC_2_34, None)

    def test_minusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_minusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), RoundingMode.UNNECESSARY)

    def test_minusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:
        test = self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), RoundingMode.DOWN)
        self.assertEqual("GBP 1.10", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_negative(self) -> None:
        test = self.__GBP_2_34.minusRetainScale1(
            self.__bd("-1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_positive(self) -> None:
        test = self.__GBP_2_34.minusRetainScale1(
            self.__bd("1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_zero(self) -> None:
        test = self.__GBP_2_34.minusRetainScale1(
            decimal.Decimal(0), RoundingMode.UNNECESSARY
        )
        assertSame(self.__GBP_2_34, test)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.minusRetainScale0(BigMoney.parse("GBP 123"), None)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullBigMoneyProvider(
        self,
    ) -> None:

        pass  # LLM could not translate this method

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(
        self,
    ) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.minusRetainScale0(
                BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY
            )

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.235"), RoundingMode.DOWN
        )
        self.assertEqual("GBP 1.10", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP -1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.zero0(self.__GBP), RoundingMode.UNNECESSARY
        )
        assertSame(self.__GBP_2_34, test)

    def test_minusMinor_scale(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 12").minusMinor(123)
        self.assertEqual("GBP 10.77", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minusMinor_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusMinor(-123)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minusMinor_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusMinor(123)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minusMinor_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusMinor(0)
        assert test == self.__GBP_2_34

    def test_minusMajor_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusMajor(-123)
        self.assertEqual("GBP 125.34", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minusMajor_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusMajor(123)
        self.assertEqual("GBP -120.66", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minusMajor_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.minusMajor(0)
        assert test == self.__GBP_2_34

    def test_minus_double_scale(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus3(1.235)
        self.assertEqual("GBP 1.105", test.toString())
        self.assertEqual(3, test.getScale())

    def test_minus_double_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus3(-1.23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_double_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus3(1.23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_double_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus3(0.0)
        assert test == self.__GBP_2_34

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.minus2(None)

    def test_minus_BigDecimal_scale(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus2(self.__bd("1.235"))
        self.assertEqual("GBP 1.105", test.toString())
        self.assertEqual(3, test.getScale())

    def test_minus_BigDecimal_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus2(self.__bd("-1.23"))
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigDecimal_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus2(self.__bd("1.23"))
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigDecimal_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus2(decimal.Decimal(0))
        assert test == self.__GBP_2_34

    def test_minus_BigMoneyProvider_badProvider(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.minus1(None)

    def test_minus_BigMoneyProvider_currencyMismatch(self) -> None:
        with self.assertRaises(CurrencyMismatchException):
            self.__GBP_M5_78.minus1(self.__USD_1_23)

    def test_minus_BigMoneyProvider_Money(self) -> None:
        test = self.__GBP_2_34.minus1(BigMoney.ofMinor(self.__GBP, 1))
        self.assertEqual("GBP 2.33", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigMoneyProvider_scale(self) -> None:
        test = self.__GBP_2_34.minus1(BigMoney.parse("GBP 1.111"))
        self.assertEqual("GBP 1.229", test.toString())
        self.assertEqual(3, test.getScale())

    def test_minus_BigMoneyProvider_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus1(self.__GBP_M1_23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigMoneyProvider_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.minus1(self.__GBP_1_23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigMoneyProvider_zero(self) -> None:
        test = self.__GBP_2_34.minus1(self.__GBP_0_00)
        assert test == self.__GBP_2_34

    def test_minus_Iterable_badProvider(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = typing.cast(
            typing.Iterable[BigMoneyProvider],
            typing.cast(typing.List[BigMoneyProvider], [BigMoneyProvider()]),
        )
        self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_nullIterable(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.minus0(None)

    def test_minus_Iterable_nullEntry(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__GBP_2_33, None]
        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_currencyMismatch(self) -> None:
        iterable: Iterable[BigMoneyProvider] = Arrays.asList(GBP_2_33, JPY_423)
        with self.assertRaises(CurrencyMismatchException):
            GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_zero(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__GBP_0_00]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        self.assertEqual(self.__GBP_2_34, test)

    def test_minus_Iterable_Mixed(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_Iterable_Money(self) -> None:
        iterable: typing.Iterable[Money] = [
            self.__GBP_2_33.toMoney0(),
            self.__GBP_1_23.toMoney0(),
        ]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_minus_Iterable_BigMoney(self) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_minus_Iterable_BigMoneyProvider(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_plusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.plusRetainScale2(2.34, None)

    def test_plusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.plusRetainScale2(1.235, RoundingMode.UNNECESSARY)

    def test_plusRetainScale_doubleRoundingMode_roundDown(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusRetainScale2(1.235, RoundingMode.DOWN)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_doubleRoundingMode_negative(self) -> None:
        test = self.__GBP_2_34.plusRetainScale2(-1.23, RoundingMode.UNNECESSARY)
        self.assertEqual("GBP 1.11", test.toString())

    def test_plusRetainScale_doubleRoundingMode_positive(self) -> None:
        test = self.__GBP_2_34.plusRetainScale2(1.23, RoundingMode.UNNECESSARY)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_doubleRoundingMode_zero(self) -> None:

        pass  # LLM could not translate this method

    def test_plusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_M5_78.plusRetainScale1(self.__BIGDEC_2_34, None)

    def test_plusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_plusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        self.__GBP_2_34.plusRetainScale1(self.__bd("1.235"), RoundingMode.UNNECESSARY)

    def test_plusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:
        test = self.__GBP_2_34.plusRetainScale1(self.__bd("1.235"), RoundingMode.DOWN)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_BigDecimalRoundingMode_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusRetainScale1(
            self.__bd("-1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_plusRetainScale_BigDecimalRoundingMode_positive(self) -> None:
        test = self.__GBP_2_34.plusRetainScale1(
            self.__bd("1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_BigDecimalRoundingMode_zero(self) -> None:
        test = self.__GBP_2_34.plusRetainScale1(
            decimal.Decimal(0), RoundingMode.UNNECESSARY
        )
        assert test == self.__GBP_2_34

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.plusRetainScale0(BigMoney.parse("GBP 1.23"), None)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.plusRetainScale0(
                BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY
            )

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:
        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP 1.235"), RoundingMode.DOWN
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:
        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP -1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_plusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:
        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:
        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.zero0(self.__GBP), RoundingMode.UNNECESSARY
        )
        assertSame(self.__GBP_2_34, test)

    def test_plusMinor_scale(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 12").plusMinor(123)
        self.assertEqual("GBP 13.23", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMinor_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusMinor(-123)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMinor_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusMinor(123)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMinor_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusMinor(0)
        assert test == self.__GBP_2_34

    def test_plusMajor_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusMajor(-123)
        self.assertEqual("GBP -120.66", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMajor_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusMajor(123)
        self.assertEqual("GBP 125.34", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMajor_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.plusMajor(0)
        assert test == self.__GBP_2_34

    def test_plus_double_scale(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus3(1.234)
        self.assertEqual("GBP 3.574", test.toString())
        self.assertEqual(3, test.getScale())

    def test_plus_double_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus3(-1.23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_double_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus3(1.23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_double_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus3(0.0)
        assert self.__GBP_2_34 == test

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_BigDecimal_scale(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus2(self.__bd("1.235"))
        self.assertEqual("GBP 3.575", test.toString())
        self.assertEqual(3, test.getScale())

    def test_plus_BigDecimal_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus2(self.__bd("-1.23"))
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigDecimal_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus2(self.__bd("1.23"))
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigDecimal_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus2(decimal.Decimal(0))
        assert test == self.__GBP_2_34

    def test_plus_BigMoneyProvider_badProvider(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.plus1(None)

    def test_plus_BigMoneyProvider_currencyMismatch(self) -> None:
        with self.assertRaises(CurrencyMismatchException):
            self.__GBP_M5_78.plus1(self.__USD_1_23)

    def test_plus_BigMoneyProvider_Money(self) -> None:
        test = self.__GBP_2_34.plus1(BigMoney.ofMinor(self.__GBP, 1))
        self.assertEqual("GBP 2.35", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigMoneyProvider_scale(self) -> None:
        test = self.__GBP_2_34.plus1(BigMoney.parse("GBP 1.111"))
        self.assertEqual("GBP 3.451", test.toString())
        self.assertEqual(3, test.getScale())

    def test_plus_BigMoneyProvider_negative(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus1(self.__GBP_M1_23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigMoneyProvider_positive(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus1(self.__GBP_1_23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigMoneyProvider_zero(self) -> None:
        test: BigMoney = self.__GBP_2_34.plus1(self.__GBP_0_00)
        assert test == self.__GBP_2_34

    def test_plus_Iterable_badProvider(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = typing.cast(
            typing.Iterable[BigMoneyProvider],
            typing.cast(typing.List[BigMoneyProvider], [BigMoneyProvider()]),
        )
        self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_nullIterable(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_M5_78.plus0(None)

    def test_plus_Iterable_nullEntry(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__GBP_2_33, None]
        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_currencyMismatch(self) -> None:
        iterable: Iterable[BigMoneyProvider] = Arrays.asList(GBP_2_33, JPY_423)
        with self.assertRaises(CurrencyMismatchException):
            GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_zero(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__GBP_0_00]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        self.assertEqual(self.__GBP_2_34, test)

    def test_plus_Iterable_Mixed(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_Iterable_Money(self) -> None:
        iterable: typing.Iterable[Money] = [
            self.__GBP_2_33.toMoney0(),
            self.__GBP_1_23.toMoney0(),
        ]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_plus_Iterable_BigMoney(self) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_plus_Iterable_BigMoneyProvider(self) -> None:
        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_withAmount_double_same(self) -> None:
        test: BigMoney = self.__GBP_2_34.withAmount1(2.34)
        assertSame(self.__GBP_2_34, test)

    def test_withAmount_double(self) -> None:
        test: BigMoney = self.__GBP_2_34.withAmount1(2.345)
        self.assertEqual(self.__bd("2.345"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_2_34.withAmount0(None)

    def test_withAmount_BigDecimal_same(self) -> None:
        test: BigMoney = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_34)
        assert test is self.__GBP_2_34

    def test_withAmount_BigDecimal(self) -> None:
        test: BigMoney = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_345)
        self.assertEqual(self.__bd("2.345"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_isNegativeOrZero(self) -> None:
        self.assertEqual(True, self.__GBP_0_00.isNegativeOrZero())
        self.assertEqual(False, self.__GBP_2_34.isNegativeOrZero())
        self.assertEqual(True, self.__GBP_M5_78.isNegativeOrZero())

    def test_isNegative(self) -> None:
        self.assertEqual(False, self.__GBP_0_00.isNegative())
        self.assertEqual(False, self.__GBP_2_34.isNegative())
        self.assertEqual(True, self.__GBP_M5_78.isNegative())

    def test_isPositiveOrZero(self) -> None:
        self.assertEqual(True, self.__GBP_0_00.isPositiveOrZero())
        self.assertEqual(True, self.__GBP_2_34.isPositiveOrZero())
        self.assertEqual(False, self.__GBP_M5_78.isPositiveOrZero())

    def test_isPositive(self) -> None:
        self.assertEqual(False, self.__GBP_0_00.isPositive())
        self.assertEqual(True, self.__GBP_2_34.isPositive())
        self.assertEqual(False, self.__GBP_M5_78.isPositive())

    def test_isZero(self) -> None:
        self.assertEqual(True, self.__GBP_0_00.isZero())
        self.assertEqual(False, self.__GBP_2_34.isZero())
        self.assertEqual(False, self.__GBP_M5_78.isZero())

    def test_getMinorPart_negative(self) -> None:
        self.assertEqual(-78, self.__GBP_M5_78.getMinorPart())

    def test_getMinorPart_positive(self) -> None:
        self.assertEqual(34, self.__GBP_2_34.getMinorPart())

    def test_getAmountMinorInt_tooBigNegative(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_INT_MIN_MINUS1.getAmountMinorInt()

    def test_getAmountMinorInt_tooBigPositive(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_INT_MAX_PLUS1.getAmountMinorInt()

    def test_getAmountMinorInt_negative(self) -> None:
        self.assertEqual(-578, self.__GBP_M5_78.getAmountMinorInt())

    def test_getAmountMinorInt_positive(self) -> None:
        self.assertEqual(234, self.__GBP_2_34.getAmountMinorInt())

    def test_getAmountMinorLong_tooBigNegative(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_LONG_MIN_MINUS1.getAmountMinorLong()

    def test_getAmountMinorLong_tooBigPositive(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_LONG_MAX_PLUS1.getAmountMinorLong()

    def test_getAmountMinorLong_negative(self) -> None:
        self.assertEqual(-578, self.__GBP_M5_78.getAmountMinorLong())

    def test_getAmountMinorLong_positive(self) -> None:
        self.assertEqual(234, self.__GBP_2_34.getAmountMinorLong())

    def test_getAmountMinor_negative(self) -> None:
        self.assertEqual(decimal.Decimal(-578), self.__GBP_M5_78.getAmountMinor())

    def test_getAmountMinor_positive(self) -> None:
        self.assertEqual(decimal.Decimal(234), self.__GBP_2_34.getAmountMinor())

    def test_getAmountMajorInt_tooBigNegative(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_INT_MIN_MAJOR_MINUS1.getAmountMajorInt()

    def test_getAmountMajorInt_tooBigPositive(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_INT_MAX_MAJOR_PLUS1.getAmountMajorInt()

    def test_getAmountMajorInt_negative(self) -> None:
        self.assertEqual(-5, self.__GBP_M5_78.getAmountMajorInt())

    def test_getAmountMajorInt_positive(self) -> None:
        self.assertEqual(2, self.__GBP_2_34.getAmountMajorInt())

    def test_getAmountMajorLong_tooBigNegative(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_LONG_MIN_MAJOR_MINUS1.getAmountMajorLong()

    def test_getAmountMajorLong_tooBigPositive(self) -> None:
        with self.assertRaises(ArithmeticError):
            self.__GBP_LONG_MAX_MAJOR_PLUS1.getAmountMajorLong()

    def test_getAmountMajorLong_negative(self) -> None:
        self.assertEqual(-5, self.__GBP_M5_78.getAmountMajorLong())

    def test_getAmountMajorLong_positive(self) -> None:
        self.assertEqual(2, self.__GBP_2_34.getAmountMajorLong())

    def test_getAmountMajor_negative(self) -> None:
        self.assertEqual(decimal.Decimal(-5), self.__GBP_M5_78.getAmountMajor())

    def test_getAmountMajor_positive(self) -> None:
        self.assertEqual(decimal.Decimal(2), self.__GBP_2_34.getAmountMajor())

    def test_getAmount_negative(self) -> None:
        self.assertEqual(self.__BIGDEC_M5_78, self.__GBP_M5_78.getAmount())

    def test_getAmount_positive(self) -> None:
        self.assertEqual(self.__BIGDEC_2_34, self.__GBP_2_34.getAmount())

    def test_withCurrencyScale_intRoundingMode_lessJPY(self) -> None:
        test: BigMoney = BigMoney.parse("JPY 2.345").withCurrencyScale1(RoundingMode.UP)
        self.assertEqual(self.__bd("3"), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_withCurrencyScale_intRoundingMode_more(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 2.3").withCurrencyScale1(RoundingMode.UP)
        self.assertEqual(self.__bd("2.30"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_intRoundingMode_less(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 2.345").withCurrencyScale1(RoundingMode.UP)
        self.assertEqual(self.__bd("2.35"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_int_less(self) -> None:
        with self.assertRaises(ArithmeticException):
            BigMoney.parse("GBP 2.345").withCurrencyScale0()

    def test_withCurrencyScale_int_more(self) -> None:
        test: BigMoney = BigMoney.parse("GBP 2.3").withCurrencyScale0()
        self.assertEqual(self.__bd("2.30"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_int_same(self) -> None:
        test: BigMoney = self.__GBP_2_34.withCurrencyScale0()
        assertSame(self.__GBP_2_34, test)

    def test_withScale_intRoundingMode_more(self) -> None:
        test: BigMoney = self.__GBP_2_34.withScale1(3, RoundingMode.UP)
        self.assertEqual(self.__bd("2.340"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_withScale_intRoundingMode_less(self) -> None:
        test: BigMoney = self.__GBP_2_34.withScale1(1, RoundingMode.UP)
        self.assertEqual(self.__bd("2.4"), test.getAmount())
        self.assertEqual(1, test.getScale())

    def test_withScale_int_less(self) -> None:
        with self.assertRaises(ArithmeticException):
            BigMoney.parse("GBP 2.345").withScale0(2)

    def test_withScale_int_more(self) -> None:
        test: BigMoney = self.__GBP_2_34.withScale0(3)
        self.assertEqual(self.__bd("2.340"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_withScale_int_same(self) -> None:
        test: BigMoney = self.__GBP_2_34.withScale0(2)
        assertSame(self.__GBP_2_34, test)

    def test_isCurrencyScale_JPY(self) -> None:
        self.assertEqual(True, BigMoney.parse("JPY 2").isCurrencyScale())
        self.assertEqual(False, BigMoney.parse("JPY 2.3").isCurrencyScale())
        self.assertEqual(False, BigMoney.parse("JPY 2.34").isCurrencyScale())
        self.assertEqual(False, BigMoney.parse("JPY 2.345").isCurrencyScale())

    def test_isCurrencyScale_GBP(self) -> None:
        self.assertEqual(False, BigMoney.parse("GBP 2").isCurrencyScale())
        self.assertEqual(False, BigMoney.parse("GBP 2.3").isCurrencyScale())
        self.assertEqual(True, BigMoney.parse("GBP 2.34").isCurrencyScale())
        self.assertEqual(False, BigMoney.parse("GBP 2.345").isCurrencyScale())

    def test_getScale_JPY(self) -> None:
        self.assertEqual(0, self.__JPY_423.getScale())

    def test_getScale_GBP(self) -> None:
        self.assertEqual(2, self.__GBP_2_34.getScale())

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_2_34.withCurrencyUnit(None)

    def test_withCurrencyUnit_Currency_differentCurrencyScale(self) -> None:
        test: BigMoney = self.__GBP_2_34.withCurrencyUnit(self.__JPY)
        self.assertEqual("JPY 2.34", test.toString())

    def test_withCurrencyUnit_Currency_same(self) -> None:
        test: BigMoney = self.__GBP_2_34.withCurrencyUnit(self.__GBP)
        assert test is self.__GBP_2_34

    def test_withCurrencyUnit_Currency(self) -> None:
        test: BigMoney = self.__GBP_2_34.withCurrencyUnit(self.__USD)
        self.assertEqual("USD 2.34", test.toString())

    def test_getCurrencyUnit_EUR(self) -> None:
        self.assertEqual(self.__EUR, BigMoney.parse("EUR -5.78").getCurrencyUnit())

    def test_getCurrencyUnit_GBP(self) -> None:
        self.assertEqual(self.__GBP, self.__GBP_2_34.getCurrencyUnit())

    def test_scaleNormalization3(self) -> None:
        a: BigMoney = BigMoney.of0(self.__GBP, decimal.Decimal("100"))
        b: BigMoney = BigMoney.of0(self.__GBP, decimal.Decimal("1E+2"))
        self.assertEqual("GBP 100", a.toString())
        self.assertEqual("GBP 100", b.toString())
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

    def test_scaleNormalization2(self) -> None:
        a: BigMoney = BigMoney.ofScale2(self.__GBP, 1, 1)
        b: BigMoney = BigMoney.ofScale2(self.__GBP, 10, 2)
        self.assertEqual("GBP 0.1", a.toString())
        self.assertEqual("GBP 0.10", b.toString())
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(False, a.equals(b))
        self.assertEqual(False, b.equals(a))
        self.assertEqual(False, a.hashCode() == b.hashCode())

    def test_scaleNormalization1(self) -> None:
        a: BigMoney = BigMoney.ofScale2(self.__GBP, 100, 0)
        b: BigMoney = BigMoney.ofScale2(self.__GBP, 1, -2)
        self.assertEqual("GBP 100", a.toString())
        self.assertEqual("GBP 100", b.toString())
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

    def test_constructor_null2(self) -> None:
        con = BigMoney.__init__.__annotations__["return"]
        try:
            con.setAccessible(True)
            con.newInstance([0, None, self.__GBP])
            self.fail()
        except InvocationTargetException as ex:
            self.assertEqual(AssertionError, ex.getCause().__class__)

    def test_constructor_null1(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_parse_String_nullString(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.parse(None)

    def test_factory_parse_String_badCurrency(self) -> None:
        with self.assertRaises(ValueError):
            BigMoney.parse("GBX 2.34")

    def test_factory_parse_String_exponent(self) -> None:
        with self.assertRaises(ValueError):
            BigMoney.parse("GBP 234E2")

    def test_factory_parse_String_tooShort(self) -> None:
        with self.assertRaises(ValueError):
            BigMoney.parse("GBP")

    def test_factory_parse(
        self, str: str, currency: CurrencyUnit, amountStr: str, scale: int
    ) -> None:
        test = BigMoney.parse(str)
        self.assertEqual(currency, test.getCurrencyUnit())
        self.assertEqual(self.__bd(amountStr), test.getAmount())
        self.assertEqual(scale, test.getScale())

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:
        return [
            ["GBP 2.43", TestBigMoney.__GBP, "2.43", 2],
            ["GBP +12.57", TestBigMoney.__GBP, "12.57", 2],
            ["GBP -5.87", TestBigMoney.__GBP, "-5.87", 2],
            ["GBP 0.99", TestBigMoney.__GBP, "0.99", 2],
            ["GBP .99", TestBigMoney.__GBP, "0.99", 2],
            ["GBP +.99", TestBigMoney.__GBP, "0.99", 2],
            ["GBP +0.99", TestBigMoney.__GBP, "0.99", 2],
            ["GBP -.99", TestBigMoney.__GBP, "-0.99", 2],
            ["GBP -0.99", TestBigMoney.__GBP, "-0.99", 2],
            ["GBP 0", TestBigMoney.__GBP, "0", 0],
            ["GBP 2", TestBigMoney.__GBP, "2", 0],
            ["GBP 123.", TestBigMoney.__GBP, "123", 0],
            ["GBP3", TestBigMoney.__GBP, "3", 0],
            ["GBP3.10", TestBigMoney.__GBP, "3.10", 2],
            ["GBP  3.10", TestBigMoney.__GBP, "3.10", 2],
            ["GBP   3.10", TestBigMoney.__GBP, "3.10", 2],
            ["GBP                           3.10", TestBigMoney.__GBP, "3.10", 2],
            ["GBP 123.456789", TestBigMoney.__GBP, "123.456789", 6],
        ]

    def test_factory_total_CurrencyUnitIterable_badProvider(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__BAD_PROVIDER]
        with pytest.raises(NullPointerException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:
        with self.assertRaises(NullPointerException):
            iterable: typing.Iterable[BigMoney] = [
                None,
                self.__GBP_2_33,
                self.__GBP_2_36,
            ]
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(
        self,
    ) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__GBP_2_33, self.__JPY_423]
        BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:
        iterable: typing.Iterable[BigMoney] = []
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitIterable_Mixed(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33,
        ]
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("356.00"), test.getAmount())

    def test_factory_total_CurrencyUnitIterable(self) -> None:
        iterable: typing.Iterable[BigMoney] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            BigMoney.of1(self.__GBP, 2.361),
        ]
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("5921"), test.getAmount())

    def test_factory_total_CurrencyUnitArray_badProvider(self) -> None:
        array: typing.List[BigMoneyProvider] = [self.__BAD_PROVIDER]
        with pytest.raises(NullPointerException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_badProvider(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.total2(self.__GBP, self.__BAD_PROVIDER)

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:
        array: typing.List[BigMoney] = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.total2(self.__GBP, self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:
        array: typing.List[BigMoney] = [None, self.__GBP_2_33, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.total2(self.__GBP, None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:
        array: typing.List[BigMoney] = [self.__GBP_2_33, self.__JPY_423]
        BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:
        with self.assertRaises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, self.__GBP_2_33, self.__JPY_423)

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:
        array: typing.List[BigMoney] = [self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:
        with self.assertRaises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, self.__JPY_423)

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:
        array: typing.List[BigMoney] = []
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:
        test: BigMoney = BigMoney.total2(self.__GBP)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3Money(self) -> None:
        array: typing.List[Money] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36.toMoney0(),
        ]
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3Mixed(self) -> None:
        array: typing.List[BigMoneyProvider] = [
            self.__GBP_1_23,
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36,
        ]
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_3Mixed(self) -> None:
        test: BigMoney = BigMoney.total2(
            self.__GBP, self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3(self) -> None:
        array: typing.List[BigMoney] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            self.__GBP_2_36,
        ]
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:
        test: BigMoney = BigMoney.total2(
            self.__GBP, self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_1(self) -> None:
        array: typing.List[BigMoney] = [self.__GBP_1_23]
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:
        test: BigMoney = BigMoney.total2(self.__GBP, self.__GBP_1_23)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_Iterable_badProvider(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [self.__BAD_PROVIDER]
        BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullNotFirst(self) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullFirst(self) -> None:
        iterable: typing.Iterable[BigMoney] = [None, self.__GBP_2_33, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:
        iterable: typing.Iterable[BigMoney] = [self.__GBP_2_33, self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_empty(self) -> None:
        with self.assertRaises(ValueError):
            iterable: typing.Iterable[BigMoneyProvider] = []
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_Mixed(self) -> None:
        iterable: typing.Iterable[BigMoneyProvider] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33,
        ]
        test: BigMoney = BigMoney.total1(iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("356.00"), test.getAmount())

    def test_factory_total_Iterable(self) -> None:
        iterable: typing.Iterable[BigMoney] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            BigMoney.of1(self.__GBP, 2.361),
        ]
        test: BigMoney = BigMoney.total1(iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("5921"), test.getAmount())

    def test_factory_total_array_badProvider(self) -> None:
        array: typing.List[BigMoneyProvider] = [self.__BAD_PROVIDER]
        BigMoney.total0(array)

    def test_factory_total_varargs_badProvider(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.total0(self.__BAD_PROVIDER)

    def test_factory_total_array_nullNotFirst(self) -> None:
        array: typing.List[BigMoneyProvider] = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total0(array)

    def test_factory_total_varargs_nullNotFirst(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.total0([self.__GBP_2_33, None, self.__GBP_2_36])

    def test_factory_total_array_nullFirst(self) -> None:
        with self.assertRaises(NullPointerException):
            array: typing.List[BigMoneyProvider] = [
                None,
                self.__GBP_2_33,
                self.__GBP_2_36,
            ]
            BigMoney.total0(array)

    def test_factory_total_varargs_nullFirst(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.total0(None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_array_currenciesDiffer(self) -> None:
        array: typing.List[BigMoneyProvider] = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total0(array)

    def test_factory_total_varargs_currenciesDiffer(self) -> None:
        with self.assertRaises(CurrencyMismatchException):
            BigMoney.total0([self.__GBP_2_33, self.__JPY_423])

    def test_factory_total_array_empty(self) -> None:
        with self.assertRaises(ValueError):
            array = []
            BigMoney.total0(array)

    def test_factory_total_varargs_empty(self) -> None:
        with self.assertRaises(ValueError):
            BigMoney.total0()

    def test_factory_total_array_3Money(self) -> None:
        array: typing.List[Money] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36.toMoney0(),
        ]
        test: BigMoney = BigMoney.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_array_3Mixed(self) -> None:
        array: typing.List[BigMoneyProvider] = [
            self.__GBP_1_23,
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36,
        ]
        test: BigMoney = BigMoney.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_varargs_3Mixed(self) -> None:
        test: BigMoney = BigMoney.total0(
            [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_array_1BigMoney(self) -> None:
        array: typing.List[BigMoneyProvider] = [self.__GBP_1_23]
        test: BigMoney = BigMoney.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_varargs_1BigMoney(self) -> None:
        test: BigMoney = BigMoney.total0([self.__GBP_1_23])
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_from_BigMoneyProvider_badProvider(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.of2(self.__BAD_PROVIDER)

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.of2(None)

    def test_factory_from_BigMoneyProvider(self) -> None:
        test = BigMoney.of2(BigMoney.parse("GBP 104.23"))
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(10423, test.getAmountMinorInt())
        self.assertEqual(2, test.getScale())

    def test_factory_zero_Currency_int_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.zero1(None, 3)

    def test_factory_zero_Currency_int_negativeScale(self) -> None:
        test: BigMoney = BigMoney.zero1(self.__GBP, -3)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(0), test.getAmount())

    def test_factory_zero_Currency_int(self) -> None:
        test: BigMoney = BigMoney.zero1(self.__GBP, 3)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(0, 3), test.getAmount())

    def test_factory_zero_Currency_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.zero0(None)

    def test_factory_zero_Currency(self) -> None:
        test: BigMoney = BigMoney.zero0(self.__GBP)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(0), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.ofMinor(None, 234)

    def test_factory_ofMinor_Currency_long(self) -> None:
        test: BigMoney = BigMoney.ofMinor(self.__GBP, 234)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__bd("2.34"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.ofMajor(None, 234)

    def test_factory_ofMajor_Currency_long(self) -> None:
        test: BigMoney = BigMoney.ofMajor(self.__GBP, 234)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__bd("234"), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_factory_ofScale_Currency_long_int_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofScale2(None, 234, 2)

    def test_factory_ofScale_Currency_long_int_negativeScale(self) -> None:
        test: BigMoney = BigMoney.ofScale2(self.__GBP, 234, -4)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(BigDecimal.valueOf(2340000, 0), test.getAmount())

    def test_factory_ofScale_Currency_long_int(self) -> None:
        test: BigMoney = BigMoney.ofScale2(self.__GBP, 234, 4)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(BigDecimal.valueOf(234, 4), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullRoundingMode(
        self,
    ) -> None:
        with self.assertRaises(TypeError):
            BigMoney.ofScale1(self.__GBP, self.__BIGDEC_2_34, 2, None)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullBigDecimal(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.ofScale1(self.__GBP, None, 2, RoundingMode.DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullCurrency(
        self,
    ) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.ofScale1(None, self.__BIGDEC_2_34, 2, RoundingMode.DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_UNNECESSARY(
        self,
    ) -> None:
        with self.assertRaises(ArithmeticException):
            BigMoney.ofScale1(
                self.__JPY, self.__BIGDEC_2_34, 1, RoundingMode.UNNECESSARY
            )

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_negativeScale(
        self,
    ) -> None:

        pass  # LLM could not translate this method

    def test_factory_ofScale_Currency_BigDecimal_int_JPY_RoundingMode_UP(self) -> None:
        test: BigMoney = BigMoney.ofScale1(
            self.__JPY, self.__BIGDEC_2_34, 0, RoundingMode.UP
        )
        self.assertEqual(self.__JPY, test.getCurrencyUnit())
        self.assertEqual(BigDecimal.valueOf(3, 0), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_DOWN(self) -> None:
        test: BigMoney = BigMoney.ofScale1(
            self.__GBP, self.__BIGDEC_2_34, 1, RoundingMode.DOWN
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(BigDecimal.valueOf(23, 1), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(TypeError):
            BigMoney.ofScale0(self.__GBP, None, 2)

    def test_factory_ofScale_Currency_BigDecimal_nullCurrency(self) -> None:
        with self.assertRaises(TypeError):
            BigMoney.ofScale0(None, self.__BIGDEC_2_34, 2)

    def test_factory_ofScale_Currency_BigDecimal_invalidScale(self) -> None:
        with self.assertRaises(ArithmeticException):
            BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_345, 2)

    def test_factory_ofScale_Currency_BigDecimal_negativeScale(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_ofScale_Currency_BigDecimal_int(self) -> None:
        test: BigMoney = BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_34, 4)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("23400").scaleb(4), test.getAmount())

    def test_factory_of_Currency_double_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.of1(None, 2.345)

    def test_factory_of_Currency_double_big(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_medium(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_zero(self) -> None:
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0)), BigMoney.of1(self.__GBP, 0)
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0)), BigMoney.of1(self.__GBP, -0)
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0)), BigMoney.of1(self.__GBP, 0.0)
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0)), BigMoney.of1(self.__GBP, 0.00)
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0)), BigMoney.of1(self.__GBP, -0.0)
        )

    def test_factory_of_Currency_double_trailingZero2(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_trailingZero1(self) -> None:
        test: BigMoney = BigMoney.of1(self.__GBP, 1.230)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(BigDecimal.valueOf(123, 2), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_factory_of_Currency_double(self) -> None:
        test: BigMoney = BigMoney.of1(self.__GBP, 2.345)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__BIGDEC_2_345, test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_factory_of_Currency_subClass2(self) -> None:
        class BadInteger(BigInteger):
            serialVersionUID: int = 1

            def __init__(self) -> None:
                super().__init__("123")

        class BadDecimal(BigDecimal):
            serialVersionUID: int = 1

            def __init__(self) -> None:
                super().__init__(432)

            def unscaledValue(self) -> BigInteger:
                return BadInteger()

            def scale(self) -> int:
                return 1

        sub: BigDecimal = BadDecimal()
        test: BigMoney = BigMoney.of0(self.__GBP, sub)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__bd("12.3"), test.getAmount())
        self.assertEqual(1, test.getScale())
        self.assertEqual(True, test.getAmount().__class__ == BigDecimal)

    def test_factory_of_Currency_subClass1(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.of0(self.__GBP, None)

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:
        with self.assertRaises(NullPointerException):
            BigMoney.of0(None, self.__BIGDEC_2_345)

    def test_factory_of_Currency_BigDecimal(self) -> None:
        test: BigMoney = BigMoney.of0(self.__GBP, self.__BIGDEC_2_345)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__BIGDEC_2_345, test.getAmount())
        self.assertEqual(3, test.getScale())

    @staticmethod
    def __bd(str: str) -> decimal.Decimal:
        return decimal.Decimal(str)
