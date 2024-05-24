from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypedFromStringConverter import *
import typing
from typing import *
import io

# Imports End


class MethodFromStringConverter(TypedFromStringConverter):

    # Class Fields Begin
    __fromString: typing.Union[inspect.Signature, typing.Callable] = None
    __effectiveType: typing.Type[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def __init__(
        self,
        cls: typing.Type[typing.Any],
        fromString: typing.Union[inspect.Signature, typing.Callable],
        effectiveType: typing.Type[typing.Any],
    ) -> None:
        pass

    # Class Methods End
