from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceMethodMethod:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str) -> DistanceMethodMethod:

        # Remove the last character from the string
        amount = amount[:-1]

        # Convert the string to an integer
        amount = int(amount)

        # Return a new instance of the class with the parsed amount
        return DistanceMethodMethod(amount)

    def __init__(self, amount: int) -> None:

        self.amount = amount
