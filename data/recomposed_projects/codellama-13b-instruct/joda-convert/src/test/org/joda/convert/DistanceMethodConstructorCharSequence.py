# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import unittest

# Imports End


class DistanceMethodConstructorCharSequence(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Distance[{self.amount}m]"

    def print(self) -> str:

        return f"{self.amount}m"

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            amt = self.amount1[:-1]
            self.amount = int(amt)
        else:
            self.amount = amount

    # Class Methods End
