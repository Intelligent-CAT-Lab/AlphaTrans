from __future__ import annotations
import time
import traceback
import copy
import re
from io import StringIO
from abc import ABC
import io
import typing
from typing import *
import datetime
import os
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.SwallowedExceptionListener import *
from src.main.org.apache.commons.pool2.impl.AbandonedConfig import *
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class EvictionIterator:

    __idleObjectIterator: typing.Iterator[PooledObject[typing.Any]] = None

    __idleObjects: typing.Deque[PooledObject[typing.Any]] = None

    def remove(self) -> None:
        self.__idleObjectIterator.remove()

    def next(self) -> PooledObject[typing.Any]:
        return self.__idleObjectIterator.next()

    def hasNext(self) -> bool:
        return self.__idleObjectIterator.hasNext()

    def getIdleObjects(self) -> typing.Deque[PooledObject[typing.Any]]:
        return self.__idleObjects

    def __init__(self, idleObjects: typing.Deque[PooledObject[typing.Any]]) -> None:

        self.__idleObjects = idleObjects

        if self.getLifo():
            self.__idleObjectIterator = reversed(self.__idleObjects)
        else:
            self.__idleObjectIterator = iter(self.__idleObjects)


class IdentityWrapper:

    __instance: typing.Any = None

    def toString(self) -> str:
        return f"IdentityWrapper [instance={self.__instance}]"

    def hashCode(self) -> int:
        return id(self.__instance)

    def equals(self, other: typing.Any) -> bool:
        return (
            isinstance(other, IdentityWrapper) and other.__instance == self.__instance
        )

    def getObject(self) -> typing.Any:
        return self.__instance

    def __init__(self, instance: typing.Any) -> None:
        self.__instance = instance


class StatsStore:

    __index: int = 0

    __size: int = 0

    __values: typing.List[int] = None

    __NULL: int = -1

    def toString(self) -> str:
        return f"StatsStore [{self.getCurrentValues()}], size={self.__size}, index={self.__index}"

    def getMean(self) -> int:

        result = 0.0
        counter = 0
        for i in range(self.__size):
            value = self.__values[i]
            if value != self.__NULL:
                counter += 1
                result = result * ((counter - 1) / counter) + value / counter
        return int(result)

    def getCurrentValues(self) -> typing.List[int]:
        return self.__values[: self.__index]

    def add1(self, value: int) -> None:

        with self.__lock:
            self.__values[self.__index] = value
            self.__index += 1
            if self.__index == self.__size:
                self.__index = 0

    def add0(self, value: datetime.timedelta) -> None:
        self.add1(int(value.total_seconds() * 1000))

    def __init__(self, size: int) -> None:
        self.__size = size
        self.__NULL = -1
        self.__values = [AtomicLong(self.__NULL) for _ in range(size)]


class Evictor:

    __scheduledFuture: concurrent.futures.Future[typing.Any] = None

    def setScheduledFuture(
        self, scheduledFuture: concurrent.futures.Future[typing.Any]
    ) -> None:
        self.__scheduledFuture = scheduledFuture

    def cancel(self) -> None:
        self.__scheduledFuture.cancel()


