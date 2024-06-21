from __future__ import annotations
import io
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.money.BigMoney import *
from src.main.org.joda.money.CurrencyUnit import *

# src.main.org.joda.money.Money


class TestStringConvert:

    def test_CurrencyUnit(self) -> None:

        test = CurrencyUnit.CHF
        str = StringConvert.INSTANCE.convertToString(test)
        assert str == "CHF"
        assert test == StringConvert.INSTANCE.convertFromString(CurrencyUnit, str)

    def test_Money(self) -> None:

        test = Money.of2(CurrencyUnit.CHF, 1234.56)
        str = StringConvert.INSTANCE.convertToString(test)
        assert str == "CHF 1234.56"
        assert test == StringConvert.INSTANCE.convertFromString(Money, str)

    def test_BigMoney(self) -> None:

        test = BigMoney.of1(CurrencyUnit.CHF, 1234.5678)
        str = StringConvert.INSTANCE.convertToString(test)
        assert str == "CHF 1234.5678"
        assert test == StringConvert.INSTANCE.convertFromString(BigMoney, str)
