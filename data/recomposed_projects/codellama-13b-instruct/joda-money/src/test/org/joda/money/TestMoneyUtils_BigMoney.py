# Imports Begin
from src.main.org.joda.money.MoneyUtils import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.BigMoney import *
import unittest
import os

# Imports End


class TestMoneyUtils_BigMoney(unittest.TestCase):

    # Class Fields Begin
    __GBP_0: BigMoney = BigMoney.parse("GBP 0")
    __GBP_20: BigMoney = BigMoney.parse("GBP 20")
    __GBP_30: BigMoney = BigMoney.parse("GBP 30")
    __GBP_50: BigMoney = BigMoney.parse("GBP 50")
    __GBP_M10: BigMoney = BigMoney.parse("GBP -10")
    __GBP_M30: BigMoney = BigMoney.parse("GBP -30")
    __EUR_30: BigMoney = BigMoney.parse("EUR 30")
    # Class Fields End

    # Class Methods Begin
    def test_subtract_nullBoth(self) -> None:

        self.assertEqual(None, MoneyUtils.subtract1(None, None))

    def test_subtract_null2(self) -> None:

        assertSame(self.__GBP_20, MoneyUtils.subtract1(self.__GBP_20, None))

    def test_subtract_null1(self) -> None:

        self.assertEqual(self.__GBP_M30, self.subtract1(None, self.__GBP_30))

    def test_subtract_differentCurrencies(self) -> None:

        MoneyUtils.subtract1(self.__GBP_20, self.__EUR_30)

    def test_subtract(self) -> None:

        self.assertEqual(self.__GBP_M10, self.subtract1(self.__GBP_20, self.__GBP_30))

    def test_add_nullBoth(self) -> None:

        self.assertEqual(None, MoneyUtils.add1(None, None))

    def test_add_null2(self) -> None:

        self.assertIs(self.__GBP_20, MoneyUtils.add1(self.__GBP_20, None))

    def test_add_null1(self) -> None:

        self.assertIs(self.__GBP_30, MoneyUtils.add1(None, self.__GBP_30))

    def test_add_differentCurrencies(self) -> None:

        MoneyUtils.add1(self.__GBP_20, self.__EUR_30)

    def test_add(self) -> None:

        pass  # LLM could not translate method body

    def test_min_nullBoth(self) -> None:

        self.assertIsNone(MoneyUtils.min1(None, None))

    def test_min_null2(self) -> None:

        self.assertIs(self.__GBP_20, MoneyUtils.min1(self.__GBP_20, None))

    def test_min_null1(self) -> None:

        self.assertIs(self.__GBP_30, MoneyUtils.min1(None, self.__GBP_30))

    def test_min_differentCurrencies(self) -> None:

        self.min1(self.__GBP_20, self.__EUR_30)

    def test_min2(self) -> None:

        self.assertIs(self.__GBP_20, MoneyUtils.min1(self.__GBP_30, self.__GBP_20))

    def test_min1(self) -> None:

        self.assertIs(self.__GBP_20, MoneyUtils.min1(self.__GBP_20, self.__GBP_30))

    def test_max_nullBoth(self) -> None:

        self.assertEqual(None, MoneyUtils.max1(None, None))

    def test_max_null2(self) -> None:

        self.assertIs(self.__GBP_20, MoneyUtils.max1(self.__GBP_20, None))

    def test_max_null1(self) -> None:

        self.assertIs(self.__GBP_30, MoneyUtils.max1(None, self.__GBP_30))

    def test_max_differentCurrencies(self) -> None:

        MoneyUtils.max1(self.__GBP_20, self.__EUR_30)

    def test_max2(self) -> None:

        self.assertIs(self.__GBP_30, MoneyUtils.max1(self.__GBP_30, self.__GBP_20))

    def test_max1(self) -> None:

        self.assertIs(self.__GBP_30, MoneyUtils.max1(self.__GBP_20, self.__GBP_30))

    def test_isNegativeOrZero(self) -> None:

        self.assertTrue(MoneyUtils.isNegativeOrZero(None))
        self.assertTrue(MoneyUtils.isNegativeOrZero(self.__GBP_0))
        self.assertFalse(MoneyUtils.isNegativeOrZero(self.__GBP_30))
        self.assertTrue(MoneyUtils.isNegativeOrZero(self.__GBP_M30))

    def test_isNegative(self) -> None:

        pass  # LLM could not translate method body

    def test_isPositiveOrZero(self) -> None:

        self.assertTrue(MoneyUtils.isPositiveOrZero(None))
        self.assertTrue(MoneyUtils.isPositiveOrZero(self.__GBP_0))
        self.assertTrue(MoneyUtils.isPositiveOrZero(self.__GBP_30))
        self.assertFalse(MoneyUtils.isPositiveOrZero(self.__GBP_M30))

    def test_isPositive(self) -> None:

        self.assertFalse(MoneyUtils.isPositive(None))
        self.assertFalse(MoneyUtils.isPositive(self.__GBP_0))
        self.assertTrue(MoneyUtils.isPositive(self.__GBP_30))
        self.assertFalse(MoneyUtils.isPositive(self.__GBP_M30))

    def test_isZero(self) -> None:

        pass  # LLM could not translate method body

    def test_constructor(self) -> None:

        con = MoneyUtils.__init__
        assert con.modifiers == Modifier.PRIVATE
        con.setAccessible(True)
        con.newInstance()

    # Class Methods End
