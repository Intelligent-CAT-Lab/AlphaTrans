from __future__ import annotations
import inspect
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedStringConverter import *


class OptionalLongStringConverter(TypedStringConverter):

    __METHOD_GET: typing.Union[inspect.Signature, typing.Callable] = None

    __METHOD_IS_PRESENT: typing.Union[inspect.Signature, typing.Callable] = None

    __METHOD_OF: typing.Union[inspect.Signature, typing.Callable] = None

    __EMPTY: typing.Any = None

    __TYPE: typing.Type[typing.Any] = None

    @staticmethod
    def run_static_init():

        try:
            OptionalLongStringConverter.__TYPE = getattr(
                __import__("java.util"), "OptionalLong"
            )
            OptionalLongStringConverter.__EMPTY = (
                OptionalLongStringConverter.__TYPE.getDeclaredMethod("empty").invoke(
                    None
                )
            )
            OptionalLongStringConverter.__METHOD_OF = (
                OptionalLongStringConverter.__TYPE.getDeclaredMethod("of", long)
            )
            OptionalLongStringConverter.__METHOD_IS_PRESENT = (
                OptionalLongStringConverter.__TYPE.getDeclaredMethod("isPresent")
            )
            OptionalLongStringConverter.__METHOD_GET = (
                OptionalLongStringConverter.__TYPE.getDeclaredMethod("getAsLong")
            )

        except Exception as ex:
            raise RuntimeError(ex)

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return OptionalLongStringConverter.__TYPE

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        if str == "":
            return self.__EMPTY

        value = int(str)

        try:
            return self.__METHOD_OF(value)
        except Exception as ex:
            raise ValueError(ex)

    def convertToString(self, object: typing.Any) -> str:

        try:
            is_present = OptionalLongStringConverter.__METHOD_IS_PRESENT(object)
            return (
                str(OptionalLongStringConverter.__METHOD_GET(object))
                if is_present
                else ""
            )
        except Exception as ex:
            raise ValueError(ex)

    def __init__(self) -> None:

        pass  # LLM could not translate this method


OptionalLongStringConverter.run_static_init()
