from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.TypedFromStringConverter import *
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.ReflectionStringConverter import *
from src.main.org.joda.convert.MethodFromStringConverter import *
from src.main.org.joda.convert.FromStringFactory import *
from src.main.org.joda.convert.FromString import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *
import typing
from typing import *
import io

# Imports End


class AnnotationStringConverterFactory(StringConverterFactory):

    # Class Fields Begin
    INSTANCE: AnnotationStringConverterFactory = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    def __eliminateEnumSubclass(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Type[typing.Any]:
        pass

    def __findFromString(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Union[inspect.Signature, typing.Callable]:
        pass

    def __findFromStringMethod(
        self, cls: typing.Type[typing.Any], searchSuperclasses: bool
    ) -> TypedStringConverter[typing.Any]:
        pass

    def __findFromStringConstructor(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    def __findToStringMethod(
        self, cls: typing.Type[typing.Any]
    ) -> typing.Union[inspect.Signature, typing.Callable]:
        pass

    def __findAnnotatedFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    def __findAnnotatedConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:
        pass

    def __init__(self) -> None:
        pass

    def findFromStringConverter(
        self, cls: typing.Type[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    # Class Methods End
