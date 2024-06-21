from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *


class DoubleArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: DoubleArrayStringConverter = DoubleArrayStringConverter()

    __EMPTY: List[float] = []


class FloatArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: FloatArrayStringConverter = FloatArrayStringConverter()

    __EMPTY: List[float] = []


class IntArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: IntArrayStringConverter = IntArrayStringConverter()

    __EMPTY: List[int] = []


class LongArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: LongArrayStringConverter = LongArrayStringConverter()

    __EMPTY: typing.List[int] = []


class ShortArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: ShortArrayStringConverter = ShortArrayStringConverter()

    __EMPTY: List[int] = []


class NumericArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = NumericArrayStringConverterFactory()

    def toString(self) -> str:

        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == list and cls.getComponentType().isPrimitive():
            if cls == list[long]:
                return LongArrayStringConverter.INSTANCE
            if cls == list[int]:
                return IntArrayStringConverter.INSTANCE
            if cls == list[short]:
                return ShortArrayStringConverter.INSTANCE
            if cls == list[double]:
                return DoubleArrayStringConverter.INSTANCE
            if cls == list[float]:
                return FloatArrayStringConverter.INSTANCE

        return None

    def __init__(self) -> None:

        pass
