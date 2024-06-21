from __future__ import annotations
import io
import typing
from typing import *
import decimal
import os
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class TestBigMoney:

    __BAD_PROVIDER: BigMoneyProvider = BigMoneyProvider()

    __USD_2_35: BigMoney = BigMoney.parse("USD 2.35")

    __USD_2_34: BigMoney = BigMoney.parse("USD 2.34")

    __USD_1_23: BigMoney = BigMoney.parse("USD 1.23")

    __JPY_423: BigMoney = BigMoney.parse("JPY 423")

    __GBP_LONG_MIN_MAJOR_MINUS1: BigMoney = BigMoney.of0(
        GBP, decimal.Decimal(long.MIN_VALUE) - 1 * 100
    )

    __GBP_LONG_MAX_MAJOR_PLUS1: BigMoney = BigMoney.of0(
        GBP, decimal.Decimal(float(float(decimal.Decimal(Long.MAX_VALUE)) + 1) * 100)
    )

    __GBP_LONG_MIN_MINUS1: BigMoney = BigMoney.of0(
        GBP, decimal.Decimal(Long.MIN_VALUE) - decimal.Decimal(1)
    )

    __GBP_LONG_MAX_PLUS1: BigMoney = BigMoney.of0(
        GBP, decimal.Decimal(Long.MAX_VALUE) + decimal.Decimal(1)
    )

    __GBP_INT_MIN_MAJOR_MINUS1: BigMoney = BigMoney.ofMinor(
        CurrencyUnit.GBP, (((long(int.__MIN_VALUE__) - 1) * 100))
    )

    __GBP_INT_MAX_MAJOR_PLUS1: BigMoney = BigMoney.ofMinor(
        GBP, (((long(Integer.MAX_VALUE)) + 1) * 100)
    )

    __GBP_INT_MIN_MINUS1: BigMoney = BigMoney.ofMinor(
        CurrencyUnit.GBP, ((long(int.__MIN_VALUE__)) - 1)
    )

    __GBP_INT_MAX_PLUS1: BigMoney = BigMoney.ofMinor(
        CurrencyUnit.GBP, ((long)(integer.MAX_VALUE)) + 1
    )

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

    __JPY: CurrencyUnit = CurrencyUnit.of("JPY")

    __USD: CurrencyUnit = CurrencyUnit.of("USD")

    __EUR: CurrencyUnit = CurrencyUnit.of("EUR")

    __GBP: CurrencyUnit = CurrencyUnit.of("GBP")

    def test_toString_negative(self) -> None:

        test = BigMoney.of0(TestBigMoney.__EUR, TestBigMoney.__BIGDEC_M5_78)
        assert test.toString() == "EUR -5.78"

    def test_toString_positive(self) -> None:

        test = BigMoney.of0(TestBigMoney.__GBP, TestBigMoney.__BIGDEC_2_34)
        assert test.toString() == "GBP 2.34"

    def test_equals_false(self) -> None:

        a = self.__GBP_2_34
        assert not a.equals(None)
        assert not a.equals(object())

    def test_equals_hashCode_positive(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_34
        c = self.__GBP_2_35

        assert a.equals(a)
        assert b.equals(b)
        assert c.equals(c)

        assert a.equals(b)
        assert b.equals(a)
        assert a.hashCode() == b.hashCode()

        assert not a.equals(c)
        assert not b.equals(c)

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.isLessThanOrEqual(b)

    def test_isLessThanOrEqual(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36

        assert a.isLessThanOrEqual(a) == True
        assert a.isLessThanOrEqual(b) == True
        assert a.isLessThanOrEqual(c) == True

        assert b.isLessThanOrEqual(a) == False
        assert b.isLessThanOrEqual(b) == True
        assert b.isLessThanOrEqual(c) == True

        assert c.isLessThanOrEqual(a) == False
        assert c.isLessThanOrEqual(b) == False
        assert c.isLessThanOrEqual(c) == True

    def test_isLessThan_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.isLessThan(b)

    def test_isLessThan(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36

        assert not a.isLessThan(a)
        assert a.isLessThan(b)
        assert a.isLessThan(c)

        assert not b.isLessThan(a)
        assert not b.isLessThan(b)
        assert b.isLessThan(c)

        assert not c.isLessThan(a)
        assert not c.isLessThan(b)
        assert not c.isLessThan(c)

    def test_isGreaterThanOrEqual_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.isGreaterThanOrEqual(b)

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

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.isGreaterThan(b)

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

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.isEqual(b)

    def test_isEqual_Money(self) -> None:

        a = TestBigMoney.__GBP_2_34
        b = Money.ofMinor(TestBigMoney.__GBP, 234)
        assert a.isEqual(b)

    def test_isEqual(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36

        assert a.isEqual(a) == True
        assert b.isEqual(b) == True
        assert c.isEqual(c) == True

        assert a.isEqual(b) == False
        assert b.isEqual(a) == False

        assert a.isEqual(c) == False
        assert c.isEqual(a) == False

        assert b.isEqual(c) == False
        assert c.isEqual(b) == False

    def test_compareTo_wrongType(self) -> None:

        a: Comparable = self.__GBP_2_34
        try:
            a.compareTo("NotRightType")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    def test_compareTo_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35
        a.compareTo(b)

    def test_compareTo_Money(self) -> None:

        t = TestBigMoney.__GBP_2_35
        a = Money.ofMinor(TestBigMoney.__GBP, 234)
        b = Money.ofMinor(TestBigMoney.__GBP, 235)
        c = Money.ofMinor(TestBigMoney.__GBP, 236)

        assert t.compareTo(a) == 1
        assert t.compareTo(b) == 0
        assert t.compareTo(c) == -1

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

        # Assuming that GBP_2_34 is an instance of BigMoney
        # and isSameCurrency is a method of BigMoney
        self.__GBP_2_34.isSameCurrency(None)

    def test_isSameCurrency_Money_different(self) -> None:

        usd_money = Money.parse("USD 2")
        assert not self.__GBP_2_34.isSameCurrency(usd_money)

    def test_isSameCurrency_Money_same(self) -> None:

        # Assuming GBP_2_34 and GBP are defined somewhere else in the code
        # and they are instances of BigMoney and CurrencyUnit respectively
        # Also assuming that the parse method returns an instance of Money

        assert self.__GBP_2_34.isSameCurrency(Money.parse("GBP 2").getCurrencyUnit())

    def test_isSameCurrency_BigMoney_different(self) -> None:

        assert not self.__GBP_2_34.isSameCurrency(self.__USD_2_34)

    def test_isSameCurrency_BigMoney_same(self) -> None:

        assert self.__GBP_2_34.isSameCurrency(self.__GBP_2_35)

    def test_toMoney_RoundingMode_round(self) -> None:

        money = BigMoney.parse("GBP 2.355")
        self.assertEqual(
            Money.parse("GBP 2.36"), money.toMoney1(RoundingMode.HALF_EVEN)
        )

    def test_toMoney_RoundingMode(self) -> None:

        # Assuming that the placeholders are replaced with the actual values
        # and the RoundingMode is imported from decimal

        from decimal import RoundingMode

        assert Money.parse("GBP 2.34") == self.__GBP_2_34.toMoney1(
            RoundingMode.HALF_EVEN
        )

    def test_toMoney(self) -> None:

        self.assertEqual(
            Money.of0(self.__GBP, self.__BIGDEC_2_34), self.__GBP_2_34.toMoney0()
        )

    def test_toBigMoney(self) -> None:

        assert self.__GBP_2_34 is self.__GBP_2_34.toBigMoney()

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullRoundingMode(
        self,
    ) -> None:

        self.__GBP_5_78.convertRetainScale(self.__EUR, self.__bd("2"), None)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullBigDecimal(
        self,
    ) -> None:

        self.__GBP_5_78.convertRetainScale(self.__EUR, None, decimal.ROUND_DOWN)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullCurrency(
        self,
    ) -> None:

        pass  # LLM could not translate this method

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_sameCurrency(
        self,
    ) -> None:

        self.__GBP_2_33.convertRetainScale(
            self.__GBP, self.__bd("2.5"), decimal.ROUND_DOWN
        )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_negative(
        self,
    ) -> None:

        self.__GBP_2_33.convertRetainScale(
            self.__EUR, self.__bd("-2.5"), decimal.ROUND_DOWN
        )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_roundHalfUp(
        self,
    ) -> None:

        test = BigMoney.parse("GBP 2.21").convertRetainScale(
            self.__EUR, self.__bd("2.5"), decimal.ROUND_HALF_UP
        )
        assert test.toString() == "EUR 5.53"

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_positive(
        self,
    ) -> None:

        test = BigMoney.parse("GBP 2.2").convertRetainScale(
            self.__EUR, self.__bd("2.5"), decimal.ROUND_DOWN
        )
        assert test.toString() == "EUR 5.5"

    def test_convertedTo_CurrencyUnit_BigDecimal_nullBigDecimal(self) -> None:

        self.__GBP_5_78.convertedTo(self.__EUR, None)

    def test_convertedTo_CurrencyUnit_BigDecimal_nullCurrency(self) -> None:

        self.__GBP_5_78.convertedTo(None, self.__bd("2"))

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyWrongFactor(self) -> None:

        self.__GBP_2_33.convertedTo(self.__GBP, self.__bd("2.5"))

    def test_convertedTo_CurrencyUnit_BigDecimal_negative(self) -> None:

        self.__GBP_2_33.convertedTo(self.__EUR, self.__bd("-2.5"))

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyCorrectFactor(
        self,
    ) -> None:

        test = self.__GBP_2_33.convertedTo(self.__GBP, self.__bd("1.00000"))
        self.assertEqual(self.__GBP_2_33, test)

    def test_convertedTo_CurrencyUnit_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_33.convertedTo(self.__EUR, self.__bd("2.5"))
        assert test.toString() == "EUR 5.825"

    def test_round_3(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(3, RoundingMode.DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_round_M1up(self) -> None:

        test = BigMoney.parse("GBP 432.34").rounded(-1, RoundingMode.UP)
        assert test.toString() == "GBP 440.00"

    def test_round_M1down(self) -> None:

        test = BigMoney.parse("GBP 432.34").rounded(-1, RoundingMode.DOWN)
        assert test.toString() == "GBP 430.00"

    def test_round_0up(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(0, RoundingMode.UP)
        assert test.toString() == "GBP 3.00"

    def test_round_0down(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(0, RoundingMode.DOWN)
        assert test.toString() == "GBP 2.00"

    def test_round_1up(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(1, RoundingMode.UP)
        assert test.toString() == "GBP 2.40"

    def test_round_1down(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(1, RoundingMode.DOWN)
        assert test.toString() == "GBP 2.30"

    def test_round_2up(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_round_2down(self) -> None:

        test = TestBigMoney.__GBP_2_34.rounded(2, RoundingMode.DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_abs_negative(self) -> None:

        test = BigMoney.parse("GBP -2.34").abs()
        assert test.toString() == "GBP 2.34"

    def test_abs_positive(self) -> None:

        test = TestBigMoney.__GBP_2_34.abs()
        assert test == TestBigMoney.__GBP_2_34

    def test_negated_negative(self) -> None:

        test = BigMoney.parse("GBP -2.34").negated()
        assert test.toString() == "GBP 2.34"

    def test_negated_positive(self) -> None:

        test = TestBigMoney.__GBP_2_34.negated()
        assert test.toString() == "GBP -2.34"

    def test_negated_zero(self) -> None:

        test = TestBigMoney.__GBP_0_00.negated()
        assert test == TestBigMoney.__GBP_0_00

    def test_dividedBy_long_negative(self) -> None:

        test = self.__GBP_2_34.dividedBy2(-3, RoundingMode.DOWN)
        assert test.toString() == "GBP -0.78"

    def test_dividedBy_long_positive_roundUp(self) -> None:

        test = self.__GBP_2_35.dividedBy2(3, RoundingMode.UP)
        assert test.toString() == "GBP 0.79"

    def test_dividedBy_long_positive_roundDown(self) -> None:

        test = self.__GBP_2_35.dividedBy2(3, RoundingMode.DOWN)
        assert test.toString() == "GBP 0.78"

    def test_dividedBy_long_positive(self) -> None:

        test = self.__GBP_2_34.dividedBy2(3, RoundingMode.DOWN)
        assert test.toString() == "GBP 0.78"

    def test_dividedBy_long_one(self) -> None:

        test = TestBigMoney.__GBP_2_34.dividedBy2(1, RoundingMode.DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:

        # Calling the dividedBy1 method from BigMoney class
        # Since the RoundingMode is null in Java, we can pass None in Python
        self.__GBP_5_78.dividedBy1(2.5, None)

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.dividedBy1(-2.5, decimal.ROUND_FLOOR)
        assert test.toString() == "GBP -0.94"

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:

        test = self.__GBP_2_34.dividedBy1(2.5, decimal.ROUND_HALF_UP)
        assert test.toString() == "GBP 0.94"

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.dividedBy1(2.5, decimal.ROUND_DOWN)
        assert test.toString() == "GBP 0.93"

    def test_dividedBy_doubleRoundingMode_one(self) -> None:

        test = TestBigMoney.__GBP_2_34.dividedBy1(1.0, RoundingMode.DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        # The Python equivalent of Java's null is None
        self.__GBP_5_78.dividedBy0(self.__bd("2.5"), None)

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        # Calling the dividedBy0 method from BigMoney class
        self.__GBP_5_78.dividedBy0(None, decimal.ROUND_DOWN)

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.dividedBy0(self.__bd("-2.5"), decimal.ROUND_FLOOR)
        assert test.toString() == "GBP -0.94"

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        test = self.__GBP_2_34.dividedBy0(self.__bd("2.5"), RoundingMode.HALF_UP)
        assert test.toString() == "GBP 0.94"

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.dividedBy0(self.__bd("2.5"), decimal.ROUND_DOWN)
        assert test.toString() == "GBP 0.93"

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.dividedBy0(decimal.Decimal("1"), decimal.ROUND_DOWN)
        assert test == self.__GBP_2_34

    def test_multiplyRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_5_78.multiplyRetainScale1(2.5, None)

    def test_multiplyRetainScale_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale1(-2.5, decimal.ROUND_FLOOR)
        assert test.toString() == "GBP -5.83"

    def test_multiplyRetainScale_doubleRoundingMode_positive_halfUp(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale1(2.5, decimal.ROUND_HALF_UP)
        assert test.toString() == "GBP 5.83"

    def test_multiplyRetainScale_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale1(2.5, decimal.ROUND_DOWN)
        assert test.toString() == "GBP 5.82"

    def test_multiplyRetainScale_doubleRoundingMode_one(self) -> None:

        test = TestBigMoney.__GBP_2_34.multiplyRetainScale1(1.0, decimal.ROUND_DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        # The Python version of the Java code does not have a direct equivalent because the Java method is calling a method that takes a RoundingMode object, which is null in Java.
        # In Python, the decimal.Decimal class does not have a direct equivalent to the RoundingMode object in Java.
        # Therefore, we can't directly translate the Java code to Python.
        # If you want to use Python, you may need to find an alternative way to perform the operation without specifying a RoundingMode.

        # For example, you can use the default rounding mode of the decimal.Decimal class, which is ROUND_HALF_EVEN:
        TestBigMoney.__GBP_5_78.multiplyRetainScale0(TestBigMoney.__bd("2.5"))

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        self.__GBP_5_78.multiplyRetainScale0(None, decimal.ROUND_DOWN)

    def test_multiplyRetainScale_BigDecimalRoundingMode_negative(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("-2.5"), decimal.ROUND_FLOOR
        )
        assert test.toString() == "GBP -5.83"

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("2.5"), decimal.ROUND_HALF_UP
        )
        assert test.toString() == "GBP 5.83"

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("2.5"), decimal.ROUND_DOWN
        )
        assert test.toString() == "GBP 5.82"

    def test_multiplyRetainScale_BigDecimalRoundingMode_one(self) -> None:

        test = TestBigMoney.__GBP_2_34.multiplyRetainScale0(
            decimal.Decimal(1), decimal.ROUND_DOWN
        )
        assert test == TestBigMoney.__GBP_2_34

    def test_multipliedBy_long_negative(self) -> None:

        test = self.__GBP_2_34.multipliedBy2(-3)
        assert test.toString() == "GBP -7.02"
        assert test.getScale() == 2

    def test_multipliedBy_long_positive(self) -> None:

        test = self.__GBP_2_34.multipliedBy2(3)
        assert test.toString() == "GBP 7.02"
        assert test.getScale() == 2

    def test_multipliedBy_long_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy2(1)
        assert test == self.__GBP_2_34

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_33.multipliedBy1(-2.5)
        assert test.toString() == "GBP -5.825"
        assert test.getScale() == 3

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_33.multipliedBy1(2.5)
        assert test.toString() == "GBP 5.825"
        assert test.getScale() == 3

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy1(1.0)
        assert test == self.__GBP_2_34

    def test_multipliedBy_BigDecimal_nullBigDecimal(self) -> None:

        # Calling the method multipliedBy0 from BigMoney class
        self.__GBP_5_78.multipliedBy0(None)

    def test_multipliedBy_BigDecimal_negative(self) -> None:

        test = self.__GBP_2_33.multipliedBy0(self.__bd("-2.5"))
        assert test.toString() == "GBP -5.825"
        assert test.getScale() == 3

    def test_multipliedBy_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_33.multipliedBy0(self.__bd("2.5"))
        assert test.toString() == "GBP 5.825"
        assert test.getScale() == 3

    def test_multipliedBy_BigDecimal_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy0(decimal.Decimal(1))
        assert test == self.__GBP_2_34

    def test_minusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.minusRetainScale2(2.34, None)

    def test_minusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.minusRetainScale2(1.235, decimal.ROUND_DOWN)

    def test_minusRetainScale_doubleRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.minusRetainScale2(1.235, decimal.ROUND_DOWN)
        assert test.toString() == "GBP 1.10"

    def test_minusRetainScale_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.minusRetainScale2(-1.23, decimal.ROUND_UP)
        assert test.toString() == "GBP 3.57"

    def test_minusRetainScale_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.minusRetainScale2(1.23, decimal.ROUND_UP)
        assert test.toString() == "GBP 1.11"

    def test_minusRetainScale_doubleRoundingMode_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.minusRetainScale2(0.0, decimal.ROUND_DOWN)
        assert test == TestBigMoney.__GBP_2_34

    def test_minusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.minusRetainScale1(self.__BIGDEC_2_34, None)

    def test_minusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        self.__GBP_M5_78.minusRetainScale1(None, decimal.ROUND_UNNECESSARY)

    def test_minusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), decimal.ROUND_UNNECESSARY)

    def test_minusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), decimal.ROUND_DOWN)
        assert test.toString() == "GBP 1.10"

    def test_minusRetainScale_BigDecimalRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.minusRetainScale1(self.__bd("-1.23"), decimal.ROUND_DOWN)
        assert test.toString() == "GBP 3.57"

    def test_minusRetainScale_BigDecimalRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.minusRetainScale1(self.__bd("1.23"), decimal.ROUND_UP)
        assert test.toString() == "GBP 1.11"

    def test_minusRetainScale_BigDecimalRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.minusRetainScale1(decimal.Decimal(0), decimal.ROUND_DOWN)
        assert test == self.__GBP_2_34

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(
        self,
    ) -> None:

        self.__GBP_M5_78.minusRetainScale0(BigMoney.parse("GBP 123"), None)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullBigMoneyProvider(
        self,
    ) -> None:

        self.__GBP_M5_78.minusRetainScale0(None, decimal.ROUND_UNNECESSARY)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(
        self,
    ) -> None:

        self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY
        )

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.235"), RoundingMode.DOWN
        )
        assert test.toString() == "GBP 1.10"

    def test_minusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP -1.23"), RoundingMode.UNNECESSARY
        )
        assert test.toString() == "GBP 3.57"

    def test_minusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY
        )
        assert test.toString() == "GBP 1.11"

    def test_minusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.zero0(self.__GBP), RoundingMode.UNNECESSARY
        )
        assert test == self.__GBP_2_34

    def test_minusMinor_scale(self) -> None:

        test = BigMoney.parse("GBP 12").minusMinor(123)
        assert test.toString() == "GBP 10.77"
        assert test.getScale() == 2

    def test_minusMinor_negative(self) -> None:

        test = self.__GBP_2_34.minusMinor(-123)
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_minusMinor_positive(self) -> None:

        test = self.__GBP_2_34.minusMinor(123)
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_minusMinor_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.minusMinor(0)
        assert test == TestBigMoney.__GBP_2_34

    def test_minusMajor_negative(self) -> None:

        test = self.__GBP_2_34.minusMajor(-123)
        assert test.toString() == "GBP 125.34"
        assert test.getScale() == 2

    def test_minusMajor_positive(self) -> None:

        test = self.__GBP_2_34.minusMajor(123)
        assert test.toString() == "GBP -120.66"
        assert test.getScale() == 2

    def test_minusMajor_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.minusMajor(0)
        assert test == TestBigMoney.__GBP_2_34

    def test_minus_double_scale(self) -> None:

        test = self.__GBP_2_34.minus3(1.235)
        assert test.toString() == "GBP 1.105"
        assert test.getScale() == 3

    def test_minus_double_negative(self) -> None:

        test = self.__GBP_2_34.minus3(-1.23)
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_minus_double_positive(self) -> None:

        test = self.__GBP_2_34.minus3(1.23)
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_minus_double_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.minus3(0.0)
        assert test == TestBigMoney.__GBP_2_34

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:

        # Assuming that the BigMoney class has a method called minus2 that accepts a BigDecimal
        # and the BigDecimal is null in Java, we can pass None in Python
        self.__GBP_M5_78.minus2(None)

    def test_minus_BigDecimal_scale(self) -> None:

        test = self.__GBP_2_34.minus2(self.__bd("1.235"))
        assert test.toString() == "GBP 1.105"
        assert test.getScale() == 3

    def test_minus_BigDecimal_negative(self) -> None:

        test = self.__GBP_2_34.minus2(self.__bd("-1.23"))
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_minus_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_34.minus2(self.__bd("1.23"))
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_minus_BigDecimal_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.minus2(decimal.Decimal(0))
        assert test == TestBigMoney.__GBP_2_34

    def test_minus_BigMoneyProvider_badProvider(self) -> None:

        class AnonymousBigMoneyProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        self.__GBP_M5_78.minus1(AnonymousBigMoneyProvider())

    def test_minus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

        # Calling the minus1 method from BigMoney class
        self.__GBP_M5_78.minus1(None)

    def test_minus_BigMoneyProvider_currencyMismatch(self) -> None:

        try:
            self.__GBP_M5_78.minus1(self.__USD_1_23)
        except Exception as e:
            print(f"Caught exception: {e}")

    def test_minus_BigMoneyProvider_Money(self) -> None:

        test = self.__GBP_2_34.minus1(BigMoney.ofMinor(self.__GBP, 1))
        assert test.toString() == "GBP 2.33"
        assert test.getScale() == 2

    def test_minus_BigMoneyProvider_scale(self) -> None:

        test = TestBigMoney.__GBP_2_34.minus1(BigMoney.parse("GBP 1.111"))
        assert test.toString() == "GBP 1.229"
        assert test.getScale() == 3

    def test_minus_BigMoneyProvider_negative(self) -> None:

        test = self.__GBP_2_34.minus1(self.__GBP_M1_23)
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_minus_BigMoneyProvider_positive(self) -> None:

        test = self.__GBP_2_34.minus1(self.__GBP_1_23)
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_minus_BigMoneyProvider_zero(self) -> None:

        test = self.__GBP_2_34.minus1(self.__GBP_0_00)
        assert test == self.__GBP_2_34

    def test_minus_Iterable_badProvider(self) -> None:

        class BigMoneyProviderImpl(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        iterable: Iterable[BigMoneyProvider] = [BigMoneyProviderImpl()]
        self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_nullIterable(self) -> None:

        # Calling the BigMoney method minus0 with None as argument
        self.__GBP_M5_78.minus0(None)

    def test_minus_Iterable_nullEntry(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, None]
        self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_currencyMismatch(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, self.__JPY_423]
        self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_zero(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_0_00]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        assert test == self.__GBP_2_34

    def test_minus_Iterable_Mixed(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_Iterable_Money(self) -> None:

        iterable: Iterable[Money] = [
            self.__GBP_2_33.toMoney0(),
            self.__GBP_1_23.toMoney0(),
        ]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        assert test.toString() == "GBP -1.22"

    def test_minus_Iterable_BigMoney(self) -> None:

        iterable: Iterable[BigMoney] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        assert test.toString() == "GBP -1.22"

    def test_minus_Iterable_BigMoneyProvider(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.minus0(iterable)
        assert test.toString() == "GBP -1.22"

    def test_plusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.plusRetainScale2(2.34, None)

    def test_plusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.plusRetainScale2(1.235, decimal.ROUND_UP)

    def test_plusRetainScale_doubleRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.plusRetainScale2(1.235, decimal.ROUND_DOWN)
        assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.plusRetainScale2(
            decimal.Decimal("-1.23"), decimal.ROUND_UP
        )
        assert test.toString() == "GBP 1.11"

    def test_plusRetainScale_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.plusRetainScale2(1.23, decimal.ROUND_UP)
        assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_doubleRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.plusRetainScale2(0.0, decimal.ROUND_UNNECESSARY)
        assert test == self.__GBP_2_34

    def test_plusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        self.__GBP_M5_78.plusRetainScale1(self.__BIGDEC_2_34, None)

    def test_plusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:

        self.__GBP_M5_78.plusRetainScale1(None, decimal.ROUND_UNNECESSARY)

    def test_plusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        TestBigMoney.__GBP_2_34.plusRetainScale1(
            TestBigMoney.__bd("1.235"), decimal.ROUND_UNNECESSARY
        )

    def test_plusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:

        from decimal import Decimal, ROUND_DOWN
        from src.main.org.joda.money.BigMoney import BigMoney
        from src.main.org.joda.money.BigMoneyProvider import BigMoneyProvider
        from src.main.org.joda.money.CurrencyUnit import CurrencyUnit
        from src.main.org.joda.money.Money import Money

        test = TestBigMoney.__GBP_2_34.plusRetainScale1(
            TestBigMoney.__bd("1.235"), ROUND_DOWN
        )
        assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_BigDecimalRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.plusRetainScale1(self.__bd("-1.23"), decimal.ROUND_DOWN)
        assert test.toString() == "GBP 1.11"

    def test_plusRetainScale_BigDecimalRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.plusRetainScale1(self.__bd("1.23"), decimal.ROUND_UP)
        assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_BigDecimalRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.plusRetainScale1(decimal.Decimal(0), decimal.ROUND_DOWN)
        assert test == self.__GBP_2_34

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(
        self,
    ) -> None:

        # Calling BigMoney.parse("GBP 1.23")
        money = BigMoney.parse("GBP 1.23")

        # Calling GBP_M5_78.plusRetainScale0(money, None)
        self.__GBP_M5_78.plusRetainScale0(money, None)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullBigDecimal(self) -> None:

        self.__GBP_M5_78.plusRetainScale1(None, decimal.ROUND_UNNECESSARY)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(self) -> None:

        self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY
        )

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:

        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP 1.235"), RoundingMode.DOWN
        )
        assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:

        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP -1.23"), RoundingMode.UNNECESSARY
        )
        assert test.toString() == "GBP 1.11"

    def test_plusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:

        test = self.__GBP_2_34.plusRetainScale0(
            BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY
        )
        assert test.toString() == "GBP 3.57"

    def test_plusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:

        test = BigMoney.plusRetainScale0(
            BigMoney.zero0(self.__GBP), RoundingMode.UNNECESSARY
        )
        assert test == self.__GBP_2_34

    def test_plusMinor_scale(self) -> None:

        test = BigMoney.parse("GBP 12").plusMinor(123)
        assert test.toString() == "GBP 13.23"
        assert test.getScale() == 2

    def test_plusMinor_negative(self) -> None:

        test = self.__GBP_2_34.plusMinor(-123)
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_plusMinor_positive(self) -> None:

        test = self.__GBP_2_34.plusMinor(123)
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_plusMinor_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.plusMinor(0)
        assert test == TestBigMoney.__GBP_2_34

    def test_plusMajor_negative(self) -> None:

        test = self.__GBP_2_34.plusMajor(-123)
        assert test.toString() == "GBP -120.66"
        assert test.getScale() == 2

    def test_plusMajor_positive(self) -> None:

        test = self.__GBP_2_34.plusMajor(123)
        assert test.toString() == "GBP 125.34"
        assert test.getScale() == 2

    def test_plusMajor_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.plusMajor(0)
        assert test == TestBigMoney.__GBP_2_34

    def test_plus_double_scale(self) -> None:

        test = self.__GBP_2_34.plus3(1.234)
        assert test.toString() == "GBP 3.574"
        assert test.getScale() == 3

    def test_plus_double_negative(self) -> None:

        test = self.__GBP_2_34.plus3(-1.23)
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_plus_double_positive(self) -> None:

        test = self.__GBP_2_34.plus3(1.23)
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_plus_double_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.plus3(0.0)
        assert test == TestBigMoney.__GBP_2_34

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:

        # Assuming that the plus2 method takes a BigDecimal as an argument
        # and returns a BigMoney object
        # If the plus2 method is not defined in the BigMoney class, you will need to define it

        self.__GBP_M5_78.plus2(None)

    def test_plus_BigDecimal_scale(self) -> None:

        test = self.__GBP_2_34.plus2(self.__bd("1.235"))
        assert test.toString() == "GBP 3.575"
        assert test.getScale() == 3

    def test_plus_BigDecimal_negative(self) -> None:

        test = self.__GBP_2_34.plus2(self.__bd("-1.23"))
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_plus_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_34.plus2(self.__bd("1.23"))
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_plus_BigDecimal_zero(self) -> None:

        test = TestBigMoney.__GBP_2_34.plus2(decimal.Decimal(0))
        assert test == TestBigMoney.__GBP_2_34

    def test_plus_BigMoneyProvider_badProvider(self) -> None:

        class AnonymousBigMoneyProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        self.__GBP_M5_78.plus1(AnonymousBigMoneyProvider())

    def test_plus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

        # Calling the plus1 method from BigMoney class
        self.__GBP_M5_78.plus1(None)

    def test_plus_BigMoneyProvider_currencyMismatch(self) -> None:

        try:
            self.__GBP_M5_78.plus1(self.__USD_1_23)
        except Exception as e:
            print(f"Caught exception: {e}")

    def test_plus_BigMoneyProvider_Money(self) -> None:

        test = self.__GBP_2_34.plus1(BigMoney.ofMinor(self.__GBP, 1))
        assert test.toString() == "GBP 2.35"
        assert test.getScale() == 2

    def test_plus_BigMoneyProvider_scale(self) -> None:

        test = self.__GBP_2_34.plus1(BigMoney.parse("GBP 1.111"))
        assert test.toString() == "GBP 3.451"
        assert test.getScale() == 3

    def test_plus_BigMoneyProvider_negative(self) -> None:

        test = self.__GBP_2_34.plus1(self.__GBP_M1_23)
        assert test.toString() == "GBP 1.11"
        assert test.getScale() == 2

    def test_plus_BigMoneyProvider_positive(self) -> None:

        test: BigMoney = self.__GBP_2_34.plus1(self.__GBP_1_23)
        assert test.toString() == "GBP 3.57"
        assert test.getScale() == 2

    def test_plus_BigMoneyProvider_zero(self) -> None:

        test = self.__GBP_2_34.plus1(self.__GBP_0_00)
        assert test == self.__GBP_2_34

    def test_plus_Iterable_badProvider(self) -> None:

        class BigMoneyProviderImpl(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        iterable: Iterable[BigMoneyProvider] = [BigMoneyProviderImpl()]
        self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_nullIterable(self) -> None:

        # Calling BigMoney.plus0 method
        self.__GBP_M5_78.plus0(None)

    def test_plus_Iterable_nullEntry(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, None]
        self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_currencyMismatch(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, self.__JPY_423]
        self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_zero(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_0_00]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        assert test == self.__GBP_2_34

    def test_plus_Iterable_Mixed(self) -> None:

        class GBP_2_33:
            @staticmethod
            def toMoney0() -> BigMoney:
                return self.__GBP_2_33

        class GBP_1_23:
            @staticmethod
            def toBigMoney() -> BigMoney:
                return self.__GBP_1_23

        iterable = [GBP_2_33.toMoney0(), GBP_1_23()]
        test = self.__GBP_2_34.plus0(iterable)
        assert test.toString() == "GBP 5.90"

    def test_plus_Iterable_Money(self) -> None:

        iterable: Iterable[Money] = [
            self.__GBP_2_33.toMoney0(),
            self.__GBP_1_23.toMoney0(),
        ]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        assert test.toString() == "GBP 5.90"

    def test_plus_Iterable_BigMoney(self) -> None:

        iterable: Iterable[BigMoney] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        assert test.toString() == "GBP 5.90"

    def test_plus_Iterable_BigMoneyProvider(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__GBP_2_33, self.__GBP_1_23]
        test: BigMoney = self.__GBP_2_34.plus0(iterable)
        assert test.toString() == "GBP 5.90"

    def test_withAmount_double_same(self) -> None:

        test = TestBigMoney.__GBP_2_34.withAmount1(2.34)
        assert test == TestBigMoney.__GBP_2_34

    def test_withAmount_double(self) -> None:

        test = self.__GBP_2_34.withAmount1(2.345)
        assert self.__bd("2.345") == test.getAmount()
        assert 3 == test.getScale()

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:

        # Calling the method withAmount0 from BigMoney class
        self.__GBP_2_34.withAmount0(None)

    def test_withAmount_BigDecimal_same(self) -> None:

        test = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_34)
        assert test is self.__GBP_2_34

    def test_withAmount_BigDecimal(self) -> None:

        test = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_345)
        assert self.__bd("2.345") == test.getAmount()
        assert 3 == test.getScale()

    def test_isNegativeOrZero(self) -> None:

        assert self.__GBP_0_00.isNegativeOrZero() == True
        assert self.__GBP_2_34.isNegativeOrZero() == False
        assert self.__GBP_M5_78.isNegativeOrZero() == True

    def test_isNegative(self) -> None:

        assert not self.__GBP_0_00.isNegative()
        assert not self.__GBP_2_34.isNegative()
        assert self.__GBP_M5_78.isNegative()

    def test_isPositiveOrZero(self) -> None:

        assert self.__GBP_0_00.isPositiveOrZero() == True
        assert self.__GBP_2_34.isPositiveOrZero() == True
        assert self.__GBP_M5_78.isPositiveOrZero() == False

    def test_isPositive(self) -> None:

        assert not self.__GBP_0_00.isPositive()
        assert self.__GBP_2_34.isPositive()
        assert not self.__GBP_M5_78.isPositive()

    def test_isZero(self) -> None:

        assert self.__GBP_0_00.isZero() == True
        assert self.__GBP_2_34.isZero() == False
        assert self.__GBP_M5_78.isZero() == False

    def test_getMinorPart_negative(self) -> None:

        # Create a BigMoney instance with a negative minor part
        negative_minor_part = BigMoney.of(self.__GBP, -78)

        # Check if the minor part of the BigMoney instance is equal to -78
        assert negative_minor_part.getMinorPart() == -78

    def test_getMinorPart_positive(self) -> None:

        # Assuming GBP_2_34 is a BigMoney object and getMinorPart is a method in BigMoney class
        # Replace <placeholder> with the actual value or object creation
        self.assertEqual(34, self.__GBP_2_34.getMinorPart())

    def test_getAmountMinorInt_tooBigNegative(self) -> None:

        # Call the getAmountMinorInt method
        result = self.__GBP_INT_MIN_MINUS1.getAmountMinorInt()

    def test_getAmountMinorInt_tooBigPositive(self) -> None:

        try:
            self.__GBP_INT_MAX_PLUS1.getAmountMinorInt()
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_getAmountMinorInt_negative(self) -> None:

        # Call the method getAmountMinorInt from BigMoney class
        result = self.__GBP_M5_78.getAmountMinorInt()

        # Assert the result
        assert result == -578

    def test_getAmountMinorInt_positive(self) -> None:

        # Assuming that GBP_2_34 and GBP are defined somewhere else in the code
        # and they are instances of BigMoney and CurrencyUnit respectively.
        # If not, you need to define them or import them from somewhere.

        self.assertEqual(234, self.__GBP_2_34.getAmountMinorInt())

    def test_getAmountMinorLong_tooBigNegative(self) -> None:

        # Call the getAmountMinorLong method
        self.__GBP_LONG_MIN_MINUS1.getAmountMinorLong()

    def test_getAmountMinorLong_tooBigPositive(self) -> None:

        try:
            self.__GBP_LONG_MAX_PLUS1.getAmountMinorLong()
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_getAmountMinorLong_negative(self) -> None:

        # Call the method getAmountMinorLong from BigMoney class
        result = self.__GBP_M5_78.getAmountMinorLong()

        # Assert the result
        assert result == -578

    def test_getAmountMinorLong_positive(self) -> None:

        # Call the method getAmountMinorLong from BigMoney class
        result = self.__GBP_2_34.getAmountMinorLong()

        # Assert the result
        assert result == 234

    def test_getAmountMinor_negative(self) -> None:

        # Create a BigMoney object with a negative value
        negative_money = BigMoney.of(self.__GBP, -5.78)

        # Call the getAmountMinor method and compare the result
        self.assertEqual(negative_money.getAmountMinor(), decimal.Decimal(-578))

    def test_getAmountMinor_positive(self) -> None:

        # Create a BigMoney object with the value of 234 minor units of GBP
        test_money = BigMoney.of(self.__GBP, 234)

        # Check if the amount in minor units is equal to 234
        assert test_money.getAmountMinor() == decimal.Decimal(234)

    def test_getAmountMajorInt_tooBigNegative(self) -> None:

        # Call the getAmountMajorInt method
        self.__GBP_INT_MIN_MAJOR_MINUS1.getAmountMajorInt()

    def test_getAmountMajorInt_tooBigPositive(self) -> None:

        # Call the getAmountMajorInt method
        self.__GBP_INT_MAX_MAJOR_PLUS1.getAmountMajorInt()

    def test_getAmountMajorInt_negative(self) -> None:

        # Call the getAmountMajorInt method
        result = self.__GBP_M5_78.getAmountMajorInt()

        # Assert that the result is equal to -5
        assert result == -5

    def test_getAmountMajorInt_positive(self) -> None:

        # Call the method getAmountMajorInt from BigMoney class
        result = self.__GBP_2_34.getAmountMajorInt()

        # Assert the result
        self.assertEqual(2, result)

    def test_getAmountMajorLong_tooBigNegative(self) -> None:

        # Call the getAmountMajorLong method
        self.__GBP_LONG_MIN_MAJOR_MINUS1.getAmountMajorLong()

    def test_getAmountMajorLong_tooBigPositive(self) -> None:

        # Call the getAmountMajorLong method on GBP_LONG_MAX_MAJOR_PLUS1
        self.__GBP_LONG_MAX_MAJOR_PLUS1.getAmountMajorLong()

    def test_getAmountMajorLong_negative(self) -> None:

        # Call the method getAmountMajorLong from BigMoney class
        result = self.__GBP_M5_78.getAmountMajorLong()

        # Assert the result
        self.assertEqual(-5, result)

    def test_getAmountMajorLong_positive(self) -> None:

        # Call the method getAmountMajorLong from BigMoney class
        result = self.__GBP_2_34.getAmountMajorLong()

        # Assert the result
        self.assertEqual(2, result)

    def test_getAmountMajor_negative(self) -> None:

        # Create a BigMoney object with a negative value
        negative_money = BigMoney.of(self.__GBP, -5)

        # Call the getAmountMajor method and compare the result with the expected value
        assert negative_money.getAmountMajor() == decimal.Decimal(-5)

    def test_getAmountMajor_positive(self) -> None:

        # Call the getAmountMajor method
        result = self.__GBP_2_34.getAmountMajor()

        # Assert that the result is equal to BigDecimal.valueOf(2)
        assert result == decimal.Decimal(2)

    def test_getAmount_negative(self) -> None:

        assert self.__BIGDEC_M5_78 == self.__GBP_M5_78.getAmount()

    def test_getAmount_positive(self) -> None:

        assert self.__BIGDEC_2_34 == self.__GBP_2_34.getAmount()

    def test_withCurrencyScale_intRoundingMode_lessJPY(self) -> None:

        test = BigMoney.parse("JPY 2.345").withCurrencyScale1(RoundingMode.UP)
        assert self.__bd("3") == test.getAmount()
        assert 0 == test.getScale()

    def test_withCurrencyScale_intRoundingMode_more(self) -> None:

        test = BigMoney.parse("GBP 2.3").withCurrencyScale1(RoundingMode.UP)
        assert self.__bd("2.30") == test.getAmount()
        assert 2 == test.getScale()

    def test_withCurrencyScale_intRoundingMode_less(self) -> None:

        test = BigMoney.parse("GBP 2.345").withCurrencyScale1(RoundingMode.UP)
        assert self.__bd("2.35") == test.getAmount()
        assert 2 == test.getScale()

    def test_withCurrencyScale_int_less(self) -> None:

        # Assuming that BigMoney.parse() returns a BigMoney object
        money = BigMoney.parse("GBP 2.345")
        money.withCurrencyScale0()

    def test_withCurrencyScale_int_more(self) -> None:

        test = BigMoney.parse("GBP 2.3").withCurrencyScale0()
        assert self.__bd("2.30") == test.getAmount()
        assert 2 == test.getScale()

    def test_withCurrencyScale_int_same(self) -> None:

        test = TestBigMoney.__GBP_2_34.withCurrencyScale0()
        assert test == TestBigMoney.__GBP_2_34

    def test_withScale_intRoundingMode_more(self) -> None:

        test = TestBigMoney.__GBP_2_34.withScale1(3, RoundingMode.UP)
        assert TestBigMoney.__bd("2.340") == test.getAmount()
        assert 3 == test.getScale()

    def test_withScale_intRoundingMode_less(self) -> None:

        test = self.__GBP_2_34.withScale1(1, RoundingMode.UP)
        assert self.__bd("2.4") == test.getAmount()
        assert 1 == test.getScale()

    def test_withScale_int_less(self) -> None:

        BigMoney.parse("GBP 2.345").withScale0(2)

    def test_withScale_int_more(self) -> None:

        test = TestBigMoney.__GBP_2_34.withScale0(3)
        assert TestBigMoney.__bd("2.340") == test.getAmount()
        assert 3 == test.getScale()

    def test_withScale_int_same(self) -> None:

        test = TestBigMoney.__GBP_2_34.withScale0(2)
        assert test == TestBigMoney.__GBP_2_34

    def test_isCurrencyScale_JPY(self) -> None:

        assert BigMoney.parse("JPY 2").isCurrencyScale() == True
        assert BigMoney.parse("JPY 2.3").isCurrencyScale() == False
        assert BigMoney.parse("JPY 2.34").isCurrencyScale() == False
        assert BigMoney.parse("JPY 2.345").isCurrencyScale() == False

    def test_isCurrencyScale_GBP(self) -> None:

        assert BigMoney.parse("GBP 2").isCurrencyScale() == False
        assert BigMoney.parse("GBP 2.3").isCurrencyScale() == False
        assert BigMoney.parse("GBP 2.34").isCurrencyScale() == True
        assert BigMoney.parse("GBP 2.345").isCurrencyScale() == False

    def test_getScale_JPY(self) -> None:

        # Call the getScale method from BigMoney class
        scale = self.__JPY_423.getScale()

        # Assert that the scale is 0
        assert scale == 0

    def test_getScale_GBP(self) -> None:

        # Call the getScale method from BigMoney class
        scale = self.__GBP_2_34.getScale()

        # Assert that the scale is equal to 2
        assert scale == 2

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:

        # Call the withCurrencyUnit method with None as argument
        self.__GBP_2_34.withCurrencyUnit(None)

    def test_withCurrencyUnit_Currency_differentCurrencyScale(self) -> None:

        test = self.__GBP_2_34.withCurrencyUnit(self.__JPY)
        assert test.toString() == "JPY 2.34"

    def test_withCurrencyUnit_Currency_same(self) -> None:

        test = TestBigMoney.__GBP_2_34.withCurrencyUnit(TestBigMoney.__GBP)
        assert test is TestBigMoney.__GBP_2_34

    def test_withCurrencyUnit_Currency(self) -> None:

        test = self.__GBP_2_34.withCurrencyUnit(self.__USD)
        assert test.toString() == "USD 2.34"

    def test_getCurrencyUnit_EUR(self) -> None:

        # Assuming that BigMoney.parse() returns a BigMoney object
        # and BigMoney.getCurrencyUnit() returns a CurrencyUnit object
        # and EUR is a CurrencyUnit object

        self.assertEqual(self.__EUR, BigMoney.parse("EUR -5.78").getCurrencyUnit())

    def test_getCurrencyUnit_GBP(self) -> None:

        # Call the method getCurrencyUnit() from BigMoney class
        result = self.__GBP_2_34.getCurrencyUnit()

        # Assert that the result is equal to GBP
        assert result == self.__GBP

    def test_scaleNormalization3(self) -> None:

        a = BigMoney.of0(self.__GBP, decimal.Decimal("100"))
        b = BigMoney.of0(self.__GBP, decimal.Decimal("1E+2"))

        assert a.toString() == "GBP 100"
        assert b.toString() == "GBP 100"
        assert a.equals(a)
        assert b.equals(b)
        assert a.equals(b)
        assert b.equals(a)
        assert a.hashCode() == b.hashCode()

    def test_scaleNormalization2(self) -> None:

        a = BigMoney.ofScale2(TestBigMoney.__GBP, 1, 1)
        b = BigMoney.ofScale2(TestBigMoney.__GBP, 10, 2)

        assert a.toString() == "GBP 0.1"
        assert b.toString() == "GBP 0.10"
        assert a.equals(a)
        assert b.equals(b)
        assert not a.equals(b)
        assert not b.equals(a)
        assert a.hashCode() != b.hashCode()

    def test_scaleNormalization1(self) -> None:

        a = BigMoney.ofScale2(TestBigMoney.__GBP, 100, 0)
        b = BigMoney.ofScale2(TestBigMoney.__GBP, 1, -2)

        assert a.toString() == "GBP 100"
        assert b.toString() == "GBP 100"
        assert a.equals(a)
        assert b.equals(b)
        assert a.equals(b)
        assert b.equals(a)
        assert a.hashCode() == b.hashCode()

    def test_constructor_null2(self) -> None:

        try:
            BigMoney(0, None, TestBigMoney.__GBP)
            self.fail()
        except AssertionError as ex:
            self.assertEqual(AssertionError, type(ex))

    def test_constructor_null1(self) -> None:

        # Get the constructor of BigMoney class
        con = BigMoney.__init__

        # Check if the constructor is public
        assert inspect.isfunction(con)
        assert inspect.ismethod(con)
        assert not inspect.isabstract(con)

        # Check if the constructor is protected
        assert not inspect.isprivate(con)

        # Try to create an instance of BigMoney with null currency
        try:
            con(0, self.__BIGDEC_2_34, None)
            assert False
        except AssertionError:
            pass

    def test_factory_parse_String_nullString(self) -> None:

        BigMoney.parse(None)

    def test_factory_parse_String_badCurrency(self) -> None:

        try:
            BigMoney.parse("GBX 2.34")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_factory_parse_String_exponent(self) -> None:

        BigMoney.parse("GBP 234E2")

    def test_factory_parse_String_tooShort(self) -> None:

        # Calling BigMoney.parse("GBP")
        BigMoney.parse("GBP")

    def test_factory_parse(
        self, str: str, currency: CurrencyUnit, amountStr: str, scale: int
    ) -> None:

        test = BigMoney.parse(str)
        assert currency == test.getCurrencyUnit()
        assert self.__bd(amountStr) == test.getAmount()
        assert scale == test.getScale()

    @staticmethod
    def __bd(str: str) -> decimal.Decimal:
        return decimal.Decimal(str)

    @staticmethod
    def data_parse() -> typing.List[typing.List[typing.Any]]:

        GBP = TestBigMoney.__GBP

        return [
            ["GBP 2.43", GBP, "2.43", 2],
            ["GBP +12.57", GBP, "12.57", 2],
            ["GBP -5.87", GBP, "-5.87", 2],
            ["GBP 0.99", GBP, "0.99", 2],
            ["GBP .99", GBP, "0.99", 2],
            ["GBP +.99", GBP, "0.99", 2],
            ["GBP +0.99", GBP, "0.99", 2],
            ["GBP -.99", GBP, "-0.99", 2],
            ["GBP -0.99", GBP, "-0.99", 2],
            ["GBP 0", GBP, "0", 0],
            ["GBP 2", GBP, "2", 0],
            ["GBP 123.", GBP, "123", 0],
            ["GBP3", GBP, "3", 0],
            ["GBP3.10", GBP, "3.10", 2],
            ["GBP  3.10", GBP, "3.10", 2],
            ["GBP   3.10", GBP, "3.10", 2],
            ["GBP                           3.10", GBP, "3.10", 2],
            ["GBP 123.456789", GBP, "123.456789", 6],
        ]

    def test_factory_total_CurrencyUnitIterable_badProvider(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__BAD_PROVIDER]
        BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:

        iterable: Iterable[BigMoney] = [self.__GBP_2_33, None, self.__GBP_2_36]
        BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:

        iterable: Iterable[BigMoney] = [None, self.__GBP_2_33, self.__GBP_2_36]
        BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(
        self,
    ) -> None:

        iterable: Iterable[BigMoney] = [self.__GBP_2_33, self.__JPY_423]
        BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:

        iterable: Iterable[BigMoney] = [self.__JPY_423]
        BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:

        iterable: Iterable[BigMoney] = []
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        assert self.__GBP == test.getCurrencyUnit()
        assert 0 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitIterable_Mixed(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33,
        ]
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(3.56) == test.getAmount()

    def test_factory_total_CurrencyUnitIterable(self) -> None:

        iterable: Iterable[BigMoney] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            BigMoney.of1(self.__GBP, 2.361),
        ]
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(5921) / decimal.Decimal(10**3) == test.getAmount()

    def test_factory_total_CurrencyUnitArray_badProvider(self) -> None:

        array: List[BigMoneyProvider] = [self.__BAD_PROVIDER]
        BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_badProvider(self) -> None:

        BigMoney.total2(self.__GBP, self.__BAD_PROVIDER)

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:

        array = [self.__GBP_2_33, None, self.__GBP_2_36]
        BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:

        BigMoney.total2(self.__GBP, self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:

        array: List[BigMoney] = [None, self.__GBP_2_33, self.__GBP_2_36]
        BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:

        BigMoney.total2(self.__GBP, None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:

        array = [self.__GBP_2_33, self.__JPY_423]
        BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:

        BigMoney.total2(self.__GBP, self.__GBP_2_33, self.__JPY_423)

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:

        array = [self.__JPY_423]
        BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:

        BigMoney.total2(self.__GBP, self.__JPY_423)

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:

        array: List[BigMoney] = []
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 0 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:

        test = BigMoney.total2(self.__GBP)
        assert self.__GBP == test.getCurrencyUnit()
        assert 0 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitArray_3Money(self) -> None:

        array = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36.toMoney0(),
        ]
        test = BigMoney.total2(self.__GBP, array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitArray_3Mixed(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        test = BigMoney.total2(self.__GBP, array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitVarargs_3Mixed(self) -> None:

        test = BigMoney.total2(
            self.__GBP, self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36
        )
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitArray_3(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
        test = BigMoney.total2(self.__GBP, array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:

        test = BigMoney.total2(
            self.__GBP, self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36
        )
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitArray_1(self) -> None:

        array: List[BigMoney] = [self.__GBP_1_23]
        test: BigMoney = BigMoney.total2(self.__GBP, array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 123 == test.getAmountMinorInt()

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:

        test = BigMoney.total2(self.__GBP, self.__GBP_1_23)
        assert self.__GBP == test.getCurrencyUnit()
        assert 123 == test.getAmountMinorInt()

    def test_factory_total_Iterable_badProvider(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [self.__BAD_PROVIDER]
        BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullNotFirst(self) -> None:

        iterable: Iterable[BigMoney] = [self.__GBP_2_33, None, self.__GBP_2_36]
        BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullFirst(self) -> None:

        iterable: Iterable[BigMoney] = [None, self.__GBP_2_33, self.__GBP_2_36]
        BigMoney.total1(iterable)

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:

        iterable: Iterable[BigMoney] = [self.__GBP_2_33, self.__JPY_423]
        BigMoney.total1(iterable)

    def test_factory_total_Iterable_empty(self) -> None:

        iterable: Iterable[BigMoney] = Collections.emptyList()
        BigMoney.total1(iterable)

    def test_factory_total_Iterable_Mixed(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33,
        ]
        test: BigMoney = BigMoney.total1(iterable)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(356, 2) == test.getAmount()

    def test_factory_total_Iterable(self) -> None:

        iterable: Iterable[BigMoney] = [
            self.__GBP_1_23,
            self.__GBP_2_33,
            BigMoney.of1(self.__GBP, 2.361),
        ]
        test: BigMoney = BigMoney.total1(iterable)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(5921) / decimal.Decimal(10**3) == test.getAmount()

    def test_factory_total_array_badProvider(self) -> None:

        array: List[BigMoneyProvider] = [self.__BAD_PROVIDER]
        BigMoney.total0(array)

    def test_factory_total_varargs_badProvider(self) -> None:

        BigMoney.total0(self.__BAD_PROVIDER)

    def test_factory_total_array_nullNotFirst(self) -> None:

        array: List[BigMoneyProvider] = [self.__GBP_2_33, None, self.__GBP_2_36]
        BigMoney.total0(array)

    def test_factory_total_varargs_nullNotFirst(self) -> None:

        BigMoney.total0(self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_array_nullFirst(self) -> None:

        array: List[BigMoneyProvider] = [None, self.__GBP_2_33, self.__GBP_2_36]
        BigMoney.total0(array)

    def test_factory_total_varargs_nullFirst(self) -> None:

        BigMoney.total0(None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_array_currenciesDiffer(self) -> None:

        array = [self.__GBP_2_33, self.__JPY_423]
        BigMoney.total0(array)

    def test_factory_total_varargs_currenciesDiffer(self) -> None:

        BigMoney.total0(self.__GBP_2_33, self.__JPY_423)

    def test_factory_total_array_empty(self) -> None:

        array: List[BigMoneyProvider] = []
        BigMoney.total0(array)

    def test_factory_total_varargs_empty(self) -> None:

        BigMoney.total0()

    def test_factory_total_array_3Money(self) -> None:

        array = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36.toMoney0(),
        ]
        test = BigMoney.total0(array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_array_3Mixed(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        test = BigMoney.total0(array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_varargs_3Mixed(self) -> None:

        test = BigMoney.total0(
            self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36
        )
        assert self.__GBP == test.getCurrencyUnit()
        assert 592 == test.getAmountMinorInt()

    def test_factory_total_array_1BigMoney(self) -> None:

        array: List[BigMoneyProvider] = [self.__GBP_1_23]
        test: BigMoney = BigMoney.total0(array)
        assert self.__GBP == test.getCurrencyUnit()
        assert 123 == test.getAmountMinorInt()

    def test_factory_total_varargs_1BigMoney(self) -> None:

        test = BigMoney.total0(self.__GBP_1_23)
        assert self.__GBP == test.getCurrencyUnit()
        assert 123 == test.getAmountMinorInt()

    def test_factory_from_BigMoneyProvider_badProvider(self) -> None:

        BigMoney.of2(self.__BAD_PROVIDER)

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:

        BigMoney.of2(None)

    def test_factory_from_BigMoneyProvider(self) -> None:

        test = BigMoney.of2(BigMoney.parse("GBP 104.23"))
        assert TestBigMoney.__GBP == test.getCurrencyUnit()
        assert 10423 == test.getAmountMinorInt()
        assert 2 == test.getScale()

    def test_factory_zero_Currency_int_nullCurrency(self) -> None:

        BigMoney.zero1(None, 3)

    def test_factory_zero_Currency_int_negativeScale(self) -> None:

        test = BigMoney.zero1(self.__GBP, -3)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(0) == test.getAmount()

    def test_factory_zero_Currency_int(self) -> None:

        test = BigMoney.zero1(self.__GBP, 3)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(0) == test.getAmount()

    def test_factory_zero_Currency_nullCurrency(self) -> None:

        BigMoney.zero0(None)

    def test_factory_zero_Currency(self) -> None:

        test = BigMoney.zero0(self.__GBP)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(0) == test.getAmount()
        assert 0 == test.getScale()

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:

        BigMoney.ofMinor(None, 234)

    def test_factory_ofMinor_Currency_long(self) -> None:

        test = BigMoney.ofMinor(TestBigMoney.__GBP, 234)
        assert TestBigMoney.__GBP == test.getCurrencyUnit()
        assert self.__bd("2.34") == test.getAmount()
        assert 2 == test.getScale()

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:

        BigMoney.ofMajor(None, 234)

    def test_factory_ofMajor_Currency_long(self) -> None:

        test = BigMoney.ofMajor(TestBigMoney.__GBP, 234)
        assert TestBigMoney.__GBP == test.getCurrencyUnit()
        assert self.__bd("234") == test.getAmount()
        assert 0 == test.getScale()

    def test_factory_ofScale_Currency_long_int_nullCurrency(self) -> None:

        BigMoney.ofScale2(None, 234, 2)

    def test_factory_ofScale_Currency_long_int_negativeScale(self) -> None:

        test = BigMoney.ofScale2(self.__GBP, 234, -4)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(2340000) == test.getAmount()

    def test_factory_ofScale_Currency_long_int(self) -> None:

        test = BigMoney.ofScale2(self.__GBP, 234, 4)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(234) / 10**4 == test.getAmount()

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullRoundingMode(
        self,
    ) -> None:

        BigMoney.ofScale1(self.__GBP, self.__BIGDEC_2_34, 2, None)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullBigDecimal(
        self,
    ) -> None:

        BigMoney.ofScale1(self.__GBP, None, 2, decimal.ROUND_DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullCurrency(
        self,
    ) -> None:

        BigMoney.ofScale1(None, self.__BIGDEC_2_34, 2, decimal.ROUND_DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_UNNECESSARY(
        self,
    ) -> None:

        BigMoney.ofScale1(self.__JPY, self.__BIGDEC_2_34, 1, decimal.ROUND_DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_negativeScale(
        self,
    ) -> None:

        test = BigMoney.ofScale1(
            TestBigMoney.__GBP, decimal.Decimal(23400), -2, decimal.ROUND_DOWN
        )
        assert TestBigMoney.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(23400) == test.getAmount()

    def test_factory_ofScale_Currency_BigDecimal_int_JPY_RoundingMode_UP(self) -> None:

        test = BigMoney.ofScale1(self.__JPY, self.__BIGDEC_2_34, 0, RoundingMode.UP)
        assert self.__JPY == test.getCurrencyUnit()
        assert decimal.Decimal(3, 0) == test.getAmount()

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_DOWN(self) -> None:

        test = BigMoney.ofScale1(self.__GBP, self.__BIGDEC_2_34, 1, RoundingMode.DOWN)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(23) == test.getAmount()

    def test_factory_ofScale_Currency_BigDecimal_nullBigDecimal(self) -> None:

        BigMoney.ofScale0(self.__GBP, None, 2)

    def test_factory_ofScale_Currency_BigDecimal_nullCurrency(self) -> None:

        BigMoney.ofScale0(None, self.__BIGDEC_2_34, 2)

    def test_factory_ofScale_Currency_BigDecimal_invalidScale(self) -> None:

        BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_345, 2)

    def test_factory_ofScale_Currency_BigDecimal_negativeScale(self) -> None:

        test = BigMoney.ofScale0(TestBigMoney.__GBP, decimal.Decimal(23400), -2)
        assert TestBigMoney.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(23400) == test.getAmount()

    def test_factory_ofScale_Currency_BigDecimal_int(self) -> None:

        test = BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_34, 4)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(23400) / decimal.Decimal(10000) == test.getAmount()

    def test_factory_of_Currency_double_nullCurrency(self) -> None:

        BigMoney.of1(None, 2.345)

    def test_factory_of_Currency_double_big(self) -> None:

        test = BigMoney.of1(self.__GBP, 200000000.0)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(200000000) == test.getAmount()
        assert 0 == test.getScale()

    def test_factory_of_Currency_double_medium(self) -> None:

        test = BigMoney.of1(self.__GBP, 2000.0)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(2000) == test.getAmount()
        assert 0 == test.getScale()

    def test_factory_of_Currency_double_zero(self) -> None:

        assert BigMoney.of0(self.__GBP, decimal.Decimal(0)) == BigMoney.of1(
            self.__GBP, 0.0
        )
        assert BigMoney.of0(self.__GBP, decimal.Decimal(-0)) == BigMoney.of1(
            self.__GBP, 0.0
        )
        assert BigMoney.of0(self.__GBP, decimal.Decimal(0.0)) == BigMoney.of1(
            self.__GBP, 0.0
        )
        assert BigMoney.of0(self.__GBP, decimal.Decimal(0.00)) == BigMoney.of1(
            self.__GBP, 0.0
        )
        assert BigMoney.of0(self.__GBP, decimal.Decimal(-0.0)) == BigMoney.of1(
            self.__GBP, 0.0
        )

    def test_factory_of_Currency_double_trailingZero2(self) -> None:

        test = BigMoney.of1(self.__GBP, 1.20)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(12) == test.getAmount()
        assert 1 == test.getScale()

    def test_factory_of_Currency_double_trailingZero1(self) -> None:

        test = BigMoney.of1(self.__GBP, 1.230)
        assert self.__GBP == test.getCurrencyUnit()
        assert decimal.Decimal(123) == test.getAmount()
        assert 2 == test.getScale()

    def test_factory_of_Currency_double(self) -> None:

        test = BigMoney.of1(self.__GBP, 2.345)
        assert self.__GBP == test.getCurrencyUnit()
        assert self.__BIGDEC_2_345 == test.getAmount()
        assert 3 == test.getScale()

    def test_factory_of_Currency_subClass2(self) -> None:

        class BadInteger(BigInteger):
            serialVersionUID = 1

            def __init__(self):
                super().__init__("123")

        class BadDecimal(BigDecimal):
            serialVersionUID = 1

            def __init__(self):
                super().__init__(432)

            def unscaledValue(self) -> BigInteger:
                return BadInteger()

            def scale(self) -> int:
                return 1

        sub = BadDecimal()
        test = BigMoney.of0(self.__GBP, sub)
        assert self.__GBP == test.getCurrencyUnit()
        assert self.__bd("12.3") == test.getAmount()
        assert 1 == test.getScale()
        assert True == (test.getAmount().__class__ == decimal.Decimal)

    def test_factory_of_Currency_subClass1(self) -> None:

        class BadDecimal(decimal.Decimal):
            def __init__(self):
                super().__init__(432)

            def unscaledValue(self) -> typing.Optional[int]:
                return None

            def scale(self) -> int:
                return 1

        sub = BadDecimal()
        BigMoney.of0(self.__GBP, sub)

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:

        BigMoney.of0(self.__GBP, None)

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:

        BigMoney.of0(None, self.__BIGDEC_2_345)

    def test_factory_of_Currency_BigDecimal(self) -> None:

        test = BigMoney.of0(self.__GBP, self.__BIGDEC_2_345)
        assert self.__GBP == test.getCurrencyUnit()
        assert self.__BIGDEC_2_345 == test.getAmount()
        assert 3 == test.getScale()

    @staticmethod
    def __bd(str: str) -> decimal.Decimal:

        return decimal.Decimal(str)
