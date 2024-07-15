from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.MoneyUtils import *


class TestMoneyUtils_BigMoney(unittest.TestCase):

    __EUR_30: BigMoney = BigMoney.parse("EUR 30")
    __GBP_M30: BigMoney = BigMoney.parse("GBP -30")
    __GBP_M10: BigMoney = BigMoney.parse("GBP -10")
    __GBP_50: BigMoney = BigMoney.parse("GBP 50")
    __GBP_30: BigMoney = BigMoney.parse("GBP 30")
    __GBP_20: BigMoney = BigMoney.parse("GBP 20")
    __GBP_0: BigMoney = BigMoney.parse("GBP 0")

    def test_subtract_nullBoth(self) -> None:

        self.assertIsNone(MoneyUtils.subtract1(None, None))

    def test_subtract_null2(self) -> None:

        result = MoneyUtils.subtract1(self.__GBP_20, None)
        self.assertIs(self.__GBP_20, result)

    def test_subtract_null1(self) -> None:

        result = MoneyUtils.subtract1(None, self.__GBP_30)
        self.assertEqual(result, self.__GBP_M30)

    def test_subtract_differentCurrencies(self) -> None:

        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.subtract1(self.__GBP_20, self.__EUR_30)

    def test_subtract(self) -> None:

        result = MoneyUtils.subtract1(self.__GBP_20, self.__GBP_30)
        self.assertEqual(result, self.__GBP_M10)

    def test_add_nullBoth(self) -> None:
        self.assertIsNone(MoneyUtils.add1(None, None))

    def test_add_null2(self) -> None:
        self.assertEqual(MoneyUtils.add1(self.__GBP_20, None), self.__GBP_20)

    def test_add_null1(self) -> None:
        self.assertEqual(MoneyUtils.add1(None, self.__GBP_30), self.__GBP_30)

    def test_add_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.add1(self.__GBP_20, self.__EUR_30)

    def test_add(self) -> None:
        self.assertEqual(self.__GBP_50, MoneyUtils.add1(self.__GBP_20, self.__GBP_30))

    def test_min_nullBoth(self) -> None:
        self.assertEqual(None, MoneyUtils.min1(None, None))

    def test_min_null2(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.min1(self.__GBP_20, None))

    def test_min_null1(self) -> None:
        self.assertEqual(MoneyUtils.min1(None, self.__GBP_30), self.__GBP_30)

    def test_min_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.min1(self.__GBP_20, self.__EUR_30)

    def test_min2(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.min1(self.__GBP_30, self.__GBP_20))

    def test_min1(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.min1(self.__GBP_20, self.__GBP_30))

    def test_max_nullBoth(self) -> None:
        self.assertEqual(None, MoneyUtils.max1(None, None))

    def test_max_null2(self) -> None:
        self.assertEqual(self.__GBP_20, MoneyUtils.max1(self.__GBP_20, None))

    def test_max_null1(self) -> None:
        self.assertEqual(MoneyUtils.max1(None, self.__GBP_30), self.__GBP_30)

    def test_max_differentCurrencies(self) -> None:
        with pytest.raises(CurrencyMismatchException):
            MoneyUtils.max1(self.__GBP_20, self.__EUR_30)

    def test_max2(self) -> None:
        self.assertEqual(MoneyUtils.max1(self.__GBP_30, self.__GBP_20), self.__GBP_30)

    def test_max1(self) -> None:
        self.assertEqual(MoneyUtils.max1(self.__GBP_30, self.__GBP_20), self.__GBP_30)

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

        # Test with None
        self.assertFalse(MoneyUtils.isPositive(None))

        # Test with GBP_0
        self.assertFalse(MoneyUtils.isPositive(self.__GBP_0))

        # Test with GBP_30
        self.assertTrue(MoneyUtils.isPositive(self.__GBP_30))

        # Test with GBP_M30
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

    def test_constructor(self) -> None:

        con = MoneyUtils.__class__.getDeclaredConstructor()
        self.assertTrue(Modifier.isPrivate(con.getModifiers()))
        con.setAccessible(True)
        con.newInstance()
