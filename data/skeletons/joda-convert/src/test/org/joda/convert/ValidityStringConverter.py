from __future__ import annotations

# Imports Begin
from src.test.org.joda.convert.Validity import *
from src.main.org.joda.convert.StringConverter import *
import typing
from typing import *
import io

# Imports End


class ValidityStringConverter(StringConverter):

    # Class Fields Begin
    INSTANCE: ValidityStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(self, cls: typing.Type[Validity], str: str) -> Validity:
        pass

    def convertToString(self, object: Validity) -> str:
        pass

    # Class Methods End
