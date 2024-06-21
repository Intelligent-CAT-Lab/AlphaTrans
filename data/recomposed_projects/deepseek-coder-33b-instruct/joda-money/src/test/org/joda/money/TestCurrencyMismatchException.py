from __future__ import annotations
import io
from src.main.org.joda.money.CurrencyMismatchException import *
from src.main.org.joda.money.CurrencyUnit import *


class TestCurrencyMismatchException:

    __EUR: CurrencyUnit = CurrencyUnit.of("EUR")

    __GBP: CurrencyUnit = CurrencyUnit.of("GBP")

    def test_new_nullnull(self) -> None:

        test = CurrencyMismatchException(None, None)
        assert test.getMessage() == "Currencies differ: null/null"
        assert test.getCause() is None
        assert test.getFirstCurrency() is None
        assert test.getSecondCurrency() is None

    def test_new_GBPnull(self) -> None:

        test = CurrencyMismatchException(self.__GBP, None)
        assert test.getMessage() == "Currencies differ: GBP/null"
        assert test.getCause() is None
        assert test.getFirstCurrency() == self.__GBP
        assert test.getSecondCurrency() is None

    def test_new_nullEUR(self) -> None:

        test = CurrencyMismatchException(None, self.__EUR)
        assert test.getMessage() == "Currencies differ: None/EUR"
        assert test.getCause() is None
        assert test.getFirstCurrency() is None
        assert test.getSecondCurrency() == self.__EUR

    def test_new_GBPEUR(self) -> None:

        test = CurrencyMismatchException(self.__GBP, self.__EUR)
        assert test.getMessage() == "Currencies differ: GBP/EUR"
        assert test.getCause() is None
        assert test.getFirstCurrency() == self.__GBP
        assert test.getSecondCurrency() == self.__EUR
