from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceMethodAndConstructorAnnotations:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str) -> DistanceMethodAndConstructorAnnotations:

        amount = amount[:-1]
        return DistanceMethodAndConstructorAnnotations(1, None, int(amount))

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            amount1 = amount1[:-1]
            self.amount = int(amount1)
        else:
            self.amount = amount
