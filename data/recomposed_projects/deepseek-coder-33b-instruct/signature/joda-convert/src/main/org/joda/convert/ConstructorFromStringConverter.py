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
            if isinstance(ex, RuntimeError):
                raise ex
            else:
                raise RuntimeError(str(ex))

    def __init__(
        self, cls: typing.Type[typing.Any], fromString: typing.Callable[..., typing.Any]
    ) -> None:

        if (
            inspect.isabstract(cls)
            or inspect.isclass(cls)
            and issubclass(cls, typing.Generic)
            or cls.__module__.startswith("typing")
            or cls.__module__ == "builtins"
        ):
            raise ValueError(
                "FromString constructor must be on an instantiable class: "
                + str(fromString)
            )

        if fromString.__self__.__class__ != cls:
            raise RuntimeError(
                "FromString constructor must be defined on specified class: "
                + str(fromString)
            )

        self.__fromString = fromString
