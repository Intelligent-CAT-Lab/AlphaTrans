from __future__ import annotations
import io
import typing
from typing import *


class MethodCall:

    __returned: typing.Any = None
    __params: typing.List[typing.Any] = None
    __name: str = None

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write("MethodCall")
        sb.write("{name='")
        sb.write(self.__name)
        sb.write("'")

        if self.__params is not None and len(self.__params) > 0:
            sb.write(", params=")
            sb.write(str(self.__params))

        if self.__returned is not None:
            sb.write(", returned=")
            sb.write(str(self.__returned))

        sb.write("}")

        return sb.getvalue()

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

        if self is o:
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

    def setReturned(self, returned: typing.Any) -> None:
        self.__returned = returned

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

        return MethodCall(2, None, [param], None, name, None)

    @staticmethod
    def MethodCall0(name: str, param1: typing.Any, param2: typing.Any) -> MethodCall:

        return MethodCall(2, None, [param1, param2], None, name, None)

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
