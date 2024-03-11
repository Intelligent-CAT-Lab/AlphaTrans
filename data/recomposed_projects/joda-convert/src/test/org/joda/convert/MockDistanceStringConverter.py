# Imports Begin
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.DistanceMethodMethod import *
import unittest
import typing
from typing import *
# Imports End

class MockDistanceStringConverter(unittest.TestCase, Enum<MockDistanceStringConverter>, StringConverter<DistanceMethodMethod>):

    # Class Fields Begin
    INSTANCE: MockDistanceStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[DistanceMethodMethod], str: str) -> DistanceMethodMethod:

            return cls.parse(str)

    def convertToString(self, object: DistanceMethodMethod) -> str:

            return object.print()

    # Class Methods End


