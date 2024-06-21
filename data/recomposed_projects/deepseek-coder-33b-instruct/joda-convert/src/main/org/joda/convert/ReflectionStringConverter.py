from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *


class ReflectionStringConverter(TypedStringConverter):

    fromString: TypedStringConverter[typing.Any] = None
    __toString: typing.Union[inspect.Signature, typing.Callable] = None
    __cls: typing.Type[typing.Any] = None

    def toString(self) -> str:

        return "RefectionStringConverter[" + self.__cls.__name__ + "]"

    def getEffectiveType(self) -> typing.Type[typing.Any]:

        return self.fromString.getEffectiveType()

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        if self.fromString is None:
            raise ValueError("fromString is not set")

        return self.fromString.convertFromString(cls, str)

    def convertToString(self, object: typing.Any) -> str:

        try:
            return str(object)
        except Exception as ex:
            raise RuntimeError("Error converting object to string: " + str(ex))

    def __init__(
        self,
        cls: typing.Type[typing.Any],
        toString: typing.Union[inspect.Signature, typing.Callable],
        fromString: TypedStringConverter[typing.Any],
    ) -> None:

        if toString.parameters and len(list(toString.parameters.values())) != 0:
            raise RuntimeError("ToString method must have no parameters: " + toString)

        if toString.return_annotation != str:
            raise RuntimeError("ToString method must return a String: " + toString)

        self.__cls = cls
        self.__toString = toString
        self.fromString = fromString
