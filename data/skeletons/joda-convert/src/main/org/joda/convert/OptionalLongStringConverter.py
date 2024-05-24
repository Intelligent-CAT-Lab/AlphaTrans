from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
import typing
from typing import *
import io

# Imports End


class OptionalLongStringConverter(TypedStringConverter):

    # Class Fields Begin
    __TYPE: typing.Type[typing.Any] = None
    __EMPTY: typing.Any = None
    __METHOD_OF: typing.Union[inspect.Signature, typing.Callable] = None
    __METHOD_IS_PRESENT: typing.Union[inspect.Signature, typing.Callable] = None
    __METHOD_GET: typing.Union[inspect.Signature, typing.Callable] = None
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString(self, object: typing.Any) -> str:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
