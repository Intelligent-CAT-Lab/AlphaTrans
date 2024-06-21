from __future__ import annotations
import io


class DistanceNoAnnotations:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            amount1 = amount1[:-1]
            self.amount = int(amount1)
        else:
            self.amount = amount

    @staticmethod
    def parse(amount: str) -> DistanceNoAnnotations:

        return DistanceNoAnnotations(0, amount, 0)
