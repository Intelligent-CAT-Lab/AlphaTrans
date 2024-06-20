from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyFormatException import *
import unittest
import io

# Imports End


class TestMoneyFormatterException(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_MoneyFormatException_nonIOException_notRethrown(self) -> None:
        pass

    def test_MoneyFormatException_IOException_notRethrown(self) -> None:
        pass

    # Class Methods End
