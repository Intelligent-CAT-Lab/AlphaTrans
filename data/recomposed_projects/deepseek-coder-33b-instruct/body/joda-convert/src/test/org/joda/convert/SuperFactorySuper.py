from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class SuperFactorySuper:

    amount: int = 0

    def toString(self) -> str:
        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:
        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str) -> SuperFactorySuper:
        amount = amount[:-1]
        i = int(amount)
        return SuperFactorySuper(i) if i > 10 else SuperFactorySub(i)

    def __init__(self, amount: int) -> None:
        self.amount = amount
