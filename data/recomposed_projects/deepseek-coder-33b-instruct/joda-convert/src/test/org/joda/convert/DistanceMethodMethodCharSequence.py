from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceMethodMethodCharSequence:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str) -> DistanceMethodMethodCharSequence:

        amt = amount[:-1]
        return DistanceMethodMethodCharSequence(int(amt))

    def __init__(self, amount: int) -> None:

        self.amount = amount
