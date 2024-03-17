# Imports Begin
from src.main.org.joda.convert.test4.Test4Interface import *
import unittest

# Imports End


class Test4Class(unittest.TestCase, Test4Interface):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Weight[{self.amount}g]"

    def print(self) -> str:

        return f"{self.amount}g"

    def __init__(self, amount: int) -> None:

        self.amount = amount

    # Class Methods End
