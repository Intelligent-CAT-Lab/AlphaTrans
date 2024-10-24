from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.impl.EvictionPolicy import *
from src.main.org.apache.commons.pool2.impl.DefaultEvictionPolicy import *
from src.main.org.apache.commons.pool2.BaseObject import *
import datetime
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class BaseObjectPoolConfig(BaseObject, ABC):

    # Class Fields Begin
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS: int = None
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME: datetime.timedelta = None
    DEFAULT_SOFT_MIN_EVICTABLE_IDLE_DURATION: datetime.timedelta = None
    DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT_MILLIS: int = None
    DEFAULT_EVICTOR_SHUTDOWN_TIMEOUT: datetime.timedelta = None
    DEFAULT_NUM_TESTS_PER_EVICTION_RUN: int = None
    DEFAULT_TEST_ON_CREATE: bool = None
    DEFAULT_TEST_ON_BORROW: bool = None
    DEFAULT_TEST_ON_RETURN: bool = None
    DEFAULT_TEST_WHILE_IDLE: bool = None
    DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS: int = None
    DEFAULT_TIME_BETWEEN_EVICTION_RUNS: datetime.timedelta = None
    DEFAULT_BLOCK_WHEN_EXHAUSTED: bool = None
    DEFAULT_JMX_ENABLE: bool = None
    DEFAULT_JMX_NAME_PREFIX: str = None
    DEFAULT_JMX_NAME_BASE: str = None
    DEFAULT_EVICTION_POLICY_CLASS_NAME: str = None
    __lifo: bool = None
    __fairness: bool = None
    __maxWaitDuration: datetime.timedelta = None
    __minEvictableIdleDuration: datetime.timedelta = None
    __evictorShutdownTimeoutDuration: datetime.timedelta = None
    __softMinEvictableIdleDuration: datetime.timedelta = None
    __numTestsPerEvictionRun: int = None
    __evictionPolicy: EvictionPolicy[typing.Any] = None
    __evictionPolicyClassName: str = None
    __testOnCreate: bool = None
    __testOnBorrow: bool = None
    __testOnReturn: bool = None
    __testWhileIdle: bool = None
    __durationBetweenEvictionRuns: datetime.timedelta = None
    __blockWhenExhausted: bool = None
    __jmxEnabled: bool = None
    __jmxNamePrefix: str = None
    __jmxNameBase: str = None
    DEFAULT_LIFO: bool = None
    DEFAULT_FAIRNESS: bool = None
    DEFAULT_MAX_WAIT_MILLIS: int = None
    DEFAULT_MAX_WAIT: datetime.timedelta = None
    DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS: int = None
    DEFAULT_MIN_EVICTABLE_IDLE_DURATION: datetime.timedelta = None
    DEFAULT_MIN_EVICTABLE_IDLE_TIME: datetime.timedelta = None
    # Class Fields End

    # Class Methods Begin
    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    def setTimeBetweenEvictionRunsMillis(
        self, timeBetweenEvictionRunsMillis: int
    ) -> None:
        pass

    def setSoftMinEvictableIdleTimeMillis(
        self, softMinEvictableIdleTimeMillis: int
    ) -> None:
        pass

    def setMinEvictableIdleTimeMillis(self, minEvictableIdleTimeMillis: int) -> None:
        pass

    def setMaxWaitMillis(self, maxWaitMillis: int) -> None:
        pass

    def setEvictorShutdownTimeoutMillis1(
        self, evictorShutdownTimeoutMillis: int
    ) -> None:
        pass

    def setEvictorShutdownTimeoutMillis0(
        self, evictorShutdownTimeout: datetime.timedelta
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

    def setTimeBetweenEvictionRuns(
        self, timeBetweenEvictionRuns: datetime.timedelta
    ) -> None:
        pass

    def setTestWhileIdle(self, testWhileIdle: bool) -> None:
        pass

    def setTestOnReturn(self, testOnReturn: bool) -> None:
        pass

    def setTestOnCreate(self, testOnCreate: bool) -> None:
        pass

    def setTestOnBorrow(self, testOnBorrow: bool) -> None:
        pass

    def setSoftMinEvictableIdleTime(
        self, softMinEvictableIdleTime: datetime.timedelta
    ) -> None:
        pass

    def setNumTestsPerEvictionRun(self, numTestsPerEvictionRun: int) -> None:
        pass

    def setMinEvictableIdleTime(self, minEvictableIdleTime: datetime.timedelta) -> None:
        pass

    def setMaxWait(self, maxWaitDuration: datetime.timedelta) -> None:
        pass

    def setLifo(self, lifo: bool) -> None:
        pass

    def setJmxNamePrefix(self, jmxNamePrefix: str) -> None:
        pass

    def setJmxNameBase(self, jmxNameBase: str) -> None:
        pass

    def setJmxEnabled(self, jmxEnabled: bool) -> None:
        pass

    def setFairness(self, fairness: bool) -> None:
        pass

    def setEvictorShutdownTimeout(
        self, evictorShutdownTimeoutDuration: datetime.timedelta
    ) -> None:
        pass

    def setEvictionPolicyClassName(self, evictionPolicyClassName: str) -> None:
        pass

    def setEvictionPolicy(self, evictionPolicy: EvictionPolicy[typing.Any]) -> None:
        pass

    def setBlockWhenExhausted(self, blockWhenExhausted: bool) -> None:
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

    def getSoftMinEvictableIdleDuration(self) -> datetime.timedelta:
        pass

    def getNumTestsPerEvictionRun(self) -> int:
        pass

    def getMinEvictableIdleDuration(self) -> datetime.timedelta:
        pass

    def getMaxWaitDuration(self) -> datetime.timedelta:
        pass

    def getLifo(self) -> bool:
        pass

    def getJmxNamePrefix(self) -> str:
        pass

    def getJmxNameBase(self) -> str:
        pass

    def getJmxEnabled(self) -> bool:
        pass

    def getFairness(self) -> bool:
        pass

    def getEvictorShutdownTimeoutDuration(self) -> datetime.timedelta:
        pass

    def getEvictionPolicyClassName(self) -> str:
        pass

    def getEvictionPolicy(self) -> EvictionPolicy[typing.Any]:
        pass

    def getBlockWhenExhausted(self) -> bool:
        pass

    # Class Methods End
