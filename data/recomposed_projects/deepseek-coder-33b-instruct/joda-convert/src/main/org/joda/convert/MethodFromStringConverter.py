from __future__ import annotations
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
            return cls.cast(self.__fromString.invoke(None, str))
        except IllegalAccessException as ex:
            raise RuntimeError("Method is not accessible: " + self.__fromString)
        except InvocationTargetException as ex:
            if isinstance(ex.getCause(), RuntimeError):
                raise ex.getCause()
            raise RuntimeError(ex.getMessage(), ex.getCause())

    def __init__(
        self,
        cls: typing.Type[typing.Any],
        fromString: typing.Union[inspect.Signature, typing.Callable],
        effectiveType: typing.Type[typing.Any],
    ) -> None:

        if (
            not inspect.isfunction(fromString)
            or not inspect.ismethod(fromString)
            or not hasattr(fromString, "__self__")
        ):
            raise TypeError("FromString method must be a method: " + str(fromString))

        if not inspect.signature(fromString).parameters:
            raise ValueError(
                "FromString method must have one parameter: " + str(fromString)
            )

        param = list(inspect.signature(fromString).parameters.values())[0]
        if param.annotation != str and param.annotation != typing.AnyStr:
            raise ValueError(
                "FromString method must take a String or CharSequence: "
                + str(fromString)
            )

        if not issubclass(cls, fromString.__self__.__class__) and not issubclass(
            fromString.__self__.__class__, cls
        ):
            raise ValueError(
                "FromString method must return specified class or a supertype: "
                + str(fromString)
            )

        self.__fromString = fromString
        self.__effectiveType = effectiveType
