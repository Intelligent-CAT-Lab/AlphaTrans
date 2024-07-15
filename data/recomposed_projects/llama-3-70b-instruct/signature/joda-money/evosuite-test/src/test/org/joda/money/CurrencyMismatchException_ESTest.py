from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.CurrencyMismatchException import *

# from src.test.org.joda.money.CurrencyMismatchException_ESTest_scaffolding import *
from src.main.org.joda.money.CurrencyUnit import *


class CurrencyMismatchException_ESTest(unittest.TestCase):

    def test7(self) -> None:

        currencyUnit0 = CurrencyUnit("Uk\tvgjlFlIk%}5W", -2117, -2117)
        currencyMismatchException0 = CurrencyMismatchException(
            currencyUnit0, currencyUnit0
        )
        currencyUnit1 = currencyMismatchException0.getFirstCurrency()
        self.assertIs(currencyUnit1, currencyUnit0)

    def test6(self) -> None:

        currencyUnit0 = CurrencyUnit("Uk\tvgjlFlIk%}5W", -2117, -2117)
        currencyMismatchException0 = CurrencyMismatchException(
            currencyUnit0, currencyUnit0
        )
        currencyUnit1 = currencyMismatchException0.getSecondCurrency()
        self.assertEqual("Uk\tvgjlFlIk%}5W", currencyUnit1.getCode())

    def test5(self) -> None:

        currencyMismatchException0 = CurrencyMismatchException(None, None)
        currencyUnit0 = currencyMismatchException0.getFirstCurrency()
        self.assertIsNone(currencyUnit0)

    def test4(self) -> None:

        currencyUnit0 = CurrencyUnit("", 0, 716)
        currencyMismatchException0 = CurrencyMismatchException(
            currencyUnit0, currencyUnit0
        )
        currencyUnit1 = currencyMismatchException0.getFirstCurrency()
        self.assertIs(currencyUnit1, currencyUnit0)

    def test3(self) -> None:

        currencyUnit0 = CurrencyUnit.EUR
        currencyMismatchException0 = CurrencyMismatchException(
            currencyUnit0, currencyUnit0
        )
        currencyUnit1 = currencyMismatchException0.getFirstCurrency()
        assert not currencyUnit1.isPseudoCurrency()

    def test2(self) -> None:

        currencyUnit0 = CurrencyUnit.CAD
        currencyMismatchException0 = CurrencyMismatchException(
            currencyUnit0, currencyUnit0
        )
        currencyUnit1 = currencyMismatchException0.getSecondCurrency()
        self.assertIs(currencyUnit0, currencyUnit1)

    def test1(self) -> None:

        currencyUnit0 = CurrencyUnit("", 0, 716)
        currencyMismatchException0 = CurrencyMismatchException(
            currencyUnit0, currencyUnit0
        )
        currencyUnit1 = currencyMismatchException0.getSecondCurrency()
        self.assertFalse(currencyUnit1.isPseudoCurrency())

    def test0(self) -> None:

        currencyMismatchException0 = CurrencyMismatchException(None, None)
        currencyUnit0 = currencyMismatchException0.getSecondCurrency()
        self.assertIsNone(currencyUnit0)
