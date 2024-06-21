from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceToStringException:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        raise ParseException("Test", 2)

    @staticmethod
    def parse(amount: str) -> DistanceToStringException:

        # Remove the last character from the string
        amount = amount[:-1]

        # Convert the string to an integer
        amount = int(amount)

        # Return a new instance of DistanceToStringException with the parsed amount
        return DistanceToStringException(amount)

    def __init__(self, amount: int) -> None:

        self.amount = amount
