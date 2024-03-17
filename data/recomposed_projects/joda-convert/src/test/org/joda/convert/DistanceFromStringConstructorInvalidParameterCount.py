# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import unittest

# Imports End


class DistanceFromStringConstructorInvalidParameterCount(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Distance[{self.amount}m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    def __init__(
        self, constructorId: int, value: int, amount1: str, amount: int
    ) -> None:

        if constructorId == 0:
            self.amount = amount
        else:
            self.amount = 0

    # Class Methods End
