from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceFromStringInvalidParameterCount:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str, value: int) -> DistanceFromStringInvalidParameterCount:

        # Here you can add your logic to parse the string and assign it to the 'amount' attribute
        # For now, I'm just returning None
        return None

    def __init__(self, amount: int) -> None:

        self.amount = amount
