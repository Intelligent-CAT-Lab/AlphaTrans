from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceMethodConstructorCharSequence:

    amount: int = 0

    def toString(self) -> str:
        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:
        return str(self.amount) + "m"

    def __init__(self, constructorId: int, amount1: str, amount: int) -> None:
        if constructorId == 0:
            amt = amount1[0 : amount1.__len__() - 1]
            self.amount = int(amt)
        else:
            self.amount = amount
