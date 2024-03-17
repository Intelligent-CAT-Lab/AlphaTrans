# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import unittest
import typing
from typing import *
# Imports End

class DistanceFromStringInvalidReturnType(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

            return f"Distance[{self.amount}m]"

    def print(self) -> str:

            return f"{self.amount}m"

    @staticmethod

    def parse(self.amount: str) -> int:

            return int(self.amount)

    def __init__(self, amount: int) -> None:

            self.amount = amount

    # Class Methods End


