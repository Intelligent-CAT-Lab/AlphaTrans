from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *


class DoubleArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: typing.List[float] = []


class FloatArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: typing.List[float] = []


class IntArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: typing.List[int] = []


class LongArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: typing.List[int] = []


class ShortArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: List[int] = []


class NumericArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = None

    @staticmethod
    def initialize_fields() -> None:
        NumericArrayStringConverterFactory.INSTANCE: StringConverterFactory = (
            NumericArrayStringConverterFactory()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if (
            isinstance(cls, type)
            and issubclass(cls, list)
            and issubclass(cls.__args__[0], (int, float, long, float))
        ):
            if cls == typing.List[long]:
                return LongArrayStringConverter.INSTANCE
            if cls == typing.List[int]:
                return IntArrayStringConverter.INSTANCE
            if cls == typing.List[short]:
                return ShortArrayStringConverter.INSTANCE
            if cls == typing.List[double]:
                return DoubleArrayStringConverter.INSTANCE
            if cls == typing.List[float]:
                return FloatArrayStringConverter.INSTANCE
        return None

    def __init__(self) -> None:

        self.INSTANCE: StringConverterFactory = None


NumericArrayStringConverterFactory.initialize_fields()
