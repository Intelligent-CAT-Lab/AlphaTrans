from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class MethodCall:

    # Class Fields Begin
    __name: str = None
    __params: typing.List[typing.Any] = None
    __returned: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, o: typing.Any) -> bool:
        pass

    def setReturned(self, returned: typing.Any) -> None:
        pass

    def returned(self, obj: typing.Any) -> MethodCall:
        pass

    def getReturned(self) -> typing.Any:
        pass

    def getParams(self) -> typing.List[typing.Any]:
        pass

    def getName(self) -> str:
        pass

    @staticmethod
    def MethodCall3(name: str) -> MethodCall:
        pass

    @staticmethod
    def MethodCall1(name: str, param: typing.Any) -> MethodCall:
        pass

    @staticmethod
    def MethodCall0(name: str, param1: typing.Any, param2: typing.Any) -> MethodCall:
        pass

    def __init__(
        self,
        constructorId: int,
        param2: typing.Any,
        params: typing.List[typing.Any],
        param1: typing.Any,
        name: str,
        param: typing.Any,
    ) -> None:
        pass

    # Class Methods End
