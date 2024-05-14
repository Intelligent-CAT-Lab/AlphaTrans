# Imports Begin
from src.main.org.joda.convert.StringConverter import *
import typing

# Imports End


class MockIntegerStringConverter(Enum, StringConverter):

    # Class Fields Begin
    INSTANCE: MockIntegerStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[int], str: str) -> int:
        pass

    def convertToString(self, object: int) -> str:
        pass

    # Class Methods End
