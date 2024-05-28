from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.TypedFromStringConverter import *
import typing
from typing import *
import io

# Imports End


class ReflectionStringConverter(TypedStringConverter):

    # Class Fields Begin
    __cls: typing.Type[typing.Any] = None
    __toString: typing.Union[inspect.Signature, typing.Callable] = None
    fromString: TypedStringConverter[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString(self, object: typing.Any) -> str:
        pass

    def __init__(
        self,
        cls: typing.Type[typing.Any],
        toString: typing.Union[inspect.Signature, typing.Callable],
        fromString: TypedStringConverter[typing.Any],
    ) -> None:
        pass

    # Class Methods End
