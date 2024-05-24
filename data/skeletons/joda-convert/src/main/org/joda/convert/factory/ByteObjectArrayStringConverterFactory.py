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


class ByteArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[bytes], str: str) -> typing.List[int]:
        pass

    def convertToString(self, array: typing.List[int]) -> str:
        pass

    # Class Methods End


class ByteArrayStringConverter(TypedStringConverter, ABC):

    # Class Fields Begin
    __EMPTY: typing.List[int] = None
    __HEX: str = None
    INSTANCE: ByteArrayStringConverter = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class ByteObjectArrayStringConverterFactory(StringConverterFactory):

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
