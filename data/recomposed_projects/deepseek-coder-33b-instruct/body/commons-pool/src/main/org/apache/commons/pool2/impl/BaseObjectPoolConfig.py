from __future__ import annotations
import time
import re
from abc import ABC
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.impl.DefaultEvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class BaseObjectPoolConfig(BaseObject, ABC):

    DEFAULT_EVICTION_POLICY_CLASS_NAME: str = DefaultEvictionPolicy.__name__
    DEFAULT_JMX_NAME_BASE: str = None
    DEFAULT_JMX_NAME_PREFIX: str = "pool"
    DEFAULT_JMX_ENABLE: bool = True
    DEFAULT_BLOCK_WHEN_EXHAUSTED: bool = True
    DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS: int = -1
    DEFAULT_TEST_WHILE_IDLE: bool = False
    DEFAULT_TEST_ON_RETURN: bool = False
    DEFAULT_TEST_ON_BORROW: bool = False
    DEFAULT_TEST_ON_CREATE: bool = False
    DEFAULT_NUM_TESTS_PER_EVICTION_RUN: int = 3
    DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT_MILLIS: int = 10 * 1000
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS: int = -1
    DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS: int = 1000 * 60 * 30
    DEFAULT_MAX_WAIT_MILLIS: int = -1
    DEFAULT_FAIRNESS: bool = False
    DEFAULT_LIFO: bool = True
    __jmxNameBase: str = DEFAULT_JMX_NAME_BASE
    __jmxNamePrefix: str = DEFAULT_JMX_NAME_PREFIX
    __jmxEnabled: bool = DEFAULT_JMX_ENABLE
    __blockWhenExhausted: bool = DEFAULT_BLOCK_WHEN_EXHAUSTED
    __testWhileIdle: bool = DEFAULT_TEST_WHILE_IDLE
    __testOnReturn: bool = DEFAULT_TEST_ON_RETURN
    __testOnBorrow: bool = DEFAULT_TEST_ON_BORROW
    __testOnCreate: bool = DEFAULT_TEST_ON_CREATE
    __evictionPolicyClassName: str = DEFAULT_EVICTION_POLICY_CLASS_NAME
    __evictionPolicy: EvictionPolicy[typing.Any] = None

    __numTestsPerEvictionRun: int = DEFAULT_NUM_TESTS_PER_EVICTION_RUN
    __fairness: bool = DEFAULT_FAIRNESS
    __lifo: bool = DEFAULT_LIFO
    DEFAULT_TIME_BETWEEN_EVICTION_RUNS: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS
    )
    DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT_MILLIS
    )
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS
    )
    DEFAULT_MIN_EVICTABLE_IDLE_TIME: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS
    )
    DEFAULT_MIN_EVICTABLE_IDLE_DURATION: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS
    )
    DEFAULT_MAX_WAIT: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_MAX_WAIT_MILLIS
    )
    __durationBetweenEvictionRuns: datetime.timedelta = (
        DEFAULT_TIME_BETWEEN_EVICTION_RUNS
    )
    __softMinEvictableIdleDuration: datetime.timedelta = (
        DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME
    )
    __evictorShutdownTimeoutDuration: datetime.timedelta = (
        DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
    )
    __minEvictableIdleDuration: datetime.timedelta = DEFAULT_MIN_EVICTABLE_IDLE_TIME
    __maxWaitDuration: datetime.timedelta = DEFAULT_MAX_WAIT
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION: datetime.timedelta = datetime.timedelta(
        milliseconds=DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS
    )

    def _toStringAppendFields(self, builder: str) -> None:

        builder += "lifo=" + str(self.__lifo)
        builder += ", fairness=" + str(self.__fairness)
        builder += ", maxWaitDuration=" + str(self.__maxWaitDuration)
        builder += ", minEvictableIdleTime=" + str(self.__minEvictableIdleDuration)
        builder += ", softMinEvictableIdleTime=" + str(
            self.__softMinEvictableIdleDuration
        )
        builder += ", numTestsPerEvictionRun=" + str(self.__numTestsPerEvictionRun)
        builder += ", evictionPolicyClassName=" + str(self.__evictionPolicyClassName)
        builder += ", testOnCreate=" + str(self.__testOnCreate)
        builder += ", testOnBorrow=" + str(self.__testOnBorrow)
        builder += ", testOnReturn=" + str(self.__testOnReturn)
        builder += ", testWhileIdle=" + str(self.__testWhileIdle)
        builder += ", timeBetweenEvictionRuns=" + str(
            self.__durationBetweenEvictionRuns
        )
        builder += ", blockWhenExhausted=" + str(self.__blockWhenExhausted)
        builder += ", jmxEnabled=" + str(self.__jmxEnabled)
        builder += ", jmxNamePrefix=" + str(self.__jmxNamePrefix)
        builder += ", jmxNameBase=" + str(self.__jmxNameBase)

    def setTimeBetweenEvictionRunsMillis(
        self, timeBetweenEvictionRunsMillis: int
    ) -> None:
        self.__durationBetweenEvictionRuns = PoolImplUtils.nonNull(
            datetime.timedelta(milliseconds=timeBetweenEvictionRunsMillis),
            DEFAULT_TIME_BETWEEN_EVICTION_RUNS,
        )

    def setSoftMinEvictableIdleTimeMillis(
        self, softMinEvictableIdleTimeMillis: int
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            datetime.timedelta(milliseconds=softMinEvictableIdleTimeMillis),
            DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME,
        )

    def setMinEvictableIdleTimeMillis(self, minEvictableIdleTimeMillis: int) -> None:
        self.__minEvictableIdleDuration = datetime.timedelta(
            milliseconds=minEvictableIdleTimeMillis
        )

    def setMaxWaitMillis(self, maxWaitMillis: int) -> None:
        self.__maxWaitDuration = PoolImplUtils.nonNull(
            datetime.timedelta(milliseconds=maxWaitMillis), self.DEFAULT_MAX_WAIT
        )

    def setEvictorShutdownTimeoutMillis1(
        self, evictorShutdownTimeoutMillis: int
    ) -> None:
        self.__evictorShutdownTimeoutDuration = PoolImplUtils.nonNull(
            datetime.timedelta(milliseconds=evictorShutdownTimeoutMillis),
            DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT,
        )

    def setEvictorShutdownTimeoutMillis0(
        self, evictorShutdownTimeout: datetime.timedelta
    ) -> None:
        self.setEvictorShutdownTimeout(evictorShutdownTimeout)

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        return self.__durationBetweenEvictionRuns.total_seconds() * 1000

    def getTimeBetweenEvictionRuns(self) -> datetime.timedelta:
        return self.__durationBetweenEvictionRuns

    def getSoftMinEvictableIdleTimeMillis(self) -> int:
        return self.__softMinEvictableIdleDuration.total_seconds() * 1000

    def getSoftMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getMinEvictableIdleTimeMillis(self) -> int:
        return self.__minEvictableIdleDuration.total_seconds() * 1000

    def getMinEvictableIdleTime(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMaxWaitMillis(self) -> int:
        return self.__maxWaitDuration.total_seconds() * 1000

    def getEvictorShutdownTimeoutMillis(self) -> int:
        return self.__evictorShutdownTimeoutDuration.total_seconds() * 1000

    def getEvictorShutdownTimeout(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def setTimeBetweenEvictionRuns(
        self, timeBetweenEvictionRuns: datetime.timedelta
    ) -> None:
        self.__durationBetweenEvictionRuns = PoolImplUtils.nonNull(
            timeBetweenEvictionRuns, DEFAULT_TIME_BETWEEN_EVICTION_RUNS
        )

    def setTestWhileIdle(self, testWhileIdle: bool) -> None:
        self.__testWhileIdle = testWhileIdle

    def setTestOnReturn(self, testOnReturn: bool) -> None:
        self.__testOnReturn = testOnReturn

    def setTestOnCreate(self, testOnCreate: bool) -> None:
        self.__testOnCreate = testOnCreate

    def setTestOnBorrow(self, testOnBorrow: bool) -> None:
        self.__testOnBorrow = testOnBorrow

    def setSoftMinEvictableIdleTime(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        self.__softMinEvictableIdleDuration = PoolImplUtils.nonNull(
            softMinEvictableIdleTime, DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME
        )

    def setNumTestsPerEvictionRun(self, numTestsPerEvictionRun: int) -> None:
        self.__numTestsPerEvictionRun = numTestsPerEvictionRun

    def setMinEvictableIdleTime(self, minEvictableIdleTime: datetime.timedelta) -> None:
        self.__minEvictableIdleDuration = PoolImplUtils.nonNull(
            minEvictableIdleTime, self.DEFAULT_MIN_EVICTABLE_IDLE_TIME
        )

    def setMaxWait(self, maxWaitDuration: datetime.timedelta) -> None:
        self.__maxWaitDuration = PoolImplUtils.nonNull(
            maxWaitDuration, self.DEFAULT_MAX_WAIT
        )

    def setLifo(self, lifo: bool) -> None:
        self.__lifo = lifo

    def setJmxNamePrefix(self, jmxNamePrefix: str) -> None:
        self.__jmxNamePrefix = jmxNamePrefix

    def setJmxNameBase(self, jmxNameBase: str) -> None:
        self.__jmxNameBase = jmxNameBase

    def setJmxEnabled(self, jmxEnabled: bool) -> None:
        self.__jmxEnabled = jmxEnabled

    def setFairness(self, fairness: bool) -> None:
        self.__fairness = fairness

    def setEvictorShutdownTimeout(
        self, evictorShutdownTimeoutDuration: datetime.timedelta
    ) -> None:
        self.__evictorShutdownTimeoutDuration = PoolImplUtils.nonNull(
            evictorShutdownTimeoutDuration, DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT
        )

    def setEvictionPolicyClassName(self, evictionPolicyClassName: str) -> None:
        self.__evictionPolicyClassName = evictionPolicyClassName

    def setEvictionPolicy(self, evictionPolicy: EvictionPolicy[typing.Any]) -> None:
        self.__evictionPolicy = evictionPolicy

    def setBlockWhenExhausted(self, blockWhenExhausted: bool) -> None:
        self.__blockWhenExhausted = blockWhenExhausted

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

    def getSoftMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__softMinEvictableIdleDuration

    def getNumTestsPerEvictionRun(self) -> int:
        return self.__numTestsPerEvictionRun

    def getMinEvictableIdleDuration(self) -> datetime.timedelta:
        return self.__minEvictableIdleDuration

    def getMaxWaitDuration(self) -> datetime.timedelta:
        return self.__maxWaitDuration

    def getLifo(self) -> bool:
        return self.__lifo

    def getJmxNamePrefix(self) -> str:
        return self.__jmxNamePrefix

    def getJmxNameBase(self) -> str:
        return self.__jmxNameBase

    def getJmxEnabled(self) -> bool:
        return self.__jmxEnabled

    def getFairness(self) -> bool:
        return self.__fairness

    def getEvictorShutdownTimeoutDuration(self) -> datetime.timedelta:
        return self.__evictorShutdownTimeoutDuration

    def getEvictionPolicyClassName(self) -> str:
        return self.__evictionPolicyClassName

    def getEvictionPolicy(self) -> EvictionPolicy[typing.Any]:
        return self.__evictionPolicy

    def getBlockWhenExhausted(self) -> bool:
        return self.__blockWhenExhausted
