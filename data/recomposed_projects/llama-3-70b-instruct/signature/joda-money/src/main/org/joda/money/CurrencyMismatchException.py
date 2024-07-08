from __future__ import annotations
import re
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

        pass  # LLM could not translate this method
