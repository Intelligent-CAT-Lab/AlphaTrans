# Imports Begin
from src.main.org.joda.convert.test1.Test1Interface import *
from src.main.org.joda.convert.FromString import *

# Imports End


class Test1Class(Test1Interface):

    # Class Fields Begin
    amount: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def print(self) -> str:
        pass

    @staticmethod
    def parse(amount: str) -> "Test1Class":
        pass

    def __init__(self, amount: int) -> None:
        pass

    # Class Methods End
