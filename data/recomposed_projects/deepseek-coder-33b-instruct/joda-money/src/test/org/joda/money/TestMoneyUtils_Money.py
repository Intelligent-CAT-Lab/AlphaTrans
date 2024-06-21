from __future__ import annotations
import io
import os
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.Money import *
from src.main.org.joda.money.MoneyUtils import *


class TestMoneyUtils_Money:

    __EUR_30: Money = Money.parse("EUR 30")

    __GBP_M30: Money = Money.parse("GBP -30")

    __GBP_M10: Money = Money.parse("GBP -10")

    __GBP_50: Money = Money.parse("GBP 50")

    __GBP_30: Money = Money.parse("GBP 30")

    __GBP_20: Money = Money.parse("GBP 20")

    __GBP_0: Money = Money.parse("GBP 0")

    def test_subtract_nullBoth(self) -> None:

        # Call the subtract0 method from MoneyUtils class
        result = MoneyUtils.subtract0(None, None)

        # Assert that the result is None
        assert result is None

    def test_subtract_null2(self) -> None:

        assert MoneyUtils.subtract0(self.__GBP_20, None) == self.__GBP_20

    def test_subtract_null1(self) -> None:

        assert MoneyUtils.subtract0(None, self.__GBP_30) == self.__GBP_M30

    def test_subtract_differentCurrencies(self) -> None:

        MoneyUtils.subtract0(self.__GBP_20, self.__EUR_30)

    def test_subtract(self) -> None:

        assert self.__GBP_M10 == MoneyUtils.subtract0(self.__GBP_20, self.__GBP_30)

    def test_add_nullBoth(self) -> None:

        # Call the method from MoneyUtils class
        result = MoneyUtils.add0(None, None)

        # Assert the result
        self.assertEqual(None, result)

    def test_add_null2(self) -> None:

        assert self.__GBP_20 == MoneyUtils.add0(self.__GBP_20, None)

    def test_add_null1(self) -> None:

        assert TestMoneyUtils_Money.__GBP_30 == MoneyUtils.add0(
            None, TestMoneyUtils_Money.__GBP_30
        )

    def test_add_differentCurrencies(self) -> None:

        MoneyUtils.add0(self.__GBP_20, self.__EUR_30)

    def test_add(self) -> None:

        assert self.__GBP_50 == MoneyUtils.add0(self.__GBP_20, self.__GBP_30)

    def test_min_nullBoth(self) -> None:

        assert MoneyUtils.min0(None, None) is None

    def test_min_null2(self) -> None:

        assert self.__GBP_20 is MoneyUtils.min0(self.__GBP_20, None)

    def test_min_null1(self) -> None:

        assert self.__GBP_30 == MoneyUtils.min0(None, self.__GBP_30)

    def test_min_differentCurrencies(self) -> None:

        MoneyUtils.min0(self.__GBP_20, self.__EUR_30)

    def test_min2(self) -> None:

        assert self.__GBP_20 == MoneyUtils.min0(self.__GBP_30, self.__GBP_20)

    def test_min1(self) -> None:

        assert self.__GBP_20 == MoneyUtils.min0(self.__GBP_20, self.__GBP_30)

    def test_max_nullBoth(self) -> None:

        # Call the method from MoneyUtils class
        result = MoneyUtils.max0(None, None)

        # Assert the result
        self.assertEqual(None, result)

    def test_max_null2(self) -> None:

        assert self.__GBP_20 is MoneyUtils.max0(self.__GBP_20, None)

    def test_max_null1(self) -> None:

        assert self.__GBP_30 == MoneyUtils.max0(None, self.__GBP_30)

    def test_max_differentCurrencies(self) -> None:

        MoneyUtils.max0(self.__GBP_20, self.__EUR_30)

    def test_max2(self) -> None:

        assert self.__GBP_30 == MoneyUtils.max0(self.__GBP_30, self.__GBP_20)

    def test_max1(self) -> None:

        assert self.__GBP_30 == MoneyUtils.max0(self.__GBP_20, self.__GBP_30)

    def test_isNegativeOrZero(self) -> None:

        assert MoneyUtils.isNegativeOrZero(None)
        assert MoneyUtils.isNegativeOrZero(self.__GBP_0)
        assert not MoneyUtils.isNegativeOrZero(self.__GBP_30)
        assert MoneyUtils.isNegativeOrZero(self.__GBP_M30)

    def test_isNegative(self) -> None:

        assert not MoneyUtils.isNegative(None)
        assert not MoneyUtils.isNegative(self.__GBP_0)
        assert not MoneyUtils.isNegative(self.__GBP_30)
        assert MoneyUtils.isNegative(self.__GBP_M30)

    def test_isPositiveOrZero(self) -> None:

        assert MoneyUtils.isPositiveOrZero(None)
        assert MoneyUtils.isPositiveOrZero(self.__GBP_0)
        assert MoneyUtils.isPositiveOrZero(self.__GBP_30)
        assert not MoneyUtils.isPositiveOrZero(self.__GBP_M30)

    def test_isPositive(self) -> None:

        assert not MoneyUtils.isPositive(None)
        assert not MoneyUtils.isPositive(self.__GBP_0)
        assert MoneyUtils.isPositive(self.__GBP_30)
        assert not MoneyUtils.isPositive(self.__GBP_M30)

    def test_isZero(self) -> None:

        assert MoneyUtils.isZero(None)
        assert MoneyUtils.isZero(self.__GBP_0)
        assert not MoneyUtils.isZero(self.__GBP_30)
        assert not MoneyUtils.isZero(self.__GBP_M30)

    def test_checkNotNull_null(self) -> None:

        try:
            MoneyUtils.checkNotNull(None, "Hello")
        except NullPointerException as ex:
            self.assertEqual("Hello", str(ex))
            raise ex

    def test_checkNotNull_notNull(self) -> None:

        # Create an instance of the MoneyUtils class
        money_utils = MoneyUtils()

        # Call the checkNotNull method
        money_utils.checkNotNull(object(), "")
