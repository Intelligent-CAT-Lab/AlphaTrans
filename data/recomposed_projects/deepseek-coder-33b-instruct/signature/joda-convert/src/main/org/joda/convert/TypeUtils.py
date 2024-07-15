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

        TypeUtils.__PRIMITIVES = {
            "byte": byte,
            "short": short,
            "int": int,
            "long": long,
            "boolean": bool,
            "char": char,
            "float": float,
            "double": double,
        }

    @staticmethod
    def parse(str: str) -> typing.Type:
        try:
            return TypeUtils.__doParse(str)
        except RuntimeError as ex:
            raise ex
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

        result = []
        generic_count = 0
        start_pos = 0
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

        token = TypeUtils.__PRIMITIVES.get(str)
        if token is not None:
            return token

        first = str.find("<")
        if first < 0:
            return StringConvert.loadType(str)

        last = str.rfind(">")
        baseStr = str[0:first]
        base = StringConvert.loadType(baseStr)
        argsStr = str[first + 1 : last]
        splitArgs = TypeUtils.__split(argsStr)
        types = []

        for splitArg in splitArgs:
            if splitArg.startswith(TypeUtils.__EXTENDS):
                remainder = splitArg[len(TypeUtils.__EXTENDS) :]
                argType = TypeUtils.__wildExtendsType(TypeUtils.__doParse(remainder))
            elif splitArg.startswith(TypeUtils.__SUPER):
                remainder = splitArg[len(TypeUtils.__SUPER) :]
                argType = TypeUtils.__wildSuperType(TypeUtils.__doParse(remainder))
            elif splitArg == "?":
                argType = TypeUtils.__wildExtendsType(object)
            elif splitArg.endswith("[]"):
                componentStr = splitArg[:-2]
                componentCls = StringConvert.loadType(componentStr)
                argType = Array.newInstance(componentCls, 0).__class__
            elif splitArg.startswith("[L") and splitArg.endswith(";"):
                componentStr = splitArg[2:-1]
                componentCls = StringConvert.loadType(componentStr)
                argType = Array.newInstance(componentCls, 0).__class__
            else:
                argType = TypeUtils.__doParse(splitArg)
            types.append(argType)

        return TypeUtils.__newParameterizedType(base, types)

    def __init__(self) -> None:
        pass


TypeUtils.run_static_init()
