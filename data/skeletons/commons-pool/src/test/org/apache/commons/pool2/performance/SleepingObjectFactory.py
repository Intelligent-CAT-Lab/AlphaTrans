from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.pool2.Waiter import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from typing import *
import io

# Imports End


class SleepingObjectFactory:

    # Class Fields Begin
    __counter: int = None
    __debug: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, obj: PooledObject[int]) -> bool:
        pass

    def setDebug(self, b: bool) -> None:
        pass

    def passivateObject(self, obj: PooledObject[int]) -> None:
        pass

    def isDebug(self) -> bool:
        pass

    def destroyObject(self, obj: PooledObject[int]) -> None:
        pass

    def activateObject(self, obj: PooledObject[int]) -> None:
        pass

    def __debug(self, method: str, obj: typing.Any) -> None:
        pass

    # Class Methods End
