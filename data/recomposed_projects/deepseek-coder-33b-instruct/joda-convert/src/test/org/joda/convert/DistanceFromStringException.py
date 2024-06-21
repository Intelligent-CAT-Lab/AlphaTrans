from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceFromStringException:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str) -> DistanceFromStringException:

        # Python does not have a built-in ParseException class, so we will use a custom exception
        class ParseException(Exception):
            def __init__(self, message: str, position: int):
                self.message = message
                self.position = position

        raise ParseException("Test", 2)

    def __init__(self, amount: int) -> None:

        self.amount = amount
