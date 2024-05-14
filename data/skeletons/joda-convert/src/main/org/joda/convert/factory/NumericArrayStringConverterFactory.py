# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
import typing
from abc import ABC

# Imports End


class NumericArrayStringConverterFactory(StringConverterFactory):

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


class DoubleArrayStringConverter(Enum, TypedStringConverter, ABC):

    # Class Fields Begin
    INSTANCE: DoubleArrayStringConverter = None
    __EMPTY: typing.List[float] = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class FloatArrayStringConverter(Enum, TypedStringConverter, ABC):

    # Class Fields Begin
    INSTANCE: FloatArrayStringConverter = None
    __EMPTY: typing.List[float] = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class IntArrayStringConverter(Enum, TypedStringConverter, ABC):

    # Class Fields Begin
    INSTANCE: IntArrayStringConverter = None
    __EMPTY: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class LongArrayStringConverter(Enum, TypedStringConverter, ABC):

    # Class Fields Begin
    __EMPTY: typing.List[int] = None
    INSTANCE: LongArrayStringConverter = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class ShortArrayStringConverter(Enum, TypedStringConverter, ABC):

    # Class Fields Begin
    INSTANCE: ShortArrayStringConverter = None
    __EMPTY: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class LongArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(
        self, cls: typing.Type[typing.List[int]], str: str
    ) -> typing.List[int]:
        pass

    def convertToString(self, array: typing.List[int]) -> str:
        pass

    # Class Methods End


class IntArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(
        self, cls: typing.Type[typing.List[int]], str: str
    ) -> typing.List[int]:
        pass

    def convertToString(self, array: typing.List[int]) -> str:
        pass

    # Class Methods End


class ShortArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(
        self, cls: typing.Type[typing.List[int]], str: str
    ) -> typing.List[int]:
        pass

    def convertToString(self, array: typing.List[int]) -> str:
        pass

    # Class Methods End


class DoubleArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(
        self, cls: typing.Type[typing.List[float]], str: str
    ) -> typing.List[float]:
        pass

    def convertToString(self, array: typing.List[float]) -> str:
        pass

    # Class Methods End


class FloatArrayStringConverter:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(
        self, cls: typing.Type[typing.List[float]], str: str
    ) -> typing.List[float]:
        pass

    def convertToString(self, array: typing.List[float]) -> str:
        pass

    # Class Methods End
