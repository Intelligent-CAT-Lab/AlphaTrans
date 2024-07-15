from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.joda.convert.FromString import *


class DistanceFromStringNoToString:

    amount: int = 0

    def toString(self) -> str:
        return "Distance[" + str(self.amount) + "m]"

    def hashCode(self) -> int:
        return self.amount

    def equals(self, obj: typing.Any) -> bool:
        return (
            isinstance(obj, DistanceFromStringNoToString) and obj.amount == self.amount
        )

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:

        if constructorId == 0:
            self.amount = int(amount1[:-1])
        else:
            self.amount = amount

    def print(self) -> str:
        return str(self.amount) + "m"
