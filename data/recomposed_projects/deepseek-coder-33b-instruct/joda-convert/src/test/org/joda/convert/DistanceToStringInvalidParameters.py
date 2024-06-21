from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceToStringInvalidParameters:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self, num: int) -> typing.Any:

        return str(self.amount) + "m"

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            amount1 = amount1[:-1]
            self.amount = int(amount1)
        else:
            self.amount = amount
