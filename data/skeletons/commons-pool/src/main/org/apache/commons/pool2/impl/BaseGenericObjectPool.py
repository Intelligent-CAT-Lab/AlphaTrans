from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.AbandonedConfig import *
from src.main.org.apache.commons.pool2.SwallowedExceptionListener import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.BaseObject import *
import os
import datetime
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class EvictionIterator:

    # Class Fields Begin
    __idleObjects: typing.Deque[PooledObject[typing.Any]] = None
    __idleObjectIterator: typing.Iterator[PooledObject[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def remove(self) -> None:
        pass

    def next_(self) -> PooledObject[typing.Any]:
        pass

    def hasNext(self) -> bool:
        pass

    def getIdleObjects(self) -> typing.Deque[PooledObject[typing.Any]]:
        pass

    def __init__(self, idleObjects: typing.Deque[PooledObject[typing.Any]]) -> None:
        pass

    # Class Methods End


class IdentityWrapper:

    # Class Fields Begin
    __instance: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, other: typing.Any) -> bool:
        pass

    def getObject(self) -> typing.Any:
        pass

    def __init__(self, instance: typing.Any) -> None:
        pass

    # Class Methods End


class StatsStore:

    # Class Fields Begin
    __NULL: int = None
    __values: typing.List[int] = None
    __size: int = None
    __index: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getMean(self) -> int:
        pass

    def getCurrentValues(self) -> typing.List[int]:
        pass

    def add1(self, value: int) -> None:
        pass

    def add0(self, value: datetime.timedelta) -> None:
        pass

    def __init__(self, size: int) -> None:
        pass

    # Class Methods End


class Evictor:

    # Class Fields Begin
    __scheduledFuture: concurrent.futures.Future[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def setScheduledFuture(
        self, scheduledFuture: concurrent.futures.Future[typing.Any]
    ) -> None:
        pass

    def cancel(self) -> None:
        pass

    # Class Methods End


class BaseGenericObjectPool(BaseObject, ABC):

    # Class Fields Begin
    MEAN_TIMING_STATS_CACHE_SIZE: int = None
    __EVICTION_POLICY_TYPE_NAME: str = None
    __DEFAULT_REMOVE_ABANDONED_TIMEOUT: datetime.timedelta = None
    __maxTotal: int = None
    __blockWhenExhausted: bool = None
    __maxWaitDuration: datetime.timedelta = None
    __lifo: bool = None
    __testOnCreate: bool = None
    __testOnBorrow: bool = None
    __testOnReturn: bool = None
    __testWhileIdle: bool = None
    __durationBetweenEvictionRuns: datetime.timedelta = None
    __numTestsPerEvictionRun: int = None
    __minEvictableIdleDuration: datetime.timedelta = None
    __softMinEvictableIdleDuration: datetime.timedelta = None
    __evictionPolicy: EvictionPolicy[typing.Any] = None
    __evictorShutdownTimeoutDuration: datetime.timedelta = None
    closeLock: typing.Any = None
    closed: bool = None
    evictionLock: typing.Any = None
    __evictor: Evictor = None
    evictionIterator: EvictionIterator = None
    __borrowedCount: int = None
    __returnedCount: int = None
    createdCount: int = None
    destroyedCount: int = None
    destroyedByEvictorCount: int = None
    destroyedByBorrowValidationCount: int = None
    __activeTimes: StatsStore = None
    __idleTimes: StatsStore = None
    __waitTimes: StatsStore = None
    __maxBorrowWaitDuration: typing.Generic[
        typing.TypeVar("T", bound=datetime.timedelta)
    ] = None
    __swallowedExceptionListener: SwallowedExceptionListener = None
    __messageStatistics: bool = None
    _abandonedConfig: AbandonedConfig = None
    # Class Fields End

    # Class Methods Begin
    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    def setSoftMinEvictableIdleTimeMillis(
        self, softMinEvictableIdleTimeMillis: int
    ) -> None:
        pass

    def setSoftMinEvictableIdleTime(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        pass

    def setMinEvictableIdleTimeMillis(self, minEvictableIdleTimeMillis: int) -> None:
        pass

    def setMinEvictableIdleTime(self, minEvictableIdleTime: datetime.timedelta) -> None:
        pass

    def setMaxWaitMillis(self, maxWaitMillis: int) -> None:
        pass

    def setEvictorShutdownTimeoutMillis(
        self, evictorShutdownTimeoutMillis: int
    ) -> None:
        pass

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        pass

    def getTimeBetweenEvictionRuns(self) -> datetime.timedelta:
        pass

    def getSoftMinEvictableIdleTimeMillis(self) -> int:
        pass

    def getSoftMinEvictableIdleTime(self) -> datetime.timedelta:
        pass

    def getRemoveAbandonedTimeout(self) -> int:
        pass

    def getMinEvictableIdleTimeMillis(self) -> int:
        pass

    def getMinEvictableIdleTime(self) -> datetime.timedelta:
        pass

    def getMaxWaitMillis(self) -> int:
        pass

    def getEvictorShutdownTimeoutMillis(self) -> int:
        pass

    def getEvictorShutdownTimeout(self) -> datetime.timedelta:
        pass

    def __setEvictionPolicy1(self, className: str, classLoader: typing.Any) -> None:
        pass

    def updateStatsReturn(self, activeTime: datetime.timedelta) -> None:
        pass

    def updateStatsBorrow(
        self, p: PooledObject[typing.Any], waitDuration: datetime.timedelta
    ) -> None:
        pass

    def swallowException(self, swallowException: Exception) -> None:
        pass

    def setTestWhileIdle(self, testWhileIdle: bool) -> None:
        pass

    def setTestOnReturn(self, testOnReturn: bool) -> None:
        pass

    def setTestOnCreate(self, testOnCreate: bool) -> None:
        pass

    def setTestOnBorrow(self, testOnBorrow: bool) -> None:
        pass

    def setSwallowedExceptionListener(
        self, swallowedExceptionListener: SwallowedExceptionListener
    ) -> None:
        pass

    def setSoftMinEvictableIdle(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        pass

    def setNumTestsPerEvictionRun(self, numTestsPerEvictionRun: int) -> None:
        pass

    def setMinEvictableIdle(self, minEvictableIdleTime: datetime.timedelta) -> None:
        pass

    def setMessagesStatistics(self, messagesDetails: bool) -> None:
        pass

    def setMaxWait(self, maxWaitDuration: datetime.timedelta) -> None:
        pass

    def setMaxTotal(self, maxTotal: int) -> None:
        pass

    def setLifo(self, lifo: bool) -> None:
        pass

    def setEvictorShutdownTimeout(
        self, evictorShutdownTimeout: datetime.timedelta
    ) -> None:
        pass

    def setEvictionPolicyClassName1(
        self, evictionPolicyClassName: str, classLoader: typing.Any
    ) -> None:
        pass

    def setEvictionPolicyClassName0(self, evictionPolicyClassName: str) -> None:
        pass

    def setEvictionPolicy0(self, evictionPolicy: EvictionPolicy[typing.Any]) -> None:
        pass

    def setBlockWhenExhausted(self, blockWhenExhausted: bool) -> None:
        pass

    def setAbandonedConfig(self, abandonedConfig: AbandonedConfig) -> None:
        pass

    def _markReturningState(self, pooledObject: PooledObject[typing.Any]) -> None:
        pass

    def isClosed(self) -> bool:
        pass

    def isAbandonedConfig(self) -> bool:
        pass

    def getDurationBetweenEvictionRuns(self) -> datetime.timedelta:
        pass

    def getTestWhileIdle(self) -> bool:
        pass

    def getTestOnReturn(self) -> bool:
        pass

    def getTestOnCreate(self) -> bool:
        pass

    def getTestOnBorrow(self) -> bool:
        pass

    def getSwallowedExceptionListener(self) -> SwallowedExceptionListener:
        pass

    def getSoftMinEvictableIdleDuration(self) -> datetime.timedelta:
        pass

    def getReturnedCount(self) -> int:
        pass

    def getRemoveAbandonedTimeoutDuration(self) -> datetime.timedelta:
        pass

    def getRemoveAbandonedOnMaintenance(self) -> bool:
        pass

    def getRemoveAbandonedOnBorrow(self) -> bool:
        pass

    def getNumTestsPerEvictionRun(self) -> int:
        pass

    def getMinEvictableIdleDuration(self) -> datetime.timedelta:
        pass

    def getMessageStatistics(self) -> bool:
        pass

    def getMeanIdleTimeMillis(self) -> int:
        pass

    def getMeanBorrowWaitTimeMillis(self) -> int:
        pass

    def getMeanActiveTimeMillis(self) -> int:
        pass

    def getMaxWaitDuration(self) -> datetime.timedelta:
        pass

    def getMaxTotal(self) -> int:
        pass

    def getMaxBorrowWaitTimeMillis(self) -> int:
        pass

    def getLogAbandoned(self) -> bool:
        pass

    def getLifo(self) -> bool:
        pass

    def getEvictorShutdownTimeoutDuration(self) -> datetime.timedelta:
        pass

    def getEvictionPolicyClassName(self) -> str:
        pass

    def getEvictionPolicy(self) -> EvictionPolicy[typing.Any]:
        pass

    def getDestroyedCount(self) -> int:
        pass

    def getDestroyedByEvictorCount(self) -> int:
        pass

    def getDestroyedByBorrowValidationCount(self) -> int:
        pass

    def getCreatedCount(self) -> int:
        pass

    def getBorrowedCount(self) -> int:
        pass

    def getBlockWhenExhausted(self) -> bool:
        pass

    def assertOpen(self) -> None:
        pass

    def __getStackTrace(self, e: Exception) -> str:
        pass

    def createRemoveList(
        self,
        abandonedConfig: AbandonedConfig,
        allObjects: typing.Dict[IdentityWrapper[typing.Any], PooledObject[typing.Any]],
    ) -> typing.List[PooledObject[typing.Any]]:
        pass

    def getNumIdle(self) -> int:
        pass

    def evict(self) -> None:
        pass

    def ensureMinIdle(self) -> None:
        pass

    def close(self) -> None:
        pass

    # Class Methods End
