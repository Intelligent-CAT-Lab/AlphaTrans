# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
import typing
from abc import ABC

# Imports End


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


class CharecterArrayStringConverter(Enum, TypedStringConverter, ABC):

    # Class Fields Begin
    __EMPTY: typing.List[str] = None
    INSTANCE: CharecterArrayStringConverter = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class CharecterArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(
        self, cls: typing.Type[typing.List[str]], str: str
    ) -> typing.List[str]:
        pass

    def convertToString(self, array: typing.List[str]) -> str:
        pass

    # Class Methods End
