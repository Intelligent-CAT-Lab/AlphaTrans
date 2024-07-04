from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ToString import *


class DistanceFromStringInvalidParameterCount:

    amount: int = 0

    def toString(self) -> str:
        return "Distance[" + str(self.amount) + "m]"

    def print(self) -> str:
        return str(self.amount) + "m"

    @staticmethod
    def parse(amount: str, value: int) -> DistanceFromStringInvalidParameterCount:
        return DistanceFromStringInvalidParameterCount(value)

    def __init__(self, amount: int) -> None:
        self.amount = amount
