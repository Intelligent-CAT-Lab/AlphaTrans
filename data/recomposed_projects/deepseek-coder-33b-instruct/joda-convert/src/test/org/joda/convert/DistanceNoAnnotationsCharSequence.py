from __future__ import annotations
import io


class DistanceNoAnnotationsCharSequence:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            amt = amount1[:-1]
            self.amount = int(amt)
        else:
            self.amount = amount

    @staticmethod
    def parse(amount: str) -> DistanceNoAnnotationsCharSequence:

        return DistanceNoAnnotationsCharSequence(0, amount, 0)
