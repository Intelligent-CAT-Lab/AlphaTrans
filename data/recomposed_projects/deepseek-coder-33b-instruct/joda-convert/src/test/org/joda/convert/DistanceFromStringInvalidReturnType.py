from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceFromStringInvalidReturnType:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str) -> int:

        return None

    def __init__(self, amount: int) -> None:

        self.amount = amount
