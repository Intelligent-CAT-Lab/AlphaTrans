# Imports Begin
from src.main.org.joda.convert.test3.Test3SuperClass import *
from src.main.org.joda.convert.test3.Test3Interface import *

# Imports End


class Test3Class(Test3Interface, Test3SuperClass):

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
