from __future__ import annotations

# Imports Begin
from src.test.org.joda.convert.test2.Test2Interface import *
import io

# Imports End


class Test2Class(Test2Interface):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def print(self) -> str:
        pass

    def __init__(self, amount: int) -> None:
        pass

    # Class Methods End
