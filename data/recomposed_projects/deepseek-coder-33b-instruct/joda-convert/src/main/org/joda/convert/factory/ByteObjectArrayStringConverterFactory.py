from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *


class ByteArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: ByteArrayStringConverter = ByteArrayStringConverter()

    __HEX: str = "0123456789ABCDEF"

    __EMPTY: typing.List[int] = []


class ByteObjectArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = ByteObjectArrayStringConverterFactory()

    def toString(self) -> str:

        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == bytearray:
            return ByteArrayStringConverter.INSTANCE
        return None

    def __init__(self) -> None:

        pass
