from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.test.org.joda.money.CurrencyUnitDataProvider_ESTest_scaffolding import *
from src.main.org.joda.money.DefaultCurrencyUnitDataProvider import *


class CurrencyUnitDataProvider_ESTest(unittest.TestCase):

    def test6(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()

        # Undeclared exception
        try:
            defaultCurrencyUnitDataProvider0._registerCurrency(None, 1, 1)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Currency code must not be null
            self.assertIsInstance(e, RuntimeError)
            self.verifyException("org.joda.money.MoneyUtils", e)

    def test5(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()

        with pytest.raises(RuntimeError):
            defaultCurrencyUnitDataProvider0._registerCountry(None, None)
            pytest.fail("Expecting exception: RuntimeError")

    def test4(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()

        with pytest.raises(RuntimeError):
            defaultCurrencyUnitDataProvider0._registerCountry(None, "CAD")

        # verifyException("java.util.concurrent.ConcurrentSkipListMap", e)
        # This line is not needed in Python as Python exceptions do not have a message.
        # If you want to check the exception type, you can use the isinstance() function.
        # assert isinstance(e, RuntimeError)

    def test3(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()

        with pytest.raises(ValueError):
            defaultCurrencyUnitDataProvider0._registerCountry(
                "CHF", "Currency code must not be null"
            )

        # verifyException("org.joda.money.CurrencyUnit", e)
        # This is a bit tricky because we don't have a direct equivalent in Python.
        # However, we can check if the exception message is as expected.
        assert "Unknown currency 'Currency code must not be null'" in str(e.value)

    def test2(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()

        try:
            defaultCurrencyUnitDataProvider0._registerCurrency("{(Zp?2", -369, 1512)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid string code, must be length 3
            self.verifyException("org.joda.money.CurrencyUnit", e)

    def test1(self) -> None:
        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()
        defaultCurrencyUnitDataProvider0._registerCountry("USD", "USD")

    def test0(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()
        defaultCurrencyUnitDataProvider0._registerCurrency("CHF", 3, 3)
