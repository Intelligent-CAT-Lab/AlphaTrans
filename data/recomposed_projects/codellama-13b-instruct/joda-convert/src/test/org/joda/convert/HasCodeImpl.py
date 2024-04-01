# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.HasCodeInterface import *
from src.main.org.joda.convert.FromString import *
import unittest
# Imports End

class HasCodeImpl(unittest.TestCase, HasCodeInterface<String>):

    # Class Fields Begin
    code: str = None
    # Class Fields End

    # Class Methods Begin
    def getCode(self) -> str:

            return self.code

    def __init__(self, code: str) -> None:

            self.code = code

    # Class Methods End


