from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.DefaultPooledObjectInfoMBean import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from typing import *
import io

# Imports End


class DefaultPooledObjectInfo(DefaultPooledObjectInfoMBean):

    # Class Fields Begin
    __PATTERN: str = None
    __pooledObject: PooledObject[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getPooledObjectType(self) -> str:
        pass

    def getPooledObjectToString(self) -> str:
        pass

    def getLastReturnTimeFormatted(self) -> str:
        pass

    def getLastReturnTime(self) -> int:
        pass

    def getLastBorrowTrace(self) -> str:
        pass

    def getLastBorrowTimeFormatted(self) -> str:
        pass

    def getLastBorrowTime(self) -> int:
        pass

    def getCreateTimeFormatted(self) -> str:
        pass

    def getCreateTime(self) -> int:
        pass

    def getBorrowedCount(self) -> int:
        pass

    def __init__(self, pooledObject: PooledObject[typing.Any]) -> None:
        pass

    def __getTimeFormatted(self, millis: int) -> str:
        pass

    # Class Methods End
