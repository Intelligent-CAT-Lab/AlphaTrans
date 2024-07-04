from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypeUtils import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.Types import *


class TypeStringConverter(TypedStringConverter):

    __effectiveType: typing.Type[typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__effectiveType

    def convertFromString(self, cls: typing.Type[typing.Type], str: str) -> typing.Type:
        return TypeUtils.parse(str)

    def convertToString(self, type: typing.Type) -> str:
        try:
            return Types.toString(type)
        except Exception as ex:
            return str(type)

    def __init__(self, effectiveType: typing.Type[typing.Any]) -> None:
        self.__effectiveType = effectiveType


class TypeStringConverterFactory(StringConverterFactory):

    INSTANCE: TypeStringConverterFactory = None

    @staticmethod
    def initialize_fields() -> None:
        TypeStringConverterFactory.INSTANCE: TypeStringConverterFactory = (
            TypeStringConverterFactory()
        )

    def toString(self) -> str:
        return self.__class__.__name__

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        if issubclass(Type, cls) and cls != type:
            return TypeStringConverter(cls)
        return None

    def __init__(self) -> None:
        pass


TypeStringConverterFactory.initialize_fields()
