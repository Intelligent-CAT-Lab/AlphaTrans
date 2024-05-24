from __future__ import annotations

# Imports Begin
from src.test.org.joda.convert.test4.Test4Interface import *
import io

# Imports End


class Test4Class(Test4Interface):

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
