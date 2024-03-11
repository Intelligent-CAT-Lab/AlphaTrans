# Imports Begin
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.CurrencyMismatchException import *
import unittest

# Imports End


class TestCurrencyMismatchException(unittest.TestCase):

    # Class Fields Begin
    __GBP: CurrencyUnit = CurrencyUnit.of1("GBP")
    __EUR: CurrencyUnit = CurrencyUnit.of1("EUR")
    # Class Fields End

    # Class Methods Begin
    def test_new_nullnull(self) -> None:

        pass  # LLM could not translate method body

    def test_new_GBPnull(self) -> None:

        pass  # LLM could not translate method body

    def test_new_nullEUR(self) -> None:

        pass  # LLM could not translate method body

    def test_new_GBPEUR(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
