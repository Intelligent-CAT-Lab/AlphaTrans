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
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class TestMoney(unittest.TestCase):

    __USD_2_35: Money = Money.parse("USD 2.35")
    __USD_2_34: Money = Money.parse("USD 2.34")
    __USD_1_23: Money = Money.parse("USD 1.23")
    __JPY_423: Money = Money.parse("JPY 423")
    __GBP_INT_MIN_MAJOR_MINUS1: Money = None  # LLM could not translate this field

    __GBP_INT_MAX_MAJOR_PLUS1: Money = None  # LLM could not translate this field

    __GBP_INT_MIN_MINUS1: Money = None  # LLM could not translate this field

    __GBP_INT_MAX_PLUS1: Money = None  # LLM could not translate this field

    __GBP_M5_78: Money = Money.parse("GBP -5.78")
    __GBP_M1_23: Money = Money.parse("GBP -1.23")
    __GBP_5_78: Money = Money.parse("GBP 5.78")
    __GBP_2_36: Money = Money.parse("GBP 2.36")
    __GBP_2_35: Money = Money.parse("GBP 2.35")
    __GBP_2_34: Money = Money.parse("GBP 2.34")
    __GBP_2_33: Money = Money.parse("GBP 2.33")
    __GBP_1_23: Money = Money.parse("GBP 1.23")
    __GBP_0_00: Money = Money.parse("GBP 0.00")
    __BIGDEC_M5_78: decimal.Decimal = decimal.Decimal("-5.78")
    __BIGDEC_2_345: decimal.Decimal = decimal.Decimal("2.345")
    __BIGDEC_2_34: decimal.Decimal = decimal.Decimal("2.34")
    __BIGDEC_2_3: decimal.Decimal = decimal.Decimal("2.3")
    __JPY: CurrencyUnit = CurrencyUnit.of1("JPY")
    __USD: CurrencyUnit = CurrencyUnit.of1("USD")
    __EUR: CurrencyUnit = CurrencyUnit.of1("EUR")
    __GBP: CurrencyUnit = CurrencyUnit.of1("GBP")
    __GBP_LONG_MIN_MAJOR_MINUS1: Money = Money.of0(
        __GBP,
        decimal.Decimal(Long.MIN_VALUE)
        .subtract(decimal.Decimal(1))
        .multiply(decimal.Decimal(100)),
    )
    __GBP_LONG_MAX_MAJOR_PLUS1: Money = Money.of0(
        __GBP,
        decimal.Decimal(Long.MAX_VALUE)
        .add(decimal.Decimal(1))
        .multiply(decimal.Decimal(100)),
    )
    __GBP_LONG_MIN_MINUS1: Money = Money.of0(
        __GBP, decimal.Decimal(-9223372036854775808)
    )
    __GBP_LONG_MAX_PLUS1: Money = Money.of0(
        __GBP, BigDecimal.valueOf(Long.MAX_VALUE).add(BigDecimal.ONE)
    )

    def test_toString_negative(self) -> None:
        test: Money = Money.of0(self.__EUR, self.__BIGDEC_M5_78)
        self.assertEqual("EUR -5.78", test.toString())

    def test_toString_positive(self) -> None:
        test: Money = Money.of0(self.__GBP, self.__BIGDEC_2_34)
        self.assertEqual("GBP 2.34", test.toString())

    def test_equals_false(self) -> None:
        a: Money = self.__GBP_2_34
        self.assertEqual(False, a.equals(None))
        self.assertEqual(False, a.equals(Object()))

    def test_equals_hashCode_positive(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_34
        c: Money = self.__GBP_2_35
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, c.equals(c))

        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

        self.assertEqual(False, a.equals(c))
        self.assertEqual(False, b.equals(c))

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__USD_2_35
        a.isLessThanOrEqual(b)

    def test_isLessThanOrEqual(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_35
        c: Money = self.__GBP_2_36
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
        a: Money = self.__GBP_2_34
        b: Money = self.__USD_2_35
        with self.assertRaises(CurrencyMismatchException):
            a.isLessThan(b)

    def test_isLessThan(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_35
        c: Money = self.__GBP_2_36
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
        a: Money = self.__GBP_2_34
        b: Money = self.__USD_2_35
        a.isGreaterThanOrEqual(b)

    def test_isGreaterThanOrEqual(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_35
        c: Money = self.__GBP_2_36
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
        a: Money = self.__GBP_2_34
        b: Money = self.__USD_2_35
        with pytest.raises(CurrencyMismatchException):
            a.isGreaterThan(b)

    def test_isGreaterThan(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_35
        c: Money = self.__GBP_2_36
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
        a: Money = self.__GBP_2_34
        b: Money = self.__USD_2_35
        with pytest.raises(CurrencyMismatchException):
            a.isEqual(b)

    def test_isEqual_Money(self) -> None:
        a: Money = self.__GBP_2_34
        b: BigMoney = BigMoney.ofMinor(self.__GBP, 234)
        self.assertEqual(True, a.isEqual(b))

    def test_isEqual(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_35
        c: Money = self.__GBP_2_36
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
        a: Money = self.__GBP_2_34
        b: Money = self.__USD_2_35
        with self.assertRaises(CurrencyMismatchException):
            a.compareTo(b)

    def test_compareTo_BigMoney(self) -> None:
        t: Money = self.__GBP_2_35
        a: BigMoney = BigMoney.ofMinor(self.__GBP, 234)
        b: BigMoney = BigMoney.ofMinor(self.__GBP, 235)
        c: BigMoney = BigMoney.ofMinor(self.__GBP, 236)
        self.assertEqual(1, t.compareTo(a))
        self.assertEqual(0, t.compareTo(b))
        self.assertEqual(-1, t.compareTo(c))

    def test_compareTo_Money(self) -> None:
        a: Money = self.__GBP_2_34
        b: Money = self.__GBP_2_35
        c: Money = self.__GBP_2_36
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
        with pytest.raises(RuntimeError):
            self.__GBP_2_34.isSameCurrency(None)

    def test_isSameCurrency_BigMoney_different(self) -> None:
        self.assertEqual(False, self.__GBP_2_34.isSameCurrency(BigMoney.parse("USD 2")))

    def test_isSameCurrency_BigMoney_same(self) -> None:
        self.assertEqual(True, self.__GBP_2_34.isSameCurrency(BigMoney.parse("GBP 2")))

    def test_isSameCurrency_Money_different(self) -> None:
        self.assertEqual(False, self.__GBP_2_34.isSameCurrency(self.__USD_2_34))

    def test_isSameCurrency_Money_same(self) -> None:
        self.assertEqual(True, self.__GBP_2_34.isSameCurrency(self.__GBP_2_35))

    def test_toBigMoney(self) -> None:
        self.assertEqual(
            BigMoney.ofMinor(self.__GBP, 234), self.__GBP_2_34.toBigMoney()
        )

    def test_convertedTo_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_5_78.convertedTo(self.__EUR, decimal.Decimal("2.5"), None)

    def test_convertedTo_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_5_78.convertedTo(self.__EUR, None, RoundingMode.DOWN)

    def test_convertedTo_BigDecimalRoundingMode_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_5_78.convertedTo(None, decimal.Decimal("2"), RoundingMode.DOWN)

    def test_convertedTo_BigDecimalRoundingMode_sameCurrency(self) -> None:
        with self.assertRaises(ValueError):
            self.__GBP_2_33.convertedTo(
                self.__GBP, decimal.Decimal("2.5"), RoundingMode.DOWN
            )

    def test_convertedTo_BigDecimalRoundingMode_negative(self) -> None:
        with self.assertRaises(ValueError):
            self.__GBP_2_33.convertedTo(
                self.__EUR, decimal.Decimal("-2.5"), RoundingMode.FLOOR
            )

    def test_convertedTo_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        test: Money = self.__GBP_2_33.convertedTo(
            self.__EUR, decimal.Decimal("2.5"), RoundingMode.HALF_UP
        )
        self.assertEqual("EUR 5.83", test.toString())

    def test_convertedTo_BigDecimalRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_33.convertedTo(
            self.__EUR, decimal.Decimal("2.5"), RoundingMode.DOWN
        )
        self.assertEqual("EUR 5.82", test.toString())

    def test_round_3(self) -> None:
        test: Money = self.__GBP_2_34.rounded(3, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_round_M1up(self) -> None:
        test: Money = Money.parse("GBP 432.34").rounded(-1, RoundingMode.UP)
        self.assertEqual("GBP 440.00", test.toString())

    def test_round_M1down(self) -> None:
        test: Money = Money.parse("GBP 432.34").rounded(-1, RoundingMode.DOWN)
        self.assertEqual("GBP 430.00", test.toString())

    def test_round_0up(self) -> None:
        test: Money = self.__GBP_2_34.rounded(0, RoundingMode.UP)
        self.assertEqual("GBP 3.00", test.toString())

    def test_round_0down(self) -> None:
        test: Money = self.__GBP_2_34.rounded(0, RoundingMode.DOWN)
        self.assertEqual("GBP 2.00", test.toString())

    def test_round_1up(self) -> None:
        test: Money = self.__GBP_2_34.rounded(1, RoundingMode.UP)
        self.assertEqual("GBP 2.40", test.toString())

    def test_round_1down(self) -> None:
        test: Money = self.__GBP_2_34.rounded(1, RoundingMode.DOWN)
        self.assertEqual("GBP 2.30", test.toString())

    def test_round_2up(self) -> None:
        test: Money = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_round_2down(self) -> None:
        test: Money = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_abs_negative(self) -> None:
        test: Money = Money.parse("GBP -2.34").abs()
        self.assertEqual("GBP 2.34", test.toString())

    def test_abs_positive(self) -> None:
        test: Money = self.__GBP_2_34.abs()
        assertSame(self.__GBP_2_34, test)

    def test_negated_negative(self) -> None:
        test: Money = Money.parse("GBP -2.34").negated()
        self.assertEqual("GBP 2.34", test.toString())

    def test_negated_positive(self) -> None:
        test: Money = self.__GBP_2_34.negated()
        self.assertEqual("GBP -2.34", test.toString())

    def test_dividedBy_long_negative(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy2(-3, RoundingMode.DOWN)
        self.assertEqual("GBP -0.78", test.toString())

    def test_dividedBy_long_positive_roundUp(self) -> None:
        test: Money = self.__GBP_2_35.dividedBy2(3, RoundingMode.UP)
        self.assertEqual("GBP 0.79", test.toString())

    def test_dividedBy_long_positive_roundDown(self) -> None:
        test: Money = self.__GBP_2_35.dividedBy2(3, RoundingMode.DOWN)
        self.assertEqual("GBP 0.78", test.toString())

    def test_dividedBy_long_positive(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy2(3, RoundingMode.DOWN)
        self.assertEqual("GBP 0.78", test.toString())

    def test_dividedBy_long_one(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy2(1, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_doubleRoundingMode_one(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_5_78.dividedBy0(decimal.Decimal("2.5"), None)

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy0(
            decimal.Decimal("-2.5"), RoundingMode.FLOOR
        )
        self.assertEqual("GBP -0.94", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy0(
            decimal.Decimal("2.5"), RoundingMode.HALF_UP
        )
        self.assertEqual("GBP 0.94", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy0(
            decimal.Decimal("2.5"), RoundingMode.DOWN
        )
        self.assertEqual("GBP 0.93", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:
        test: Money = self.__GBP_2_34.dividedBy0(decimal.Decimal(1), RoundingMode.DOWN)
        assert test == self.__GBP_2_34

    def test_multipliedBy_long_negative(self) -> None:
        test: Money = self.__GBP_2_34.multipliedBy2(-3)
        self.assertEqual("GBP -7.02", test.toString())

    def test_multipliedBy_long_positive(self) -> None:
        test: Money = self.__GBP_2_34.multipliedBy2(3)
        self.assertEqual("GBP 7.02", test.toString())

    def test_multipliedBy_long_one(self) -> None:
        test: Money = self.__GBP_2_34.multipliedBy2(1)
        assertSame(self.__GBP_2_34, test)

    def test_multipliedBy_doubleRoundingMode_nullRoundingMode(self) -> None:

        pass  # LLM could not translate this method

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate this method

    def test_multipliedBy_doubleRoundingMode_positive_halfUp(self) -> None:

        pass  # LLM could not translate this method

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:

        pass  # LLM could not translate this method

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:

        pass  # LLM could not translate this method

    def test_multipliedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_5_78.multipliedBy0(decimal.Decimal("2.5"), None)

    def test_multipliedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_multipliedBy_BigDecimalRoundingMode_negative(self) -> None:
        test: Money = self.__GBP_2_33.multipliedBy0(
            decimal.Decimal("-2.5"), RoundingMode.FLOOR
        )
        self.assertEqual("GBP -5.83", test.toString())

    def test_multipliedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:
        test: Money = self.__GBP_2_33.multipliedBy0(
            decimal.Decimal("2.5"), RoundingMode.HALF_UP
        )
        self.assertEqual("GBP 5.83", test.toString())

    def test_multipliedBy_BigDecimalRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_33.multipliedBy0(
            decimal.Decimal("2.5"), RoundingMode.DOWN
        )
        self.assertEqual("GBP 5.82", test.toString())

    def test_multipliedBy_BigDecimalRoundingMode_one(self) -> None:
        test: Money = self.__GBP_2_34.multipliedBy0(
            decimal.Decimal(1), RoundingMode.DOWN
        )
        assert test == self.__GBP_2_34

    def test_minusMinor_negative(self) -> None:
        test: Money = self.__GBP_2_34.minusMinor(-123)
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusMinor_positive(self) -> None:
        test: Money = self.__GBP_2_34.minusMinor(123)
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusMinor_zero(self) -> None:
        test: Money = self.__GBP_2_34.minusMinor(0)
        assert test == self.__GBP_2_34

    def test_minusMajor_negative(self) -> None:
        test: Money = self.__GBP_2_34.minusMajor(-123)
        self.assertEqual("GBP 125.34", test.toString())

    def test_minusMajor_positive(self) -> None:
        test: Money = self.__GBP_2_34.minusMajor(123)
        self.assertEqual("GBP -120.66", test.toString())

    def test_minusMajor_zero(self) -> None:
        test: Money = self.__GBP_2_34.minusMajor(0)
        assert test == self.__GBP_2_34

    def test_minus_doubleRoundingMode_nullRoundingMode(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_doubleRoundingMode_roundUnecessary(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_doubleRoundingMode_roundDown(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_doubleRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_34.minus5(1.23, RoundingMode.UNNECESSARY)
        self.assertEqual("GBP 1.11", test.toString())

    def test_minus_doubleRoundingMode_zero(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_double_invalidScale(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_double_negative(self) -> None:
        test: Money = self.__GBP_2_34.minus4(-1.23)
        self.assertEqual("GBP 3.57", test.toString())

    def test_minus_double_positive(self) -> None:
        test: Money = self.__GBP_2_34.minus4(1.23)
        self.assertEqual("GBP 1.11", test.toString())

    def test_minus_double_zero(self) -> None:
        test: Money = self.__GBP_2_34.minus4(0.0)
        assert test == self.__GBP_2_34

    def test_minus_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.minus3(self.__BIGDEC_2_34, None)

    def test_minus_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.minus3(decimal.Decimal("1.235"), RoundingMode.UNNECESSARY)

    def test_minus_BigDecimalRoundingMode_roundDown(self) -> None:
        test: Money = self.__GBP_2_34.minus3(
            decimal.Decimal("1.235"), RoundingMode.DOWN
        )
        self.assertEqual("GBP 1.10", test.toString())

    def test_minus_BigDecimalRoundingMode_negative(self) -> None:
        test: Money = self.__GBP_2_34.minus3(
            decimal.Decimal("-1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_minus_BigDecimalRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_34.minus3(
            decimal.Decimal("1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_minus_BigDecimalRoundingMode_zero(self) -> None:
        test: Money = self.__GBP_2_34.minus3(BigDecimal.ZERO, RoundingMode.UNNECESSARY)
        assertSame(self.__GBP_2_34, test)

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.minus2(None)

    def test_minus_BigDecimal_invalidScale(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.minus2(decimal.Decimal("1.235"))

    def test_minus_BigDecimal_negative(self) -> None:
        test: Money = self.__GBP_2_34.minus2(decimal.Decimal("-1.23"))
        self.assertEqual("GBP 3.57", test.toString())

    def test_minus_BigDecimal_positive(self) -> None:
        test: Money = self.__GBP_2_34.minus2(decimal.Decimal("1.23"))
        self.assertEqual("GBP 1.11", test.toString())

    def test_minus_BigDecimal_zero(self) -> None:
        test: Money = self.__GBP_2_34.minus2(decimal.Decimal(0))
        assert test == self.__GBP_2_34

    def test_minus_Money_nullMoney(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.minus1(None)

    def test_minus_Money_currencyMismatch(self) -> None:
        with pytest.raises(CurrencyMismatchException) as ex:
            self.__GBP_M5_78.minus1(self.__USD_1_23)
        assert self.__GBP == ex.value.getFirstCurrency()
        assert self.__USD == ex.value.getSecondCurrency()

    def test_minus_Money_negative(self) -> None:
        test: Money = self.__GBP_2_34.minus1(self.__GBP_M1_23)
        self.assertEqual("GBP 3.57", test.toString())

    def test_minus_Money_positive(self) -> None:
        test: Money = self.__GBP_2_34.minus1(self.__GBP_1_23)
        self.assertEqual("GBP 1.11", test.toString())

    def test_minus_Money_zero(self) -> None:
        test: Money = self.__GBP_2_34.minus1(self.__GBP_0_00)
        assert test == self.__GBP_2_34

    def test_minus_Iterable_nullIterable(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_Iterable_nullEntry(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, None]
        self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_currencyMismatch(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException) as ex:
            self.__GBP_M5_78.minus0(iterable)
        assert self.__GBP == ex.value.getFirstCurrency()
        assert self.__JPY == ex.value.getSecondCurrency()

    def test_minus_Iterable_zero(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_0_00]
        test: Money = self.__GBP_2_34.minus0(iterable)
        assert test == self.__GBP_2_34

    def test_minus_Iterable(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, self.__GBP_1_23]
        test: Money = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_plusMinor_negative(self) -> None:
        test: Money = self.__GBP_2_34.plusMinor(-123)
        self.assertEqual("GBP 1.11", test.toString())

    def test_plusMinor_positive(self) -> None:
        test: Money = self.__GBP_2_34.plusMinor(123)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusMinor_zero(self) -> None:
        test: Money = self.__GBP_2_34.plusMinor(0)
        assert test == self.__GBP_2_34

    def test_plusMajor_negative(self) -> None:
        test: Money = self.__GBP_2_34.plusMajor(-123)
        self.assertEqual("GBP -120.66", test.toString())

    def test_plusMajor_positive(self) -> None:
        test: Money = self.__GBP_2_34.plusMajor(123)
        self.assertEqual("GBP 125.34", test.toString())

    def test_plusMajor_zero(self) -> None:
        test: Money = self.__GBP_2_34.plusMajor(0)
        assert test == self.__GBP_2_34

    def test_plus_doubleRoundingMode_nullRoundingMode(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_doubleRoundingMode_roundUnecessary(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_doubleRoundingMode_roundDown(self) -> None:
        test: Money = self.__GBP_2_34.plus5(1.235, RoundingMode.DOWN)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_doubleRoundingMode_negative(self) -> None:
        test: Money = self.__GBP_2_34.plus5(-1.23, RoundingMode.UNNECESSARY)
        self.assertEqual("GBP 1.11", test.toString())

    def test_plus_doubleRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_34.plus5(1.23, RoundingMode.UNNECESSARY)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_doubleRoundingMode_zero(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_double_invalidScale(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_double_negative(self) -> None:
        test: Money = self.__GBP_2_34.plus4(-1.23)
        self.assertEqual("GBP 1.11", test.toString())

    def test_plus_double_positive(self) -> None:
        test: Money = self.__GBP_2_34.plus4(1.23)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_double_zero(self) -> None:
        test: Money = self.__GBP_2_34.plus4(0.0)
        assert self.__GBP_2_34 == test

    def test_plus_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_M5_78.plus3(self.__BIGDEC_2_34, None)

    def test_plus_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_M5_78.plus3(None, RoundingMode.UNNECESSARY)

    def test_plus_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.plus3(decimal.Decimal("1.235"), RoundingMode.UNNECESSARY)

    def test_plus_BigDecimalRoundingMode_roundDown(self) -> None:
        test: Money = self.__GBP_2_34.plus3(decimal.Decimal("1.235"), RoundingMode.DOWN)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_BigDecimalRoundingMode_negative(self) -> None:
        test: Money = self.__GBP_2_34.plus3(
            decimal.Decimal("-1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 1.11", test.toString())

    def test_plus_BigDecimalRoundingMode_positive(self) -> None:
        test: Money = self.__GBP_2_34.plus3(
            decimal.Decimal("1.23"), RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_BigDecimalRoundingMode_zero(self) -> None:
        test: Money = self.__GBP_2_34.plus3(
            decimal.Decimal(0), RoundingMode.UNNECESSARY
        )
        assert test == self.__GBP_2_34

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.plus2(None)

    def test_plus_BigDecimal_invalidScale(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.plus2(decimal.Decimal("1.235"))

    def test_plus_BigDecimal_negative(self) -> None:
        test: Money = self.__GBP_2_34.plus2(decimal.Decimal("-1.23"))
        self.assertEqual("GBP 1.11", test.toString())

    def test_plus_BigDecimal_positive(self) -> None:
        test: Money = self.__GBP_2_34.plus2(decimal.Decimal("1.23"))
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_BigDecimal_zero(self) -> None:
        test: Money = self.__GBP_2_34.plus2(decimal.Decimal(0))
        assert test == self.__GBP_2_34

    def test_plus_Money_nullMoney(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.plus1(None)

    def test_plus_Money_currencyMismatch(self) -> None:
        with pytest.raises(CurrencyMismatchException) as ex:
            self.__GBP_M5_78.plus1(self.__USD_1_23)
        assert self.__GBP == ex.value.getFirstCurrency()
        assert self.__USD == ex.value.getSecondCurrency()

    def test_plus_Money_negative(self) -> None:
        test: Money = self.__GBP_2_34.plus1(self.__GBP_M1_23)
        self.assertEqual("GBP 1.11", test.toString())

    def test_plus_Money_positive(self) -> None:
        test: Money = self.__GBP_2_34.plus1(self.__GBP_1_23)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plus_Money_zero(self) -> None:
        test: Money = self.__GBP_2_34.plus1(self.__GBP_0_00)
        assert test == self.__GBP_2_34

    def test_plus_Iterable_nullIterable(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.plus0(None)

    def test_plus_Iterable_nullEntry(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, None]
        with self.assertRaises(RuntimeError):
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_currencyMismatch(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException) as ex:
            self.__GBP_M5_78.plus0(iterable)
        assert self.__GBP == ex.value.getFirstCurrency()
        assert self.__JPY == ex.value.getSecondCurrency()

    def test_plus_Iterable_zero(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_0_00]
        test: Money = self.__GBP_2_34.plus0(iterable)
        assert test == self.__GBP_2_34

    def test_plus_Iterable(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, self.__GBP_1_23]
        test: Money = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_withAmount_doubleRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_2_34.withAmount1(self.__BIGDEC_2_34, None)

    def test_withAmount_doubleRoundingMode_roundUnecessary(self) -> None:

        pass  # LLM could not translate this method

    def test_withAmount_doubleRoundingMode_roundDown(self) -> None:
        test: Money = self.__GBP_2_34.withAmount3(2.355, RoundingMode.DOWN)
        self.assertEqual(self.__GBP_2_35, test)

    def test_withAmount_doubleRoundingMode_same(self) -> None:
        test: Money = self.__GBP_2_34.withAmount3(2.34, RoundingMode.UNNECESSARY)
        assertSame(self.__GBP_2_34, test)

    def test_withAmount_doubleRoundingMode(self) -> None:
        test: Money = self.__GBP_2_34.withAmount3(-5.78, RoundingMode.UNNECESSARY)
        self.assertEqual("GBP -5.78", test.toString())

    def test_withAmount_double_invalidScale(self) -> None:

        pass  # LLM could not translate this method

    def test_withAmount_double_same(self) -> None:
        test: Money = self.__GBP_2_34.withAmount2(2.34)
        assert test is self.__GBP_2_34

    def test_withAmount_double(self) -> None:
        test: Money = self.__GBP_2_34.withAmount2(-5.78)
        self.assertEqual("GBP -5.78", test.toString())

    def test_withAmount_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_2_34.withAmount1(self.__BIGDEC_2_34, None)

    def test_withAmount_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with self.assertRaises(TypeError):
            self.__GBP_2_34.withAmount1(None, RoundingMode.UNNECESSARY)

    def test_withAmount_BigDecimalRoundingMode_roundUnecessary(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.withAmount1(
                decimal.Decimal("2.345"), RoundingMode.UNNECESSARY
            )

    def test_withAmount_BigDecimalRoundingMode_roundDown(self) -> None:
        test: Money = self.__GBP_2_34.withAmount1(
            decimal.Decimal("2.355"), RoundingMode.DOWN
        )
        self.assertEqual(self.__GBP_2_35, test)

    def test_withAmount_BigDecimalRoundingMode_same(self) -> None:
        test: Money = self.__GBP_2_34.withAmount1(
            self.__BIGDEC_2_34, RoundingMode.UNNECESSARY
        )
        assertSame(self.__GBP_2_34, test)

    def test_withAmount_BigDecimalRoundingMode(self) -> None:
        test: Money = self.__GBP_2_34.withAmount1(
            self.__BIGDEC_M5_78, RoundingMode.UNNECESSARY
        )
        self.assertEqual("GBP -5.78", test.toString())

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_2_34.withAmount0(None)

    def test_withAmount_BigDecimal_invalidScale(self) -> None:
        with pytest.raises(ArithmeticException):
            self.__GBP_2_34.withAmount0(decimal.Decimal("2.345"))

    def test_withAmount_BigDecimal_same(self) -> None:
        test: Money = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_34)
        assert test is self.__GBP_2_34

    def test_withAmount_BigDecimal(self) -> None:
        test: Money = self.__GBP_2_34.withAmount0(self.__BIGDEC_M5_78)
        self.assertEqual("GBP -5.78", test.toString())

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
        with self.assertRaises(ArithmeticException):
            self.GBP_INT_MIN_MINUS1.getAmountMinorInt()

    def test_getAmountMinorInt_tooBigPositive(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.GBP_INT_MAX_PLUS1.getAmountMinorInt()

    def test_getAmountMinorInt_negative(self) -> None:
        self.assertEqual(-578, self.__GBP_M5_78.getAmountMinorInt())

    def test_getAmountMinorInt_positive(self) -> None:
        self.assertEqual(234, self.__GBP_2_34.getAmountMinorInt())

    def test_getAmountMinorLong_tooBigNegative(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_LONG_MIN_MINUS1.getAmountMinorLong()

    def test_getAmountMinorLong_tooBigPositive(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_LONG_MAX_PLUS1.getAmountMinorLong()

    def test_getAmountMinorLong_negative(self) -> None:

        pass  # LLM could not translate this method

    def test_getAmountMinorLong_positive(self) -> None:

        pass  # LLM could not translate this method

    def test_getAmountMinor_negative(self) -> None:
        self.assertEqual(decimal.Decimal(-578), self.__GBP_M5_78.getAmountMinor())

    def test_getAmountMinor_positive(self) -> None:
        self.assertEqual(decimal.Decimal(234), self.__GBP_2_34.getAmountMinor())

    def test_getAmountMajorInt_tooBigNegative(self) -> None:
        with self.assertRaises(ArithmeticException):
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

    def test_getScale_JPY(self) -> None:
        self.assertEqual(0, self.__JPY_423.getScale())

    def test_getScale_GBP(self) -> None:
        self.assertEqual(2, self.__GBP_2_34.getScale())

    def test_withCurrencyUnit_CurrencyRoundingMode_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_2_34.withCurrencyUnit1(None, RoundingMode.UNNECESSARY)

    def test_withCurrencyUnit_CurrencyRoundingMode_UNECESSARY(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.withCurrencyUnit1(self.__JPY, RoundingMode.UNNECESSARY)

    def test_withCurrencyUnit_CurrencyRoundingMode_same(self) -> None:
        test: Money = self.__GBP_2_34.withCurrencyUnit1(self.__GBP, RoundingMode.DOWN)
        assertSame(self.__GBP_2_34, test)

    def test_withCurrencyUnit_CurrencyRoundingMode_UP(self) -> None:
        test: Money = self.__GBP_2_34.withCurrencyUnit1(self.__JPY, RoundingMode.UP)
        self.assertEqual("JPY 3", test.toString())

    def test_withCurrencyUnit_CurrencyRoundingMode_DOWN(self) -> None:
        test: Money = self.__GBP_2_34.withCurrencyUnit1(self.__JPY, RoundingMode.DOWN)
        self.assertEqual("JPY 2", test.toString())

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            self.__GBP_2_34.withCurrencyUnit0(None)

    def test_withCurrencyUnit_Currency_scaleProblem(self) -> None:
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.withCurrencyUnit0(self.__JPY)

    def test_withCurrencyUnit_Currency_same(self) -> None:
        test: Money = self.__GBP_2_34.withCurrencyUnit0(self.__GBP)
        assert test == self.__GBP_2_34

    def test_withCurrencyUnit_Currency(self) -> None:
        test: Money = self.__GBP_2_34.withCurrencyUnit0(self.__USD)
        self.assertEqual("USD 2.34", test.toString())

    def test_getCurrencyUnit_EUR(self) -> None:
        self.assertEqual(self.__EUR, Money.parse("EUR -5.78").getCurrencyUnit())

    def test_getCurrencyUnit_GBP(self) -> None:
        self.assertEqual(self.__GBP, self.__GBP_2_34.getCurrencyUnit())

    def test_constructor_scale(self) -> None:
        con = Money.__init__.__annotations__["return"]
        try:
            con.setAccessible(True)
            con.newInstance([0, BigMoney.of0(self.__GBP, self.__BIGDEC_2_3)])
            self.fail()
        except InvocationTargetException as ex:
            self.assertEqual(AssertionError.__class__, ex.getCause().__class__)

    def test_constructor_null1(self) -> None:
        con = Money.__init__.__annotations__["return"]
        self.assertEqual(True, Modifier.isPublic(con.getModifiers()))
        self.assertEqual(False, Modifier.isProtected(con.getModifiers()))
        try:
            con.setAccessible(True)
            con.newInstance([0, None])
            self.fail()
        except InvocationTargetException as ex:
            self.assertEqual(AssertionError, ex.getCause().__class__)

    def test_factory_parse_String_nullString(self) -> None:
        with pytest.raises(RuntimeError):
            Money.parse(None)

    def test_factory_parse_String_badCurrency(self) -> None:
        with pytest.raises(ValueError):
            Money.parse("GBX 2.34")

    def test_factory_parse_String_tooShort(self) -> None:
        with self.assertRaises(ValueError):
            Money.parse("GBP ")

    def test_factory_parse(self, str: str, currency: CurrencyUnit, amount: int) -> None:
        test: Money = Money.parse(str)
        self.assertEqual(currency, test.getCurrencyUnit())
        self.assertEqual(amount, test.getAmountMinorInt())

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:
        return [
            ["GBP 2.43", TestMoney.__GBP, 243],
            ["GBP +12.57", TestMoney.__GBP, 1257],
            ["GBP -5.87", TestMoney.__GBP, -587],
            ["GBP 0.99", TestMoney.__GBP, 99],
            ["GBP .99", TestMoney.__GBP, 99],
            ["GBP +.99", TestMoney.__GBP, 99],
            ["GBP +0.99", TestMoney.__GBP, 99],
            ["GBP -.99", TestMoney.__GBP, -99],
            ["GBP -0.99", TestMoney.__GBP, -99],
            ["GBP 0", TestMoney.__GBP, 0],
            ["GBP 2", TestMoney.__GBP, 200],
            ["GBP 123.", TestMoney.__GBP, 12300],
            ["GBP3", TestMoney.__GBP, 300],
            ["GBP3.10", TestMoney.__GBP, 310],
            ["GBP  3.10", TestMoney.__GBP, 310],
            ["GBP   3.10", TestMoney.__GBP, 310],
            ["GBP                           3.10", TestMoney.__GBP, 310],
        ]

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(RuntimeError):
            Money.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:
        iterable: typing.Iterable[Money] = [None, self.__GBP_2_33, self.__GBP_2_36]
        with pytest.raises(Exception) as excinfo:
            Money.total3(self.__GBP, iterable)
        assert excinfo.type == CurrencyMismatchException

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(
        self,
    ) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException) as ex:
            Money.total3(self.__GBP, iterable)
        assert self.__GBP == ex.value.getFirstCurrency()
        assert self.__JPY == ex.value.getSecondCurrency()
        raise ex.value

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:
        iterable: typing.Iterable[Money] = [self.__JPY_423]
        with pytest.raises(CurrencyMismatchException) as ex:
            Money.total3(self.__GBP, iterable)
        assert ex.value.getFirstCurrency() == self.__GBP
        assert ex.value.getSecondCurrency() == self.__JPY
        raise ex.value

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:
        iterable: typing.Iterable[Money] = []
        test: Money = Money.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitIterable(self) -> None:
        iterable: typing.Iterable[Money] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            self.__GBP_2_36,
        ]
        test: Money = Money.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:
        array: typing.List[Money] = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(RuntimeError):
            Money.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.total2(self.__GBP, self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:
        array: typing.List[Money] = [None, self.__GBP_2_33, self.__GBP_2_36]
        with pytest.raises(RuntimeError):
            Money.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.total2(self.__GBP, None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:
        with self.assertRaises(CurrencyMismatchException) as cm:
            array: typing.List[Money] = [self.__GBP_2_33, self.__JPY_423]
            Money.total2(self.__GBP, array)
        ex: CurrencyMismatchException = cm.exception
        self.assertEqual(self.__GBP, ex.getFirstCurrency())
        self.assertEqual(self.__JPY, ex.getSecondCurrency())
        raise ex

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total2(self.__GBP, self.__GBP_2_33, self.__JPY_423)
        ex: CurrencyMismatchException = cm.exception
        self.assertEqual(self.__GBP, ex.getFirstCurrency())
        self.assertEqual(self.__JPY, ex.getSecondCurrency())
        raise ex

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:
        array: typing.List[Money] = [self.__JPY_423]
        with pytest.raises(CurrencyMismatchException) as ex:
            Money.total2(self.__GBP, array)
        assert ex.value.getFirstCurrency() == self.__GBP
        assert ex.value.getSecondCurrency() == self.__JPY
        raise ex.value

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total2(self.__GBP, self.__JPY_423)
        ex = cm.exception
        self.assertEqual(self.__GBP, ex.getFirstCurrency())
        self.assertEqual(self.__JPY, ex.getSecondCurrency())
        raise ex

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:
        array: typing.List[Money] = []
        test: Money = Money.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:
        test: Money = Money.total2(self.__GBP)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3(self) -> None:
        array: typing.List[Money] = [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
        test: Money = Money.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:
        test: Money = Money.total2(
            self.__GBP, self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_1(self) -> None:
        array: typing.List[Money] = [TestMoney.__GBP_1_23]
        test: Money = Money.total2(TestMoney.__GBP, array)
        self.assertEqual(TestMoney.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:
        test: Money = Money.total2(self.__GBP, self.__GBP_1_23)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_Iterable_nullNotFirst(self) -> None:
        iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
        with self.assertRaises(RuntimeError):
            Money.total1(iterable)

    def test_factory_total_Iterable_nullFirst(self) -> None:
        iterable = [None, self.__GBP_2_33, self.__GBP_2_36]
        with self.assertRaises(RuntimeError):
            Money.total1(iterable)

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:
        iterable: typing.Iterable[Money] = [self.__GBP_2_33, self.__JPY_423]
        try:
            Money.total1(iterable)
        except CurrencyMismatchException as ex:
            self.assertEqual(self.__GBP, ex.getFirstCurrency())
            self.assertEqual(self.__JPY, ex.getSecondCurrency())
            raise ex

    def test_factory_total_Iterable_empty(self) -> None:
        with self.assertRaises(ValueError):
            Money.total1([])

    def test_factory_total_Iterable(self) -> None:
        iterable: typing.Iterable[Money] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            self.__GBP_2_36,
        ]
        test: Money = Money.total1(iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_array_nullNotFirst(self) -> None:
        array = [self.__GBP_2_33, None, self.__GBP_2_36]
        with self.assertRaises(RuntimeError):
            Money.total0(array)

    def test_factory_total_varargs_nullNotFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.total0(self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_array_nullFirst(self) -> None:
        array = [None, self.__GBP_2_33, self.__GBP_2_36]
        with self.assertRaises(RuntimeError):
            Money.total0(array)

    def test_factory_total_varargs_nullFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.total0(None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_array_currenciesDiffer(self) -> None:
        try:
            array = [self.__GBP_2_33, self.__JPY_423]
            Money.total0(array)
        except CurrencyMismatchException as ex:
            self.assertEqual(self.__GBP, ex.getFirstCurrency())
            self.assertEqual(self.__JPY, ex.getSecondCurrency())
            raise ex

    def test_factory_total_varargs_currenciesDiffer(self) -> None:
        try:
            Money.total0(self.__GBP_2_33, self.__JPY_423)
        except CurrencyMismatchException as ex:
            self.assertEqual(self.__GBP, ex.getFirstCurrency())
            self.assertEqual(self.__JPY, ex.getSecondCurrency())
            raise ex

    def test_factory_total_array_empty(self) -> None:
        with self.assertRaises(ValueError):
            Money.total0([])

    def test_factory_total_varargs_empty(self) -> None:
        with self.assertRaises(ValueError):
            Money.total0()

    def test_factory_total_array_3(self) -> None:
        array: typing.List[Money] = [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
        test: Money = Money.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_varargs_3(self) -> None:
        test = Money.total0([self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36])
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_array_1(self) -> None:
        array: typing.List[Money] = [self.__GBP_1_23]
        test: Money = Money.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_varargs_1(self) -> None:
        test = Money.total0([self.__GBP_1_23])
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_from_BigMoneyProvider_RoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of5(BigMoney.parse("GBP 104.235"), None)

    def test_factory_from_BigMoneyProvider_RoundingMode_nullBigMoneyProvider(
        self,
    ) -> None:
        with self.assertRaises(RuntimeError):
            Money.of5(None, RoundingMode.DOWN)

    def test_factory_from_BigMoneyProvider_RoundingMode(self) -> None:
        test = Money.of5(BigMoney.parse("GBP 104.235"), RoundingMode.HALF_EVEN)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(10424, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of4(None)

    def test_factory_from_BigMoneyProvider_invalidCurrencyScale(self) -> None:
        with self.assertRaises(ArithmeticException):
            Money.of4(BigMoney.parse("GBP 104.235"))

    def test_factory_from_BigMoneyProvider_fixScale(self) -> None:
        test: Money = Money.of4(BigMoney.parse("GBP 104.2"))
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(10420, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_from_BigMoneyProvider(self) -> None:
        test = Money.of4(BigMoney.parse("GBP 104.23"))
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(10423, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_zero_Currency_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.zero(None)

    def test_factory_zero_Currency(self) -> None:
        test = Money.zero(self.__GBP)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.ofMinor(None, 234)

    def test_factory_ofMinor_Currency_long(self) -> None:
        test: Money = Money.ofMinor(self.__GBP, 234)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(234, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:
        with pytest.raises(RuntimeError):
            Money.ofMajor(None, 234)

    def test_factory_ofMajor_Currency_long(self) -> None:
        test: Money = Money.ofMajor(self.__GBP, 234)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(23400, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_of_Currency_double_RoundingMode_nullRoundingMode(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_RoundingMode_nullCurrency(self) -> None:
        with pytest.raises(RuntimeError):
            Money.of3(None, 2.34, RoundingMode.DOWN)

    def test_factory_of_Currency_double_RoundingMode_UNNECESSARY(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_JPY_RoundingMode_UP(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_JPY_RoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_GBP_RoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of0(None, self.__BIGDEC_2_34)

    def test_factory_of_Currency_double_invalidScaleJPY(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_invalidScaleGBP(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_big(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_medium(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_trailingZero2(self) -> None:
        test: Money = Money.of2(self.__GBP, 1.20)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(120, 2), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_factory_of_Currency_double_trailingZero1(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_double_correctScale(self) -> None:
        test: Money = Money.of2(self.__GBP, 2.3)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(230, test.getAmountMinorInt())
        self.assertEqual(2, test.getScale())

    def test_factory_of_Currency_double(self) -> None:

        pass  # LLM could not translate this method

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullRoundingMode(self) -> None:
        with self.assertRaises(TypeError):
            Money.of1(self.__GBP, self.__BIGDEC_2_34, None)

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullBigDecimal(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of1(self.__GBP, None, RoundingMode.DOWN)

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of1(None, self.__BIGDEC_2_34, RoundingMode.DOWN)

    def test_factory_of_Currency_BigDecimal_RoundingMode_UNNECESSARY(self) -> None:
        with self.assertRaises(ArithmeticException):
            Money.of1(self.__JPY, self.__BIGDEC_2_34, RoundingMode.UNNECESSARY)

    def test_factory_of_Currency_BigDecimal_JPY_RoundingMode_UP(self) -> None:
        test = Money.of1(self.__JPY, self.__BIGDEC_2_34, RoundingMode.UP)
        self.assertEqual(self.__JPY, test.getCurrencyUnit())
        self.assertEqual(3, test.getAmountMinorInt())
        self.assertEqual(0, test.getAmount().scale())

    def test_factory_of_Currency_BigDecimal_JPY_RoundingMode_DOWN(self) -> None:
        test = Money.of1(self.__JPY, self.__BIGDEC_2_34, RoundingMode.DOWN)
        self.assertEqual(self.__JPY, test.getCurrencyUnit())
        self.assertEqual(2, test.getAmountMinorInt())
        self.assertEqual(0, test.getAmount().scale())

    def test_factory_of_Currency_BigDecimal_GBP_RoundingMode_DOWN(self) -> None:
        test = Money.of1(self.__GBP, self.__BIGDEC_2_34, RoundingMode.DOWN)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(234, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of0(self.__GBP, None)

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:
        with self.assertRaises(RuntimeError):
            Money.of0(None, self.__BIGDEC_2_34)

    def test_factory_of_Currency_BigDecimal_invalidScaleJPY(self) -> None:
        with self.assertRaises(ArithmeticException):
            Money.of0(self.__JPY, self.__BIGDEC_2_3)

    def test_factory_of_Currency_BigDecimal_invalidScaleGBP(self) -> None:
        with self.assertRaises(ArithmeticException):
            Money.of0(self.__GBP, self.__BIGDEC_2_345)

    def test_factory_of_Currency_BigDecimal_correctScale(self) -> None:
        test: Money = Money.of0(self.__GBP, self.__BIGDEC_2_3)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(230, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_of_Currency_BigDecimal(self) -> None:
        test: Money = Money.of0(self.__GBP, self.__BIGDEC_2_34)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(234, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())
