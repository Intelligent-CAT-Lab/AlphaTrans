# Imports Begin
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import unittest
import os
import typing
from typing import *
# Imports End

class TestBigMoney(unittest.TestCase):

    # Class Fields Begin
    __GBP: CurrencyUnit = CurrencyUnit.of("GBP")
    __EUR: CurrencyUnit = CurrencyUnit.of1("EUR")
    __USD: CurrencyUnit = CurrencyUnit.of("USD")
    __JPY: CurrencyUnit = CurrencyUnit.of("JPY")
    __BIGDEC_2_34: decimal.Decimal = 2.34
    __BIGDEC_2_345: decimal.Decimal = 2.345
    __BIGDEC_M5_78: decimal.Decimal = decimal.Decimal("-5.78")
    __GBP_0_00: BigMoney = BigMoney.parse("GBP 0.00")
    __GBP_1_23: BigMoney = BigMoney.parse("GBP 1.23")
    __GBP_2_33: BigMoney = BigMoney.parse("GBP 2.33")
    __GBP_2_34: BigMoney = BigMoney.parse("GBP 2.34")
    __GBP_2_35: BigMoney = BigMoney.parse("GBP 2.35")
    __GBP_2_36: BigMoney = BigMoney.parse("GBP 2.36")
    __GBP_5_78: BigMoney = BigMoney.parse("GBP 5.78")
    __GBP_M1_23: BigMoney = BigMoney.parse("GBP -1.23")
    __GBP_M5_78: BigMoney = BigMoney.parse("GBP -5.78")
    __GBP_INT_MAX_PLUS1: BigMoney = BigMoney.of_minor(GBP, (Integer.MAX_VALUE + 1))
    __GBP_INT_MIN_MINUS1: BigMoney = "" # LLM could not translate field
    __GBP_INT_MAX_MAJOR_PLUS1: BigMoney = "" # LLM could not translate field
    __GBP_INT_MIN_MAJOR_MINUS1: BigMoney = "" # LLM could not translate field
    __GBP_LONG_MAX_PLUS1: BigMoney = BigMoney.of(GBP, BigDecimal.valueOf(Long.MAX_VALUE).add(BigDecimal.ONE))
    __GBP_LONG_MIN_MINUS1: BigMoney = BigMoney.of(GBP, BigDecimal.valueOf(Long.MIN_VALUE).subtract(BigDecimal.ONE))
    __GBP_LONG_MAX_MAJOR_PLUS1: BigMoney = BigMoney.of(GBP, BigDecimal.valueOf(Long.MAX_VALUE).add(BigDecimal.ONE).multiply(BigDecimal.valueOf(100)))
    __GBP_LONG_MIN_MAJOR_MINUS1: BigMoney = BigMoney.of(GBP, BigDecimal.valueOf(Long.MIN_VALUE).subtract(BigDecimal.ONE).multiply(BigDecimal.valueOf(100)))
    __JPY_423: BigMoney = BigMoney.parse("JPY 423")
    __USD_1_23: BigMoney = BigMoney.parse("USD 1.23")
    __USD_2_34: BigMoney = BigMoney.parse("USD 2.34")
    __USD_2_35: BigMoney = BigMoney.parse("USD 2.35")
    __BAD_PROVIDER: BigMoneyProvider = BigMoneyProvider()
    # Class Fields End

    # Class Methods Begin
    def test_toString_negative(self) -> None:


        pass # LLM could not translate method body

    def test_toString_positive(self) -> None:


        pass # LLM could not translate method body

    def test_equals_false(self) -> None:


        pass # LLM could not translate method body

    def test_equals_hashCode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:


        pass # LLM could not translate method body

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


        pass # LLM could not translate method body

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


        pass # LLM could not translate method body

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


        pass # LLM could not translate method body

    def test_isGreaterThan(self) -> None:

            a = self.__GBP_2_34
            b = self.__GBP_2_35
            c = self.__GBP_2_36
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


        pass # LLM could not translate method body

    def test_isEqual_Money(self) -> None:


        pass # LLM could not translate method body

    def test_isEqual(self) -> None:


        pass # LLM could not translate method body

    def test_compareTo_wrongType(self) -> None:

            a = self.__GBP_2_34
            a.compareTo("NotRightType")

    def test_compareTo_currenciesDiffer(self) -> None:

            a = self.__GBP_2_34
            b = self.__USD_2_35
            a.compareTo(b)

    def test_compareTo_Money(self) -> None:


        pass # LLM could not translate method body

    def test_compareTo_BigMoney(self) -> None:

            a = self.__GBP_2_34
            b = self.__GBP_2_35
            c = self.__GBP_2_36
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

            self.__GBP_2_34.isSameCurrency(None)

    def test_isSameCurrency_Money_different(self) -> None:


        pass # LLM could not translate method body

    def test_isSameCurrency_Money_same(self) -> None:


        pass # LLM could not translate method body

    def test_isSameCurrency_BigMoney_different(self) -> None:


        pass # LLM could not translate method body

    def test_isSameCurrency_BigMoney_same(self) -> None:


        pass # LLM could not translate method body

    def test_toMoney_RoundingMode_round(self) -> None:

            money = BigMoney.parse("GBP 2.355")
            self.assertEqual(Money.parse("GBP 2.36"), money.toMoney1(RoundingMode.HALF_EVEN))

    def test_toMoney_RoundingMode(self) -> None:

            self.assertEqual(Money.parse("GBP 2.34"), GBP_2_34.toMoney1(RoundingMode.HALF_EVEN))

    def test_toMoney(self) -> None:


        pass # LLM could not translate method body

    def test_toBigMoney(self) -> None:


        pass # LLM could not translate method body

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_5_78.convertRetainScale(self.__EUR, self.__bd("2"), None)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullBigDecimal(self) -> None:

            self.assertRaises(
                TypeError,
                self.__GBP_5_78.convertRetainScale,
                self.__EUR,
                None,
                RoundingMode.DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullCurrency(self) -> None:

            self.assertRaises(
                TypeError,
                self.__GBP_5_78.convertRetainScale,
                None,
                self.__bd("2"),
                RoundingMode.DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_sameCurrency(self) -> None:


        pass # LLM could not translate method body

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_roundHalfUp(self) -> None:

            test = BigMoney.parse("GBP 2.21").convertRetainScale(EUR, bd("2.5"), RoundingMode.HALF_UP)
            self.assertEqual("EUR 5.53", test.toString())

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_positive(self) -> None:

            test = self.parse("GBP 2.2").convertRetainScale(self.__EUR, self.__bd("2.5"), RoundingMode.DOWN)
            assert test.toString() == "EUR 5.5"

    def test_convertedTo_CurrencyUnit_BigDecimal_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_5_78.convertedTo(self.__EUR, None)

    def test_convertedTo_CurrencyUnit_BigDecimal_nullCurrency(self) -> None:


        pass # LLM could not translate method body

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyWrongFactor(self) -> None:


        pass # LLM could not translate method body

    def test_convertedTo_CurrencyUnit_BigDecimal_negative(self) -> None:


        pass # LLM could not translate method body

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyCorrectFactor(self) -> None:

            test = self.GBP_2_33.convertedTo(self.__GBP, self.__bd("1.00000"))
            self.assertEqual(self.GBP_2_33, test)

    def test_convertedTo_CurrencyUnit_BigDecimal_positive(self) -> None:


        pass # LLM could not translate method body

    def test_round_3(self) -> None:

            test = self.__GBP_2_34.rounded(3, RoundingMode.DOWN)
            self.assertSame(self.__GBP_2_34, test)

    def test_round_M1up(self) -> None:

            test = BigMoney.parse("GBP 432.34").rounded(-1, RoundingMode.UP)
            self.assertEqual("GBP 440.00", test.toString())

    def test_round_M1down(self) -> None:

            test = BigMoney.parse("GBP 432.34").rounded(-1, RoundingMode.DOWN)
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
            self.assertEqual("GBP 2.30", test.toString())

    def test_round_2up(self) -> None:

            test = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
            self.assertSame(self.__GBP_2_34, test)

    def test_round_2down(self) -> None:

            test = self.__GBP_2_34.rounded(2, RoundingMode.DOWN)
            self.assertSame(self.__GBP_2_34, test)

    def test_abs_negative(self) -> None:


        pass # LLM could not translate method body

    def test_abs_positive(self) -> None:


        pass # LLM could not translate method body

    def test_negated_negative(self) -> None:


        pass # LLM could not translate method body

    def test_negated_positive(self) -> None:


        pass # LLM could not translate method body

    def test_negated_zero(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_long_negative(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_long_positive_roundUp(self) -> None:

            test = self.__GBP_2_35.dividedBy2(3, RoundingMode.UP)
            assert test.toString() == "GBP 0.79"

    def test_dividedBy_long_positive_roundDown(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_long_positive(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_long_one(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_5_78.dividedBy1(2.5, None)

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_doubleRoundingMode_one(self) -> None:

            test = self.__GBP_2_34.dividedBy1(1.0, RoundingMode.DOWN)
            self.assertIs(self.__GBP_2_34, test)

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_5_78.dividedBy0(self.__bd("2.5"), None)

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_5_78.dividedBy0(None, RoundingMode.DOWN)

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:

            test = self.__GBP_2_34.dividedBy0(decimal.Decimal(1), RoundingMode.DOWN)
            assert test is self.__GBP_2_34

    def test_multiplyRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_5_78.multiplyRetainScale1(2.5, None)

    def test_multiplyRetainScale_doubleRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_multiplyRetainScale_doubleRoundingMode_positive_halfUp(self) -> None:


        pass # LLM could not translate method body

    def test_multiplyRetainScale_doubleRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_multiplyRetainScale_doubleRoundingMode_one(self) -> None:

            test = self.__GBP_2_34.multiplyRetainScale1(1.0, RoundingMode.DOWN)
            self.assertIs(test, self.__GBP_2_34)

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_5_78.multiplyRetainScale0(self.__bd("2.5"), None)

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_5_78.multiplyRetainScale0(None, RoundingMode.DOWN)

    def test_multiplyRetainScale_BigDecimalRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive_halfUp(self) -> None:


        pass # LLM could not translate method body

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_multiplyRetainScale_BigDecimalRoundingMode_one(self) -> None:

            test = self.__GBP_2_34.multiplyRetainScale0(decimal.Decimal(1), RoundingMode.DOWN)
            self.assertSame(self.__GBP_2_34, test)

    def test_multipliedBy_long_negative(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_long_positive(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_long_one(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:

            test = self.__GBP_2_34.multipliedBy1(1.0)
            self.assertIs(test, self.__GBP_2_34)

    def test_multipliedBy_BigDecimal_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_5_78.multipliedBy0(None)

    def test_multipliedBy_BigDecimal_negative(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_BigDecimal_positive(self) -> None:


        pass # LLM could not translate method body

    def test_multipliedBy_BigDecimal_one(self) -> None:

            test = self.__GBP_2_34.multipliedBy0(decimal.Decimal(1))
            self.assertIs(test, self.__GBP_2_34)

    def test_minusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_M5_78.minusRetainScale2(2.34, None)

    def test_minusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

            self.__GBP_2_34.minusRetainScale2(1.235, RoundingMode.UNNECESSARY)

    def test_minusRetainScale_doubleRoundingMode_roundDown(self) -> None:

            test = self.__GBP_2_34.minusRetainScale2(1.235, RoundingMode.DOWN)
            assert test.toString() == "GBP 1.10"

    def test_minusRetainScale_doubleRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_minusRetainScale_doubleRoundingMode_positive(self) -> None:

            test = self.__GBP_2_34.minusRetainScale2(1.23, RoundingMode.UNNECESSARY)
            assert test.toString() == "GBP 1.11"

    def test_minusRetainScale_doubleRoundingMode_zero(self) -> None:

            test = self.__GBP_2_34.minusRetainScale2(0.0, RoundingMode.UNNECESSARY)
            self.assertIs(test, self.__GBP_2_34)

    def test_minusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_M5_78.minusRetainScale1(self.__BIGDEC_2_34, None)

    def test_minusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_M5_78.minusRetainScale1(None, RoundingMode.UNNECESSARY)

    def test_minusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:

            self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), RoundingMode.UNNECESSARY)

    def test_minusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:

            test = self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), RoundingMode.DOWN)
            assert test.toString() == "GBP 1.10"

    def test_minusRetainScale_BigDecimalRoundingMode_negative(self) -> None:

            test = self.__GBP_2_34.minusRetainScale1(self.__bd("-1.23"), RoundingMode.UNNECESSARY)
            self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_positive(self) -> None:

            test = self.__GBP_2_34.minusRetainScale1(self.__bd("1.23"), RoundingMode.UNNECESSARY)
            assert test.toString() == "GBP 1.11"

    def test_minusRetainScale_BigDecimalRoundingMode_zero(self) -> None:

            test = self.__GBP_2_34.minusRetainScale1(decimal.Decimal(0), RoundingMode.UNNECESSARY)
            self.assertIs(test, self.__GBP_2_34)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_M5_78.minusRetainScale0(BigMoney.parse("GBP 123"), None)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullBigMoneyProvider(self) -> None:

            self.__GBP_M5_78.minusRetainScale0(None, RoundingMode.UNNECESSARY)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(self) -> None:

            self.__GBP_2_34.minusRetainScale0(BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:

            test = self.__GBP_2_34.minusRetainScale0(BigMoney.parse("GBP 1.235"), RoundingMode.DOWN)
            assert test.toString() == "GBP 1.10"

    def test_minusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:

            test = self.__GBP_2_34.minusRetainScale0(BigMoney.parse("GBP -1.23"), RoundingMode.UNNECESSARY)
            self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:

            test = self.__GBP_2_34.minusRetainScale0(BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY)
            assert test.toString() == "GBP 1.11"

    def test_minusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:

            test = self.__GBP_2_34.minusRetainScale0(self.__zero0(self.__GBP), RoundingMode.UNNECESSARY)
            assert test == self.__GBP_2_34

    def test_minusMinor_scale(self) -> None:


        pass # LLM could not translate method body

    def test_minusMinor_negative(self) -> None:


        pass # LLM could not translate method body

    def test_minusMinor_positive(self) -> None:


        pass # LLM could not translate method body

    def test_minusMinor_zero(self) -> None:

            test = self.__GBP_2_34.minusMinor(0)
            self.assertIs(test, self.__GBP_2_34)

    def test_minusMajor_negative(self) -> None:


        pass # LLM could not translate method body

    def test_minusMajor_positive(self) -> None:


        pass # LLM could not translate method body

    def test_minusMajor_zero(self) -> None:

            test = self.__GBP_2_34.minusMajor(0)
            self.assertIs(test, self.__GBP_2_34)

    def test_minus_double_scale(self) -> None:


        pass # LLM could not translate method body

    def test_minus_double_negative(self) -> None:


        pass # LLM could not translate method body

    def test_minus_double_positive(self) -> None:


        pass # LLM could not translate method body

    def test_minus_double_zero(self) -> None:

            test = self.__GBP_2_34.minus3(0.0)
            assert test is self.__GBP_2_34

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_M5_78.minus2(None)

    def test_minus_BigDecimal_scale(self) -> None:


        pass # LLM could not translate method body

    def test_minus_BigDecimal_negative(self) -> None:


        pass # LLM could not translate method body

    def test_minus_BigDecimal_positive(self) -> None:


        pass # LLM could not translate method body

    def test_minus_BigDecimal_zero(self) -> None:

            test = self.__GBP_2_34.minus2(decimal.Decimal(0))
            self.assertIs(test, self.__GBP_2_34)

    def test_minus_BigMoneyProvider_badProvider(self) -> None:

            self.__GBP_M5_78.minus1(
                BigMoneyProvider()
            )

    def test_minus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

            self.__GBP_M5_78.minus1(None)

    def test_minus_BigMoneyProvider_currencyMismatch(self) -> None:

            with self.assertRaises(CurrencyMismatchException):
                self.__GBP_M5_78.minus1(self.__USD_1_23)

    def test_minus_BigMoneyProvider_Money(self) -> None:


        pass # LLM could not translate method body

    def test_minus_BigMoneyProvider_scale(self) -> None:

            test = self.__GBP_2_34.minus1(BigMoney.parse("GBP 1.111"))
            assert test.toString() == "GBP 1.229"
            assert test.getScale() == 3

    def test_minus_BigMoneyProvider_negative(self) -> None:


        pass # LLM could not translate method body

    def test_minus_BigMoneyProvider_positive(self) -> None:


        pass # LLM could not translate method body

    def test_minus_BigMoneyProvider_zero(self) -> None:

            test = self.__GBP_2_34.minus1(self.__GBP_0_00)
            self.assertSame(self.__GBP_2_34, test)

    def test_minus_Iterable_badProvider(self) -> None:

            iterable = [BigMoneyProvider()]
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_nullIterable(self) -> None:

            self.__GBP_M5_78.minus0(None)

    def test_minus_Iterable_nullEntry(self) -> None:

            iterable = [self.__GBP_2_33, None]
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_currencyMismatch(self) -> None:

            iterable = [self.__GBP_2_33, self.__JPY_423]
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_zero(self) -> None:

            iterable = [self.__GBP_0_00]
            test = self.__GBP_2_34.minus0(iterable)
            assert test == self.__GBP_2_34

    def test_minus_Iterable_Mixed(self) -> None:

            iterable = [self.__GBP_2_33.toMoney0(),
                        BigMoneyProvider(GBP_1_23)]
            test = self.__GBP_2_34.minus0(iterable)
            assert test.toString() == "GBP -1.22"

    def test_minus_Iterable_Money(self) -> None:

            iterable = [self.__GBP_2_33.toMoney0(), self.__GBP_1_23.toMoney0()]
            test = self.__GBP_2_34.minus0(iterable)
            self.assertEqual("GBP -1.22", test.toString())

    def test_minus_Iterable_BigMoney(self) -> None:

            iterable = [self.__GBP_2_33, self.__GBP_1_23]
            test = self.__GBP_2_34.minus0(iterable)
            assert test.toString() == "GBP -1.22"

    def test_minus_Iterable_BigMoneyProvider(self) -> None:

            iterable = [self.__GBP_2_33, self.__GBP_1_23]
            test = self.__GBP_2_34.minus0(iterable)
            assert test.toString() == "GBP -1.22"

    def test_plusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_M5_78.plusRetainScale2(2.34, None)

    def test_plusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

            self.__GBP_2_34.plusRetainScale2(1.235, RoundingMode.UNNECESSARY)

    def test_plusRetainScale_doubleRoundingMode_roundDown(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_doubleRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_doubleRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_doubleRoundingMode_zero(self) -> None:

            test = self.__GBP_2_34.plusRetainScale2(0.0, RoundingMode.UNNECESSARY)
            self.assertIs(test, self.__GBP_2_34)

    def test_plusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_M5_78.plusRetainScale1(self.__BIGDEC_2_34, None)

    def test_plusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_M5_78.plusRetainScale1(None, RoundingMode.UNNECESSARY)

    def test_plusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:

            self.__GBP_2_34.plusRetainScale1(self.__bd("1.235"), RoundingMode.UNNECESSARY)

    def test_plusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:

            test = self.__GBP_2_34.plusRetainScale1(self.__bd("1.235"), RoundingMode.DOWN)
            assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_BigDecimalRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_BigDecimalRoundingMode_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_BigDecimalRoundingMode_zero(self) -> None:

            test = self.__GBP_2_34.plusRetainScale1(decimal.Decimal(0), RoundingMode.UNNECESSARY)
            assert test is self.__GBP_2_34

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(self) -> None:

            self.__GBP_M5_78.plusRetainScale0(BigMoney.parse("GBP 1.23"), None)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_M5_78.plusRetainScale1(None, RoundingMode.UNNECESSARY)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:

            test = self.__GBP_2_34.plusRetainScale0(BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY)
            assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:

            test = self.__GBP_2_34.plusRetainScale0(self.__zero0(self.__GBP), RoundingMode.UNNECESSARY)
            self.assertSame(self.__GBP_2_34, test)

    def test_plusMinor_scale(self) -> None:


        pass # LLM could not translate method body

    def test_plusMinor_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plusMinor_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plusMinor_zero(self) -> None:

            test = self.__GBP_2_34.plusMinor(0)
            self.assertIs(test, self.__GBP_2_34)

    def test_plusMajor_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plusMajor_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plusMajor_zero(self) -> None:

            test = self.__GBP_2_34.plusMajor(0)
            self.assertIs(test, self.__GBP_2_34)

    def test_plus_double_scale(self) -> None:


        pass # LLM could not translate method body

    def test_plus_double_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plus_double_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plus_double_zero(self) -> None:

            test = self.__GBP_2_34.plus3(0.0)
            self.assertIs(test, self.__GBP_2_34)

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_M5_78.plus2(None)

    def test_plus_BigDecimal_scale(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigDecimal_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigDecimal_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigDecimal_zero(self) -> None:

            test = self.__GBP_2_34.plus2(decimal.Decimal(0))
            self.assertIs(test, self.__GBP_2_34)

    def test_plus_BigMoneyProvider_badProvider(self) -> None:

            self.__GBP_M5_78.plus1(
                BigMoneyProvider()
            )

    def test_plus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

            self.__GBP_M5_78.plus1(None)

    def test_plus_BigMoneyProvider_currencyMismatch(self) -> None:

            with self.assertRaises(CurrencyMismatchException):
                self.__GBP_M5_78.plus1(self.__USD_1_23)

    def test_plus_BigMoneyProvider_Money(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigMoneyProvider_scale(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigMoneyProvider_negative(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigMoneyProvider_positive(self) -> None:


        pass # LLM could not translate method body

    def test_plus_BigMoneyProvider_zero(self) -> None:

            test = self.GBP_2_34.plus1(self.GBP_0_00)
            self.assertSame(self.GBP_2_34, test)

    def test_plus_Iterable_badProvider(self) -> None:

            iterable = [BigMoneyProvider()]
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_nullIterable(self) -> None:

            self.__GBP_M5_78.plus0(None)

    def test_plus_Iterable_nullEntry(self) -> None:

            iterable = [self.__GBP_2_33, None]
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_currencyMismatch(self) -> None:

            iterable = [self.__GBP_2_33, self.__JPY_423]
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_zero(self) -> None:

            iterable = [self.__GBP_0_00]
            test = self.__GBP_2_34.plus0(iterable)
            assert test == self.__GBP_2_34

    def test_plus_Iterable_Mixed(self) -> None:


        pass # LLM could not translate method body

    def test_plus_Iterable_Money(self) -> None:


        pass # LLM could not translate method body

    def test_plus_Iterable_BigMoney(self) -> None:

            iterable = [self.__GBP_2_33, self.__GBP_1_23]
            test = self.__GBP_2_34.plus0(iterable)
            assert test.toString() == "GBP 5.90"

    def test_plus_Iterable_BigMoneyProvider(self) -> None:

            iterable = [self.__GBP_2_33, self.__GBP_1_23]
            test = self.__GBP_2_34.plus0(iterable)
            assert test.toString() == "GBP 5.90"

    def test_withAmount_double_same(self) -> None:

            test = self.__GBP_2_34.withAmount1(2.34)
            self.assertIs(self.__GBP_2_34, test)

    def test_withAmount_double(self) -> None:


        pass # LLM could not translate method body

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:

            self.__GBP_2_34.withAmount0(None)

    def test_withAmount_BigDecimal_same(self) -> None:

            test = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_34)
            self.assertIs(test, self.__GBP_2_34)

    def test_withAmount_BigDecimal(self) -> None:


        pass # LLM could not translate method body

    def test_isNegativeOrZero(self) -> None:


        pass # LLM could not translate method body

    def test_isNegative(self) -> None:


        pass # LLM could not translate method body

    def test_isPositiveOrZero(self) -> None:


        pass # LLM could not translate method body

    def test_isPositive(self) -> None:


        pass # LLM could not translate method body

    def test_isZero(self) -> None:


        pass # LLM could not translate method body

    def test_getMinorPart_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getMinorPart_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorInt_tooBigNegative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorInt_tooBigPositive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorInt_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorInt_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorLong_tooBigNegative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorLong_tooBigPositive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorLong_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinorLong_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinor_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMinor_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorInt_tooBigNegative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorInt_tooBigPositive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorInt_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorInt_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorLong_tooBigNegative(self) -> None:

            with self.assertRaises(ArithmeticError):
                self.__GBP_LONG_MIN_MAJOR_MINUS1.getAmountMajorLong()

    def test_getAmountMajorLong_tooBigPositive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorLong_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajorLong_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajor_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmountMajor_positive(self) -> None:


        pass # LLM could not translate method body

    def test_getAmount_negative(self) -> None:


        pass # LLM could not translate method body

    def test_getAmount_positive(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyScale_intRoundingMode_lessJPY(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyScale_intRoundingMode_more(self) -> None:

            test = BigMoney.parse("GBP 2.3").withCurrencyScale1(RoundingMode.UP)
            self.assertEqual(bd("2.30"), test.getAmount())
            self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_intRoundingMode_less(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyScale_int_less(self) -> None:

            self.withCurrencyScale0(BigMoney.parse("GBP 2.345"))

    def test_withCurrencyScale_int_more(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyScale_int_same(self) -> None:


        pass # LLM could not translate method body

    def test_withScale_intRoundingMode_more(self) -> None:


        pass # LLM could not translate method body

    def test_withScale_intRoundingMode_less(self) -> None:


        pass # LLM could not translate method body

    def test_withScale_int_less(self) -> None:

            BigMoney.parse("GBP 2.345").withScale0(2)

    def test_withScale_int_more(self) -> None:


        pass # LLM could not translate method body

    def test_withScale_int_same(self) -> None:

            test = self.__GBP_2_34.withScale0(2)
            self.assertSame(self.__GBP_2_34, test)

    def test_isCurrencyScale_JPY(self) -> None:


        pass # LLM could not translate method body

    def test_isCurrencyScale_GBP(self) -> None:


        pass # LLM could not translate method body

    def test_getScale_JPY(self) -> None:


        pass # LLM could not translate method body

    def test_getScale_GBP(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:

            with self.assertRaises(TypeError):
                self.__GBP_2_34.withCurrencyUnit(None)

    def test_withCurrencyUnit_Currency_differentCurrencyScale(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyUnit_Currency_same(self) -> None:


        pass # LLM could not translate method body

    def test_withCurrencyUnit_Currency(self) -> None:


        pass # LLM could not translate method body

    def test_getCurrencyUnit_EUR(self) -> None:


        pass # LLM could not translate method body

    def test_getCurrencyUnit_GBP(self) -> None:


        pass # LLM could not translate method body

    def test_scaleNormalization3(self) -> None:


        pass # LLM could not translate method body

    def test_scaleNormalization2(self) -> None:


        pass # LLM could not translate method body

    def test_scaleNormalization1(self) -> None:


        pass # LLM could not translate method body

    def test_constructor_null2(self) -> None:

            con = BigMoney.__init__
            try:
                con(0, None, self.__GBP)
                self.fail()
            except AssertionError:
                pass

    def test_constructor_null1(self) -> None:


        pass # LLM could not translate method body

    def test_factory_parse_String_nullString(self) -> None:

            BigMoney.parse(None)

    def test_factory_parse_String_badCurrency(self) -> None:

            with self.assertRaises(IllegalArgumentException):
                BigMoney.parse("GBX 2.34")

    def test_factory_parse_String_exponent(self) -> None:

            BigMoney.parse("GBP 234E2")

    def test_factory_parse_String_tooShort(self) -> None:

            with self.assertRaises(ValueError):
                BigMoney.parse("GBP")

    def test_factory_parse(self, str: str, currency: CurrencyUnit, amountStr: str, scale: int) -> None:

            test = BigMoney.parse(str)
            self.assertEqual(currency, test.getCurrencyUnit())
            self.assertEqual(bd(amountStr), test.getAmount())
            self.assertEqual(scale, test.getScale())

    @staticmethod

    def data_parse() -> typing.List[typing.List[typing.Any]]:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitIterable_badProvider(self) -> None:

            iterable = [self.__BAD_PROVIDER]
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:

            iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:

            iterable = [None, self.__GBP_2_33, self.__GBP_2_36]
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(self) -> None:

            iterable = [self.__GBP_2_33, self.__JPY_423]
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:

            iterable = [self.__JPY_423]
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitIterable_Mixed(self) -> None:

            iterable = [self.__GBP_1_23.toMoney0(), self.__GBP_2_33]
            test = BigMoney.total3(self.__GBP, iterable)
            self.assertEqual(self.__GBP, test.getCurrencyUnit())
            self.assertEqual(Decimal('356.00'), test.getAmount())

    def test_factory_total_CurrencyUnitIterable(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_badProvider(self) -> None:

            array = [self.__BAD_PROVIDER]
            self.assertRaises(ArithmeticError, BigMoney.total2, self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_badProvider(self) -> None:

            BigMoney.total2(self.__GBP, self.__BAD_PROVIDER)

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:

            array = [self.__GBP_2_33, None, self.__GBP_2_36]
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:

            BigMoney.total2(self.__GBP, self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:

            array = [None, self.__GBP_2_33, self.__GBP_2_36]
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:

            BigMoney.total2(self.__GBP, None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:

            array = [self.__GBP_2_33, self.__JPY_423]
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:

            BigMoney.total2(self.__GBP, [self.__GBP_2_33, self.__JPY_423])

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:

            array = [self.__JPY_423]
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:

            BigMoney.total2(self.__GBP, self.__JPY_423)

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_3Money(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_3Mixed(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitVarargs_3Mixed(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitArray_3(self) -> None:

            array = [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
            test = BigMoney.total2(self.__GBP, array)
            self.assertEqual(test.getCurrencyUnit(), self.__GBP)
            self.assertEqual(test.getAmountMinorInt(), 592)

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:

            test = BigMoney.total2(GBP, [GBP_1_23, GBP_2_33, GBP_2_36])
            self.assertEqual(GBP, test.getCurrencyUnit())
            self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_1(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_Iterable_badProvider(self) -> None:

            iterable = [self.__BAD_PROVIDER]
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullNotFirst(self) -> None:

            iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullFirst(self) -> None:

            iterable = [None, self.__GBP_2_33, self.__GBP_2_36]
            self.__GBP.total1(iterable)

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:

            iterable = [self.__GBP_2_33, self.__JPY_423]
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_empty(self) -> None:

            iterable = []
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_Mixed(self) -> None:

            iterable = [self.__GBP_1_23.toMoney0(), self.__GBP_2_33]
            test = BigMoney.total1(iterable)
            self.assertEqual(self.__GBP, test.getCurrencyUnit())
            self.assertEqual(Decimal('356.00'), test.getAmount())

    def test_factory_total_Iterable(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_array_badProvider(self) -> None:

            array = [self.__BAD_PROVIDER]
            BigMoney.total0(array)

    def test_factory_total_varargs_badProvider(self) -> None:

            BigMoney.total0([self.__BAD_PROVIDER])

    def test_factory_total_array_nullNotFirst(self) -> None:

            array = [self.__GBP_2_33, None, self.__GBP_2_36]
            self.__GBP.total0(array)

    def test_factory_total_varargs_nullNotFirst(self) -> None:

            BigMoney.total0(self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_array_nullFirst(self) -> None:

            array = [None, self.__GBP_2_33, self.__GBP_2_36]
            BigMoney.total0(array)

    def test_factory_total_varargs_nullFirst(self) -> None:

            BigMoney.total0(None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_array_currenciesDiffer(self) -> None:

            array = [self.__GBP_2_33, self.__JPY_423]
            BigMoney.total0(array)

    def test_factory_total_varargs_currenciesDiffer(self) -> None:

            BigMoney.total0([self.__GBP_2_33, self.__JPY_423])

    def test_factory_total_array_empty(self) -> None:

            array = []
            BigMoney.total0(array)

    def test_factory_total_varargs_empty(self) -> None:

            BigMoney.total0()

    def test_factory_total_array_3Money(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_array_3Mixed(self) -> None:

            array = [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
            test = BigMoney.total0(array)
            self.assertEqual(self.__GBP, test.getCurrencyUnit())
            self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_varargs_3Mixed(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_array_1BigMoney(self) -> None:


        pass # LLM could not translate method body

    def test_factory_total_varargs_1BigMoney(self) -> None:


        pass # LLM could not translate method body

    def test_factory_from_BigMoneyProvider_badProvider(self) -> None:

            BigMoney.of2(self.__BAD_PROVIDER)

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

            BigMoney.of2(None)

    def test_factory_from_BigMoneyProvider(self) -> None:


        pass # LLM could not translate method body

    def test_factory_zero_Currency_int_nullCurrency(self) -> None:

            BigMoney.zero1(None, 3)

    def test_factory_zero_Currency_int_negativeScale(self) -> None:


        pass # LLM could not translate method body

    def test_factory_zero_Currency_int(self) -> None:


        pass # LLM could not translate method body

    def test_factory_zero_Currency_nullCurrency(self) -> None:

            BigMoney.zero0(None)

    def test_factory_zero_Currency(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:

            BigMoney.ofMinor(None, 234)

    def test_factory_ofMinor_Currency_long(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:

            BigMoney.ofMajor(None, 234)

    def test_factory_ofMajor_Currency_long(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofScale_Currency_long_int_nullCurrency(self) -> None:

            BigMoney.ofScale2(None, 234, 2)

    def test_factory_ofScale_Currency_long_int_negativeScale(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofScale_Currency_long_int(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullRoundingMode(self) -> None:

            BigMoney.ofScale1(self.__GBP, self.__BIGDEC_2_34, 2, None)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullBigDecimal(self) -> None:

            BigMoney.ofScale1(self.__GBP, None, 2, RoundingMode.DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullCurrency(self) -> None:

            BigMoney.ofScale1(None, self.__BIGDEC_2_34, 2, RoundingMode.DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_UNNECESSARY(self) -> None:

            BigMoney.ofScale1(JPY, BIGDEC_2_34, 1, RoundingMode.UNNECESSARY)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_negativeScale(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofScale_Currency_BigDecimal_int_JPY_RoundingMode_UP(self) -> None:

            test = BigMoney.ofScale1(JPY, BIGDEC_2_34, 0, RoundingMode.UP)
            self.assertEqual(self, JPY, test.getCurrencyUnit())
            self.assertEqual(self, BigDecimal.valueOf(3, 0), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_DOWN(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofScale_Currency_BigDecimal_nullBigDecimal(self) -> None:

            BigMoney.ofScale0(self.__GBP, None, 2)

    def test_factory_ofScale_Currency_BigDecimal_nullCurrency(self) -> None:

            BigMoney.ofScale0(None, self.__BIGDEC_2_34, 2)

    def test_factory_ofScale_Currency_BigDecimal_invalidScale(self) -> None:

            BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_345, 2)

    def test_factory_ofScale_Currency_BigDecimal_negativeScale(self) -> None:


        pass # LLM could not translate method body

    def test_factory_ofScale_Currency_BigDecimal_int(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_double_nullCurrency(self) -> None:

            BigMoney.of1(None, 2.345)

    def test_factory_of_Currency_double_big(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_double_medium(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_double_zero(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_double_trailingZero2(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_double_trailingZero1(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_double(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_subClass2(self) -> None:

            class BadInteger(unittest.TestCase, BigInteger):
                def __init__(self) -> None:
                    super().__init__("123")
            class BadDecimal(unittest.TestCase, BigDecimal):
                def __init__(self) -> None:
                    super().__init__(432)
                def unscaledValue(self) -> BigInteger:
                    return BadInteger()
                def scale(self) -> int:
                    return 1
            sub = BadDecimal()
            test = BigMoney.of0(GBP, sub)
            self.assertEqual(self, GBP, test.getCurrencyUnit())
            self.assertEqual(self, bd("12.3"), test.getAmount())
            self.assertEqual(self, 1, test.getScale())
            self.assertEqual(self, True, test.getAmount().__class__ == BigDecimal)

    def test_factory_of_Currency_subClass1(self) -> None:


        pass # LLM could not translate method body

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:

            BigMoney.of0(self.__GBP, None)

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:

            BigMoney.of0(None, self.__BIGDEC_2_345)

    def test_factory_of_Currency_BigDecimal(self) -> None:


        pass # LLM could not translate method body

    @staticmethod

    def __bd(str: str) -> decimal.Decimal:


        pass # LLM could not translate method body

    # Class Methods End


class new BigMoneyProvider(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toBigMoney(self) -> BigMoney:

            return None

    def toBigMoney(self) -> BigMoney:

        return GBP_1_23

    def toBigMoney(self) -> BigMoney:

            return None

    def toBigMoney(self) -> BigMoney:

            return None

    def toBigMoney(self) -> BigMoney:

            return GBP_1_23

    def toBigMoney(self) -> BigMoney:

            return None

    def toBigMoney(self) -> BigMoney:

            return None

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


class BadDecimal(unittest.TestCase, BigDecimal, BigDecimal):

    # Class Fields Begin
    __serialVersionUID: int = 1
    __serialVersionUID: int = 1
    # Class Fields End

    # Class Methods Begin
    def scale(self) -> int:

            return 1

    def unscaledValue(self) -> int:

            return None

    def scale(self) -> int:

            return 1

    def unscaledValue(self) -> int:

            return BadInteger()

    def __init__(self) -> None:


        pass # LLM could not translate method body

    def __init__(self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


class BadInteger(unittest.TestCase, BigInteger):

    # Class Fields Begin
    __serialVersionUID: int = 1
    # Class Fields End

    # Class Methods Begin
    def __init__(self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


