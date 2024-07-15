from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.MoneyUtils import *


class TestMoneyUtils_Money(unittest.TestCase):

    __EUR_30: Money = Money.parse("EUR 30")
    __GBP_M30: Money = Money.parse("GBP -30")
    __GBP_M10: Money = Money.parse("GBP -10")
    __GBP_50: Money = Money.parse("GBP 50")
    __GBP_30: Money = Money.parse("GBP 30")
    __GBP_20: Money = Money.parse("GBP 20")
    __GBP_0: Money = Money.parse("GBP 0")

    def test_subtract_nullBoth(self) -> None:
        self.assertEqual(None, MoneyUtils.subtract0(None, None))

    def test_subtract_null2(self) -> None:
        self.assertEqual(MoneyUtils.subtract0(self.__GBP_20, None), self.__GBP_20)

    def test_subtract_null1(self) -> None:
        self.assertEqual(self.__GBP_M30, MoneyUtils.subtract0(None, self.__GBP_30))

    def test_subtract_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.subtract0(self.__GBP_20, self.__EUR_30)

    def test_subtract(self) -> None:
        self.assertEqual(
            self.__GBP_M10, MoneyUtils.subtract0(self.__GBP_20, self.__GBP_30)
        )

    def test_add_nullBoth(self) -> None:
        self.assertIsNone(MoneyUtils.add0(None, None))

    def test_add_null2(self) -> None:
        self.assertEqual(MoneyUtils.add0(self.__GBP_20, None), self.__GBP_20)

    def test_add_null1(self) -> None:
        self.assertEqual(MoneyUtils.add0(None, self.__GBP_30), self.__GBP_30)

    def test_add_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.add0(self.__GBP_20, self.__EUR_30)

    def test_add(self) -> None:
        self.assertEqual(self.__GBP_50, MoneyUtils.add0(self.__GBP_20, self.__GBP_30))

    def test_min_nullBoth(self) -> None:
        self.assertEqual(None, MoneyUtils.min0(None, None))

    def test_min_null2(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.min0(self.__GBP_20, None))

    def test_min_null1(self) -> None:
        self.assertEqual(MoneyUtils.min0(None, self.__GBP_30), self.__GBP_30)

    def test_min_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.min0(self.__GBP_20, self.__EUR_30)

    def test_min2(self) -> None:
        self.assertEqual(MoneyUtils.min0(self.__GBP_30, self.__GBP_20), self.__GBP_20)

    def test_min1(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.min0(self.__GBP_20, self.__GBP_30))

    def test_max_nullBoth(self) -> None:
        self.assertEqual(None, MoneyUtils.max0(None, None))

    def test_max_null2(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.max0(self.__GBP_20, None))

    def test_max_null1(self) -> None:
        self.assertEqual(MoneyUtils.max0(None, self.__GBP_30), self.__GBP_30)

    def test_max_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.max0(self.__GBP_20, self.__EUR_30)

    def test_max2(self) -> None:
        self.assertEqual(MoneyUtils.max0(self.__GBP_30, self.__GBP_20), self.__GBP_30)

    def test_max1(self) -> None:
        self.assertEqual(MoneyUtils.max0(self.__GBP_30, self.__GBP_20), self.__GBP_30)

    def test_isNegativeOrZero(self) -> None:

        assert MoneyUtils.isNegativeOrZero(None) == True
        assert MoneyUtils.isNegativeOrZero(self.__GBP_0) == True
        assert MoneyUtils.isNegativeOrZero(self.__GBP_30) == False
        assert MoneyUtils.isNegativeOrZero(self.__GBP_M30) == True

    def test_isNegative(self) -> None:

        self.assertFalse(MoneyUtils.isNegative(None))
        self.assertFalse(MoneyUtils.isNegative(self.__GBP_0))
        self.assertFalse(MoneyUtils.isNegative(self.__GBP_30))
        self.assertTrue(MoneyUtils.isNegative(self.__GBP_M30))

    def test_isPositiveOrZero(self) -> None:

        assert MoneyUtils.isPositiveOrZero(None)
        assert MoneyUtils.isPositiveOrZero(self.__GBP_0)
        assert MoneyUtils.isPositiveOrZero(self.__GBP_30)
        assert not MoneyUtils.isPositiveOrZero(self.__GBP_M30)

    def test_isPositive(self) -> None:

        self.assertFalse(MoneyUtils.isPositive(None))
        self.assertFalse(MoneyUtils.isPositive(self.__GBP_0))
        self.assertTrue(MoneyUtils.isPositive(self.__GBP_30))
        self.assertFalse(MoneyUtils.isPositive(self.__GBP_M30))

    def test_isZero(self) -> None:

        # Test with None
        self.assertTrue(MoneyUtils.isZero(None))

        # Test with GBP_0
        self.assertTrue(MoneyUtils.isZero(self.__GBP_0))

        # Test with GBP_30
        self.assertFalse(MoneyUtils.isZero(self.__GBP_30))

        # Test with GBP_M30
        self.assertFalse(MoneyUtils.isZero(self.__GBP_M30))

    def test_checkNotNull_null(self) -> None:
        with pytest.raises(ValueError) as ex:
            MoneyUtils.checkNotNull(None, "Hello")
        assert str(ex.value) == "Hello"

    def test_checkNotNull_notNull(self) -> None:
        MoneyUtils.checkNotNull(object(), "")
