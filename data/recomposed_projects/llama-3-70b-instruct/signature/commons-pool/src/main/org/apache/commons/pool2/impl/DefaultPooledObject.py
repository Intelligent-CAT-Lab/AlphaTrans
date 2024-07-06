from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
import datetime
import sys
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.TrackedUse import *
from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class DefaultPooledObject:

    __borrowedCount: int = 0

    __usedBy: CallStack = NoOpCallStack.INSTANCE
    __borrowedBy: CallStack = NoOpCallStack.INSTANCE
    __logAbandoned: bool = False

    __createInstant: datetime.datetime = self.__now()
    __systemClock: datetime.datetime = datetime.datetime.now()
    __state: PooledObjectState = PooledObjectState.IDLE
    __object: typing.Any = None

    __lastReturnInstant: datetime.datetime = __createInstant
    __lastUseInstant: datetime.datetime = __createInstant
    __lastBorrowInstant: datetime.datetime = __createInstant

    def use(self) -> None:
        self.__lastUseInstant = self.__now()
        self.__usedBy.fillInStackTrace()

    def toString(self) -> str:

        pass  # LLM could not translate this method

    def startEvictionTest(self) -> bool:
        if self.__state == PooledObjectState.IDLE:
            self.__state = PooledObjectState.EVICTION
            return True
        return False

    def setLogAbandoned(self, logAbandoned: bool) -> None:
        self.__logAbandoned = logAbandoned

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:
        written = self.__borrowedBy.printStackTrace(writer)
        written |= self.__usedBy.printStackTrace(writer)
        if written:
            writer.flush()

    def markReturning(self) -> None:
        self.__state = PooledObjectState.RETURNING

    def markAbandoned(self) -> None:
        self.__state = PooledObjectState.ABANDONED

    def invalidate(self) -> None:
        self.__state = PooledObjectState.INVALID

    def getState(self) -> PooledObjectState:
        return self.__state

    def getObject(self) -> typing.Any:
        return self.__object

    def getLastUsedTime(self) -> int:
        return self.getLastUsedInstant().timestamp() * 1000

    def getLastUsedInstant(self) -> datetime.datetime:
        if isinstance(self.__object, TrackedUse):
            return PoolImplUtils.max(
                self.__object.getLastUsedInstant(), self.__lastUseInstant
            )
        return self.__lastUseInstant

    def getLastReturnTime(self) -> int:
        return self.__lastReturnInstant.timestamp() * 1000

    def getLastReturnInstant(self) -> datetime.datetime:
        return self.__lastReturnInstant

    def getLastBorrowTime(self) -> int:
        return self.__lastBorrowInstant.timestamp() * 1000

    def getLastBorrowInstant(self) -> datetime.datetime:
        return self.__lastBorrowInstant

    def getIdleTimeMillis(self) -> int:
        return self.getIdleDuration().total_seconds() * 1000

    def getIdleTime(self) -> datetime.timedelta:
        return self.getIdleDuration()

    def getIdleDuration(self) -> datetime.timedelta:
        elapsed = datetime.timedelta.between(self.__lastReturnInstant, self.__now())
        return datetime.timedelta.ZERO if elapsed.is_negative() else elapsed

    def getCreateTime(self) -> int:
        return self.__createInstant.timestamp() * 1000

    def getCreateInstant(self) -> datetime.datetime:
        return self.__createInstant

    def getBorrowedCount(self) -> int:
        return self.__borrowedCount

    def deallocate(self) -> bool:
        if (
            self.__state == PooledObjectState.ALLOCATED
            or self.__state == PooledObjectState.RETURNING
        ):
            self.__state = PooledObjectState.IDLE
            self.__lastReturnInstant = self.__now()
            self.__borrowedBy.clear()
            return True
        return False

    def compareTo(self, other: PooledObject[typing.Any]) -> int:
        compareTo = self.getLastReturnInstant().compareTo(other.getLastReturnInstant())
        if compareTo == 0:
            return System.identityHashCode(self) - System.identityHashCode(other)
        return compareTo

    def allocate(self) -> bool:

        pass  # LLM could not translate this method

    def __init__(self, object: typing.Any) -> None:
        self.__object = object

    def __now(self) -> datetime.datetime:
        return self.__systemClock.now()
