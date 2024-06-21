from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class ConstructorFromStringConverter(TypedFromStringConverter):

    __fromString: typing.Callable[..., typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:

        return self.__fromString.getDeclaringClass()

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        try:
            return cls(str)
        except Exception as ex:
            raise RuntimeError(str(ex)) from ex

    def __init__(
        self, cls: typing.Type[typing.Any], fromString: typing.Callable[..., typing.Any]
    ) -> None:

        if (
            inspect.isabstract(cls)
            or cls.__dict__.get("__abstractmethods__")
            or inspect.isclass(cls)
            or cls.__dict__.get("__slots__")
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
