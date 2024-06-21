from __future__ import annotations
import io
import os
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.BigMoneyProvider import *
from src.main.org.joda.money.MoneyUtils import *


class TestMoneyUtils_BigMoney:

    __EUR_30: BigMoney = BigMoney.parse("EUR 30")

    __GBP_M30: BigMoney = BigMoney.parse("GBP -30")

    __GBP_M10: BigMoney = BigMoney.parse("GBP -10")

    __GBP_50: BigMoney = BigMoney.parse("GBP 50")

    __GBP_30: BigMoney = BigMoney.parse("GBP 30")

    __GBP_20: BigMoney = BigMoney.parse("GBP 20")

    __GBP_0: BigMoney = BigMoney.parse("GBP 0")

    def test_subtract_nullBoth(self) -> None:

        # The 'assertEquals' method in Java is equivalent to 'assert' in Python.
        # The 'null' in Java is equivalent to 'None' in Python.
        # The 'subtract1' method is called from the 'MoneyUtils' class.
        # The 'MoneyUtils' class is imported at the top of the file.

        assert MoneyUtils.subtract1(None, None) is None

    def test_subtract_null2(self) -> None:

        assert MoneyUtils.subtract1(self.__GBP_20, None) == self.__GBP_20

    def test_subtract_null1(self) -> None:

        # Call the subtract1 method from MoneyUtils class
        result = MoneyUtils.subtract1(None, self.__GBP_30)

        # Assert the result
        self.assertEqual(self.__GBP_M30, result)

    def test_subtract_differentCurrencies(self) -> None:

        MoneyUtils.subtract1(self.__GBP_20, self.__EUR_30)

    def test_subtract(self) -> None:

        assert self.__GBP_M10 == MoneyUtils.subtract1(self.__GBP_20, self.__GBP_30)

    def test_add_nullBoth(self) -> None:

        # The 'assertEquals' method in Java is equivalent to 'assert' in Python.
        # The 'null' in Java is equivalent to 'None' in Python.
        # The 'MoneyUtils.add1' method is equivalent to 'MoneyUtils.add1' in Python.
        # The '(BigMoney) null' in Java is equivalent to 'None' in Python.

        assert MoneyUtils.add1(None, None) is None

    def test_add_null2(self) -> None:

        assert MoneyUtils.add1(self.__GBP_20, None) == self.__GBP_20

    def test_add_null1(self) -> None:

        assert MoneyUtils.add1(None, self.__GBP_30) == self.__GBP_30

    def test_add_differentCurrencies(self) -> None:

        MoneyUtils.add1(self.__GBP_20, self.__EUR_30)

    def test_add(self) -> None:

        assert self.__GBP_50 == MoneyUtils.add1(self.__GBP_20, self.__GBP_30)

    def test_min_nullBoth(self) -> None:

        # The 'assertEquals' method in Java is equivalent to 'assert' in Python.
        # The 'null' in Java is equivalent to 'None' in Python.
        # The 'MoneyUtils.min1' method is equivalent to 'MoneyUtils.min1' in Python.
        # The '(BigMoney) null' in Java is equivalent to 'None' in Python.

        assert MoneyUtils.min1(None, None) is None

    def test_min_null2(self) -> None:

        assert TestMoneyUtils_BigMoney.__GBP_20 == MoneyUtils.min1(
            TestMoneyUtils_BigMoney.__GBP_20, None
        )

    def test_min_null1(self) -> None:

        assert self.__GBP_30 == MoneyUtils.min1(None, self.__GBP_30)

    def test_min_differentCurrencies(self) -> None:

        MoneyUtils.min1(self.__GBP_20, self.__EUR_30)

    def test_min2(self) -> None:

        assert MoneyUtils.min1(self.__GBP_30, self.__GBP_20) == self.__GBP_20

    def test_min1(self) -> None:

        assert self.__GBP_20 == MoneyUtils.min1(self.__GBP_20, self.__GBP_30)

    def test_max_nullBoth(self) -> None:

        # The 'assertEquals' method in Java is equivalent to 'assert' in Python.
        # The 'null' in Java is equivalent to 'None' in Python.
        # The 'MoneyUtils.max1' method is equivalent to 'MoneyUtils.max1' in Python.
        # The '(BigMoney) null' in Java is equivalent to 'None' in Python.

        assert MoneyUtils.max1(None, None) is None

    def test_max_null2(self) -> None:

        assert self.__GBP_20 == MoneyUtils.max1(self.__GBP_20, None)

    def test_max_null1(self) -> None:

        assert MoneyUtils.max1(None, self.__GBP_30) == self.__GBP_30

    def test_max_differentCurrencies(self) -> None:

        MoneyUtils.max1(self.__GBP_20, self.__EUR_30)

    def test_max2(self) -> None:

        assert MoneyUtils.max1(self.__GBP_30, self.__GBP_20) == self.__GBP_30

    def test_max1(self) -> None:

        assert MoneyUtils.max1(self.__GBP_20, self.__GBP_30) == self.__GBP_30

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

    def test_constructor(self) -> None:

        # Get the constructor of the MoneyUtils class
        con = MoneyUtils.__class__.__init__

        # Check if the constructor is private
        assert inspect.isfunction(con)

        # Make the constructor accessible
        con.__globals__[con.__name__] = con

        # Create an instance of the MoneyUtils class
        con()
