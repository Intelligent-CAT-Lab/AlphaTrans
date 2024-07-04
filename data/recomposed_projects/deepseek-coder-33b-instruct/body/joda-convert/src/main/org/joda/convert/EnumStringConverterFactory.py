from __future__ import annotations
import re
import io
import enum
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
# from src.main.org.joda.convert.RenameHandler import *
from src.main.org.joda.convert.TypedStringConverter import *


class EnumStringConverter(TypedStringConverter):

    __effectiveType: typing.Type[typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__effectiveType

    def convertFromString(self, cls: typing.Type[enum.Enum], str: str) -> enum.Enum:

        if cls is None:
            raise ValueError("cls must not be None")

        if str is None:
            raise ValueError("str must not be None")

        return RenameHandler.INSTANCE.lookupEnum(cls, str)

    def convertToString(self, en: enum.Enum) -> str:
        return en.name

    def __init__(self, effectiveType: typing.Type[typing.Any]) -> None:
        self.__effectiveType = effectiveType


class EnumStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = None

    @staticmethod
    def initialize_fields() -> None:
        EnumStringConverterFactory.INSTANCE: StringConverterFactory = (
            EnumStringConverterFactory()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        sup = cls.__base__
        if sup is enum.EnumMeta:
            return EnumStringConverter(cls)
        elif sup is not None and sup.__base__ is enum.EnumMeta:
            return EnumStringConverter(sup)
        return None

    def __init__(self) -> None:
        pass


EnumStringConverterFactory.initialize_fields()
