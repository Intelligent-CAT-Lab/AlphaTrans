from __future__ import annotations
import inspect
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedStringConverter import *


class OptionalIntStringConverter(TypedStringConverter):

    __METHOD_GET: typing.Union[inspect.Signature, typing.Callable] = None

    __METHOD_IS_PRESENT: typing.Union[inspect.Signature, typing.Callable] = None

    __METHOD_OF: typing.Union[inspect.Signature, typing.Callable] = None

    __EMPTY: typing.Any = None

    __TYPE: typing.Type[typing.Any] = None

    @staticmethod
    def run_static_init():

        try:
            OptionalIntStringConverter.__TYPE = getattr(
                importlib.import_module("java.util"), "OptionalInt"
            )
            OptionalIntStringConverter.__EMPTY = (
                OptionalIntStringConverter.__TYPE.getDeclaredMethod("empty").invoke(
                    None
                )
            )
            OptionalIntStringConverter.__METHOD_OF = (
                OptionalIntStringConverter.__TYPE.getDeclaredMethod("of", int)
            )
            OptionalIntStringConverter.__METHOD_IS_PRESENT = (
                OptionalIntStringConverter.__TYPE.getDeclaredMethod("isPresent")
            )
            OptionalIntStringConverter.__METHOD_GET = (
                OptionalIntStringConverter.__TYPE.getDeclaredMethod("getAsInt")
            )

        except Exception as ex:
            raise RuntimeError(ex)

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__TYPE

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
            is_present = OptionalIntStringConverter.__METHOD_IS_PRESENT(object)
            return (
                str(OptionalIntStringConverter.__METHOD_GET(object))
                if is_present
                else ""
            )
        except Exception as ex:
            raise ValueError(ex)

    def __init__(self) -> None:

        pass  # LLM could not translate this method


OptionalIntStringConverter.run_static_init()
