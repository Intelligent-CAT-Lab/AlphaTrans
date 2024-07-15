from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.CurrencyUnit import *


class TestCurrencyMismatchException(unittest.TestCase):

    __EUR: CurrencyUnit = CurrencyUnit.of1("EUR")
    __GBP: CurrencyUnit = CurrencyUnit.of1("GBP")

    def test_new_nullnull(self) -> None:
        test = CurrencyMismatchException(None, None)
        self.assertEqual("Currencies differ: null/null", test.getMessage())
        self.assertEqual(None, test.getCause())
        self.assertEqual(None, test.getFirstCurrency())
        self.assertEqual(None, test.getSecondCurrency())

    def test_new_GBPnull(self) -> None:
        test = CurrencyMismatchException(self.__GBP, None)
        self.assertEqual("Currencies differ: GBP/null", test.getMessage())
        self.assertEqual(None, test.getCause())
        self.assertEqual(self.__GBP, test.getFirstCurrency())
        self.assertEqual(None, test.getSecondCurrency())

    def test_new_nullEUR(self) -> None:
        test = CurrencyMismatchException(None, self.__EUR)
        self.assertEqual("Currencies differ: null/EUR", test.getMessage())
        self.assertEqual(None, test.getCause())
        self.assertEqual(None, test.getFirstCurrency())
        self.assertEqual(self.__EUR, test.getSecondCurrency())

    def test_new_GBPEUR(self) -> None:
        test = CurrencyMismatchException(self.__GBP, self.__EUR)
        self.assertEqual("Currencies differ: GBP/EUR", test.getMessage())
        self.assertEqual(None, test.getCause())
        self.assertEqual(self.__GBP, test.getFirstCurrency())
        self.assertEqual(self.__EUR, test.getSecondCurrency())
