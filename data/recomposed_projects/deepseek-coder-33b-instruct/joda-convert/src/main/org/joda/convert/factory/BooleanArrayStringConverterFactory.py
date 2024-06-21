from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *


class BooleanArrayStringConverter(TypedStringConverter, ABC):

    INSTANCE: BooleanArrayStringConverter = BooleanArrayStringConverter()

    __EMPTY: List[bool] = []


class BooleanArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = BooleanArrayStringConverterFactory()

    def toString(self) -> str:

        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == typing.List[bool]:
            return BooleanArrayStringConverter.INSTANCE
        return None

    def __init__(self) -> None:

        pass
