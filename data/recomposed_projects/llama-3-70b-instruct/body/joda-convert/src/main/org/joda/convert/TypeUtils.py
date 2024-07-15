from __future__ import annotations
import time
import re
import os
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.Types import *


class TypeUtils:

    __PRIMITIVES: typing.Dict[str, typing.Type[typing.Any]] = None

    __SUPER: str = "? super "
    __EXTENDS: str = "? extends "

    @staticmethod
    def run_static_init():
        map = {}
        map["byte"] = int
        map["short"] = int
        map["int"] = int
        map["long"] = int
        map["boolean"] = bool
        map["char"] = str
        map["float"] = float
        map["double"] = float
        TypeUtils.__PRIMITIVES = map

    @staticmethod
    def parse(str: str) -> typing.Type:
        try:
            return TypeUtils.__doParse(str)
        except Exception as ex:
            raise RuntimeError(ex)

    @staticmethod
    def __newParameterizedType(
        base: typing.Type[typing.Any], args: typing.List[typing.Type]
    ) -> typing.Generic[typing.TypeVar("T")]:
        return Types.newParameterizedType(base, args)

    @staticmethod
    def __wildSuperType(bound: typing.Type) -> typing.Type:
        return Types.supertypeOf(bound)

    @staticmethod
    def __wildExtendsType(bound: typing.Type) -> typing.Type:
        return Types.subtypeOf(bound)

    @staticmethod
    def __split(str: str) -> typing.List[str]:
        result: typing.List[str] = []
        generic_count: int = 0
        start_pos: int = 0
        for i in range(len(str)):
            if str[i] == "," and generic_count == 0:
                result.append(str[start_pos:i].strip())
                start_pos = i + 1
            elif str[i] == "<":
                generic_count += 1
            elif str[i] == ">":
                generic_count -= 1
        result.append(str[start_pos:].strip())
        return result

    @staticmethod
    def __doParse(str: str) -> typing.Type:
        token: typing.Type[typing.Any] = TypeUtils.__PRIMITIVES.get(str)
        if token is not None:
            return token
        first: int = str.index("<")
        if first < 0:
            return StringConvert.loadType(str)
        last: int = str.rindex(">")
        baseStr: str = str[0:first]
        base: typing.Type[typing.Any] = StringConvert.loadType(baseStr)
        argsStr: str = str[first + 1 : last]
        splitArgs: typing.List[str] = TypeUtils.__split(argsStr)
        types: typing.List[typing.Type] = []
        for splitArg in splitArgs:
            argType: typing.Type
            if splitArg.startswith(TypeUtils.__EXTENDS):
                remainder: str = splitArg[len(TypeUtils.__EXTENDS) :]
                argType = TypeUtils.__wildExtendsType(TypeUtils.__doParse(remainder))
            elif splitArg.startswith(TypeUtils.__SUPER):
                remainder: str = splitArg[len(TypeUtils.__SUPER) :]
                argType = TypeUtils.__wildSuperType(TypeUtils.__doParse(remainder))
            elif splitArg == "?":
                argType = TypeUtils.__wildExtendsType(Object)
            elif splitArg.endswith("[]"):
                componentStr: str = splitArg[0 : len(splitArg) - 2]
                componentCls: typing.Type[typing.Any] = StringConvert.loadType(
                    componentStr
                )
                argType = Array.newInstance(componentCls, 0).getClass()
            elif splitArg.startswith("[L") and splitArg.endswith(";"):
                componentStr: str = splitArg[2 : len(splitArg) - 1]
                componentCls: typing.Type[typing.Any] = StringConvert.loadType(
                    componentStr
                )
                argType = Array.newInstance(componentCls, 0).getClass()
            else:
                argType = TypeUtils.__doParse(splitArg)
            types.append(argType)
        return TypeUtils.__newParameterizedType(base, types)

    def __init__(self) -> None:
        pass


TypeUtils.run_static_init()
