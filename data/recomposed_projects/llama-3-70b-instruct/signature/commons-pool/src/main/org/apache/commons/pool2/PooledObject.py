from __future__ import annotations
import time
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.PooledObjectState import *


class PooledObject(ABC):

    def use(self) -> None:
        pass

    def toString(self) -> str:
        return f"PooledObject({self._obj})"

    def startEvictionTest(self) -> bool:
        return True

    def setLogAbandoned(self, logAbandoned: bool) -> None:
        self._logAbandoned = logAbandoned

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:
        writer.write(self.toString())
        writer.write("\n")
        writer.write("PooledObjectState: ")
        writer.write(self.getState().toString())
        writer.write("\n")
        writer.write("StackTrace: ")
        writer.write("\n")
        for stackTraceElement in self.getStackTrace():
            writer.write(stackTraceElement.toString())
            writer.write("\n")

    def markReturning(self) -> None:
        self._state = PooledObjectState.RETURNING

    def markAbandoned(self) -> None:
        self._state = PooledObjectState.ABANDONED

    def invalidate(self) -> None:
        self.state = PooledObjectState.INVALID

    def hashCode(self) -> int:
        return hash(self)

    def getState(self) -> PooledObjectState:
        return PooledObjectState()

    def getObject(self) -> typing.Any:
        return self._obj

    def getLastUsedTime(self) -> int:
        return self.lastUsedTime

    def getLastReturnTime(self) -> int:
        return self._lastReturnTime

    def getLastBorrowTime(self) -> int:
        return self._lastBorrowTime

    def getIdleTimeMillis(self) -> int:
        return self.getIdleTime().toMillis()

    def getCreateTime(self) -> int:
        return self._createTime

    def getActiveTimeMillis(self) -> int:
        return self._activeTimeMillis

    def equals(self, obj: typing.Any) -> bool:
        if obj is None:
            return False
        if self is obj:
            return True
        if not isinstance(obj, PooledObject):
            return False
        other = obj
        if self._obj is None:
            if other._obj is not None:
                return False
        elif self._obj != other._obj:
            return False
        if self._state != other._state:
            return False
        return True

    def endEvictionTest(self, idleQueue: typing.Deque[PooledObject]) -> bool:
        return idleQueue.remove(self)

    def deallocate(self) -> bool:
        return True

    def compareTo(self, other: PooledObject) -> int:
        return self._state.compareTo(other._state)

    def allocate(self) -> bool:
        return True

    def setRequireFullStackTrace(self) -> None:
        pass

    def getLastUsedInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastUsedTime() / 1000)

    def getLastReturnInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastReturnTime() / 1000)

    def getLastBorrowInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getLastBorrowTime() / 1000)

    def getIdleTime(self) -> datetime.timedelta:
        return datetime.timedelta(milliseconds=self.getIdleTimeMillis())

    def getIdleDuration(self) -> datetime.timedelta:
        return datetime.timedelta(milliseconds=self.getIdleTimeMillis())

    def getCreateInstant(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.getCreateTime() / 1000)

    def getBorrowedCount(self) -> int:
        return -1

    def getActiveTime(self) -> datetime.timedelta:
        return self.getActiveDuration()

    def getActiveDuration(self) -> datetime.timedelta:
        lastReturnInstant = self.getLastReturnInstant()
        lastBorrowInstant = self.getLastBorrowInstant()
        return (
            datetime.timedelta.between(lastBorrowInstant, lastReturnInstant)
            if lastReturnInstant.isAfter(lastBorrowInstant)
            else datetime.timedelta.between(lastBorrowInstant, datetime.datetime.now())
        )
