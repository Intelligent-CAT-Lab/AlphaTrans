# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import unittest
import typing
from typing import *

# Imports End


class DistanceToStringInvalidReturnType(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Distance[{self.amount}m]"

    def print(self) -> typing.Any:

        return str(self.amount) + "m"

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            self.amount1 = self.amount1[:-1]
            self.amount = int(amount1)
        else:
            self.amount = amount

    # Class Methods End
