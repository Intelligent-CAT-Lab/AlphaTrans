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

    __EMPTY: List[float] = []


class IntArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: typing.List[int] = []


class LongArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: typing.List[int] = []


class ShortArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: List[int] = []


class NumericObjectArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = None

    @staticmethod
    def initialize_fields() -> None:
        NumericObjectArrayStringConverterFactory.INSTANCE: StringConverterFactory = (
            NumericObjectArrayStringConverterFactory()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == list:
            if cls == typing.List[int]:
                return LongArrayStringConverter.INSTANCE
            if cls == typing.List[int]:
                return IntArrayStringConverter.INSTANCE
            if cls == typing.List[int]:
                return ShortArrayStringConverter.INSTANCE
            if cls == typing.List[float]:
                return DoubleArrayStringConverter.INSTANCE
            if cls == typing.List[float]:
                return FloatArrayStringConverter.INSTANCE
        return None

    def __init__(self) -> None:
        pass


NumericObjectArrayStringConverterFactory.initialize_fields()
