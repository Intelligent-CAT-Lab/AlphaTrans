# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import unittest
import typing
from typing import *

# Imports End


class DistanceFromStringConstructorInvalidParameter(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Distance[{self.amount}m]"

    def print(self) -> str:

        return f"{self.amount}m"

    def __init__(self, constructorId: int, amount1: typing.Any, amount: int) -> None:

        if constructorId == 0:
            self.amount = amount
        else:
            self.amount = 0

    # Class Methods End