class BaseGenericObjectPool(BaseObject, ABC):

    _abandonedConfig: AbandonedConfig = None

    destroyedByBorrowValidationCount: int = None  # LLM could not translate this field

    destroyedByEvictorCount: int = None  # LLM could not translate this field

    destroyedCount: int = None  # LLM could not translate this field

    createdCount: int = None  # LLM could not translate this field

    evictionLock: typing.Any = None  # LLM could not translate this field

    closed: bool = False

    closeLock: typing.Any = None  # LLM could not translate this field

    MEAN_TIMING_STATS_CACHE_SIZE: int = 100
    __messageStatistics: bool = False

    __swallowedExceptionListener: SwallowedExceptionListener = None

    __maxBorrowWaitDuration: datetime.timedelta = datetime.timedelta()
    __waitTimes: StatsStore = None
    __waitTimes: StatsStore = None
    __idleTimes: StatsStore = None
    __activeTimes: StatsStore = None
    __activeTimes: StatsStore = None
    __returnedCount: int = None  # LLM could not translate this field

    __borrowedCount: int = None  # LLM could not translate this field

    __evictor: Evictor = None

    __evictorShutdownTimeoutDuration: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
    )
    __evictionPolicy: EvictionPolicy[typing.Any] = None

    __softMinEvictableIdleDuration: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION
    )
    __minEvictableIdleDuration: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION
    )
    __numTestsPerEvictionRun: int = (
        BaseObjectPoolConfig.DEFAULT_NUM_TESTS_PER_EVICTION_RUN
    )
    __durationBetweenEvictionRuns: datetime.timedelta = (
        BaseObjectPoolConfig.DEFAULT_TIME_BETWEEN_EVICTION_RUNS
    )
    __testWhileIdle: bool = BaseObjectPoolConfig.DEFAULT_TEST_WHILE_IDLE
    __testOnReturn: bool = BaseObjectPoolConfig.DEFAULT_TEST_ON_RETURN
    __testOnBorrow: bool = BaseObjectPoolConfig.DEFAULT_TEST_ON_BORROW
    __testOnCreate: bool = BaseObjectPoolConfig.DEFAULT_TEST_ON_CREATE
    __lifo: bool = BaseObjectPoolConfig.DEFAULT_LIFO
    __maxWaitDuration: datetime.timedelta = BaseObjectPoolConfig.DEFAULT_MAX_WAIT
    __blockWhenExhausted: bool = BaseObjectPoolConfig.DEFAULT_BLOCK_WHEN_EXHAUSTED
    __maxTotal: int = GenericKeyedObjectPoolConfig.DEFAULT_MAX_TOTAL
    __DEFAULT_REMOVE_ABANDONED_TIMEOUT: datetime.timedelta = datetime.timedelta(
        seconds=float("inf")
    )
    __EVICTION_POLICY_TYPE_NAME: str = EvictionPolicy.__class__.__name__
    evictionIterator: EvictionIterator = None

    @staticmethod
    def initialize_fields() -> None:
        BaseGenericObjectPool.__waitTimes: StatsStore = StatsStore(
            BaseGenericObjectPool.MEAN_TIMING_STATS_CACHE_SIZE
        )

        BaseGenericObjectPool.__waitTimes: StatsStore = StatsStore(
            BaseGenericObjectPool.MEAN_TIMING_STATS_CACHE_SIZE
        )

        BaseGenericObjectPool.__idleTimes: StatsStore = StatsStore(
            MEAN_TIMING_STATS_CACHE_SIZE
        )

        BaseGenericObjectPool.__activeTimes: StatsStore = StatsStore(
            BaseGenericObjectPool.MEAN_TIMING_STATS_CACHE_SIZE
        )

        BaseGenericObjectPool.__activeTimes: StatsStore = StatsStore(
            BaseGenericObjectPool.MEAN_TIMING_STATS_CACHE_SIZE
        )

    def _toStringAppendFields(self, builder: str) -> None:

        builder += "maxTotal=" + str(self.maxTotal)
        builder += ", blockWhenExhausted=" + str(self.blockWhenExhausted)
        builder += ", maxWaitDuration=" + str(self.maxWaitDuration)
        builder += ", lifo=" + str(self.lifo)
        builder += ", testOnCreate=" + str(self.testOnCreate)
        builder += ", testOnBorrow=" + str(self.testOnBorrow)
        builder += ", testOnReturn=" + str(self.testOnReturn)
        builder += ", testWhileIdle=" + str(self.testWhileIdle)
        builder += ", durationBetweenEvictionRuns=" + str(
            self.durationBetweenEvictionRuns
        )
        builder += ", numTestsPerEvictionRun=" + str(self.numTestsPerEvictionRun)
        builder += ", minEvictableIdleTimeDuration=" + str(
            self.minEvictableIdleDuration
        )
        builder += ", softMinEvictableIdleTimeDuration=" + str(
            self.softMinEvictableIdleDuration
        )
        builder += ", evictionPolicy=" + str(self.evictionPolicy)
        builder += ", closeLock=" + str(self.closeLock)
        builder += ", closed=" + str(self.closed)
        builder += ", evictionLock=" + str(self.evictionLock)
        builder += ", evictor=" + str(self.evictor)
        builder += ", evictionIterator=" + str(self.evictionIterator)
        builder += ", borrowedCount=" + str(self.borrowedCount)
        builder += ", returnedCount=" + str(self.returnedCount)
        builder += ", createdCount=" + str(self.createdCount)
        builder += ", destroyedCount=" + str(self.destroyedCount)
        builder += ", destroyedByEvictorCount=" + str(self.destroyedByEvictorCount)
        builder += ", destroyedByBorrowValidationCount=" + str(
            self.destroyedByBorrowValidationCount
        )
        builder += ", activeTimes=" + str(self.activeTimes)
        builder += ", idleTimes=" + str(self.idleTimes)
        builder += ", waitTimes=" + str(self.waitTimes)
        builder += ", maxBorrowWaitDuration=" + str(self.maxBorrowWaitDuration)
        builder += ", swallowedExceptionListener=" + str(
            self.swallowedExceptionListener
        )

    def setSoftMinEvictableIdleTimeMillis(
        self, softMinEvictableIdleTimeMillis: int
    ) -> None:
        self.setSoftMinEvictableIdleTime(
            datetime.timedelta(milliseconds=softMinEvictableIdleTimeMillis)
        )

    def setSoftMinEvictableIdleTime(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            softMinEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setMinEvictableIdleTimeMillis(self, minEvictableIdleTimeMillis: int) -> None:
        self.setMinEvictableIdleTime(
            datetime.timedelta(milliseconds=minEvictableIdleTimeMillis)
        )

    def setMinEvictableIdleTime(self, minEvictableIdleTime: datetime.timedelta) -> None:
        self.__minEvictableIdleDuration = PoolImplUtils.nonNull(
            minEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setMaxWaitMillis(self, maxWaitMillis: int) -> None:
        self.setMaxWait(datetime.timedelta(milliseconds=maxWaitMillis))

    def setEvictorShutdownTimeoutMillis(
        self, evictorShutdownTimeoutMillis: int
    ) -> None:
        self.setEvictorShutdownTimeout(
            datetime.timedelta(milliseconds=evictorShutdownTimeoutMillis)
        )

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        return int(self.__durationBetweenEvictionRuns.total_seconds() * 1000)

    def getTimeBetweenEvictionRuns(self) -> datetime.timedelta:
        return self.__durationBetweenEvictionRuns

    def getSoftMinEvictableIdleTimeMillis(self) -> int:
        return int(self.__softMinEvictableIdleDuration.total_seconds() * 1000)

    def getSoftMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getRemoveAbandonedTimeout(self) -> int:
        return int(self.getRemoveAbandonedTimeoutDuration().total_seconds())

    def getMinEvictableIdleTimeMillis(self) -> int:
        return int(self.__minEvictableIdleDuration.total_seconds() * 1000)

    def getMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMaxWaitMillis(self) -> int:
        return int(self.__maxWaitDuration.total_seconds() * 1000)

    def getEvictorShutdownTimeoutMillis(self) -> int:
        return int(self.__evictorShutdownTimeoutDuration.total_seconds() * 1000)

    def getEvictorShutdownTimeout(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def __setEvictionPolicy1(self, className: str, classLoader: typing.Any) -> None:

        clazz = Class.forName(className, True, classLoader)
        policy = clazz.getConstructor().newInstance()
        self.__evictionPolicy = typing.cast(EvictionPolicy[typing.Any], policy)

    def updateStatsReturn(self, activeTime: datetime.timedelta) -> None:

        self.__returnedCount += 1
        self.__activeTimes.add0(activeTime)

    def updateStatsBorrow(
        self, p: PooledObject[typing.Any], waitDuration: datetime.timedelta
    ) -> None:

        self.__borrowedCount += 1
        self.__idleTimes.add0(p.getIdleDuration())
        self.__waitTimes.add0(waitDuration)

        currentMaxDuration = self.__maxBorrowWaitDuration
        if currentMaxDuration < waitDuration:
            self.__maxBorrowWaitDuration = waitDuration

    def swallowException(self, swallowException: Exception) -> None:

        listener = self.getSwallowedExceptionListener()

        if listener is None:
            return

        try:
            listener.onSwallowException(swallowException)
        except (VirtualMachineError, MemoryError) as e:
            raise e
        except Exception:
            pass

    def setTestWhileIdle(self, testWhileIdle: bool) -> None:
        self.__testWhileIdle = testWhileIdle

    def setTestOnReturn(self, testOnReturn: bool) -> None:
        self.__testOnReturn = testOnReturn

    def setTestOnCreate(self, testOnCreate: bool) -> None:
        self.__testOnCreate = testOnCreate

    def setTestOnBorrow(self, testOnBorrow: bool) -> None:
        self.__testOnBorrow = testOnBorrow

    def setSwallowedExceptionListener(
        self, swallowedExceptionListener: SwallowedExceptionListener
    ) -> None:
        self.__swallowedExceptionListener = swallowedExceptionListener

    def setSoftMinEvictableIdle(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            softMinEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setNumTestsPerEvictionRun(self, numTestsPerEvictionRun: int) -> None:
        self.__numTestsPerEvictionRun = numTestsPerEvictionRun

    def setMinEvictableIdle(self, minEvictableIdleTime: datetime.timedelta) -> None:
        self.__minEvictableIdleDuration = PoolImplUtils.nonNull(
            minEvictableIdleTime,
            BaseObjectPoolConfig.DEFAULT_MIN_EVICTABLE_IDLE_DURATION,
        )

    def setMessagesStatistics(self, messagesDetails: bool) -> None:
        self.__messageStatistics = messagesDetails

    def setMaxWait(self, maxWaitDuration: datetime.timedelta) -> None:
        self.__maxWaitDuration = PoolImplUtils.nonNull(
            maxWaitDuration, BaseObjectPoolConfig.DEFAULT_MAX_WAIT
        )

    def setMaxTotal(self, maxTotal: int) -> None:
        self.__maxTotal = maxTotal

    def setLifo(self, lifo: bool) -> None:
        self.__lifo = lifo

    def setEvictorShutdownTimeout(
        self, evictorShutdownTimeout: datetime.timedelta
    ) -> None:
        self.__evictorShutdownTimeoutDuration = PoolImplUtils.nonNull(
            evictorShutdownTimeout,
            BaseObjectPoolConfig.DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT,
        )

    def setEvictionPolicyClassName1(
        self, evictionPolicyClassName: str, classLoader: typing.Any
    ) -> None:

        epClass = EvictionPolicy
        epClassLoader = epClass.__class__.__class__

        try:
            self.__setEvictionPolicy1(evictionPolicyClassName, classLoader)
        except (TypeError, ClassNotFoundException) as e:
            self.__setEvictionPolicy1(evictionPolicyClassName, epClassLoader)
        except TypeError as e:
            raise ValueError(
                "Class "
                + evictionPolicyClassName
                + " from class loaders ["
                + classLoader
                + ", "
                + epClassLoader
                + "] do not implement "
                + self.__EVICTION_POLICY_TYPE_NAME
            )
        except (
            ClassNotFoundException,
            InstantiationException,
            IllegalAccessException,
            InvocationTargetException,
            NoSuchMethodException,
        ) as e:
            raise ValueError(
                "Unable to create "
                + self.__EVICTION_POLICY_TYPE_NAME
                + " instance of type "
                + evictionPolicyClassName,
                e,
            )

    def setEvictionPolicyClassName0(self, evictionPolicyClassName: str) -> None:
        self.setEvictionPolicyClassName1(
            evictionPolicyClassName, Thread.currentThread().getContextClassLoader()
        )

    def setEvictionPolicy0(self, evictionPolicy: EvictionPolicy[typing.Any]) -> None:
        self.__evictionPolicy = evictionPolicy

    def setBlockWhenExhausted(self, blockWhenExhausted: bool) -> None:
        self.__blockWhenExhausted = blockWhenExhausted

    def setAbandonedConfig(self, abandonedConfig: AbandonedConfig) -> None:
        self._abandonedConfig = AbandonedConfig.copy(abandonedConfig)

    def _markReturningState(self, pooledObject: PooledObject[typing.Any]) -> None:
        with pooledObject:
            if pooledObject.getState() != PooledObjectState.ALLOCATED:
                raise RuntimeError(
                    "Object has already been returned to this pool or is invalid"
                )
            pooledObject.markReturning()  # Keep from being marked abandoned

    def isClosed(self) -> bool:
        return self.closed

    def isAbandonedConfig(self) -> bool:
        return self._abandonedConfig is not None

    def getDurationBetweenEvictionRuns(self) -> datetime.timedelta:
        return self.__durationBetweenEvictionRuns

    def getTestWhileIdle(self) -> bool:
        return self.__testWhileIdle

    def getTestOnReturn(self) -> bool:
        return self.__testOnReturn

    def getTestOnCreate(self) -> bool:
        return self.__testOnCreate

    def getTestOnBorrow(self) -> bool:
        return self.__testOnBorrow

    def getSwallowedExceptionListener(self) -> SwallowedExceptionListener:
        return self.__swallowedExceptionListener

    def getSoftMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getReturnedCount(self) -> int:
        return self.__returnedCount

    def getRemoveAbandonedTimeoutDuration(self) -> datetime.timedelta:

        ac = self._abandonedConfig
        return (
            ac.getRemoveAbandonedTimeoutDuration()
            if ac is not None
            else self.__DEFAULT_REMOVE_ABANDONED_TIMEOUT
        )

    def getRemoveAbandonedOnMaintenance(self) -> bool:
        ac = self._abandonedConfig
        return ac is not None and ac._removeAbandonedOnMaintenance

    def getRemoveAbandonedOnBorrow(self) -> bool:
        ac = self._abandonedConfig
        return ac is not None and ac._removeAbandonedOnBorrow

    def getNumTestsPerEvictionRun(self) -> int:
        return self.__numTestsPerEvictionRun

    def getMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMessageStatistics(self) -> bool:
        return self.__messageStatistics

    def getMeanIdleTimeMillis(self) -> int:
        return self.__idleTimes.getMean()

    def getMeanBorrowWaitTimeMillis(self) -> int:
        return self.__waitTimes.getMean()

    def getMeanActiveTimeMillis(self) -> int:
        return self.__activeTimes.getMean()

    def getMaxWaitDuration(self) -> datetime.timedelta:
        return self.__maxWaitDuration

    def getMaxTotal(self) -> int:
        return self.__maxTotal

    def getMaxBorrowWaitTimeMillis(self) -> int:
        return self.__maxBorrowWaitDuration.total_seconds() * 1000

    def getLogAbandoned(self) -> bool:
        ac = self._abandonedConfig
        return ac is not None and ac._logAbandoned

    def getLifo(self) -> bool:
        return self.__lifo

    def getEvictorShutdownTimeoutDuration(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def getEvictionPolicyClassName(self) -> str:
        return self.__evictionPolicy.__class__.__name__

    def getEvictionPolicy(self) -> EvictionPolicy[typing.Any]:
        return self.__evictionPolicy

    def getDestroyedCount(self) -> int:
        return self.destroyedCount

    def getDestroyedByEvictorCount(self) -> int:
        return self.destroyedByEvictorCount

    def getDestroyedByBorrowValidationCount(self) -> int:
        return self.destroyedByBorrowValidationCount

    def getCreatedCount(self) -> int:
        return self.createdCount

    def getBorrowedCount(self) -> int:
        return self.__borrowedCount

    def getBlockWhenExhausted(self) -> bool:
        return self.__blockWhenExhausted

    def assertOpen(self) -> None:
        if self.isClosed():
            raise RuntimeError("Pool not open")

    def __getStackTrace(self, e: Exception) -> str:

        w = io.StringIO()
        pw = io.TextIOWrapper(w)
        traceback.print_exc(file=pw)
        return w.getvalue()

    def createRemoveList(
        self,
        abandonedConfig: AbandonedConfig,
        allObjects: typing.Dict[IdentityWrapper[typing.Any], PooledObject[typing.Any]],
    ) -> typing.List[PooledObject[typing.Any]]:

        timeout = (
            datetime.datetime.now()
            - abandonedConfig.getRemoveAbandonedTimeoutDuration()
        )
        remove = []
        for pooledObject in allObjects.values():
            with pooledObject:
                if (
                    pooledObject.getState() == PooledObjectState.ALLOCATED
                    and pooledObject.getLastUsedInstant() <= timeout
                ):
                    pooledObject.markAbandoned()
                    remove.append(pooledObject)
        return remove

    def getNumIdle(self) -> int:
        pass

    def evict(self) -> None:
        raise NotImplementedError("Subclass must implement abstract method")

    def ensureMinIdle(self) -> None:

        # Your implementation here
        pass

    def close(self) -> None:
        pass


BaseGenericObjectPool.initialize_fields()
