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

        test = CurrencyUnit.CHF
        str = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str, "CHF")
        self.assertEqual(
            test, StringConvert.INSTANCE.convertFromString(CurrencyUnit, str)
        )

    def test_Money(self) -> None:

        test = Money.of2(CurrencyUnit.CHF, 1234.56)
        str_val = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str_val, "CHF 1234.56")
        self.assertEqual(test, StringConvert.INSTANCE.convertFromString(Money, str_val))

    def test_BigMoney(self) -> None:

        test = BigMoney.of1(CurrencyUnit.CHF, 1234.5678)
        str_val = StringConvert.INSTANCE.convertToString(test)
        self.assertEqual(str_val, "CHF 1234.5678")
        self.assertEqual(
            test, StringConvert.INSTANCE.convertFromString(BigMoney, str_val)
        )
