from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class CharecterArrayStringConverter(TypedStringConverter, ABC):

    # Class Fields Begin
    __EMPTY: typing.List[str] = None
    INSTANCE: CharecterArrayStringConverter = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class CharObjectArrayStringConverterFactory(StringConverterFactory):

    # Class Fields Begin
    INSTANCE: StringConverterFactory = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
