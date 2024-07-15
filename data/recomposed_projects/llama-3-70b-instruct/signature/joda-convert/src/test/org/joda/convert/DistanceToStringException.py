from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceToStringException:

    amount: int = 0

    def toString(self) -> str:
        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:
        raise ParseException("Test", 2)

    @staticmethod
    def parse(amount: str) -> DistanceToStringException:
        amount = amount[:-1]
        return DistanceToStringException(int(amount))

    def __init__(self, amount: int) -> None:
        self.amount = amount
