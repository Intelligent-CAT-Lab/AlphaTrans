from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest

# from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *
from src.main.org.joda.money.Money import *


class TestStringConvert(unittest.TestCase):

    def test_CurrencyUnit(self) -> None:
        test: CurrencyUnit = CurrencyUnit.CHF
        str: str = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str, "CHF")
        self.assertEqual(
            test, StringConvert.INSTANCE.convertFromString(CurrencyUnit, str)
        )

    def test_Money(self) -> None:
        test: Money = Money.of2(CurrencyUnit.CHF, 1234.56)
        str: str = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str, "CHF 1234.56")
        self.assertEqual(test, StringConvert.INSTANCE.convertFromString(Money, str))

    def test_BigMoney(self) -> None:
        test = BigMoney.of1(CurrencyUnit.CHF, 1234.5678)
        str = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str, "CHF 1234.5678")
        self.assertEqual(test, StringConvert.INSTANCE.convertFromString(BigMoney, str))
