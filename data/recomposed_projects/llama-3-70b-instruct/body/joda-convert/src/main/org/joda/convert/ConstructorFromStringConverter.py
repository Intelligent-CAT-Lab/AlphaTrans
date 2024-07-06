from __future__ import annotations
import time
import re
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class ConstructorFromStringConverter(TypedFromStringConverter):

    __fromString: typing.Callable[..., typing.Any] = None

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__fromString.__self__.__class__

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        try:
            return self.__fromString(str)
        except IllegalAccessException as ex:
            raise RuntimeError("Constructor is not accessible: " + self.__fromString)
        except InstantiationException as ex:
            raise RuntimeError("Constructor is not valid: " + self.__fromString)
        except InvocationTargetException as ex:
            if isinstance(ex.getCause(), RuntimeError):
                raise ex.getCause()
            raise RuntimeError(ex.getMessage(), ex.getCause())

    def __init__(
        self, cls: typing.Type[typing.Any], fromString: typing.Callable[..., typing.Any]
    ) -> None:

        pass  # LLM could not translate this method
