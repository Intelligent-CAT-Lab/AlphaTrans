# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromStringFactory import *
import unittest
from abc import ABC

# Imports End


class Test3Interface(unittest.TestCase, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return str(self)

    # Class Methods End
