from __future__ import annotations
import io
from src.main.org.joda.money.CurrencyUnit import *


class CurrencyMismatchException(ValueError):

    __secondCurrency: CurrencyUnit = None
    __firstCurrency: CurrencyUnit = None

    __serialVersionUID: int = 1

    def getSecondCurrency(self) -> CurrencyUnit:

        return self.__secondCurrency

    def getFirstCurrency(self) -> CurrencyUnit:

        return self.__firstCurrency

    def __init__(
        self, firstCurrency: CurrencyUnit, secondCurrency: CurrencyUnit
    ) -> None:

        first_code = firstCurrency.getCode() if firstCurrency is not None else "null"
        second_code = secondCurrency.getCode() if secondCurrency is not None else "null"

        super().__init__(f"Currencies differ: {first_code}/{second_code}")

        self.__firstCurrency = firstCurrency
        self.__secondCurrency = secondCurrency
