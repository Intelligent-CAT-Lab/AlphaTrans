# Imports Begin
from src.main.org.joda.convert.SuperFactorySuper import *
import unittest

# Imports End


class SuperFactorySub(unittest.TestCase, SuperFactorySuper):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(self, amount: int) -> None:

        super().__init__(amount)

    # Class Methods End
