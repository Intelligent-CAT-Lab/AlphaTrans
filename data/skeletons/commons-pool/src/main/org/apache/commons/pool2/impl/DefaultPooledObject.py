from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *
from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.TrackedUse import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.PooledObject import *
import sys
import datetime
import typing
from typing import *
import io
from io import StringIO

# Imports End


class DefaultPooledObject:

    # Class Fields Begin
    __object: typing.Any = None
    __state: PooledObjectState = None
    __systemClock: datetime.datetime = None
    __createInstant: datetime.datetime = None
    __lastBorrowInstant: datetime.datetime = None
    __lastUseInstant: datetime.datetime = None
    __lastReturnInstant: datetime.datetime = None
    __logAbandoned: bool = None
    __borrowedBy: CallStack = None
    __usedBy: CallStack = None
    __borrowedCount: int = None
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

    def getState(self) -> PooledObjectState:
        pass

    def getObject(self) -> typing.Any:
        pass

    def getLastUsedTime(self) -> int:
        pass

    def getLastUsedInstant(self) -> datetime.datetime:
        pass

    def getLastReturnTime(self) -> int:
        pass

    def getLastReturnInstant(self) -> datetime.datetime:
        pass

    def getLastBorrowTime(self) -> int:
        pass

    def getLastBorrowInstant(self) -> datetime.datetime:
        pass

    def getIdleTimeMillis(self) -> int:
        pass

    def getIdleTime(self) -> datetime.timedelta:
        pass

    def getIdleDuration(self) -> datetime.timedelta:
        pass

    def getCreateTime(self) -> int:
        pass

    def getCreateInstant(self) -> datetime.datetime:
        pass

    def getBorrowedCount(self) -> int:
        pass

    def deallocate(self) -> bool:
        pass

    def compareTo(self, other: PooledObject[typing.Any]) -> int:
        pass

    def allocate(self) -> bool:
        pass

    def __init__(self, object_: typing.Any) -> None:
        pass

    def __now(self) -> datetime.datetime:
        pass

    # Class Methods End
