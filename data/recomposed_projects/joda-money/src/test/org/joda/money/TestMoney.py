# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import unittest
import os
import typing
from typing import *

# Imports End


class TestMoney(unittest.TestCase):

    # Class Fields Begin
    __GBP: CurrencyUnit = CurrencyUnit.of1("GBP")
    __EUR: CurrencyUnit = CurrencyUnit.of("EUR")
    __USD: CurrencyUnit = CurrencyUnit.of("USD")
    __JPY: CurrencyUnit = CurrencyUnit.of1("JPY")
    __BIGDEC_2_3: decimal.Decimal = 2.3
    __BIGDEC_2_34: decimal.Decimal = 2.34
    __BIGDEC_2_345: decimal.Decimal = 2.345
    __BIGDEC_M5_78: decimal.Decimal = decimal.Decimal("-5.78")
    __GBP_0_00: Money = Money.parse("GBP 0.00")
    __GBP_1_23: Money = Money.parse("GBP 1.23")
    __GBP_2_33: Money = Money.parse("GBP 2.33")
    __GBP_2_34: Money = Money.parse("GBP 2.34")
    __GBP_2_35: Money = Money.parse("GBP 2.35")
    __GBP_2_36: Money = Money.parse("GBP 2.36")
    __GBP_5_78: Money = Money.parse("GBP 5.78")
    __GBP_M1_23: Money = Money.parse("GBP -1.23")
    __GBP_M5_78: Money = Money.parse("GBP -5.78")
    __GBP_INT_MAX_PLUS1: Money = Money.of_minor(GBP, (int(Integer.MAX_VALUE) + 1))
    __GBP_INT_MIN_MINUS1: Money = ""  # LLM could not translate field
    __GBP_INT_MAX_MAJOR_PLUS1: Money = ""  # LLM could not translate field
    __GBP_INT_MIN_MAJOR_MINUS1: Money = ""  # LLM could not translate field
    __GBP_LONG_MAX_PLUS1: Money = Money.of(
        GBP, BigDecimal.valueOf(Long.MAX_VALUE).add(BigDecimal.ONE)
    )
    __GBP_LONG_MIN_MINUS1: Money = Money.of(
        GBP, BigDecimal.valueOf(Long.MIN_VALUE).subtract(BigDecimal.ONE)
    )
    __GBP_LONG_MAX_MAJOR_PLUS1: Money = Money.of(
        GBP,
        BigDecimal.valueOf(Long.MAX_VALUE)
        .add(BigDecimal.ONE)
        .multiply(BigDecimal.valueOf(100)),
    )
    __GBP_LONG_MIN_MAJOR_MINUS1: Money = Money.of(
        GBP,
        BigDecimal.valueOf(Long.MIN_VALUE)
        .subtract(BigDecimal.ONE)
        .multiply(BigDecimal.valueOf(100)),
    )
    __JPY_423: Money = Money.parse("JPY 423")
    __USD_1_23: Money = Money.parse("USD 1.23")
    __USD_2_34: Money = Money.parse("USD 2.34")
    __USD_2_35: Money = Money.parse("USD 2.35")
    # Class Fields End

    # Class Methods Begin
    def test_toString_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_toString_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_false(self) -> None:

        pass  # LLM could not translate method body

    def test_equals_hashCode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:

        pass  # LLM could not translate method body

    def test_isLessThanOrEqual(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36
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

        pass  # LLM could not translate method body

    def test_isLessThan(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36
        assert a.isLessThan(a) == False
        assert a.isLessThan(b) == True
        assert a.isLessThan(c) == True
        assert b.isLessThan(a) == False
        assert b.isLessThan(b) == False
        assert b.isLessThan(c) == True
        assert c.isLessThan(a) == False
        assert c.isLessThan(b) == False
        assert c.isLessThan(c) == False

    def test_isGreaterThanOrEqual_currenciesDiffer(self) -> None:

        pass  # LLM could not translate method body

    def test_isGreaterThanOrEqual(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36
        assert a.isGreaterThanOrEqual(a) == True
        assert a.isGreaterThanOrEqual(b) == False
        assert a.isGreaterThanOrEqual(c) == False
        assert b.isGreaterThanOrEqual(a) == True
        assert b.isGreaterThanOrEqual(b) == True
        assert b.isGreaterThanOrEqual(c) == False
        assert c.isGreaterThanOrEqual(a) == True
        assert c.isGreaterThanOrEqual(b) == True
        assert c.isGreaterThanOrEqual(c) == True

    def test_isGreaterThan_currenciesDiffer(self) -> None:

        pass  # LLM could not translate method body

    def test_isGreaterThan(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36
        assert not a.isGreaterThan(a)
        assert not a.isGreaterThan(b)
        assert not a.isGreaterThan(c)
        assert b.isGreaterThan(a)
        assert not b.isGreaterThan(b)
        assert not b.isGreaterThan(c)
        assert c.isGreaterThan(a)
        assert c.isGreaterThan(b)
        assert not c.isGreaterThan(c)

    def test_isEqual_currenciesDiffer(self) -> None:

        pass  # LLM could not translate method body

    def test_isEqual_Money(self) -> None:

        pass  # LLM could not translate method body

    def test_isEqual(self) -> None:

        pass  # LLM could not translate method body

    def test_compareTo_wrongType(self) -> None:

        a = self.__GBP_2_34
        a.compareTo("NotRightType")

    def test_compareTo_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.compareTo(b)

    def test_compareTo_BigMoney(self) -> None:

        t = self.__GBP_2_35
        a = BigMoney.ofMinor(self.__GBP, 234)
        b = BigMoney.ofMinor(self.__GBP, 235)
        c = BigMoney.ofMinor(self.__GBP, 236)
        self.assertEqual(1, t.compareTo(a))
        self.assertEqual(0, t.compareTo(b))
        self.assertEqual(-1, t.compareTo(c))

    def test_compareTo_Money(self) -> None:

        pass  # LLM could not translate method body

    def test_isSameCurrency_Money_nullMoney(self) -> None:

        self.GBP_2_34.isSameCurrency(None)

    def test_isSameCurrency_BigMoney_different(self) -> None:

        pass  # LLM could not translate method body

    def test_isSameCurrency_BigMoney_same(self) -> None:

        pass  # LLM could not translate method body

    def test_isSameCurrency_Money_different(self) -> None:

        pass  # LLM could not translate method body

    def test_isSameCurrency_Money_same(self) -> None:

        pass  # LLM could not translate method body

    def test_toBigMoney(self) -> None:

        self.assertEqual(BigMoney.ofMinor(GBP, 234), GBP_2_34.toBigMoney())

    def test_convertedTo_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_5_78.convertedTo(self.__EUR, decimal.Decimal("2.5"), None)

    def test_convertedTo_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_5_78.convertedTo(self.__EUR, None, RoundingMode.DOWN)

    def test_convertedTo_BigDecimalRoundingMode_nullCurrency(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_5_78.convertedTo(None, decimal.Decimal("2"), RoundingMode.DOWN)

    def test_convertedTo_BigDecimalRoundingMode_sameCurrency(self) -> None:

        self.assertEqual(
            self.__GBP_2_33.convertedTo(
                self.__GBP, decimal.Decimal("2.5"), decimal.ROUND_DOWN
            ),
            self.__GBP_2_33,
        )

    def test_convertedTo_BigDecimalRoundingMode_negative(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_33.convertedTo(
                self.__EUR, decimal.Decimal("-2.5"), decimal.ROUND_FLOOR
            )

    def test_convertedTo_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        test = self.__GBP_2_33.convertedTo(
            self.__EUR, decimal.Decimal("2.5"), decimal.ROUND_HALF_UP
        )
        assert test.toString() == "EUR 5.83"

    def test_convertedTo_BigDecimalRoundingMode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_round_3(self) -> None:

        test = self.__GBP_2_34.rounded(3, RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_round_M1up(self) -> None:

        test = Money.parse("GBP 432.34").rounded(-1, RoundingMode.UP)
        self.assertEqual("GBP 440.00", test.toString())

    def test_round_M1down(self) -> None:

        test = Money.parse("GBP 432.34").rounded(-1, RoundingMode.DOWN)
        self.assertEqual("GBP 430.00", test.toString())

    def test_round_0up(self) -> None:

        test = self.__GBP_2_34.rounded(0, RoundingMode.UP)
        assert test.toString() == "GBP 3.00"

    def test_round_0down(self) -> None:

        test = self.__GBP_2_34.rounded(0, RoundingMode.DOWN)
        assert test.toString() == "GBP 2.00"

    def test_round_1up(self) -> None:

        test = self.__GBP_2_34.rounded(1, RoundingMode.UP)
        assert test.toString() == "GBP 2.40"

    def test_round_1down(self) -> None:

        test = self.__GBP_2_34.rounded(1, RoundingMode.DOWN)
        assert test.toString() == "GBP 2.30"

    def test_round_2up(self) -> None:

        test = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_round_2down(self) -> None:

        test = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_abs_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_abs_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_negated_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_negated_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_long_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_long_positive_roundUp(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_long_positive_roundDown(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_long_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_long_one(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_5_78.dividedBy1(2.5, None)

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.dividedBy1(1.0, RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_5_78.dividedBy0(decimal.Decimal("2.5"), None)

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_5_78.dividedBy0(None, RoundingMode.DOWN)

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.dividedBy0(decimal.Decimal(1), RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_multipliedBy_long_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_long_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_long_one(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_5_78.multipliedBy1(2.5, None)

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_positive_halfUp(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy1(1.0, RoundingMode.DOWN)
        self.assertIs(test, self.__GBP_2_34)

    def test_multipliedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_5_78.multipliedBy0(decimal.Decimal("2.5"), None)

    def test_multipliedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_5_78.multipliedBy0(None, RoundingMode.DOWN)

    def test_multipliedBy_BigDecimalRoundingMode_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_BigDecimalRoundingMode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_multipliedBy_BigDecimalRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy0(decimal.Decimal(1), RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_minusMinor_negative(self) -> None:

        test = self.__GBP_2_34.minusMinor(-123)
        assert test.toString() == "GBP 3.57"

    def test_minusMinor_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_minusMinor_zero(self) -> None:

        test = self.__GBP_2_34.minusMinor(0)
        self.assertIs(test, self.__GBP_2_34)

    def test_minusMajor_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_minusMajor_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_minusMajor_zero(self) -> None:

        test = self.__GBP_2_34.minusMajor(0)
        self.assertIs(test, self.__GBP_2_34)

    def test_minus_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.minus5(2.34, None)

    def test_minus_doubleRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.minus5(1.235, RoundingMode.UNNECESSARY)

    def test_minus_doubleRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.minus5(1.235, RoundingMode.DOWN)
        assert test.toString() == "GBP 1.10"

    def test_minus_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.minus5(-1.23, RoundingMode.UNNECESSARY)
        assert test.toString() == "GBP 3.57"

    def test_minus_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.minus5(1.23, RoundingMode.UNNECESSARY)
        assert test.toString() == "GBP 1.11"

    def test_minus_doubleRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.minus5(0.0, RoundingMode.UNNECESSARY)
        self.assertIs(test, self.__GBP_2_34)

    def test_minus_double_invalidScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_34.minus4(1.235)

    def test_minus_double_negative(self) -> None:

        test = self.__GBP_2_34.minus4(-1.23)
        assert test.toString() == "GBP 3.57"

    def test_minus_double_positive(self) -> None:

        test = self.__GBP_2_34.minus4(1.23)
        assert test.toString() == "GBP 1.11"

    def test_minus_double_zero(self) -> None:

        test = self.__GBP_2_34.minus4(0.0)
        self.assertIs(test, self.__GBP_2_34)

    def test_minus_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.minus3(self.__BIGDEC_2_34, None)

    def test_minus_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_M5_78.minus3(None, RoundingMode.UNNECESSARY)

    def test_minus_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.minus3(decimal.Decimal("1.235"), RoundingMode.UNNECESSARY)

    def test_minus_BigDecimalRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.minus3(decimal.Decimal("1.235"), decimal.ROUND_DOWN)
        assert test.toString() == "GBP 1.10"

    def test_minus_BigDecimalRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.minus3(
            decimal.Decimal("-1.23"), RoundingMode.UNNECESSARY
        )
        assert test.toString() == "GBP 3.57"

    def test_minus_BigDecimalRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.minus3(decimal.Decimal("1.23"), RoundingMode.UNNECESSARY)
        assert test.toString() == "GBP 1.11"

    def test_minus_BigDecimalRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.minus3(decimal.Decimal(0), RoundingMode.UNNECESSARY)
        self.assertIs(test, self.__GBP_2_34)

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:

        self.__GBP_M5_78.minus2(None)

    def test_minus_BigDecimal_invalidScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_34.minus2(decimal.Decimal("1.235"))

    def test_minus_BigDecimal_negative(self) -> None:

        test = self.__GBP_2_34.minus2(decimal.Decimal("-1.23"))
        assert test.toString() == "GBP 3.57"

    def test_minus_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_34.minus2(decimal.Decimal("1.23"))
        assert test.toString() == "GBP 1.11"

    def test_minus_BigDecimal_zero(self) -> None:

        test = self.__GBP_2_34.minus2(decimal.Decimal(0))
        self.assertIs(test, self.__GBP_2_34)

    def test_minus_Money_nullMoney(self) -> None:

        self.__GBP_M5_78.minus1(None)

    def test_minus_Money_currencyMismatch(self) -> None:

        try:
            self.__GBP_M5_78.minus1(self.__USD_1_23)
        except CurrencyMismatchException as ex:
            self.assertEqual(self.__GBP, ex.getFirstCurrency())
            self.assertEqual(self.__USD, ex.getSecondCurrency())
            raise ex

    def test_minus_Money_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_minus_Money_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_minus_Money_zero(self) -> None:

        test = self.__GBP_2_34.minus1(self.__GBP_0_00)
        self.assertSame(self.__GBP_2_34, test)

    def test_minus_Iterable_nullIterable(self) -> None:

        self.__GBP_M5_78.minus0(None)

    def test_minus_Iterable_nullEntry(self) -> None:

        iterable = [self.__GBP_2_33, None]
        self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_currencyMismatch(self) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        try:
            self.__GBP_M5_78.minus0(iterable)
        except CurrencyMismatchException as ex:
            assert ex.getFirstCurrency() == self.__GBP
            assert ex.getSecondCurrency() == self.__JPY
            raise ex

    def test_minus_Iterable_zero(self) -> None:

        iterable = [self.__GBP_0_00]
        test = self.__GBP_2_34.minus0(iterable)
        self.assertSame(self.__GBP_2_34, test)

    def test_minus_Iterable(self) -> None:

        iterable = [self.__GBP_2_33, self.__GBP_1_23]
        test = self.__GBP_2_34.minus0(iterable)
        assert test.toString() == "GBP -1.22"

    def test_plusMinor_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_plusMinor_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_plusMinor_zero(self) -> None:

        test = self.__GBP_2_34.plusMinor(0)
        self.assertSame(self.__GBP_2_34, test)

    def test_plusMajor_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_plusMajor_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_plusMajor_zero(self) -> None:

        test = self.__GBP_2_34.plusMajor(0)
        self.assertSame(self.__GBP_2_34, test)

    def test_plus_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.plus5(2.34, None)

    def test_plus_doubleRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.plus5(1.235, RoundingMode.UNNECESSARY)

    def test_plus_doubleRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.plus5(1.235, RoundingMode.DOWN)
        assert test.toString() == "GBP 3.57"

    def test_plus_doubleRoundingMode_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_doubleRoundingMode_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_doubleRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.plus5(0.0, RoundingMode.UNNECESSARY)
        self.assertIs(test, self.__GBP_2_34)

    def test_plus_double_invalidScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_34.plus4(1.235)

    def test_plus_double_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_double_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_double_zero(self) -> None:

        test = self.__GBP_2_34.plus4(0.0)
        self.assertIs(test, self.__GBP_2_34)

    def test_plus_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.plus3(self.__BIGDEC_2_34, None)

    def test_plus_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_M5_78.plus3(None, RoundingMode.UNNECESSARY)

    def test_plus_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.plus3(decimal.Decimal("1.235"), decimal.ROUND_UNNECESSARY)

    def test_plus_BigDecimalRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.plus3(decimal.Decimal("1.235"), RoundingMode.DOWN)
        assert test.toString() == "GBP 3.57"

    def test_plus_BigDecimalRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.plus3(decimal.Decimal("-1.23"), RoundingMode.UNNECESSARY)
        assert test.toString() == "GBP 1.11"

    def test_plus_BigDecimalRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.plus3(decimal.Decimal("1.23"), RoundingMode.UNNECESSARY)
        assert test.toString() == "GBP 3.57"

    def test_plus_BigDecimalRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.plus3(decimal.Decimal(0), RoundingMode.UNNECESSARY)
        self.assertIs(test, self.__GBP_2_34)

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:

        self.__GBP_M5_78.plus2(None)

    def test_plus_BigDecimal_invalidScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_34.plus2(decimal.Decimal("1.235"))

    def test_plus_BigDecimal_negative(self) -> None:

        test = self.__GBP_2_34.plus2(decimal.Decimal("-1.23"))
        assert test.toString() == "GBP 1.11"

    def test_plus_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_34.plus2(decimal.Decimal("1.23"))
        assert test.toString() == "GBP 3.57"

    def test_plus_BigDecimal_zero(self) -> None:

        test = self.__GBP_2_34.plus2(decimal.Decimal(0))
        self.assertIs(test, self.__GBP_2_34)

    def test_plus_Money_nullMoney(self) -> None:

        self.__GBP_M5_78.plus1(None)

    def test_plus_Money_currencyMismatch(self) -> None:

        with self.assertRaises(CurrencyMismatchException) as cm:
            self.__GBP_M5_78.plus1(self.__USD_1_23)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__USD, cm.exception.getSecondCurrency())
        raise cm.exception

    def test_plus_Money_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_Money_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_Money_zero(self) -> None:

        pass  # LLM could not translate method body

    def test_plus_Iterable_nullIterable(self) -> None:

        self.__GBP_M5_78.plus0(None)

    def test_plus_Iterable_nullEntry(self) -> None:

        iterable = [self.__GBP_2_33, None]
        self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_currencyMismatch(self) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as cm:
            self.__GBP_M5_78.plus0(iterable)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__JPY, cm.exception.getSecondCurrency())

    def test_plus_Iterable_zero(self) -> None:

        iterable = [self.__GBP_0_00]
        test = self.__GBP_2_34.plus0(iterable)
        self.assertIs(test, self.__GBP_2_34)

    def test_plus_Iterable(self) -> None:

        iterable = [self.__GBP_2_33, self.__GBP_1_23]
        test = self.__GBP_2_34.plus0(iterable)
        assert test.toString() == "GBP 5.90"

    def test_withAmount_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_2_34.withAmount1(self.__BIGDEC_2_34, None)

    def test_withAmount_doubleRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.withAmount3(2.345, RoundingMode.UNNECESSARY)

    def test_withAmount_doubleRoundingMode_roundDown(self) -> None:

        pass  # LLM could not translate method body

    def test_withAmount_doubleRoundingMode_same(self) -> None:

        test = self.__GBP_2_34.withAmount3(2.34, RoundingMode.UNNECESSARY)
        self.assertIs(test, self.__GBP_2_34)

    def test_withAmount_doubleRoundingMode(self) -> None:

        test = self.__GBP_2_34.withAmount3(-5.78, RoundingMode.UNNECESSARY)
        assert test.toString() == "GBP -5.78"

    def test_withAmount_double_invalidScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_34.withAmount2(2.345)

    def test_withAmount_double_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withAmount_double(self) -> None:

        pass  # LLM could not translate method body

    def test_withAmount_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_2_34.withAmount1(self.__BIGDEC_2_34, None)

    def test_withAmount_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_2_34.withAmount1(None, RoundingMode.UNNECESSARY)

    def test_withAmount_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.withAmount1(decimal.Decimal("2.345"), RoundingMode.UNNECESSARY)

    def test_withAmount_BigDecimalRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.withAmount1(decimal.Decimal("2.355"), RoundingMode.DOWN)
        self.assertEqual(self.__GBP_2_35, test)

    def test_withAmount_BigDecimalRoundingMode_same(self) -> None:

        test = self.__GBP_2_34.withAmount1(self.__BIGDEC_2_34, RoundingMode.UNNECESSARY)
        self.assertIs(test, self.__GBP_2_34)

    def test_withAmount_BigDecimalRoundingMode(self) -> None:

        test = self.__GBP_2_34.withAmount1(
            self.__BIGDEC_M5_78, RoundingMode.UNNECESSARY
        )
        assert test.toString() == "GBP -5.78"

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:

        self.__GBP_2_34.withAmount0(None)

    def test_withAmount_BigDecimal_invalidScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_2_34.withAmount0(decimal.Decimal("2.345"))

    def test_withAmount_BigDecimal_same(self) -> None:

        test = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_34)
        self.assertSame(self.__GBP_2_34, test)

    def test_withAmount_BigDecimal(self) -> None:

        pass  # LLM could not translate method body

    def test_isNegativeOrZero(self) -> None:

        pass  # LLM could not translate method body

    def test_isNegative(self) -> None:

        pass  # LLM could not translate method body

    def test_isPositiveOrZero(self) -> None:

        pass  # LLM could not translate method body

    def test_isPositive(self) -> None:

        pass  # LLM could not translate method body

    def test_isZero(self) -> None:

        pass  # LLM could not translate method body

    def test_getMinorPart_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getMinorPart_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorInt_tooBigNegative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorInt_tooBigPositive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorInt_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorInt_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorLong_tooBigNegative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorLong_tooBigPositive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorLong_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinorLong_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinor_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMinor_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorInt_tooBigNegative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorInt_tooBigPositive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorInt_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorInt_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorLong_tooBigNegative(self) -> None:

        with self.assertRaises(ArithmeticError):
            self.__GBP_LONG_MIN_MAJOR_MINUS1.getAmountMajorLong()

    def test_getAmountMajorLong_tooBigPositive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorLong_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajorLong_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajor_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmountMajor_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmount_negative(self) -> None:

        pass  # LLM could not translate method body

    def test_getAmount_positive(self) -> None:

        pass  # LLM could not translate method body

    def test_getScale_JPY(self) -> None:

        pass  # LLM could not translate method body

    def test_getScale_GBP(self) -> None:

        pass  # LLM could not translate method body

    def test_withCurrencyUnit_CurrencyRoundingMode_nullCurrency(self) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_2_34.withCurrencyUnit1(None, RoundingMode.UNNECESSARY)

    def test_withCurrencyUnit_CurrencyRoundingMode_UNECESSARY(self) -> None:

        self.__GBP_2_34.withCurrencyUnit1(self.__JPY, RoundingMode.UNNECESSARY)

    def test_withCurrencyUnit_CurrencyRoundingMode_same(self) -> None:

        test = self.__GBP_2_34.withCurrencyUnit1(self.__GBP, RoundingMode.DOWN)
        self.assertSame(self.__GBP_2_34, test)

    def test_withCurrencyUnit_CurrencyRoundingMode_UP(self) -> None:

        pass  # LLM could not translate method body

    def test_withCurrencyUnit_CurrencyRoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate method body

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:

        self.__GBP_2_34.withCurrencyUnit0(None)

    def test_withCurrencyUnit_Currency_scaleProblem(self) -> None:

        self.__GBP_2_34.withCurrencyUnit0(self.__JPY)

    def test_withCurrencyUnit_Currency_same(self) -> None:

        pass  # LLM could not translate method body

    def test_withCurrencyUnit_Currency(self) -> None:

        pass  # LLM could not translate method body

    def test_getCurrencyUnit_EUR(self) -> None:

        pass  # LLM could not translate method body

    def test_getCurrencyUnit_GBP(self) -> None:

        pass  # LLM could not translate method body

    def test_constructor_scale(self) -> None:

        with self.assertRaises(AssertionError):
            Money(0, BigMoney.of0(self.__GBP, self.__BIGDEC_2_3))

    def test_constructor_null1(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_parse_String_nullString(self) -> None:

        Money.parse(None)

    def test_factory_parse_String_badCurrency(self) -> None:

        with self.assertRaises(ValueError):
            Money.parse("GBX 2.34")

    def test_factory_parse_String_tooShort(self) -> None:

        with self.assertRaises(ValueError):
            Money.parse("GBP ")

    def test_factory_parse(self, str: str, currency: CurrencyUnit, amount: int) -> None:

        test = Money.parse(str)
        self.assertEqual(currency, test.getCurrencyUnit())
        self.assertEqual(amount, test.getAmountMinorInt())

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:

        iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
        Money.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:

        iterable = [None, self.__GBP_2_33, self.__GBP_2_36]
        Money.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(
        self,
    ) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__JPY, cm.exception.getSecondCurrency())

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:

        iterable = [self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__JPY, cm.exception.getSecondCurrency())
        raise cm.exception

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitIterable(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:

        array = [self.__GBP_2_33, None, self.__GBP_2_36]
        Money.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:

        Money.total2(self.__GBP, self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:

        array = [None, self.__GBP_2_33, self.__GBP_2_36]
        Money.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:

        Money.total2(self.__GBP, None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:

        array = [self.__GBP_2_33, self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__JPY, cm.exception.getSecondCurrency())

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:

        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total2(self.__GBP, [self.__GBP_2_33, self.__JPY_423])
        self.assertEqual(cm.exception.first_currency, self.__GBP)
        self.assertEqual(cm.exception.second_currency, self.__JPY)
        raise cm.exception

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:

        array = [self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__JPY, cm.exception.getSecondCurrency())
        raise cm.exception

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:

        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total2(self.__GBP, self.__JPY_423)
        self.assertEqual(cm.exception.getFirstCurrency(), self.__GBP)
        self.assertEqual(cm.exception.getSecondCurrency(), self.__JPY)
        raise cm.exception

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_3(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
        test = Money.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_1(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_Iterable_nullNotFirst(self) -> None:

        iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
        self.total1(iterable)

    def test_factory_total_Iterable_nullFirst(self) -> None:

        iterable = [None, self.__GBP_2_33, self.__GBP_2_36]
        Money.total1(iterable)

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total1(iterable)
        self.assertEqual(self.__GBP, cm.exception.getFirstCurrency())
        self.assertEqual(self.__JPY, cm.exception.getSecondCurrency())
        raise cm.exception

    def test_factory_total_Iterable_empty(self) -> None:

        iterable = []
        Money.total1(iterable)

    def test_factory_total_Iterable(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_array_nullNotFirst(self) -> None:

        array = [self.__GBP_2_33, None, self.__GBP_2_36]
        self.total0(array)

    def test_factory_total_varargs_nullNotFirst(self) -> None:

        Money.total0([self.__GBP_2_33, None, self.__GBP_2_36])

    def test_factory_total_array_nullFirst(self) -> None:

        array = [None, self.__GBP_2_33, self.__GBP_2_36]
        self.total0(array)

    def test_factory_total_varargs_nullFirst(self) -> None:

        Money.total0(None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_array_currenciesDiffer(self) -> None:

        array = [self.__GBP_2_33, self.__JPY_423]
        with self.assertRaises(CurrencyMismatchException) as context:
            Money.total0(array)
        ex = context.exception
        self.assertEqual(self.__GBP, ex.getFirstCurrency())
        self.assertEqual(self.__JPY, ex.getSecondCurrency())
        raise ex

    def test_factory_total_varargs_currenciesDiffer(self) -> None:

        with self.assertRaises(CurrencyMismatchException) as cm:
            Money.total0(self.__GBP_2_33, self.__JPY_423)
        ex = cm.exception
        self.assertEqual(self.__GBP, ex.getFirstCurrency())
        self.assertEqual(self.__JPY, ex.getSecondCurrency())
        raise ex

    def test_factory_total_array_empty(self) -> None:

        array = []
        Money.total0(array)

    def test_factory_total_varargs_empty(self) -> None:

        Money.total0()

    def test_factory_total_array_3(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_varargs_3(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_array_1(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_total_varargs_1(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_from_BigMoneyProvider_RoundingMode_nullRoundingMode(self) -> None:

        Money.of5(BigMoney.parse("GBP 104.235"), None)

    def test_factory_from_BigMoneyProvider_RoundingMode_nullBigMoneyProvider(
        self,
    ) -> None:

        Money.of5(None, RoundingMode.DOWN)

    def test_factory_from_BigMoneyProvider_RoundingMode(self) -> None:

        test = Money.of5(BigMoney.parse("GBP 104.235"), RoundingMode.HALF_EVEN)
        self.assertEqual(self, test.getCurrencyUnit(), CurrencyUnit.self.__GBP)
        self.assertEqual(self, test.getAmountMinorInt(), 10424)
        self.assertEqual(self, test.getAmount().scale(), 2)

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

        Money.of4(None)

    def test_factory_from_BigMoneyProvider_invalidCurrencyScale(self) -> None:

        with self.assertRaises(ArithmeticError):
            Money.of4(BigMoney.parse("GBP 104.235"))

    def test_factory_from_BigMoneyProvider_fixScale(self) -> None:

        test = Money.of4(BigMoney.parse("GBP 104.2"))
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(10420, test.getAmountMinorInt())
        self.assertEqual(2, test.getAmount().scale())

    def test_factory_from_BigMoneyProvider(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_zero_Currency_nullCurrency(self) -> None:

        Money.zero(None)

    def test_factory_zero_Currency(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:

        Money.ofMinor(None, 234)

    def test_factory_ofMinor_Currency_long(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:

        Money.ofMajor(None, 234)

    def test_factory_ofMajor_Currency_long(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_RoundingMode_nullRoundingMode(self) -> None:

        Money.of3(self.__GBP, 2.34, None)

    def test_factory_of_Currency_double_RoundingMode_nullCurrency(self) -> None:

        Money.of3(None, 2.34, RoundingMode.DOWN)

    def test_factory_of_Currency_double_RoundingMode_UNNECESSARY(self) -> None:

        Money.of3(JPY, 2.34, RoundingMode.UNNECESSARY)

    def test_factory_of_Currency_double_JPY_RoundingMode_UP(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_JPY_RoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_GBP_RoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_nullCurrency(self) -> None:

        Money.of0(None, self.__BIGDEC_2_34)

    def test_factory_of_Currency_double_invalidScaleJPY(self) -> None:

        with self.assertRaises(ArithmeticError):
            Money.of2(JPY, 2.3)

    def test_factory_of_Currency_double_invalidScaleGBP(self) -> None:

        Money.of2(CurrencyUnit.self.__GBP, 2.345)

    def test_factory_of_Currency_double_big(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_medium(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_trailingZero2(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_trailingZero1(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double_correctScale(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_double(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullRoundingMode(self) -> None:

        Money.of1(self.__GBP, self.__BIGDEC_2_34, None)

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullBigDecimal(self) -> None:

        Money.of1(self.__GBP, None, RoundingMode.DOWN)

    def test_factory_of_Currency_BigDecimal_RoundingMode_nullCurrency(self) -> None:

        Money.of1(None, self.__BIGDEC_2_34, RoundingMode.DOWN)

    def test_factory_of_Currency_BigDecimal_RoundingMode_UNNECESSARY(self) -> None:

        Money.of1(self.__JPY, self.__BIGDEC_2_34, RoundingMode.UNNECESSARY)

    def test_factory_of_Currency_BigDecimal_JPY_RoundingMode_UP(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_BigDecimal_JPY_RoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_BigDecimal_GBP_RoundingMode_DOWN(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:

        Money.of0(self.__GBP, None)

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:

        with self.assertRaises(TypeError):
            Money.of0(None, BIGDEC_2_34)

    def test_factory_of_Currency_BigDecimal_invalidScaleJPY(self) -> None:

        with self.assertRaises(ArithmeticError):
            Money.of0(self.__JPY, self.__BIGDEC_2_3)

    def test_factory_of_Currency_BigDecimal_invalidScaleGBP(self) -> None:

        Money.of0(self.__GBP, self.__BIGDEC_2_345)

    def test_factory_of_Currency_BigDecimal_correctScale(self) -> None:

        pass  # LLM could not translate method body

    def test_factory_of_Currency_BigDecimal(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
