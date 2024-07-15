from __future__ import annotations
import time
import inspect
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class MethodFromStringConverter(TypedFromStringConverter):

    __effectiveType: typing.Type[typing.Any] = None

    __fromString: typing.Union[inspect.Signature, typing.Callable] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__effectiveType

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:

        try:
            return cls.cast(self.__fromString(str))
        except Exception as ex:
            raise RuntimeError("Method is not accessible: " + str(self.__fromString))

    def __init__(
        self,
        cls: typing.Type[typing.Any],
        fromString: typing.Union[inspect.Signature, typing.Callable],
        effectiveType: typing.Type[typing.Any],
    ) -> None:

        pass  # LLM could not translate this method
