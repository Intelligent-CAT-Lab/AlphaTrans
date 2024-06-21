from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.test1.Test1Interface import *


class Test1Class(Test1Interface):

    amount: int = None

    def toString(self) -> str:

        return "Weight[" + str(self.amount) + "g]"

    def print(self) -> str:

        return str(self.amount) + "g"

    @staticmethod
    def parse(amount: str) -> Test1Class:

        # Remove the last character from the string
        amount = amount[:-1]

        # Convert the string to an integer and create a new Test1Class object
        return Test1Class(int(amount))

    def __init__(self, amount: int) -> None:

        self.amount = amount
