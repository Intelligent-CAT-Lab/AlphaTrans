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

    __EMPTY: typing.List[Union[int, None]] = []


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

        if issubclass(cls, list):
            if cls == list[int]:
                return IntArrayStringConverter.INSTANCE
            if cls == list[float]:
                return DoubleArrayStringConverter.INSTANCE
            if cls == list[str]:
                return StringArrayStringConverter.INSTANCE
            if cls == list[bool]:
                return BooleanArrayStringConverter.INSTANCE
            if cls == list[bytes]:
                return ByteArrayStringConverter.INSTANCE
            if cls == list[short]:
                return ShortArrayStringConverter.INSTANCE
            if cls == list[long]:
                return LongArrayStringConverter.INSTANCE
        return None

    def __init__(self) -> None:

        self.INSTANCE: StringConverterFactory = None


NumericObjectArrayStringConverterFactory.initialize_fields()
