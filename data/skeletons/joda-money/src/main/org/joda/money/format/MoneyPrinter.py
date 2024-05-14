# Imports Begin
from src.main.org.joda.money.format.MoneyPrintContext import *
from src.main.org.joda.money.BigMoney import *
import io
from abc import ABC

# Imports End


class MoneyPrinter(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def print(
        self, context: MoneyPrintContext, appendable: io.TextIOBase, money: BigMoney
    ) -> None:
        pass

    # Class Methods End
