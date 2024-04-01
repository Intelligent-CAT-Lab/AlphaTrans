# Imports Begin
from src.main.org.joda.convert.test3.Test3SuperClass import *
from src.main.org.joda.convert.test3.Test3Interface import *
import unittest

# Imports End


class Test3Class(unittest.TestCase, Test3Interface, Test3SuperClass):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Weight[{self.amount}g]"

    def print(self) -> str:

        return str(self.amount) + "g"

    def __init__(self, amount: int) -> None:

        self.amount = amount

    # Class Methods End
