from __future__ import annotations
import time
import inspect
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class ConstructorFromStringConverter(TypedFromStringConverter):

    __fromString: typing.Callable[..., typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__fromString.__annotations__["return"]

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        try:
            return self.__fromString(str)
        except Exception as ex:
            raise RuntimeError(f"Error while converting from string: {ex}")

    def __init__(
        self, cls: typing.Type[typing.Any], fromString: typing.Callable[..., typing.Any]
    ) -> None:

        if (
            inspect.isabstract(cls)
            or isinstance(cls, typing._SpecialForm)
            or cls.__module__ == "typing"
            or cls.__module__ == "builtins"
        ):
            raise ValueError(
                "FromString constructor must be on an instantiable class: "
                + str(fromString)
            )
        if fromString.__qualname__.split(".")[0] != cls.__name__:
            raise ValueError(
                "FromString constructor must be defined on specified class: "
                + str(fromString)
            )
        self.__fromString = fromString
