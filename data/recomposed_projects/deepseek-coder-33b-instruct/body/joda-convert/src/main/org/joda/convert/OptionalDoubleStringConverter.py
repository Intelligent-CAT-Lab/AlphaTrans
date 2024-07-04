from __future__ import annotations
import inspect
import re
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

    @staticmethod
    def run_static_init():

        try:
            OptionalDoubleStringConverter.__TYPE = getattr(
                importlib.import_module("java.util"), "OptionalDouble"
            )
            OptionalDoubleStringConverter.__EMPTY = (
                OptionalDoubleStringConverter.__TYPE.getDeclaredMethod("empty").invoke(
                    None
                )
            )
            OptionalDoubleStringConverter.__METHOD_OF = (
                OptionalDoubleStringConverter.__TYPE.getDeclaredMethod("of", float)
            )
            OptionalDoubleStringConverter.__METHOD_IS_PRESENT = (
                OptionalDoubleStringConverter.__TYPE.getDeclaredMethod("isPresent")
            )
            OptionalDoubleStringConverter.__METHOD_GET = (
                OptionalDoubleStringConverter.__TYPE.getDeclaredMethod("getAsDouble")
            )

        except Exception as ex:
            raise RuntimeError(ex)

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
            isPresent = OptionalDoubleStringConverter.__METHOD_IS_PRESENT(object)
            return (
                str(OptionalDoubleStringConverter.__METHOD_GET(object))
                if isPresent
                else ""
            )
        except Exception as ex:
            raise ValueError(ex)

    def __init__(self) -> None:
        pass


OptionalDoubleStringConverter.run_static_init()
