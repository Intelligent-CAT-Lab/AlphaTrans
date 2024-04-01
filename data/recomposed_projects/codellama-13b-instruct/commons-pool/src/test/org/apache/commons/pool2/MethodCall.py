# Imports Begin
import unittest
import typing
from typing import *

# Imports End


class MethodCall(unittest.TestCase):

    # Class Fields Begin
    __name: str = None
    __params: typing.List[typing.Any] = None
    __returned: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        sb = StringBuilder()
        sb.append("MethodCall")
        sb.append("{name='").append(self.__name).append("'")
        if not self.__params.isEmpty():
            sb.append(", params=").append(self.__params)
        if self.__returned != None:
            sb.append(", returned=").append(self.__returned)
        sb.append("}")
        return sb.toString()

    def hashCode(self) -> int:

        result = hash(self.name) if self.name is not None else 0
        result = 29 * result + (hash(self.params) if self.params is not None else 0)
        result = 29 * result + (hash(self.returned) if self.returned is not None else 0)
        return result

    def equals(self, o: typing.Any) -> bool:

        if self is o:
            return True
        if o is None or type(self) != type(o):
            return False
        that: MethodCall = o
        if self.name != that.name:
            return False
        if self.params != that.params:
            return False
        return self.returned == that.returned

    def setReturned(self, returned: typing.Any) -> None:

        self.__returned = returned

    def returned(self, obj: typing.Any) -> "MethodCall":

        self.setReturned(obj)
        return self

    def getReturned(self) -> typing.Any:

        return self.returned

    def getParams(self) -> typing.List[typing.Any]:

        return self.__params

    def getName(self) -> str:

        return self.__name

    @staticmethod
    def MethodCall3(name: str) -> "MethodCall":

        pass  # LLM could not translate method body

    @staticmethod
    def MethodCall1(name: str, param: typing.Any) -> "MethodCall":

        pass  # LLM could not translate method body

    @staticmethod
    def MethodCall0(name: str, param1: typing.Any, param2: typing.Any) -> "MethodCall":

        pass  # LLM could not translate method body

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
                raise ValueError("name must not be None.")
            self.name = name
            if params is not None:
                self.params = params
            else:
                self.params = []
        else:
            if name is None:
                raise ValueError("name must not be None.")
            self.name = name
            if params is not None:
                self.params = params
            else:
                self.params = []

    # Class Methods End
