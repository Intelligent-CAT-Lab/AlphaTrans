from __future__ import annotations
import re
import unittest
import pytest
import io


class DistanceNoAnnotationsCharSequence:

    amount: int = 0

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

    def __str__(self) -> str:
        return ""

    @staticmethod
    def parse(amount: str) -> DistanceNoAnnotationsCharSequence:
        pass

    @staticmethod
    def parse(amount: str) -> DistanceNoAnnotationsCharSequence:

        return DistanceNoAnnotationsCharSequence(0, amount, 0)
