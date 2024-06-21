from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceFromStringConstructorInvalidParameter:

    amount: int = None

    def toString(self) -> str:

        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:

        return str(self.amount) + "m"

    def __init__(self, constructorId: int, amount1: typing.Any, amount: int) -> None:

        if constructorId == 0:
            self.amount = amount
        else:
            self.amount = 0
