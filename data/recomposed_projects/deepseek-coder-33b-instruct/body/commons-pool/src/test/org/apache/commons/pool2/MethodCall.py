from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *


class MethodCall:

    __returned: typing.Any = None

    __params: typing.List[typing.Any] = None

    __name: str = ""

    def toString(self) -> str:

        sb = "MethodCall{"
        sb += "name='" + self.__name + "'"
        if self.__params:
            sb += ", params=" + str(self.__params)
        if self.__returned is not None:
            sb += ", returned=" + str(self.__returned)
        sb += "}"
        return sb

    def hashCode(self) -> int:

        result: int = 0
        result = 29 * result + (hash(self.__name) if self.__name is not None else 0)
        result = 29 * result + (
            hash(tuple(self.__params)) if self.__params is not None else 0
        )
        result = 29 * result + (
            hash(self.__returned) if self.__returned is not None else 0
        )
        return result

    def equals(self, o: typing.Any) -> bool:

        if self == o:
            return True

        if o is None or self.__class__ != o.__class__:
            return False

        that: MethodCall = typing.cast(MethodCall, o)

        if self.__name != that.__name:
            return False

        if self.__params != that.__params:
            return False

        return self.__returned == that.__returned

    def setReturned(self, returned: typing.Any) -> None:
        self.__returned = returned

    def returned(self, obj: typing.Any) -> MethodCall:
        self.setReturned(obj)
        return self

    def getReturned(self) -> typing.Any:
        return self.__returned

    def getParams(self) -> typing.List[typing.Any]:
        return self.__params

    def getName(self) -> str:
        return self.__name

    @staticmethod
    def MethodCall3(name: str) -> MethodCall:
        return MethodCall(2, None, None, None, name, None)

    @staticmethod
    def MethodCall1(name: str, param: typing.Any) -> MethodCall:

        if name is None:
            raise ValueError("name must not be null.")

        if param is None:
            raise ValueError("param must not be null.")

        return MethodCall(2, None, [param], None, name, None)

    @staticmethod
    def MethodCall0(name: str, param1: typing.Any, param2: typing.Any) -> MethodCall:

        if name is None:
            raise ValueError("name must not be null.")

        params = [param1, param2]

        return MethodCall(2, None, params, None, name, None)

    def __init__(
        self,
        constructorId: int,
        param2: typing.Any,
        params: typing.List[typing.Any],
        param1: typing.Any,
        name: str,
        param: typing.Any,
    ) -> None:

        if constructorId == 2:
            if name is None:
                raise ValueError("name must not be null.")
            self.__name = name
            if params is not None:
                self.__params = params
            else:
                self.__params = []
        else:
            if name is None:
                raise ValueError("name must not be null.")
            self.__name = name
            if params is not None:
                self.__params = params
            else:
                self.__params = []
