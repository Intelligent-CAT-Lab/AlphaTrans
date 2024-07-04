from __future__ import annotations
import inspect
import re
import enum
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

    __GBP: CurrencyUnit = CurrencyUnit.of("GBP")
    __GBP_M1_23: BigMoney = BigMoney.parse("GBP -1.23")
    __GBP_1_23: BigMoney = BigMoney.parse("GBP 1.23")
    __GBP_0_00: BigMoney = BigMoney.parse("GBP 0.00")
    __BIGDEC_M5_78: decimal.Decimal = decimal.Decimal("-5.78")
    __BIGDEC_2_345: decimal.Decimal = decimal.Decimal("2.345")
    __BIGDEC_2_34: decimal.Decimal = decimal.Decimal("2.34")
    __JPY: CurrencyUnit = CurrencyUnit.of("JPY")
    __EUR: CurrencyUnit = CurrencyUnit.of("EUR")
    __BAD_PROVIDER: BigMoneyProvider = BigMoneyProvider()
    __USD: CurrencyUnit = CurrencyUnit.of("USD")
    __JPY_423: BigMoney = BigMoney.parse("JPY 423")
    __GBP_LONG_MIN_MAJOR_MINUS1: BigMoney = BigMoney.of(
        CurrencyUnit.of("GBP"), decimal.Decimal(float(long.MIN_VALUE - 1) * 100)
    )
    __GBP_LONG_MAX_MAJOR_PLUS1: BigMoney = BigMoney.of(
        CurrencyUnit.of("GBP"),
        (decimal.Decimal(Long.MAX_VALUE) + decimal.Decimal(1)) * decimal.Decimal(100),
    )
    __GBP_LONG_MIN_MINUS1: BigMoney = BigMoney.of(
        CurrencyUnit.of("GBP"), decimal.Decimal(Long.MIN_VALUE) - decimal.Decimal(1)
    )
    __GBP_LONG_MAX_PLUS1: BigMoney = BigMoney.of(
        GBP, decimal.Decimal(Long.MAX_VALUE) + decimal.Decimal(1)
    )
    __GBP_INT_MIN_MAJOR_MINUS1: BigMoney = BigMoney.ofMinor(
        CurrencyUnit.of("GBP"), (((-(2**31)) - 1) * 100)
    )
    __GBP_INT_MAX_MAJOR_PLUS1: BigMoney = None

    @staticmethod
    def initialize_fields() -> None:
        TestBigMoney.__GBP_INT_MAX_MAJOR_PLUS1: BigMoney = BigMoney.ofMinor(
            TestBigMoney.__GBP, (((long(int.MAX_VALUE)) + 1) * 100)
        )

    def test_toString_negative(self) -> None:

        test = BigMoney.of0(self.__EUR, self.__BIGDEC_M5_78)
        self.assertEqual("EUR -5.78", test.toString())

    def test_toString_positive(self) -> None:

        test = BigMoney.of0(self.__GBP, self.__BIGDEC_2_34)
        self.assertEqual("GBP 2.34", test.toString())

    def test_equals_false(self) -> None:

        a = self.__GBP_2_34
        self.assertEqual(False, a.equals(None))
        self.assertEqual(False, a.equals(object()))

    def test_equals_hashCode_positive(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_34
        c = self.__GBP_2_35

        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, c.equals(c))

        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

        self.assertEqual(False, a.equals(c))
        self.assertEqual(False, b.equals(c))

    def test_isLessThanOrEqual_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35

        with pytest.raises(CurrencyMismatchException):
            a.isLessThanOrEqual(b)

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

        a = self.__GBP_2_34
        b = self.__USD_2_35

        with pytest.raises(CurrencyMismatchException):
            a.isLessThan(b)

    def test_isLessThan(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36

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

        a = self.__GBP_2_34
        b = self.__USD_2_35

        with pytest.raises(CurrencyMismatchException):
            a.isGreaterThanOrEqual(b)

    def test_isGreaterThanOrEqual(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36

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

        a = self.__GBP_2_34
        b = self.__USD_2_35

        with pytest.raises(CurrencyMismatchException):
            a.isGreaterThan(b)

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

        a = self.__GBP_2_34
        b = self.__USD_2_35
        with pytest.raises(CurrencyMismatchException):
            a.isEqual(b)

    def test_isEqual_Money(self) -> None:

        a = self.__GBP_2_34
        b = Money.ofMinor(self.__GBP, 234)
        self.assertEqual(True, a.isEqual(b))

    def test_isEqual(self) -> None:

        a = self.__GBP_2_34
        b = self.__GBP_2_35
        c = self.__GBP_2_36

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
        with pytest.raises(TypeError):
            a.compareTo("NotRightType")

    def test_compareTo_currenciesDiffer(self) -> None:

        a = self.__GBP_2_34
        b = self.__USD_2_35

        with pytest.raises(CurrencyMismatchException):
            a.compareTo(b)

    def test_compareTo_Money(self) -> None:

        t = self.__GBP_2_35
        a = Money.ofMinor(self.__GBP, 234)
        b = Money.ofMinor(self.__GBP, 235)
        c = Money.ofMinor(self.__GBP, 236)

        self.assertEqual(1, t.compareTo(a))
        self.assertEqual(0, t.compareTo(b))
        self.assertEqual(-1, t.compareTo(c))

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
        with pytest.raises(TypeError):
            self.__GBP_2_34.isSameCurrency(None)

    def test_isSameCurrency_Money_different(self) -> None:

        self.assertEqual(False, self.__GBP_2_34.isSameCurrency(Money.parse("USD 2")))

    def test_isSameCurrency_Money_same(self) -> None:

        self.assertEqual(True, self.__GBP_2_34.isSameCurrency(Money.parse("GBP 2")))

    def test_isSameCurrency_BigMoney_different(self) -> None:

        self.assertEqual(False, self.__GBP_2_34.isSameCurrency(self.__USD_2_34))

    def test_isSameCurrency_BigMoney_same(self) -> None:

        self.assertTrue(self.__GBP_2_34.isSameCurrency(self.__GBP_2_35))

    def test_toMoney_RoundingMode_round(self) -> None:

        money = BigMoney.parse("GBP 2.355")
        self.assertEqual(
            Money.parse("GBP 2.36"), money.toMoney1(decimal.ROUND_HALF_EVEN)
        )

    def test_toMoney_RoundingMode(self) -> None:

        # Importing the necessary enum
        from decimal import ROUND_HALF_EVEN

        # Asserting the equality of the expected and actual values
        self.assertEqual(
            Money.parse("GBP 2.34"), self.__GBP_2_34.toMoney1(ROUND_HALF_EVEN)
        )

    def test_toMoney(self) -> None:

        expected = Money.of0(self.__GBP, self.__BIGDEC_2_34)
        actual = self.__GBP_2_34.toMoney0()

        self.assertEqual(expected, actual)

    def test_toBigMoney(self) -> None:

        self.assertIs(self.__GBP_2_34, self.__GBP_2_34.toBigMoney())

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullRoundingMode(
        self,
    ) -> None:

        with pytest.raises(TypeError):
            self.__GBP_5_78.convertRetainScale(self.__EUR, self.__bd("2"), None)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullBigDecimal(
        self,
    ) -> None:

        with self.assertRaises(TypeError):
            self.__GBP_5_78.convertRetainScale(self.__EUR, None, decimal.ROUND_DOWN)

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_nullCurrency(
        self,
    ) -> None:

        with pytest.raises(TypeError):
            self.__GBP_5_78.convertRetainScale(
                None, decimal.Decimal("2"), decimal.ROUND_DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_sameCurrency(
        self,
    ) -> None:

        with pytest.raises(ValueError):
            self.__GBP_2_33.convertRetainScale(
                self.__GBP, self.__bd("2.5"), RoundingMode.DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_negative(
        self,
    ) -> None:

        with pytest.raises(ValueError):
            self.__GBP_2_33.convertRetainScale(
                self.__EUR, self.__bd("-2.5"), RoundingMode.DOWN
            )

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_roundHalfUp(
        self,
    ) -> None:

        # Python does not have an exact equivalent to Java's RoundingMode.HALF_UP.
        # Instead, we can use decimal.ROUND_HALF_UP.
        # Also, Python does not have a direct equivalent to Java's BigDecimal.
        # Instead, we can use decimal.Decimal.

        test = BigMoney.parse("GBP 2.21").convertRetainScale(
            self.__EUR, decimal.Decimal("2.5"), decimal.ROUND_HALF_UP
        )
        self.assertEqual("EUR 5.53", test.toString())

    def test_convertRetainScale_CurrencyUnit_BigDecimal_RoundingMode_positive(
        self,
    ) -> None:

        test = BigMoney.parse("GBP 2.2").convertRetainScale(
            self.__EUR, self.__bd("2.5"), decimal.ROUND_DOWN
        )
        self.assertEqual("EUR 5.5", test.toString())

    def test_convertedTo_CurrencyUnit_BigDecimal_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.convertedTo(self.__EUR, None)

    def test_convertedTo_CurrencyUnit_BigDecimal_nullCurrency(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.convertedTo(None, self.__bd("2"))

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyWrongFactor(self) -> None:

        with pytest.raises(ValueError):
            self.__GBP_2_33.convertedTo(self.__GBP, self.__bd("2.5"))

    def test_convertedTo_CurrencyUnit_BigDecimal_negative(self) -> None:
        with pytest.raises(ValueError):
            self.__GBP_2_33.convertedTo(self.__EUR, self.__bd("-2.5"))

    def test_convertedTo_CurrencyUnit_BigDecimal_sameCurrencyCorrectFactor(
        self,
    ) -> None:

        test = self.__GBP_2_33.convertedTo(self.__GBP, self.__bd("1.00000"))
        self.assertEqual(self.__GBP_2_33, test)

    def test_convertedTo_CurrencyUnit_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_33.convertedTo(self.__EUR, self.__bd("2.5"))
        self.assertEqual("EUR 5.825", test.toString())

    def test_round_3(self) -> None:

        test = self.__GBP_2_34.rounded(3, decimal.ROUND_DOWN)
        self.assertIs(self.__GBP_2_34, test)

    def test_round_M1up(self) -> None:

        # Assuming BigMoney.parse() and BigMoney.rounded() methods are implemented
        test = BigMoney.parse("GBP 432.34").rounded(-1, decimal.ROUND_UP)
        self.assertEqual("GBP 440.00", test.toString())

    def test_round_M1down(self) -> None:

        test = BigMoney.parse("GBP 432.34").rounded(-1, decimal.ROUND_DOWN)
        self.assertEqual("GBP 430.00", test.toString())

    def test_round_0up(self) -> None:

        test = self.__GBP_2_34.rounded(0, decimal.ROUND_UP)
        self.assertEqual("GBP 3.00", test.toString())

    def test_round_0down(self) -> None:

        test = self.__GBP_2_34.rounded(0, decimal.ROUND_DOWN)
        self.assertEqual("GBP 2.00", test.toString())

    def test_round_1up(self) -> None:

        # The rounding mode is imported from decimal module
        from decimal import ROUND_UP

        test = self.__GBP_2_34.rounded(1, ROUND_UP)
        self.assertEqual("GBP 2.40", test.toString())

    def test_round_1down(self) -> None:

        test = self.__GBP_2_34.rounded(1, decimal.ROUND_DOWN)
        self.assertEqual("GBP 2.30", test.toString())

    def test_round_2up(self) -> None:

        test = self.__GBP_2_34.rounded(2, decimal.ROUND_DOWN)
        self.assertIs(self.__GBP_2_34, test)

    def test_round_2down(self) -> None:

        test = self.__GBP_2_34.rounded(2, decimal.ROUND_DOWN)
        self.assertEqual(self.__GBP_2_34, test)

    def test_abs_negative(self) -> None:

        # Assuming BigMoney.parse() method is implemented and returns a BigMoney object
        test = BigMoney.parse("GBP -2.34").abs()

        # Assuming BigMoney.toString() method is implemented and returns a string
        self.assertEqual(test.toString(), "GBP 2.34")

    def test_abs_positive(self) -> None:

        test = self.__GBP_2_34.abs()
        self.assertIs(self.__GBP_2_34, test)

    def test_negated_negative(self) -> None:

        # Assuming BigMoney.parse() method is implemented and returns a BigMoney object
        test = BigMoney.parse("GBP -2.34").negated()

        # Assuming BigMoney.toString() method is implemented and returns a string
        self.assertEqual(test.toString(), "GBP 2.34")

    def test_negated_positive(self) -> None:

        test = self.__GBP_2_34.negated()
        self.assertEqual("GBP -2.34", test.toString())

    def test_negated_zero(self) -> None:

        test = self.__GBP_0_00.negated()
        self.assertIs(self.__GBP_0_00, test)

    def test_dividedBy_long_negative(self) -> None:

        # The RoundingMode.DOWN is not available in Python, so we will use decimal.ROUND_DOWN
        test = self.__GBP_2_34.dividedBy2(-3, decimal.ROUND_DOWN)
        self.assertEqual("GBP -0.78", test.toString())

    def test_dividedBy_long_positive_roundUp(self) -> None:

        test = self.__GBP_2_35.dividedBy2(3, RoundingMode.UP)
        self.assertEqual("GBP 0.79", test.toString())

    def test_dividedBy_long_positive_roundDown(self) -> None:

        test = self.__GBP_2_35.dividedBy2(3, RoundingMode.DOWN)
        self.assertEqual("GBP 0.78", test.toString())

    def test_dividedBy_long_positive(self) -> None:

        test = self.__GBP_2_34.dividedBy2(3, RoundingMode.DOWN)
        self.assertEqual("GBP 0.78", test.toString())

    def test_dividedBy_long_one(self) -> None:

        test = self.__GBP_2_34.dividedBy2(1, RoundingMode.DOWN)
        self.assertIs(self.__GBP_2_34, test)

    def test_dividedBy_doubleRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.dividedBy1(2.5, None)

    def test_dividedBy_doubleRoundingMode_negative(self) -> None:

        # RoundingMode.FLOOR is equivalent to decimal.ROUND_DOWN in Python's decimal module
        test = self.__GBP_2_34.dividedBy1(-2.5, decimal.ROUND_DOWN)
        self.assertEqual("GBP -0.94", test.toString())

    def test_dividedBy_doubleRoundingMode_positive_halfUp(self) -> None:

        test = self.__GBP_2_34.dividedBy1(2.5, decimal.ROUND_HALF_UP)
        self.assertEqual("GBP 0.94", test.toString())

    def test_dividedBy_doubleRoundingMode_positive(self) -> None:

        # RoundingMode.DOWN is equivalent to decimal.ROUND_DOWN in Python's decimal module
        test = self.__GBP_2_34.dividedBy1(2.5, decimal.ROUND_DOWN)
        self.assertEqual("GBP 0.93", test.toString())

    def test_dividedBy_doubleRoundingMode_one(self) -> None:

        # Python doesn't have an exact equivalent to Java's RoundingMode.DOWN.
        # Instead, we can use decimal.ROUND_DOWN.
        # Also, Python doesn't have a direct equivalent to Java's BigMoney.dividedBy1 method.
        # We will assume that there is a similar method in the BigMoney class.

        test = self.__GBP_2_34.dividedBy1(1.0, decimal.ROUND_DOWN)
        self.assertIs(self.__GBP_2_34, test)

    def test_dividedBy_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.dividedBy0(self.__bd("2.5"), None)

    def test_dividedBy_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.dividedBy0(None, decimal.ROUND_DOWN)

    def test_dividedBy_BigDecimalRoundingMode_negative(self) -> None:

        # BigDecimal is not available in Python, so we use decimal.Decimal
        # RoundingMode is not available in Python, so we use decimal.ROUND_FLOOR
        test = self.__GBP_2_34.dividedBy0(decimal.Decimal("-2.5"), decimal.ROUND_FLOOR)
        self.assertEqual("GBP -0.94", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        from decimal import Decimal, ROUND_HALF_UP
        from src.main.org.joda.money.BigMoney import BigMoney
        from src.main.org.joda.money.CurrencyUnit import CurrencyUnit

        test = self.__GBP_2_34.dividedBy0(Decimal("2.5"), ROUND_HALF_UP)
        self.assertEqual(str(test), "GBP 0.94")

    def test_dividedBy_BigDecimalRoundingMode_positive(self) -> None:

        # Translate the BigDecimal RoundingMode
        from decimal import ROUND_DOWN

        # Translate the BigMoney.dividedBy method
        test = self.__GBP_2_34.dividedBy0(self.__bd("2.5"), ROUND_DOWN)

        # Translate the BigMoney.toString method
        self.assertEqual("GBP 0.93", test.toString())

    def test_dividedBy_BigDecimalRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.dividedBy0(decimal.Decimal(1), decimal.ROUND_DOWN)
        self.assertIs(self.__GBP_2_34, test)

    def test_multiplyRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.multiplyRetainScale1(2.5, None)

    def test_multiplyRetainScale_doubleRoundingMode_negative(self) -> None:

        # The Java code uses BigMoney.parse("GBP 2.33") to create a BigMoney object.
        # In Python, we can use the BigMoney constructor directly.
        # We assume that the BigMoney constructor takes a decimal.Decimal and a CurrencyUnit as arguments.
        GBP_2_33 = BigMoney(decimal.Decimal("2.33"), self.__GBP)

        # The Java code uses BigMoney.multiplyRetainScale1(-2.5d, RoundingMode.FLOOR) to multiply the BigMoney object.
        # In Python, we can use the multiplyRetainScale1 method directly.
        # We assume that the multiplyRetainScale1 method takes a float and a rounding mode as arguments.
        test = GBP_2_33.multiplyRetainScale1(-2.5, decimal.ROUND_FLOOR)

        # The Java code uses test.toString() to get a string representation of the BigMoney object.
        # In Python, we can use the toString method directly.
        self.assertEqual("GBP -5.83", test.toString())

    def test_multiplyRetainScale_doubleRoundingMode_positive_halfUp(self) -> None:

        # Assuming BigMoney.multiplyRetainScale1() returns a BigMoney object
        test = self.__GBP_2_33.multiplyRetainScale1(2.5, decimal.ROUND_HALF_UP)
        self.assertEqual(str(test), "GBP 5.83")

    def test_multiplyRetainScale_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_33.multiplyRetainScale1(2.5, decimal.ROUND_DOWN)
        self.assertEqual("GBP 5.82", test.toString())

    def test_multiplyRetainScale_doubleRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.multiplyRetainScale1(1.0, decimal.ROUND_DOWN)
        self.assertIs(self.__GBP_2_34, test)

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:

        # Python does not have a direct equivalent to Java's BigDecimal.multiplyRetainScale0 method.
        # However, we can use the decimal.Decimal.quantize method to achieve similar functionality.
        # The decimal.Decimal.quantize method rounds a number to a fixed exponent, which is similar to BigDecimal.multiplyRetainScale0.
        # We can set the rounding mode to None to mimic the behavior of BigDecimal.multiplyRetainScale0.

        # The following code assumes that the BigMoney.multiplyRetainScale0 method is implemented as follows:
        # def multiplyRetainScale0(self, valueToMultiplyBy: decimal.Decimal, roundingMode: typing.Any) -> BigMoney:
        #     return self.__amount.quantize(decimal.Decimal('1.' + '0' * self.__amount.as_tuple().exponent), roundingMode) * valueToMultiplyBy

        with self.assertRaises(TypeError):
            self.__GBP_5_78.multiplyRetainScale0(self.__bd("2.5"), None)

    def test_multiplyRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.multiplyRetainScale0(None, decimal.ROUND_DOWN)

    def test_multiplyRetainScale_BigDecimalRoundingMode_negative(self) -> None:

        # Assuming BigMoney.parse and CurrencyUnit.of are static methods
        GBP_2_33 = BigMoney.parse("GBP 2.33")
        GBP = CurrencyUnit.of("GBP")

        # Assuming bd is a static method that parses a string to a decimal
        bd = TestBigMoney.__bd("-2.5")

        # Assuming RoundingMode.FLOOR is a static attribute of decimal
        test = GBP_2_33.multiplyRetainScale0(bd, decimal.ROUND_FLOOR)

        # Assuming assertEquals is a method of unittest.TestCase
        self.assertEqual("GBP -5.83", test.toString())

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive_halfUp(self) -> None:

        # RoundingMode.HALF_UP is equivalent to decimal.ROUND_HALF_UP
        test = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("2.5"), decimal.ROUND_HALF_UP
        )
        self.assertEqual("GBP 5.83", test.toString())

    def test_multiplyRetainScale_BigDecimalRoundingMode_positive(self) -> None:

        # Assuming BigMoney.parse and BigMoney.multiplyRetainScale0 are implemented
        test = self.__GBP_2_33.multiplyRetainScale0(
            self.__bd("2.5"), decimal.ROUND_DOWN
        )
        self.assertEqual("GBP 5.82", test.toString())

    def test_multiplyRetainScale_BigDecimalRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.multiplyRetainScale0(
            decimal.Decimal(1), decimal.ROUND_DOWN
        )
        self.assertIs(self.__GBP_2_34, test)

    def test_multipliedBy_long_negative(self) -> None:

        test = self.__GBP_2_34.multipliedBy2(-3)
        self.assertEqual("GBP -7.02", test.toString())
        self.assertEqual(2, test.getScale())

    def test_multipliedBy_long_positive(self) -> None:

        test = self.__GBP_2_34.multipliedBy2(3)
        self.assertEqual("GBP 7.02", test.toString())
        self.assertEqual(2, test.getScale())

    def test_multipliedBy_long_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy2(1)
        self.assertIs(self.__GBP_2_34, test)

    def test_multipliedBy_doubleRoundingMode_negative(self) -> None:

        test = self.__GBP_2_33.multipliedBy1(-2.5)
        self.assertEqual("GBP -5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_doubleRoundingMode_positive(self) -> None:

        test = self.__GBP_2_33.multipliedBy1(2.5)
        self.assertEqual("GBP 5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_doubleRoundingMode_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy1(1.0)
        self.assertIs(self.__GBP_2_34, test)

    def test_multipliedBy_BigDecimal_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_5_78.multipliedBy0(None)

    def test_multipliedBy_BigDecimal_negative(self) -> None:

        test = self.__GBP_2_33.multipliedBy0(self.__bd("-2.5"))
        self.assertEqual("GBP -5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_33.multipliedBy0(self.__bd("2.5"))
        self.assertEqual("GBP 5.825", test.toString())
        self.assertEqual(3, test.getScale())

    def test_multipliedBy_BigDecimal_one(self) -> None:

        test = self.__GBP_2_34.multipliedBy0(decimal.Decimal(1))
        self.assertEqual(self.__GBP_2_34, test)

    def test_minusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.minusRetainScale2(2.34, None)

    def test_minusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

        # The Python equivalent of the Java BigMoney.parse method is to create a new BigMoney object.
        # The Python equivalent of the Java BigMoney.minusRetainScale2 method is to subtract the amount from the BigMoney object.
        # The Python equivalent of the Java RoundingMode.UNNECESSARY is to use the decimal.ROUND_DOWN rounding mode.

        # Create a BigMoney object with the amount 2.34 and the currency GBP
        money = BigMoney(decimal.Decimal("2.34"), self.__GBP)

        # Subtract 1.235 from the BigMoney object with the rounding mode decimal.ROUND_DOWN
        # The expected exception is ArithmeticException, which is raised when the rounding mode is UNNECESSARY and the result is not an exact integer
        with self.assertRaises(ArithmeticException):
            money.minusRetainScale2(1.235, decimal.ROUND_DOWN)

    def test_minusRetainScale_doubleRoundingMode_roundDown(self) -> None:

        # Python does not have an exact equivalent to Java's RoundingMode.DOWN.
        # Instead, we can use decimal.ROUND_DOWN.
        # Also, Python does not have BigMoney.minusRetainScale2 method.
        # Instead, we can use BigMoney.minus method with rounding mode.

        test = self.__GBP_2_34.minus(
            decimal.Decimal(1.235), rounding=decimal.ROUND_DOWN
        )
        self.assertEqual(str(test), "GBP 1.10")

    def test_minusRetainScale_doubleRoundingMode_negative(self) -> None:

        # The rounding mode is not used in the Python version, so it can be ignored.
        test = self.__GBP_2_34.minusRetainScale2(-1.23)
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_doubleRoundingMode_positive(self) -> None:

        # The rounding mode is not used in the Python version, so it can be ignored.
        test = self.__GBP_2_34.minusRetainScale2(1.23, None)
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusRetainScale_doubleRoundingMode_zero(self) -> None:

        # The RoundingMode.UNNECESSARY is not available in Python's decimal module.
        # We can use the default rounding mode which is ROUND_HALF_EVEN.
        test = self.__GBP_2_34.minusRetainScale2(0.0, None)
        self.assertIs(self.__GBP_2_34, test)

    def test_minusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.minusRetainScale1(self.__BIGDEC_2_34, None)

    def test_minusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.minusRetainScale1(None, decimal.ROUND_UNNECESSARY)

    def test_minusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        with pytest.raises(decimal.InvalidOperation):
            self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), decimal.ROUND_DOWN)

    def test_minusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:

        # Translate the BigDecimal rounding mode
        rounding_mode = decimal.ROUND_DOWN

        # Translate the BigMoney minusRetainScale1 method
        test = self.__GBP_2_34.minusRetainScale1(self.__bd("1.235"), rounding_mode)

        # Translate the BigMoney toString method
        self.assertEqual("GBP 1.10", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_negative(self) -> None:

        # The BigMoney.minusRetainScale1 method is not defined in the partial Python translation.
        # Assuming it takes two parameters: a BigDecimal and a RoundingMode, and returns a BigMoney.
        # The RoundingMode is not defined in the partial Python translation.
        # Assuming it is a string.

        test = self.__GBP_2_34.minusRetainScale1(self.__bd("-1.23"), "UNNECESSARY")
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_positive(self) -> None:

        # Translate the BigDecimal string to a decimal.Decimal object
        amountToSubtract = decimal.Decimal(self.__PARSE_REGEX.match("1.23").group())

        # Call the minusRetainScale1 method
        test = self.__GBP_2_34.minusRetainScale1(amountToSubtract, decimal.ROUND_DOWN)

        # Assert the result
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusRetainScale_BigDecimalRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.minusRetainScale1(decimal.Decimal(0), decimal.ROUND_DOWN)
        self.assertEqual(self.__GBP_2_34, test)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(
        self,
    ) -> None:

        with pytest.raises(TypeError):
            self.__GBP_M5_78.minusRetainScale0(BigMoney.parse("GBP 123"), None)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_nullBigMoneyProvider(
        self,
    ) -> None:

        with pytest.raises(TypeError):
            self.__GBP_M5_78.minusRetainScale0(None, decimal.ROUND_UNNECESSARY)

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(
        self,
    ) -> None:

        with pytest.raises(ArithmeticException):
            self.__GBP_2_34.minusRetainScale0(
                BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY
            )

    def test_minusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:

        # Assuming RoundingMode.DOWN is equivalent to decimal.ROUND_DOWN
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.235"), decimal.ROUND_DOWN
        )
        self.assertEqual("GBP 1.10", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_negative(self) -> None:

        # Assuming that BigMoney.minusRetainScale0() returns a BigMoney object
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP -1.23"), RoundingMode.UNNECESSARY
        )

        # Assuming that BigMoney.toString() returns a string
        self.assertEqual("GBP 3.57", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_positive(self) -> None:

        # Assuming that BigMoney.minusRetainScale0() returns a BigMoney object
        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.parse("GBP 1.23"), RoundingMode.UNNECESSARY
        )

        # Assuming that BigMoney.toString() returns a string
        self.assertEqual("GBP 1.11", test.toString())

    def test_minusRetainScale_BigMoneyProviderRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.minusRetainScale0(
            BigMoney.zero0(self.__GBP), decimal.ROUND_DOWN
        )
        self.assertEqual(self.__GBP_2_34, test)

    def test_minusMinor_scale(self) -> None:

        # Assuming BigMoney.parse() and BigMoney.minusMinor() methods are implemented
        test = BigMoney.parse("GBP 12").minusMinor(123)

        # Assuming toString() and getScale() methods are implemented
        self.assertEqual(test.toString(), "GBP 10.77")
        self.assertEqual(test.getScale(), 2)

    def test_minusMinor_negative(self) -> None:

        # Call the minusMinor method with -123 as the argument
        test = self.__GBP_2_34.minusMinor(-123)

        # Assert that the toString method returns "GBP 3.57"
        self.assertEqual(test.toString(), "GBP 3.57")

        # Assert that the getScale method returns 2
        self.assertEqual(test.getScale(), 2)

    def test_minusMinor_positive(self) -> None:

        test = self.__GBP_2_34.minusMinor(123)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minusMinor_zero(self) -> None:

        test = self.__GBP_2_34.minusMinor(0)
        self.assertIs(self.__GBP_2_34, test)

    def test_minusMajor_negative(self) -> None:

        # Call the minusMajor method with -123 as the argument
        test = self.__GBP_2_34.minusMajor(-123)

        # Assert that the toString method returns "GBP 125.34"
        self.assertEqual(test.toString(), "GBP 125.34")

        # Assert that the getScale method returns 2
        self.assertEqual(test.getScale(), 2)

    def test_minusMajor_positive(self) -> None:

        # Call the minusMajor method
        test = self.__GBP_2_34.minusMajor(123)

        # Assert the expected string representation
        self.assertEqual("GBP -120.66", test.toString())

        # Assert the expected scale
        self.assertEqual(2, test.getScale())

    def test_minusMajor_zero(self) -> None:

        test = self.__GBP_2_34.minusMajor(0)
        self.assertEqual(self.__GBP_2_34, test)

    def test_minus_double_scale(self) -> None:

        # Call the minus3 method with 1.235 as argument
        test = self.__GBP_2_34.minus3(1.235)

        # Assert that the string representation of the result is "GBP 1.105"
        self.assertEqual("GBP 1.105", test.toString())

        # Assert that the scale of the result is 3
        self.assertEqual(3, test.getScale())

    def test_minus_double_negative(self) -> None:

        test = self.__GBP_2_34.minus3(-1.23)
        self.assertEqual(str(test), "GBP 3.57")
        self.assertEqual(test.getScale(), 2)

    def test_minus_double_positive(self) -> None:

        test = self.__GBP_2_34.minus3(1.23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_double_zero(self) -> None:

        test = self.__GBP_2_34.minus3(0.0)
        self.assertEqual(self.__GBP_2_34, test)

    def test_minus_BigDecimal_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.minus2(None)

    def test_minus_BigDecimal_scale(self) -> None:

        # Translate the BigDecimal using the static method
        test = self.__GBP_2_34.minus2(self.__bd("1.235"))

        # Assert the expected string representation
        self.assertEqual("GBP 1.105", test.toString())

        # Assert the expected scale
        self.assertEqual(3, test.getScale())

    def test_minus_BigDecimal_negative(self) -> None:

        # Translate the BigDecimal using the static method
        test = self.__GBP_2_34.minus2(self.__bd("-1.23"))

        # Assert the expected string representation
        self.assertEqual("GBP 3.57", test.toString())

        # Assert the expected scale
        self.assertEqual(2, test.getScale())

    def test_minus_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_34.minus2(self.__bd("1.23"))
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigDecimal_zero(self) -> None:

        test = self.__GBP_2_34.minus2(decimal.Decimal(0))
        self.assertEqual(self.__GBP_2_34, test)

    def test_minus_BigMoneyProvider_badProvider(self) -> None:

        class NullBigMoneyProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.minus1(NullBigMoneyProvider())

    def test_minus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.minus1(None)

    def test_minus_BigMoneyProvider_currencyMismatch(self) -> None:

        with pytest.raises(CurrencyMismatchException):
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

        test = self.__GBP_2_34.minus1(self.__GBP_M1_23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigMoneyProvider_positive(self) -> None:

        test = self.__GBP_2_34.minus1(self.__GBP_1_23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_minus_BigMoneyProvider_zero(self) -> None:

        test = self.__GBP_2_34.minus1(self.__GBP_0_00)
        self.assertIs(self.__GBP_2_34, test)

    def test_minus_Iterable_badProvider(self) -> None:

        iterable = [BigMoneyProvider() for _ in range(1)]
        for provider in iterable:
            provider.toBigMoney = lambda: None

        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_nullIterable(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.minus0(None)

    def test_minus_Iterable_nullEntry(self) -> None:

        iterable = [self.__GBP_2_33, None]
        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_currencyMismatch(self) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            self.__GBP_M5_78.minus0(iterable)

    def test_minus_Iterable_zero(self) -> None:

        iterable = [self.__GBP_0_00]
        test = self.__GBP_2_34.minus0(iterable)
        self.assertEqual(self.__GBP_2_34, test)

    def test_minus_Iterable_Mixed(self) -> None:

        pass  # LLM could not translate this method

    def test_minus_Iterable_Money(self) -> None:

        iterable = [self.__GBP_2_33.toMoney0(), self.__GBP_1_23.toMoney0()]
        test = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_minus_Iterable_BigMoney(self) -> None:

        iterable = [self.__GBP_2_33, self.__GBP_1_23]
        test = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_minus_Iterable_BigMoneyProvider(self) -> None:

        iterable = [self.__GBP_2_33, self.__GBP_1_23]
        test = self.__GBP_2_34.minus0(iterable)
        self.assertEqual("GBP -1.22", test.toString())

    def test_plusRetainScale_doubleRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.plusRetainScale2(2.34, None)

    def test_plusRetainScale_doubleRoundingMode_roundUnecessary(self) -> None:

        with pytest.raises(ArithmeticException):
            self.__GBP_2_34.plusRetainScale2(1.235, RoundingMode.UNNECESSARY)

    def test_plusRetainScale_doubleRoundingMode_roundDown(self) -> None:

        # Python does not have a direct equivalent to Java's RoundingMode.DOWN.
        # Instead, we can use decimal.ROUND_DOWN.
        # Also, Python's decimal module does not have a direct equivalent to BigMoney's plusRetainScale2 method.
        # We can use the decimal.Decimal.quantize method to achieve similar functionality.

        test = self.__GBP_2_34.plusRetainScale2(1.235, decimal.ROUND_DOWN)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_doubleRoundingMode_negative(self) -> None:

        # The RoundingMode.UNNECESSARY is not available in Python's decimal module.
        # We can use the default rounding mode which is ROUND_HALF_EVEN.
        test = self.__GBP_2_34.plusRetainScale2(-1.23, decimal.ROUND_HALF_EVEN)
        self.assertEqual("GBP 1.11", test.toString())

    def test_plusRetainScale_doubleRoundingMode_positive(self) -> None:

        # The rounding mode is not used in the Python version, so it can be ignored.
        test = self.__GBP_2_34.plusRetainScale2(1.23)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_doubleRoundingMode_zero(self) -> None:

        # The RoundingMode.UNNECESSARY is not available in Python's decimal module.
        # We can use the default rounding mode which is ROUND_HALF_EVEN.
        test = self.__GBP_2_34.plusRetainScale2(0.0, None)
        self.assertIs(self.__GBP_2_34, test)

    def test_plusRetainScale_BigDecimalRoundingMode_nullRoundingMode(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.plusRetainScale1(self.__BIGDEC_2_34, None)

    def test_plusRetainScale_BigDecimalRoundingMode_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.plusRetainScale1(None, decimal.ROUND_UNNECESSARY)

    def test_plusRetainScale_BigDecimalRoundingMode_roundUnecessary(self) -> None:

        # Create a BigMoney object with the same currency as GBP_2_34
        money = BigMoney(self.__GBP, decimal.Decimal("1.235"))

        # Expect an ArithmeticException when trying to add money to GBP_2_34
        with self.assertRaises(ArithmeticException):
            self.__GBP_2_34.plusRetainScale1(
                money.getAmount(), decimal.ROUND_UNNECESSARY
            )

    def test_plusRetainScale_BigDecimalRoundingMode_roundDown(self) -> None:

        # Translate the BigDecimal RoundingMode
        from decimal import ROUND_DOWN

        # Translate the BigMoney.plusRetainScale1 method
        test = self.__GBP_2_34.plusRetainScale1(self.__bd("1.235"), ROUND_DOWN)

        # Translate the BigMoney.toString method
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_BigDecimalRoundingMode_negative(self) -> None:

        # The RoundingMode.UNNECESSARY is not available in Python's decimal module.
        # We can use decimal.ROUND_DOWN which is equivalent to RoundingMode.DOWN in Java.
        # If the rounding mode is not specified, it defaults to ROUND_DOWN.
        test = self.__GBP_2_34.plusRetainScale1(self.__bd("-1.23"))
        self.assertEqual("GBP 1.11", test.toString())

    def test_plusRetainScale_BigDecimalRoundingMode_positive(self) -> None:

        # The RoundingMode.UNNECESSARY is not available in Python's decimal module.
        # We can use decimal.ROUND_DOWN which is equivalent to RoundingMode.UNNECESSARY
        # in Java.
        test = self.__GBP_2_34.plusRetainScale1(self.__bd("1.23"), decimal.ROUND_DOWN)
        self.assertEqual("GBP 3.57", test.toString())

    def test_plusRetainScale_BigDecimalRoundingMode_zero(self) -> None:

        test = self.__GBP_2_34.plusRetainScale1(decimal.Decimal(0), decimal.ROUND_DOWN)
        self.assertEqual(self.__GBP_2_34, test)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullRoundingMode(
        self,
    ) -> None:

        with pytest.raises(TypeError):
            self.__GBP_M5_78.plusRetainScale0(BigMoney.parse("GBP 1.23"), None)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_nullBigDecimal(self) -> None:

        with pytest.raises(TypeError):
            self.__GBP_M5_78.plusRetainScale1(None, decimal.ROUND_UNNECESSARY)

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundUnecessary(self) -> None:

        with pytest.raises(ArithmeticException):
            self.__GBP_2_34.plusRetainScale0(
                BigMoney.parse("GBP 1.235"), RoundingMode.UNNECESSARY
            )

    def test_plusRetainScale_BigMoneyProviderRoundingMode_roundDown(self) -> None:

        # Assuming that BigMoney.parse() and RoundingMode.DOWN are available
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
            BigMoney.zero0(self.__GBP), decimal.ROUND_DOWN
        )
        self.assertEqual(self.__GBP_2_34, test)

    def test_plusMinor_scale(self) -> None:

        # Assuming BigMoney.parse() and BigMoney.plusMinor() methods are implemented
        test = BigMoney.parse("GBP 12").plusMinor(123)

        # Assuming toString() and getScale() methods are implemented
        self.assertEqual("GBP 13.23", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMinor_negative(self) -> None:

        test = self.__GBP_2_34.plusMinor(-123)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMinor_positive(self) -> None:

        test = self.__GBP_2_34.plusMinor(123)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMinor_zero(self) -> None:

        test = self.__GBP_2_34.plusMinor(0)
        self.assertIs(self.__GBP_2_34, test)

    def test_plusMajor_negative(self) -> None:

        test = self.__GBP_2_34.plusMajor(-123)
        self.assertEqual("GBP -120.66", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plusMajor_positive(self) -> None:

        test = self.__GBP_2_34.plusMajor(123)
        self.assertEqual(str(test), "GBP 125.34")
        self.assertEqual(test.getScale(), 2)

    def test_plusMajor_zero(self) -> None:

        test = self.__GBP_2_34.plusMajor(0)
        self.assertIs(self.__GBP_2_34, test)

    def test_plus_double_scale(self) -> None:

        test = self.__GBP_2_34.plus3(1.234)
        self.assertEqual("GBP 3.574", test.toString())
        self.assertEqual(3, test.getScale())

    def test_plus_double_negative(self) -> None:

        test = self.__GBP_2_34.plus3(-1.23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_double_positive(self) -> None:

        test = self.__GBP_2_34.plus3(1.23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_double_zero(self) -> None:

        test = self.__GBP_2_34.plus3(0.0)
        self.assertIs(self.__GBP_2_34, test)

    def test_plus_BigDecimal_nullBigDecimal(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.plus2(None)

    def test_plus_BigDecimal_scale(self) -> None:

        test = self.__GBP_2_34.plus2(self.__bd("1.235"))
        self.assertEqual("GBP 3.575", test.toString())
        self.assertEqual(3, test.getScale())

    def test_plus_BigDecimal_negative(self) -> None:

        # Translate the Java BigDecimal using decimal.Decimal
        test = self.__GBP_2_34.plus2(decimal.Decimal("-1.23"))

        # Assert the toString method
        self.assertEqual(str(test), "GBP 1.11")

        # Assert the getScale method
        self.assertEqual(test.getScale(), 2)

    def test_plus_BigDecimal_positive(self) -> None:

        test = self.__GBP_2_34.plus2(self.__bd("1.23"))
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigDecimal_zero(self) -> None:

        test = self.__GBP_2_34.plus2(decimal.Decimal(0))
        self.assertIs(self.__GBP_2_34, test)

    def test_plus_BigMoneyProvider_badProvider(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.plus1(None)

    def test_plus_BigMoneyProvider_currencyMismatch(self) -> None:

        with pytest.raises(CurrencyMismatchException):
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

        test = self.__GBP_2_34.plus1(self.__GBP_M1_23)
        self.assertEqual("GBP 1.11", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigMoneyProvider_positive(self) -> None:

        test = self.__GBP_2_34.plus1(self.__GBP_1_23)
        self.assertEqual("GBP 3.57", test.toString())
        self.assertEqual(2, test.getScale())

    def test_plus_BigMoneyProvider_zero(self) -> None:

        test = self.__GBP_2_34.plus1(self.__GBP_0_00)
        self.assertIs(self.__GBP_2_34, test)

    def test_plus_Iterable_badProvider(self) -> None:

        iterable = [BigMoneyProvider() for _ in range(1)]
        for provider in iterable:
            provider.toBigMoney = lambda: None

        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_nullIterable(self) -> None:
        with pytest.raises(TypeError):
            self.__GBP_M5_78.plus0(None)

    def test_plus_Iterable_nullEntry(self) -> None:

        iterable = [self.__GBP_2_33, None]
        with pytest.raises(NullPointerException):
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_currencyMismatch(self) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            self.__GBP_M5_78.plus0(iterable)

    def test_plus_Iterable_zero(self) -> None:

        iterable = [self.__GBP_0_00]
        test = self.__GBP_2_34.plus0(iterable)
        self.assertEqual(self.__GBP_2_34, test)

    def test_plus_Iterable_Mixed(self) -> None:

        pass  # LLM could not translate this method

    def test_plus_Iterable_Money(self) -> None:

        iterable = [self.__GBP_2_33.toMoney0(), self.__GBP_1_23.toMoney0()]
        test = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_plus_Iterable_BigMoney(self) -> None:

        iterable = [self.__GBP_2_33, self.__GBP_1_23]
        test = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_plus_Iterable_BigMoneyProvider(self) -> None:

        iterable = [self.__GBP_2_33, self.__GBP_1_23]
        test = self.__GBP_2_34.plus0(iterable)
        self.assertEqual("GBP 5.90", test.toString())

    def test_withAmount_double_same(self) -> None:

        test = self.__GBP_2_34.withAmount1(2.34)
        self.assertIs(self.__GBP_2_34, test)

    def test_withAmount_double(self) -> None:

        test = self.__GBP_2_34.withAmount1(2.345)
        self.assertEqual(self.__bd("2.345"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_withAmount_BigDecimal_nullBigDecimal(self) -> None:
        with self.assertRaises(NullPointerException):
            self.__GBP_2_34.withAmount0(None)

    def test_withAmount_BigDecimal_same(self) -> None:

        test = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_34)
        self.assertIs(self.__GBP_2_34, test)

    def test_withAmount_BigDecimal(self) -> None:

        test = self.__GBP_2_34.withAmount0(self.__BIGDEC_2_345)
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

        # Call the method to be tested
        result = self.__GBP_M5_78.getMinorPart()

        # Assert the expected result
        self.assertEqual(-78, result)

    def test_getMinorPart_positive(self) -> None:

        # Assuming that the getMinorPart() method returns the minor part of the BigMoney object as an integer
        self.assertEqual(34, self.__GBP_2_34.getMinorPart())

    def test_getAmountMinorInt_tooBigNegative(self) -> None:
        with pytest.raises(ArithmeticError):
            self.__GBP_INT_MIN_MINUS1.getAmountMinorInt()

    def test_getAmountMinorInt_tooBigPositive(self) -> None:

        with pytest.raises(ArithmeticError):
            self.__GBP_INT_MAX_PLUS1.getAmountMinorInt()

    def test_getAmountMinorInt_negative(self) -> None:

        # Call the method to be tested
        result = self.__GBP_M5_78.getAmountMinorInt()

        # Assert the expected result
        self.assertEqual(-578, result)

    def test_getAmountMinorInt_positive(self) -> None:

        # Assuming that the getAmountMinorInt() method returns an integer
        # and that the BigMoney.parse() method returns a BigMoney object
        self.assertEqual(234, self.__GBP_2_34.getAmountMinorInt())

    def test_getAmountMinorLong_tooBigNegative(self) -> None:

        with pytest.raises(ArithmeticError):
            self.__GBP_LONG_MIN_MINUS1.getAmountMinorLong()

    def test_getAmountMinorLong_tooBigPositive(self) -> None:
        with pytest.raises(ArithmeticError):
            self.__GBP_LONG_MAX_PLUS1.getAmountMinorLong()

    def test_getAmountMinorLong_negative(self) -> None:

        # Convert the amount to a long integer
        amount_minor_long = int(self.__GBP_M5_78.getAmountMinorLong())

        # Assert that the amount is equal to -578
        self.assertEqual(-578, amount_minor_long)

    def test_getAmountMinorLong_positive(self) -> None:

        # Assuming that the getAmountMinorLong() method returns a decimal.Decimal
        # and we need to convert it to an integer
        self.assertEqual(234, int(self.__GBP_2_34.getAmountMinorLong()))

    def test_getAmountMinor_negative(self) -> None:

        # Call the method to be tested
        result = self.__GBP_M5_78.getAmountMinor()

        # Assert the expected result
        self.assertEqual(decimal.Decimal("-578"), result)

    def test_getAmountMinor_positive(self) -> None:

        # Assuming that the getAmountMinor method returns a decimal.Decimal object
        self.assertEqual(decimal.Decimal("234"), self.__GBP_2_34.getAmountMinor())

    def test_getAmountMajorInt_tooBigNegative(self) -> None:
        with pytest.raises(ArithmeticError):
            self.__GBP_INT_MIN_MAJOR_MINUS1.getAmountMajorInt()

    def test_getAmountMajorInt_tooBigPositive(self) -> None:
        with pytest.raises(ArithmeticError):
            self.__GBP_INT_MAX_MAJOR_PLUS1.getAmountMajorInt()

    def test_getAmountMajorInt_negative(self) -> None:

        # Assuming that the BigMoney.parse method returns a BigMoney object with the amount as a decimal
        # and the getAmountMajorInt method returns the integer part of the amount
        self.assertEqual(-5, self.__GBP_M5_78.getAmountMajorInt())

    def test_getAmountMajorInt_positive(self) -> None:

        # Assuming that the getAmountMajorInt() method returns an integer
        # and that the BigMoney.parse() method returns a BigMoney object
        self.assertEqual(2, self.__GBP_2_34.getAmountMajorInt())

    def test_getAmountMajorLong_tooBigNegative(self) -> None:

        with pytest.raises(ArithmeticError):
            self.__GBP_LONG_MIN_MAJOR_MINUS1.getAmountMajorLong()

    def test_getAmountMajorLong_tooBigPositive(self) -> None:
        with pytest.raises(ArithmeticError):
            self.__GBP_LONG_MAX_MAJOR_PLUS1.getAmountMajorLong()

    def test_getAmountMajorLong_negative(self) -> None:

        # Convert the amount to a decimal
        amount = decimal.Decimal(self.__GBP_M5_78.getAmountMajorLong())

        # Assert that the amount is equal to -5
        self.assertEqual(amount, -5)

    def test_getAmountMajorLong_positive(self) -> None:

        # Assuming that the getAmountMajorLong() method returns a decimal.Decimal
        # and we need to convert it to an integer
        self.assertEqual(2, int(self.__GBP_2_34.getAmountMajorLong()))

    def test_getAmountMajor_negative(self) -> None:

        # Call the method to be tested
        result = self.__GBP_M5_78.getAmountMajor()

        # Assert the expected result
        self.assertEqual(decimal.Decimal(-5), result)

    def test_getAmountMajor_positive(self) -> None:

        # Assuming BigMoney.parse() returns a BigMoney object with the amount set to 2.34
        # and the currency set to GBP
        self.assertEqual(decimal.Decimal("2.34"), self.__GBP_2_34.getAmountMajor())

    def test_getAmount_negative(self) -> None:
        self.assertEqual(self.__BIGDEC_M5_78, self.__GBP_M5_78.getAmount())

    def test_getAmount_positive(self) -> None:
        self.assertEqual(self.__BIGDEC_2_34, self.__GBP_2_34.getAmount())

    def test_withCurrencyScale_intRoundingMode_lessJPY(self) -> None:

        # Assuming RoundingMode.UP is equivalent to decimal.ROUND_UP
        test = BigMoney.parse("JPY 2.345").withCurrencyScale1(decimal.ROUND_UP)

        # Assuming bd is a method that converts a string to a decimal
        self.assertEqual(self.__bd("3"), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_withCurrencyScale_intRoundingMode_more(self) -> None:

        # Assuming RoundingMode.UP is equivalent to decimal.ROUND_UP
        test = BigMoney.parse("GBP 2.3").withCurrencyScale1(decimal.ROUND_UP)

        # Assuming __bd is a static method that converts a string to a decimal
        self.assertEqual(self.__bd("2.30"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_intRoundingMode_less(self) -> None:

        # Assuming RoundingMode.UP is equivalent to decimal.ROUND_UP
        test = BigMoney.parse("GBP 2.345").withCurrencyScale1(decimal.ROUND_UP)

        # Assuming __bd is a static method that converts a string to a decimal
        self.assertEqual(self.__bd("2.35"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_int_less(self) -> None:

        with self.assertRaises(ArithmeticException):
            BigMoney.parse("GBP 2.345").withCurrencyScale0()

    def test_withCurrencyScale_int_more(self) -> None:

        test = BigMoney.parse("GBP 2.3").withCurrencyScale0()
        self.assertEqual(self.__bd("2.30"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_withCurrencyScale_int_same(self) -> None:

        test = self.__GBP_2_34.withCurrencyScale0()
        self.assertIs(self.__GBP_2_34, test)

    def test_withScale_intRoundingMode_more(self) -> None:

        # Assuming RoundingMode.UP is equivalent to decimal.ROUND_UP
        test = self.__GBP_2_34.withScale1(3, decimal.ROUND_UP)
        self.assertEqual(self.__bd("2.340"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_withScale_intRoundingMode_less(self) -> None:

        # Assuming RoundingMode.UP is equivalent to decimal.ROUND_UP
        test = self.__GBP_2_34.withScale1(1, decimal.ROUND_UP)
        self.assertEqual(self.__bd("2.4"), test.getAmount())
        self.assertEqual(1, test.getScale())

    def test_withScale_int_less(self) -> None:

        with pytest.raises(ArithmeticException):
            BigMoney.parse("GBP 2.345").withScale0(2)

    def test_withScale_int_more(self) -> None:

        test = self.__GBP_2_34.withScale0(3)
        self.assertEqual(self.__bd("2.340"), test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_withScale_int_same(self) -> None:

        test = self.__GBP_2_34.withScale0(2)
        self.assertIs(self.__GBP_2_34, test)

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

        # Assuming that BigMoney.getScale() returns the scale of the amount
        self.assertEqual(0, self.__JPY_423.getScale())

    def test_getScale_GBP(self) -> None:

        # Call the getScale method
        scale = self.__GBP_2_34.getScale()

        # Assert that the scale is 2
        self.assertEqual(scale, 2)

    def test_withCurrencyUnit_Currency_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            self.__GBP_2_34.withCurrencyUnit(None)

    def test_withCurrencyUnit_Currency_differentCurrencyScale(self) -> None:

        test = self.__GBP_2_34.withCurrencyUnit(self.__JPY)
        self.assertEqual("JPY 2.34", test.toString())

    def test_withCurrencyUnit_Currency_same(self) -> None:

        test = self.__GBP_2_34.withCurrencyUnit(self.__GBP)
        self.assertIs(self.__GBP_2_34, test)

    def test_withCurrencyUnit_Currency(self) -> None:

        test = self.__GBP_2_34.withCurrencyUnit(self.__USD)
        self.assertEqual("USD 2.34", test.toString())

    def test_getCurrencyUnit_EUR(self) -> None:

        # Assuming BigMoney.parse returns an instance of BigMoney
        big_money = BigMoney.parse("EUR -5.78")
        self.assertEqual(self.__EUR, big_money.getCurrencyUnit())

    def test_getCurrencyUnit_GBP(self) -> None:
        self.assertEqual(self.__GBP, self.__GBP_2_34.getCurrencyUnit())

    def test_scaleNormalization3(self) -> None:

        a = BigMoney.of0(self.__GBP, decimal.Decimal("100"))
        b = BigMoney.of0(self.__GBP, decimal.Decimal("1E+2"))

        self.assertEqual("GBP 100", a.toString())
        self.assertEqual("GBP 100", b.toString())
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

    def test_scaleNormalization2(self) -> None:

        a = BigMoney.ofScale2(self.__GBP, 1, 1)
        b = BigMoney.ofScale2(self.__GBP, 10, 2)

        self.assertEqual("GBP 0.1", a.toString())
        self.assertEqual("GBP 0.10", b.toString())
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(False, a.equals(b))
        self.assertEqual(False, b.equals(a))
        self.assertEqual(False, a.hashCode() == b.hashCode())

    def test_scaleNormalization1(self) -> None:

        a = BigMoney.ofScale2(TestBigMoney.__GBP, 100, 0)
        b = BigMoney.ofScale2(TestBigMoney.__GBP, 1, -2)

        self.assertEqual("GBP 100", a.toString())
        self.assertEqual("GBP 100", b.toString())
        self.assertEqual(True, a.equals(a))
        self.assertEqual(True, b.equals(b))
        self.assertEqual(True, a.equals(b))
        self.assertEqual(True, b.equals(a))
        self.assertEqual(True, a.hashCode() == b.hashCode())

    def test_constructor_null2(self) -> None:

        try:
            con = BigMoney.__init__
            con(0, None, self.__GBP)
            self.fail()
        except AssertionError:
            pass

    def test_constructor_null1(self) -> None:

        # Get the constructor of BigMoney class
        con = BigMoney.__init__

        # Check if the constructor is public
        self.assertTrue(inspect.isfunction(con))

        # Check if the constructor is not protected
        self.assertFalse(inspect.ismethod(con))

        # Try to create an instance of BigMoney with null currency
        try:
            con(0, self.__BIGDEC_2_34, None)
            self.fail()
        except AssertionError as ex:
            self.assertEqual(AssertionError, type(ex))

    def test_factory_parse_String_nullString(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.parse(None)

    def test_factory_parse_String_badCurrency(self) -> None:
        with pytest.raises(ValueError):
            BigMoney.parse("GBX 2.34")

    def test_factory_parse_String_exponent(self) -> None:
        with pytest.raises(ValueError):
            BigMoney.parse("GBP 234E2")

    def test_factory_parse_String_tooShort(self) -> None:
        with pytest.raises(ValueError):
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

        class BAD_PROVIDER(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        iterable = [BAD_PROVIDER()]
        with pytest.raises(NullPointerException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullNotFirst(self) -> None:

        iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_nullFirst(self) -> None:

        iterable = [None, self.__GBP_2_33, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable(
        self,
    ) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_currenciesDiffer(self) -> None:

        iterable = [self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total3(self.__GBP, iterable)

    def test_factory_total_CurrencyUnitIterable_empty(self) -> None:

        iterable: Iterable[BigMoney] = []
        test: BigMoney = BigMoney.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitIterable_Mixed(self) -> None:

        iterable = [self.__GBP_1_23.toMoney0(), self.__GBP_2_33]
        test = BigMoney.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("3.56"), test.getAmount())

    def test_factory_total_CurrencyUnitIterable(self) -> None:

        iterable = [self.__GBP_1_23, self.__GBP_2_33, BigMoney.of1(self.__GBP, 2.361)]
        test = BigMoney.total3(self.__GBP, iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(
            decimal.Decimal(5921) / decimal.Decimal(1000), test.getAmount()
        )

    def test_factory_total_CurrencyUnitArray_badProvider(self) -> None:

        class BadProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        self.__BAD_PROVIDER = BadProvider()
        array = [self.__BAD_PROVIDER]

        with self.assertRaises(NullPointerException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_badProvider(self) -> None:

        # Define a bad provider
        class BadProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        # Set the bad provider
        self.__BAD_PROVIDER = BadProvider()

        # Test that total2 raises a NullPointerException
        with pytest.raises(NullPointerException):
            BigMoney.total2(self.__GBP, [self.__BAD_PROVIDER])

    def test_factory_total_CurrencyUnitArray_nullNotFirst(self) -> None:

        array = [self.__GBP_2_33, None, self.__GBP_2_36]

        with pytest.raises(NullPointerException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullNotFirst(self) -> None:

        with pytest.raises(TypeError):
            BigMoney.total2(self.__GBP, [self.__GBP_2_33, None, self.__GBP_2_36])

    def test_factory_total_CurrencyUnitArray_nullFirst(self) -> None:

        array = [None, self.__GBP_2_33, self.__GBP_2_36]

        with pytest.raises(NullPointerException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_nullFirst(self) -> None:

        with pytest.raises(TypeError):
            BigMoney.total2(self.__GBP, None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_CurrencyUnitArray_currenciesDifferInArray(self) -> None:

        array = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray(self) -> None:

        with pytest.raises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, [self.__GBP_2_33, self.__JPY_423])

    def test_factory_total_CurrencyUnitArray_currenciesDiffer(self) -> None:

        array = [self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, array)

    def test_factory_total_CurrencyUnitVarargs_currenciesDiffer(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total2(self.__GBP, [self.__JPY_423])

    def test_factory_total_CurrencyUnitArray_empty(self) -> None:

        array = []
        test = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_empty(self) -> None:

        test = BigMoney.total2(self.__GBP, [])
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(0, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3Money(self) -> None:

        array = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36.toMoney0(),
        ]
        test = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3Mixed(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        test = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_3Mixed(self) -> None:

        test = BigMoney.total2(
            self.__GBP, [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_3(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
        test = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_3(self) -> None:

        test = BigMoney.total2(
            self.__GBP, [self.__GBP_1_23, self.__GBP_2_33, self.__GBP_2_36]
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitArray_1(self) -> None:

        array = [self.__GBP_1_23]
        test = BigMoney.total2(self.__GBP, array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_CurrencyUnitVarargs_1(self) -> None:

        test = BigMoney.total2(self.__GBP, [self.__GBP_1_23])
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_Iterable_badProvider(self) -> None:

        class BAD_PROVIDER(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        iterable = [BAD_PROVIDER()]
        with pytest.raises(NullPointerException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullNotFirst(self) -> None:

        iterable = [self.__GBP_2_33, None, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_nullFirst(self) -> None:

        iterable: Iterable[BigMoney] = [None, self.__GBP_2_33, self.__GBP_2_36]
        with pytest.raises(NullPointerException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_currenciesDiffer(self) -> None:

        iterable = [self.__GBP_2_33, self.__JPY_423]
        with pytest.raises(CurrencyMismatchException):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_empty(self) -> None:

        iterable = []
        with pytest.raises(ValueError):
            BigMoney.total1(iterable)

    def test_factory_total_Iterable_Mixed(self) -> None:

        iterable: Iterable[BigMoneyProvider] = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33,
        ]
        test: BigMoney = BigMoney.total1(iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("3.56"), test.getAmount())

    def test_factory_total_Iterable(self) -> None:

        iterable = [self.__GBP_1_23, self.__GBP_2_33, BigMoney.of1(self.__GBP, 2.361)]
        test = BigMoney.total1(iterable)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(
            decimal.Decimal(5921) / decimal.Decimal(1000), test.getAmount()
        )

    def test_factory_total_array_badProvider(self) -> None:

        class BadProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        array = [BadProvider()]
        with pytest.raises(NullPointerException):
            BigMoney.total0(array)

    def test_factory_total_varargs_badProvider(self) -> None:

        # Define a bad provider
        class BadProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        # Create an instance of the bad provider
        bad_provider = BadProvider()

        # Expect a NullPointerException when calling BigMoney.total0 with the bad provider
        with self.assertRaises(NullPointerException):
            BigMoney.total0([bad_provider])

    def test_factory_total_array_nullNotFirst(self) -> None:

        array = [self.__GBP_2_33, None, self.__GBP_2_36]

        with pytest.raises(NullPointerException):
            BigMoney.total0(array)

    def test_factory_total_varargs_nullNotFirst(self) -> None:
        with pytest.raises(TypeError):
            BigMoney.total0(self.__GBP_2_33, None, self.__GBP_2_36)

    def test_factory_total_array_nullFirst(self) -> None:

        array = [None, self.__GBP_2_33, self.__GBP_2_36]

        with pytest.raises(NullPointerException):
            BigMoney.total0(array)

    def test_factory_total_varargs_nullFirst(self) -> None:
        with pytest.raises(TypeError):
            BigMoney.total0(None, self.__GBP_2_33, self.__GBP_2_36)

    def test_factory_total_array_currenciesDiffer(self) -> None:

        array = [self.__GBP_2_33, self.__JPY_423]

        with pytest.raises(CurrencyMismatchException):
            BigMoney.total0(array)

    def test_factory_total_varargs_currenciesDiffer(self) -> None:

        with pytest.raises(CurrencyMismatchException):
            BigMoney.total0([self.__GBP_2_33, self.__JPY_423])

    def test_factory_total_array_empty(self) -> None:

        array = []
        with pytest.raises(ValueError):
            BigMoney.total0(array)

    def test_factory_total_varargs_empty(self) -> None:
        with pytest.raises(ValueError):
            BigMoney.total0()

    def test_factory_total_array_3Money(self) -> None:

        array = [
            self.__GBP_1_23.toMoney0(),
            self.__GBP_2_33.toMoney0(),
            self.__GBP_2_36.toMoney0(),
        ]
        test = BigMoney.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_array_3Mixed(self) -> None:

        array = [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        test = BigMoney.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_varargs_3Mixed(self) -> None:

        test = BigMoney.total0(
            [self.__GBP_1_23, self.__GBP_2_33.toMoney0(), self.__GBP_2_36]
        )
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(592, test.getAmountMinorInt())

    def test_factory_total_array_1BigMoney(self) -> None:

        array = [self.__GBP_1_23]
        test = BigMoney.total0(array)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_total_varargs_1BigMoney(self) -> None:

        test = BigMoney.total0([self.__GBP_1_23])
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(123, test.getAmountMinorInt())

    def test_factory_from_BigMoneyProvider_badProvider(self) -> None:

        # Define a bad provider
        class BadProvider(BigMoneyProvider):
            def toBigMoney(self) -> BigMoney:
                return None

        # Set the bad provider
        self.__BAD_PROVIDER = BadProvider()

        # Test that BigMoney.of2 raises a NullPointerException when given the bad provider
        with pytest.raises(NullPointerException):
            BigMoney.of2(self.__BAD_PROVIDER)

    def test_factory_from_BigMoneyProvider_nullBigMoneyProvider(self) -> None:
        with pytest.raises(TypeError):
            BigMoney.of2(None)

    def test_factory_from_BigMoneyProvider(self) -> None:

        test = BigMoney.of2(BigMoney.parse("GBP 104.23"))
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(10423, test.getAmountMinorInt())
        self.assertEqual(2, test.getScale())

    def test_factory_zero_Currency_int_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.zero1(None, 3)

    def test_factory_zero_Currency_int_negativeScale(self) -> None:

        test = BigMoney.zero1(self.__GBP, -3)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(0), test.getAmount())

    def test_factory_zero_Currency_int(self) -> None:

        test = BigMoney.zero1(self.__GBP, 3)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(
            decimal.Decimal(0).quantize(decimal.Decimal(".001")), test.getAmount()
        )

    def test_factory_zero_Currency_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.zero0(None)

    def test_factory_zero_Currency(self) -> None:

        test = BigMoney.zero0(self.__GBP)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(0), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_factory_ofMinor_Currency_long_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofMinor(None, 234)

    def test_factory_ofMinor_Currency_long(self) -> None:

        test = BigMoney.ofMinor(self.__GBP, 234)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__bd("2.34"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_factory_ofMajor_Currency_long_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofMajor(None, 234)

    def test_factory_ofMajor_Currency_long(self) -> None:

        test = BigMoney.ofMajor(self.__GBP, 234)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__bd("234"), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_factory_ofScale_Currency_long_int_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofScale2(None, 234, 2)

    def test_factory_ofScale_Currency_long_int_negativeScale(self) -> None:

        test = BigMoney.ofScale2(self.__GBP, 234, -4)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(2340000), test.getAmount())

    def test_factory_ofScale_Currency_long_int(self) -> None:

        test = BigMoney.ofScale2(self.__GBP, 234, 4)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(
            decimal.Decimal(234) / decimal.Decimal(10**4), test.getAmount()
        )

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullRoundingMode(
        self,
    ) -> None:
        with pytest.raises(TypeError):
            BigMoney.ofScale1(self.__GBP, self.__BIGDEC_2_34, 2, None)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullBigDecimal(
        self,
    ) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofScale1(self.__GBP, None, 2, RoundingMode.DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_nullCurrency(
        self,
    ) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofScale1(None, self.__BIGDEC_2_34, 2, RoundingMode.DOWN)

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_UNNECESSARY(
        self,
    ) -> None:
        with pytest.raises(ArithmeticException):
            BigMoney.ofScale1(
                self.__JPY, self.__BIGDEC_2_34, 1, RoundingMode.UNNECESSARY
            )

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_negativeScale(
        self,
    ) -> None:

        # Create a BigDecimal object with value 23400
        amount = decimal.Decimal(23400)

        # Call the ofScale1 method with the necessary parameters
        test = BigMoney.ofScale1(self.__GBP, amount, -2, decimal.ROUND_DOWN)

        # Assert that the currency unit is GBP
        self.assertEqual(self.__GBP, test.getCurrencyUnit())

        # Assert that the amount is equal to 23400
        self.assertEqual(decimal.Decimal(23400), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_int_JPY_RoundingMode_UP(self) -> None:

        test = BigMoney.ofScale1(self.__JPY, self.__BIGDEC_2_34, 0, decimal.ROUND_UP)
        self.assertEqual(self.__JPY, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("3"), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_int_RoundingMode_DOWN(self) -> None:

        test = BigMoney.ofScale1(self.__GBP, self.__BIGDEC_2_34, 1, decimal.ROUND_DOWN)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("23"), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_nullBigDecimal(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.ofScale0(self.__GBP, None, 2)

    def test_factory_ofScale_Currency_BigDecimal_nullCurrency(self) -> None:
        with pytest.raises(TypeError):
            BigMoney.ofScale0(None, self.__BIGDEC_2_34, 2)

    def test_factory_ofScale_Currency_BigDecimal_invalidScale(self) -> None:

        with pytest.raises(ArithmeticException):
            BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_345, 2)

    def test_factory_ofScale_Currency_BigDecimal_negativeScale(self) -> None:

        test = BigMoney.ofScale0(self.__GBP, decimal.Decimal(23400), -2)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(23400), test.getAmount())

    def test_factory_ofScale_Currency_BigDecimal_int(self) -> None:

        test = BigMoney.ofScale0(self.__GBP, self.__BIGDEC_2_34, 4)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(
            decimal.Decimal("23400") / decimal.Decimal("10000"), test.getAmount()
        )

    def test_factory_of_Currency_double_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.of1(None, 2.345)

    def test_factory_of_Currency_double_big(self) -> None:

        test = BigMoney.of1(self.__GBP, 200000000.0)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(200000000), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_factory_of_Currency_double_medium(self) -> None:

        test = BigMoney.of1(self.__GBP, 2000.0)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal(2000), test.getAmount())
        self.assertEqual(0, test.getScale())

    def test_factory_of_Currency_double_zero(self) -> None:

        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0)), BigMoney.of1(self.__GBP, 0.0)
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(-0)),
            BigMoney.of1(self.__GBP, -0.0),
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0.0)),
            BigMoney.of1(self.__GBP, 0.0),
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(0.00)),
            BigMoney.of1(self.__GBP, 0.00),
        )
        self.assertEqual(
            BigMoney.of0(self.__GBP, decimal.Decimal(-0.0)),
            BigMoney.of1(self.__GBP, -0.0),
        )

    def test_factory_of_Currency_double_trailingZero2(self) -> None:

        test = BigMoney.of1(self.__GBP, 1.20)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("1.20"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_factory_of_Currency_double_trailingZero1(self) -> None:

        test = BigMoney.of1(self.__GBP, 1.230)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(decimal.Decimal("1.23"), test.getAmount())
        self.assertEqual(2, test.getScale())

    def test_factory_of_Currency_double(self) -> None:

        test = BigMoney.of1(self.__GBP, 2.345)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__BIGDEC_2_345, test.getAmount())
        self.assertEqual(3, test.getScale())

    def test_factory_of_Currency_subClass2(self) -> None:

        class BadInteger(decimal.Decimal):
            __serialVersionUID: int = 1

            def __init__(self):
                super().__init__("123")

        class BadDecimal(decimal.Decimal):
            __serialVersionUID: int = 1

            def __init__(self):
                super().__init__("432")

            def unscaledValue(self) -> decimal.Decimal:
                return BadInteger()

            def scale(self) -> int:
                return 1

        sub = BadDecimal()
        test = BigMoney.of0(self.__GBP, sub)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__bd("12.3"), test.getAmount())
        self.assertEqual(1, test.getScale())
        self.assertEqual(True, type(test.getAmount()) == decimal.Decimal)

    def test_factory_of_Currency_subClass1(self) -> None:

        class BadDecimal(decimal.Decimal):
            __serialVersionUID: int = 1

            def __init__(self) -> None:
                super().__init__(432)

            @property
            def unscaledValue(self) -> decimal.Decimal:
                return None

            @property
            def scale(self) -> int:
                return 1

        sub = BadDecimal()
        with pytest.raises(ValueError):
            BigMoney.of0(self.__GBP, sub)

    def test_factory_of_Currency_BigDecimal_nullBigDecimal(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.of0(self.__GBP, None)

    def test_factory_of_Currency_BigDecimal_nullCurrency(self) -> None:
        with pytest.raises(NullPointerException):
            BigMoney.of0(None, self.__BIGDEC_2_345)

    def test_factory_of_Currency_BigDecimal(self) -> None:

        test = BigMoney.of0(self.__GBP, self.__BIGDEC_2_345)
        self.assertEqual(self.__GBP, test.getCurrencyUnit())
        self.assertEqual(self.__BIGDEC_2_345, test.getAmount())
        self.assertEqual(3, test.getScale())

    @staticmethod
    def __bd(str: str) -> decimal.Decimal:
        return decimal.Decimal(str)


TestBigMoney.initialize_fields()
