from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceFromStringConstructorInvalidParameterCount:

    amount: int = 0

    def toString(self) -> str:
        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:
        return str(self.amount) + "m"

    def __init__(
        self, constructorId: int, value: int, amount1: str, amount: int
    ) -> None:
        if constructorId == 0:
            self.amount = amount
        else:
            self.amount = 0
