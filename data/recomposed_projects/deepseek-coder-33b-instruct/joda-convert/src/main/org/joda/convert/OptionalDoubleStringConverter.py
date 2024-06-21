from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedStringConverter import *


class OptionalDoubleStringConverter(TypedStringConverter):

    __METHOD_GET: typing.Union[inspect.Signature, typing.Callable] = None
    __METHOD_IS_PRESENT: typing.Union[inspect.Signature, typing.Callable] = None
    __METHOD_OF: typing.Union[inspect.Signature, typing.Callable] = None
    __EMPTY: typing.Any = None
    __TYPE: typing.Type[typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:

        return self.__TYPE

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        if str == "":
            return self.__EMPTY

        try:
            value = float(str)
            return self.__METHOD_OF(value)
        except Exception as ex:
            raise ValueError(ex)

    def convertToString(self, object: typing.Any) -> str:

        try:
            is_present = self.__METHOD_IS_PRESENT(object)
            return str(self.__METHOD_GET(object)) if is_present else ""
        except Exception as ex:
            raise ValueError(ex) from ex

    def __init__(self) -> None:

        pass  # LLM could not translate this method
