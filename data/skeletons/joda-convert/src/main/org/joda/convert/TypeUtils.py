from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.Types import *
from src.main.org.joda.convert.StringConvert import *
import typing
from typing import *
import io

# Imports End


class TypeUtils:

    # Class Fields Begin
    __EXTENDS: str = None
    __SUPER: str = None
    __PRIMITIVES: typing.Dict[str, typing.Type[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def parse(str: str) -> typing.Type:
        pass

    @staticmethod
    def __newParameterizedType(
        base: typing.Type[typing.Any], args: typing.List[typing.Type]
    ) -> typing.Generic[typing.TypeVar("T")]:
        pass

    @staticmethod
    def __wildSuperType(bound: typing.Type) -> typing.Type:
        pass

    @staticmethod
    def __wildExtendsType(bound: typing.Type) -> typing.Type:
        pass

    @staticmethod
    def __split(str: str) -> typing.List[str]:
        pass

    @staticmethod
    def __doParse(str: str) -> typing.Type:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
