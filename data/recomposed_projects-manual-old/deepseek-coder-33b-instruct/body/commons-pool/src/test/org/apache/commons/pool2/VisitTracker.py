from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *


class VisitTracker:

    __key: typing.Any = None

    __id: int = 0

    __destroyed: bool = False

    __passivateCount: int = 0

    __activateCount: int = 0

    __validateCount: int = 0

    def toString(self) -> str:
        return "Key: " + str(self.__key) + " id: " + str(self.__id)

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

    def ivate(self) -> None:
        if self.__destroyed:
            self.__fail("attempted to passivate a destroyed object")
        self.__passivateCount += 1

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
        raise RuntimeError(message)
