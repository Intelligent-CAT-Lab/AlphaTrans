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

    __EMPTY: typing.List[float] = []


class FloatArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: FloatArrayStringConverter = FloatArrayStringConverter()

    __EMPTY: typing.List[float] = []


class IntArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: IntArrayStringConverter = IntArrayStringConverter()

    __EMPTY: typing.List[int] = []


class LongArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: LongArrayStringConverter = LongArrayStringConverter()

    __EMPTY: typing.List[int] = []


class ShortArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: ShortArrayStringConverter = ShortArrayStringConverter()

    __EMPTY: List[int] = []


class NumericObjectArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = NumericObjectArrayStringConverterFactory()

    def toString(self) -> str:

        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == typing.List[int]:
            return IntArrayStringConverter.INSTANCE
        elif cls == typing.List[float]:
            return FloatArrayStringConverter.INSTANCE
        elif cls == typing.List[long]:
            return LongArrayStringConverter.INSTANCE
        elif cls == typing.List[short]:
            return ShortArrayStringConverter.INSTANCE
        elif cls == typing.List[double]:
            return DoubleArrayStringConverter.INSTANCE
        else:
            return None

    def __init__(self) -> None:

        pass
