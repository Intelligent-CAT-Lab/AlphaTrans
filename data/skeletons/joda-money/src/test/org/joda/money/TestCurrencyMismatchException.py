from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.CurrencyMismatchException import *
import unittest
import io

# Imports End


class TestCurrencyMismatchException(unittest.TestCase):

    # Class Fields Begin
    __GBP: CurrencyUnit = None
    __EUR: CurrencyUnit = None
    # Class Fields End

    # Class Methods Begin
    def test_new_nullnull(self) -> None:
        pass

    def test_new_GBPnull(self) -> None:
        pass

    def test_new_nullEUR(self) -> None:
        pass

    def test_new_GBPEUR(self) -> None:
        pass

    # Class Methods End
