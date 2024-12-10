from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObjectState import *
import datetime
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class PooledObject(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def use(self) -> None:
        pass

    def toString(self) -> str:
        pass

    def startEvictionTest(self) -> bool:
        pass

    def setLogAbandoned(self, logAbandoned: bool) -> None:
        pass

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:
        pass

    def markReturning(self) -> None:
        pass

    def markAbandoned(self) -> None:
        pass

    def invalidate(self) -> None:
        pass

    def hashCode(self) -> int:
        pass

    def getState(self) -> PooledObjectState:
        pass

    def getObject(self) -> typing.Any:
        pass

    def getLastUsedTime(self) -> int:
        pass

    def getLastReturnTime(self) -> int:
        pass

    def getLastBorrowTime(self) -> int:
        pass

    def getIdleTimeMillis(self) -> int:
        pass

    def getCreateTime(self) -> int:
        pass

    def getActiveTimeMillis(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def endEvictionTest(self, idleQueue: typing.Deque[PooledObject]) -> bool:
        pass

    def deallocate(self) -> bool:
        pass

    def compareTo(self, other: PooledObject) -> int:
        pass

    def allocate(self) -> bool:
        pass

    def setRequireFullStackTrace(self) -> None:
        pass

    def getLastUsedInstant(self) -> datetime.datetime:
        pass

    def getLastReturnInstant(self) -> datetime.datetime:
        pass

    def getLastBorrowInstant(self) -> datetime.datetime:
        pass

    def getIdleTime(self) -> datetime.timedelta:
        pass

    def getIdleDuration(self) -> datetime.timedelta:
        pass

    def getCreateInstant(self) -> datetime.datetime:
        pass

    def getBorrowedCount(self) -> int:
        pass

    def getActiveTime(self) -> datetime.timedelta:
        pass

    def getActiveDuration(self) -> datetime.timedelta:
        pass

    # Class Methods End
