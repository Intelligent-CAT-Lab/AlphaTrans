# Imports Begin
from src.main.org.joda.convert.StringConverter import *
import unittest
import typing
from typing import *
# Imports End

class MockIntegerStringConverter(unittest.TestCase, Enum<MockIntegerStringConverter>, StringConverter<Integer>):

    # Class Fields Begin
    INSTANCE: MockIntegerStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[int], str: str) -> int:

            return int(str)

    def convertToString(self, object: int) -> str:

            return str(object)

    # Class Methods End


