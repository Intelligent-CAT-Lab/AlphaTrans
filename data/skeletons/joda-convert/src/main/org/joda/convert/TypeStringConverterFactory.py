from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.Types import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.TypeUtils import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
import typing
from typing import *
import io

# Imports End


class TypeStringConverter(TypedStringConverter):

    # Class Fields Begin
    __effectiveType: typing.Type[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Type], str: str) -> typing.Type:
        pass

    def convertToString(self, type: typing.Type) -> str:
        pass

    def __init__(self, effectiveType: typing.Type[typing.Any]) -> None:
        pass

    # Class Methods End


class TypeStringConverterFactory(StringConverterFactory):

    # Class Fields Begin
    INSTANCE: TypeStringConverterFactory = None
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
