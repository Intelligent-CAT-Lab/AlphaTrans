# Imports Begin
from src.main.org.joda.money.CurrencyUnit import *

# Imports End


class CurrencyMismatchException(IllegalArgumentException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __firstCurrency: CurrencyUnit = None
    __secondCurrency: CurrencyUnit = None
    # Class Fields End

    # Class Methods Begin
    def getSecondCurrency(self) -> CurrencyUnit:
        pass

    def getFirstCurrency(self) -> CurrencyUnit:
        pass

    def __init__(
        self, firstCurrency: CurrencyUnit, secondCurrency: CurrencyUnit
    ) -> None:
        pass

    # Class Methods End
