# Imports Begin
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.DistanceMethodConstructor import *
import unittest

# Imports End


class SubMethodConstructor(unittest.TestCase, DistanceMethodConstructor):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(self, amount: str) -> None:

        super().__init__(0, amount, 0)

    # Class Methods End
