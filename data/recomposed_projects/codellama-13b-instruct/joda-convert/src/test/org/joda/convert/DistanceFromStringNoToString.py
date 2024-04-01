# Imports Begin
from src.main.org.joda.convert.FromString import *
import unittest
import typing
from typing import *

# Imports End


class DistanceFromStringNoToString(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Distance[{self.amount}m]"

    def hashCode(self) -> int:

        return self.amount

    def equals(self, obj: typing.Any) -> bool:

        return (
            isinstance(obj, DistanceFromStringNoToString) and obj.amount == self.amount
        )

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            self.amount = int(amount1[:-1])
        else:
            self.amount = amount

    def print(self) -> str:

        return f"{self.amount}m"

    # Class Methods End
