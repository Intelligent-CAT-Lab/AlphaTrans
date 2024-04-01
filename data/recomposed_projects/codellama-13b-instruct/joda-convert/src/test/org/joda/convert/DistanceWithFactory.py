# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromStringFactory import *
import unittest

# Imports End


class DistanceWithFactory(unittest.TestCase):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"{self.amount}m"

    def __init__(self, amount: int) -> None:

        self.amount = amount

    # Class Methods End
