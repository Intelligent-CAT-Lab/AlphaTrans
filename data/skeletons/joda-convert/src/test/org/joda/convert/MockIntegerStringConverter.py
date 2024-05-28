from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.StringConverter import *
import typing
from typing import *
import io

# Imports End


class MockIntegerStringConverter(StringConverter):

    # Class Fields Begin
    INSTANCE: MockIntegerStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[int], str: str) -> int:
        pass

    def convertToString(self, object: int) -> str:
        pass

    # Class Methods End
