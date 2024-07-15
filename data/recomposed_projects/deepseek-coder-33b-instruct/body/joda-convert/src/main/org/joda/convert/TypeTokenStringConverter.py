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

    @staticmethod
    def run_static_init():
        try:
            TypeTokenStringConverter.TYPE_TOKEN_CLASS = TypeUtils.for_name(
                "com.google.common.reflect.TypeToken"
            )
            TypeTokenStringConverter.TYPE_TOKEN_METHOD_OF = (
                TypeTokenStringConverter.TYPE_TOKEN_CLASS.get_declared_method(
                    "of", Type
                )
            )

        except Exception as ex:
            raise RuntimeError(ex)

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.TYPE_TOKEN_CLASS

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        parsed = TypeUtils.parse(str)
        try:
            return self.TYPE_TOKEN_METHOD_OF(parsed)
        except Exception as ex:
            raise ValueError(ex)

    def convertToString(self, object: typing.Any) -> str:
        return str(object)

    def __init__(self) -> None:
        pass


TypeTokenStringConverter.run_static_init()
