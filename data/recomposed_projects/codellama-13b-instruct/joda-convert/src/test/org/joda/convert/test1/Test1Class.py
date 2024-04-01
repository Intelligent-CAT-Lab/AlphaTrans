# Imports Begin
from src.main.org.joda.convert.test1.Test1Interface import *
from src.main.org.joda.convert.FromString import *
import unittest
# Imports End

class Test1Class(unittest.TestCase, Test1Interface):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

            return f"Weight[{self.amount}g]"

    def print(self) -> str:

            return f"{self.amount}g"

    @staticmethod

    def parse(self.amount: str) -> "Test1Class":


        pass # LLM could not translate method body

    def __init__(self, amount: int) -> None:

            self.amount = amount

    # Class Methods End


