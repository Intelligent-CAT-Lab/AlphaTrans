from __future__ import annotations
import inspect
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.TypeUtils import *
from src.main.org.joda.convert.TypedStringConverter import *


class TypeTokenStringConverter(TypedStringConverter):

    TYPE_TOKEN_METHOD_OF: typing.Union[inspect.Signature, typing.Callable] = None

    TYPE_TOKEN_CLASS: typing.Type[typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return TypeTokenStringConverter.TYPE_TOKEN_CLASS

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        parsed: typing.Type = TypeUtils.parse(str)
        try:
            return TypeTokenStringConverter.TYPE_TOKEN_METHOD_OF.invoke(None, parsed)
        except Exception as ex:
            raise ValueError(ex)

    def convertToString(self, object: typing.Any) -> str:
        return object.toString()

    def __init__(self) -> None:
        super().__init__(TypeUtils.getTypeToken(self))


TypeTokenStringConverter.run_static_init()
