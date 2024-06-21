from __future__ import annotations
import io
import enum
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.RenameHandler import *
from src.main.org.joda.convert.TypedStringConverter import *


class EnumStringConverter(TypedStringConverter):

    __effectiveType: typing.Type[typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:

        return self.__effectiveType

    def convertFromString(self, cls: typing.Type[enum.Enum], str: str) -> enum.Enum:

        return RenameHandler.INSTANCE.lookupEnum(cls, str)

    def convertToString(self, en: enum.Enum) -> str:

        return en.name

    def __init__(self, effectiveType: typing.Type[typing.Any]) -> None:

        self.__effectiveType = effectiveType


class EnumStringConverterFactory(StringConverterFactory):

    INSTANCE: StringConverterFactory = EnumStringConverterFactory()

    def toString(self) -> str:

        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        sup = cls.__bases__[0] if cls.__bases__ else None

        if sup is enum.EnumMeta:
            return EnumStringConverter(cls)
        elif sup is not None and sup.__bases__[0] is enum.EnumMeta:
            return EnumStringConverter(sup)
        else:
            return None

    def __init__(self) -> None:

        pass
