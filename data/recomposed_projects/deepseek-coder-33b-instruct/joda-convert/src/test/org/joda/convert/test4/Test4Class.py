from __future__ import annotations
import io
from src.test.org.joda.convert.test4.Test4Interface import *


class Test4Class(Test4Interface):

    amount: int = None

    def toString(self) -> str:

        return "Weight[" + str(self.amount) + "g]"

    def print(self) -> str:

        return str(self.amount) + "g"

    def __init__(self, amount: int) -> None:

        self.amount = amount
