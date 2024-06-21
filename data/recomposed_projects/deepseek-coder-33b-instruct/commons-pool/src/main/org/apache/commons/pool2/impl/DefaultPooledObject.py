from __future__ import annotations
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

    __borrowedCount: int = None

    __usedBy: CallStack = NoOpCallStack.INSTANCE

    __borrowedBy: CallStack = NoOpCallStack.INSTANCE
    __logAbandoned: bool = None

    __lastReturnInstant: datetime.datetime = datetime.datetime.now()

    __lastUseInstant: datetime.datetime = datetime.datetime.now()

    __lastBorrowInstant: datetime.datetime = datetime.datetime.now()

    __createInstant: datetime.datetime = datetime.datetime.now()

    __systemClock: datetime.datetime = datetime.datetime.utcnow()

    __state: PooledObjectState = PooledObjectState.IDLE
    __object: typing.Any = None

    def use(self) -> None:

        self.__lastUseInstant = self.__now()
        self.__usedBy.fillInStackTrace()

    def toString(self) -> str:

        result = StringIO()
        result.write("Object: ")
        result.write(str(self.__object))
        result.write(", State: ")
        with self:
            result.write(str(self.__state))
        return result.getvalue()

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
                (self.__object).getLastUsedInstant(), self.__lastUseInstant
            )
        return self.__lastUseInstant

    def getLastReturnTime(self) -> int:

        return int(self.__lastReturnInstant.timestamp() * 1000)

    def getLastReturnInstant(self) -> datetime.datetime:

        return self.__lastReturnInstant

    def getLastBorrowTime(self) -> int:

        return int(self.__lastBorrowInstant.timestamp() * 1000)

    def getLastBorrowInstant(self) -> datetime.datetime:

        return self.__lastBorrowInstant

    def getIdleTimeMillis(self) -> int:

        return int(self.getIdleDuration().total_seconds() * 1000)

    def getIdleTime(self) -> datetime.timedelta:

        return self.getIdleDuration()

    def getIdleDuration(self) -> datetime.timedelta:

        elapsed = datetime.datetime.now() - self.__lastReturnInstant
        return datetime.timedelta() if elapsed.total_seconds() < 0 else elapsed

    def getCreateTime(self) -> int:

        return int(self.__createInstant.timestamp() * 1000)

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
            return id(self) - id(other)
        return compareTo

    def allocate(self) -> bool:

        if self.__state == PooledObjectState.IDLE:
            self.__state = PooledObjectState.ALLOCATED
            self.__lastBorrowInstant = self.__now()
            self.__lastUseInstant = self.__lastBorrowInstant
            self.__borrowedCount += 1
            if self.__logAbandoned:
                self.__borrowedBy.fillInStackTrace()
            return True
        if self.__state == PooledObjectState.EVICTION:
            self.__state = PooledObjectState.EVICTION_RETURN_TO_HEAD
        return False

    def __init__(self, object: typing.Any) -> None:

        self.__object = object

    def __now(self) -> datetime.datetime:

        return datetime.datetime.now(self.__systemClock.tzinfo)
