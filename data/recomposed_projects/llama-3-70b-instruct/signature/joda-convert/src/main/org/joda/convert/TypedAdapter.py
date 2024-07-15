from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *


class TypedAdapter(TypedStringConverter):

    __effectiveType: typing.Type[typing.Any] = None

    __conv: StringConverter[typing.Any] = None

    def toString(self) -> str:
        return "TypedAdapter:" + self.__conv.toString()

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__effectiveType

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        return self.__conv.convertFromString(cls, str)

    def convertToString(self, object: typing.Any) -> str:
        return self.__conv.convertToString(object)

    @staticmethod
    def adapt(
        cls: typing.Type[typing.Any], converter: StringConverter[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        if isinstance(converter, TypedStringConverter):
            return converter
        else:
            return TypedAdapter(converter, cls)

    def __init__(
        self, conv: StringConverter[typing.Any], effectiveType: typing.Type[typing.Any]
    ) -> None:
        self.__conv = conv
        self.__effectiveType = effectiveType
