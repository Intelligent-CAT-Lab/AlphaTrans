from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.test1.Test1Interface import *


class Test1Class(Test1Interface):

    amount: int = 0

    def toString(self) -> str:
        return "Weight[" + str(self.amount) + "g]"

    def print(self) -> str:
        return str(self.amount) + "g"

    @staticmethod
    def parse(amount: str) -> Test1Class:
        amount = amount[:-1]
        return Test1Class(int(amount))

    def __init__(self, amount: int) -> None:
        self.amount = amount
