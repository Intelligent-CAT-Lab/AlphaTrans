from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.CurrencyUnit import *


class TestCurrencyMismatchException(unittest.TestCase):

    __EUR: CurrencyUnit = CurrencyUnit.of("EUR")
    __GBP: CurrencyUnit = CurrencyUnit.of("GBP")

    def test_new_nullnull(self) -> None:

        test = CurrencyMismatchException(None, None)
        self.assertEqual("Currencies differ: null/null", test.getMessage())
        self.assertEqual(None, test.getCause())
        self.assertEqual(None, test.getFirstCurrency())
        self.assertEqual(None, test.getSecondCurrency())

    def test_new_GBPnull(self) -> None:

        # Create an instance of CurrencyMismatchException
        test = CurrencyMismatchException(self.__GBP, None)

        # Assert that the message is as expected
        self.assertEqual("Currencies differ: GBP/null", test.getMessage())

        # Assert that the cause is None
        self.assertEqual(None, test.getCause())

        # Assert that the first currency is GBP
        self.assertEqual(self.__GBP, test.getFirstCurrency())

        # Assert that the second currency is None
        self.assertEqual(None, test.getSecondCurrency())

    def test_new_nullEUR(self) -> None:

        # Create an instance of CurrencyMismatchException with null and EUR
        test = CurrencyMismatchException(None, self.__EUR)

        # Assert that the message is "Currencies differ: null/EUR"
        self.assertEqual("Currencies differ: null/EUR", test.getMessage())

        # Assert that the cause is None
        self.assertEqual(None, test.getCause())

        # Assert that the first currency is None
        self.assertEqual(None, test.getFirstCurrency())

        # Assert that the second currency is EUR
        self.assertEqual(self.__EUR, test.getSecondCurrency())

    def test_new_GBPEUR(self) -> None:

        # Create an instance of CurrencyMismatchException
        test = CurrencyMismatchException(self.__GBP, self.__EUR)

        # Assert that the message is as expected
        self.assertEqual("Currencies differ: GBP/EUR", test.getMessage())

        # Assert that the cause is None
        self.assertEqual(None, test.getCause())

        # Assert that the first currency is GBP
        self.assertEqual(self.__GBP, test.getFirstCurrency())

        # Assert that the second currency is EUR
        self.assertEqual(self.__EUR, test.getSecondCurrency())
