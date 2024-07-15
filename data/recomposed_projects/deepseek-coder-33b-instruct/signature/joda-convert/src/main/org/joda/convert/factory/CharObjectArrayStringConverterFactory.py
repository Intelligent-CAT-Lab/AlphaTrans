from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *


class CharecterArrayStringConverter(TypedStringConverter, ABC):

    __EMPTY: List[str] = []


class CharObjectArrayStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = None

    @staticmethod
    def initialize_fields() -> None:
        CharObjectArrayStringConverterFactory.INSTANCE: StringConverterFactory = (
            CharObjectArrayStringConverterFactory()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        if cls == typing.List[str]:
            return CharecterArrayStringConverter.INSTANCE
        return None

    def __init__(self) -> None:
        pass


CharObjectArrayStringConverterFactory.initialize_fields()
