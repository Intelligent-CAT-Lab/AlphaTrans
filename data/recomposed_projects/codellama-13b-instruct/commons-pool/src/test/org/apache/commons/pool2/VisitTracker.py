# Imports Begin
import unittest
import typing
from typing import *

# Imports End


class VisitTracker(unittest.TestCase):

    # Class Fields Begin
    __validateCount: int = None
    __activateCount: int = None
    __passivateCount: int = None
    __destroyed: bool = None
    __id: int = None
    __key: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        return f"Key: {self.__key} id: {self.__id}"

    def validate(self) -> bool:

        if self.__destroyed:
            self.__fail("attempted to validate a destroyed object")
        self.__validateCount += 1
        return True

    def reset(self) -> None:

        self.__validateCount = 0
        self.__activateCount = 0
        self.__passivateCount = 0
        self.__destroyed = False

    def passivate(self) -> None:

        pass  # LLM could not translate method body

    def isDestroyed(self) -> bool:

        return self.__destroyed

    def getValidateCount(self) -> int:

        return self.__validateCount

    def getPassivateCount(self) -> int:

        return self.__passivateCount

    def getKey(self) -> typing.Any:

        return self.__key

    def getId(self) -> int:

        return self.__id

    def getActivateCount(self) -> int:

        return self.__activateCount

    def destroy(self) -> None:

        self.__destroyed = True

    def activate(self) -> None:

        if self.__destroyed:
            self.__fail("attempted to activate a destroyed object")
        self.__activateCount += 1

    def __init__(self, constructorId: int, key: typing.Any, id: int) -> None:

        if constructorId == 0:
            self.__id = id
            self.__key = key
            self.reset()
        elif constructorId == 1:
            self.__id = id
            self.reset()
        else:
            self.reset()

    def __fail(self, message: str) -> None:

        raise IllegalStateException(message)

    # Class Methods End
