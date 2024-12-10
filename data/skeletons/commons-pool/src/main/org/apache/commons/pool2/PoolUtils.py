from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
import os
import typing
from typing import *
import threading
import io

# Imports End


class ErodingFactor:

    # Class Fields Begin
    __factor: float = None
    __nextShrinkMillis: int = None
    __idleHighWaterMark: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def update(self, nowMillis: int, numIdle: int) -> None:
        pass

    def getNextShrink(self) -> int:
        pass

    def __init__(self, factor: float) -> None:
        pass

    # Class Methods End


class ErodingKeyedObjectPool(KeyedObjectPool):

    # Class Fields Begin
    __keyedPool: KeyedObjectPool[typing.Any, typing.Any] = None
    __erodingFactor: ErodingFactor = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def close(self) -> None:
        pass

    def borrowObject(self, key: typing.Any) -> typing.Any:
        pass

    def addObject(self, key: typing.Any) -> None:
        pass

    def getNumIdle1(self, key: typing.Any) -> int:
        pass

    def getNumIdle0(self) -> int:
        pass

    def getNumActive1(self, key: typing.Any) -> int:
        pass

    def getNumActive0(self) -> int:
        pass

    def _getKeyedPool(self) -> KeyedObjectPool[typing.Any, typing.Any]:
        pass

    def _getErodingFactor(self, key: typing.Any) -> ErodingFactor:
        pass

    def clear1(self, key: typing.Any) -> None:
        pass

    def clear0(self) -> None:
        pass

    @staticmethod
    def ErodingKeyedObjectPool0(
        keyedPool: KeyedObjectPool[typing.Any], factor: float
    ) -> ErodingKeyedObjectPool[typing.Any]:
        pass

    def __init__(
        self,
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        erodingFactor: ErodingFactor,
    ) -> None:
        pass

    # Class Methods End


class ErodingObjectPool(ObjectPool):

    # Class Fields Begin
    __pool: ObjectPool[typing.Any] = None
    __factor: ErodingFactor = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def getNumIdle(self) -> int:
        pass

    def getNumActive(self) -> int:
        pass

    def close(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    def addObject(self) -> None:
        pass

    def __init__(self, pool: ObjectPool[typing.Any], factor: float) -> None:
        pass

    # Class Methods End


class ErodingPerKeyKeyedObjectPool:

    # Class Fields Begin
    __factor: float = None
    __factors: typing.Dict[typing.Any, ErodingFactor] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def _getErodingFactor(self, key: typing.Any) -> ErodingFactor:
        pass

    def __init__(
        self, keyedPool: KeyedObjectPool[typing.Any, typing.Any], factor: float
    ) -> None:
        pass

    # Class Methods End


class KeyedObjectPoolMinIdleTimerTask:

    # Class Fields Begin
    __minIdle: int = None
    __key: typing.Any = None
    __keyedPool: KeyedObjectPool[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def run(self) -> None:
        pass

    def __init__(
        self,
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        key: typing.Any,
        minIdle: int,
    ) -> None:
        pass

    # Class Methods End


class ObjectPoolMinIdleTimerTask:

    # Class Fields Begin
    __minIdle: int = None
    __pool: ObjectPool[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def run(self) -> None:
        pass

    def __init__(self, pool: ObjectPool[typing.Any], minIdle: int) -> None:
        pass

    # Class Methods End


class SynchronizedKeyedObjectPool(KeyedObjectPool):

    # Class Fields Begin
    __readWriteLock: threading.RLock = None
    __keyedPool: KeyedObjectPool[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def close(self) -> None:
        pass

    def borrowObject(self, key: typing.Any) -> typing.Any:
        pass

    def addObject(self, key: typing.Any) -> None:
        pass

    def getNumIdle1(self, key: typing.Any) -> int:
        pass

    def getNumIdle0(self) -> int:
        pass

    def getNumActive1(self, key: typing.Any) -> int:
        pass

    def getNumActive0(self) -> int:
        pass

    def clear1(self, key: typing.Any) -> None:
        pass

    def clear0(self) -> None:
        pass

    def __init__(self, keyedPool: KeyedObjectPool[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End


class SynchronizedKeyedPooledObjectFactory:

    # Class Fields Begin
    __writeLock: typing.Union[threading.RLock, threading.Lock] = None
    __keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> bool:
        pass

    def toString(self) -> str:
        pass

    def passivateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:
        pass

    def makeObject(self, key: typing.Any) -> PooledObject[typing.Any]:
        pass

    def destroyObject0(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:
        pass

    def __init__(
        self, keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> None:
        pass

    # Class Methods End


class SynchronizedObjectPool(ObjectPool):

    # Class Fields Begin
    __readWriteLock: threading.RLock = None
    __pool: ObjectPool[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def getNumIdle(self) -> int:
        pass

    def getNumActive(self) -> int:
        pass

    def close(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    def addObject(self) -> None:
        pass

    def __init__(self, pool: ObjectPool[typing.Any]) -> None:
        pass

    # Class Methods End


class SynchronizedPooledObjectFactory:

    # Class Fields Begin
    __writeLock: typing.Union[threading.RLock, threading.Lock] = None
    __factory: PooledObjectFactory[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, p: PooledObject[typing.Any]) -> bool:
        pass

    def toString(self) -> str:
        pass

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def makeObject(self) -> PooledObject[typing.Any]:
        pass

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def __init__(self, factory: PooledObjectFactory[typing.Any]) -> None:
        pass

    # Class Methods End


class TimerHolder:

    # Class Fields Begin
    MIN_IDLE_TIMER: Timer = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class PoolUtils:

    # Class Fields Begin
    __MSG_FACTOR_NEGATIVE: str = None
    __MSG_MIN_IDLE: str = None
    MSG_NULL_KEY: str = None
    __MSG_NULL_KEYED_POOL: str = None
    MSG_NULL_KEYS: str = None
    __MSG_NULL_POOL: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def prefill2(pool: ObjectPool[typing.Any], count: int) -> None:
        pass

    @staticmethod
    def prefill1(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any], key: typing.Any, count: int
    ) -> None:
        pass

    @staticmethod
    def prefill0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        keys: typing.Collection[typing.Any],
        count: int,
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def synchronizedPooledFactory(
        factory: PooledObjectFactory[typing.Any],
    ) -> PooledObjectFactory[typing.Any]:
        pass

    @staticmethod
    def synchronizedPool1(pool: ObjectPool[typing.Any]) -> ObjectPool[typing.Any]:
        pass

    @staticmethod
    def synchronizedPool0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any]
    ) -> KeyedObjectPool[typing.Any, typing.Any]:
        pass

    @staticmethod
    def synchronizedKeyedPooledFactory(
        keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedPooledObjectFactory[typing.Any, typing.Any]:
        pass

    @staticmethod
    def erodingPool4(
        pool: ObjectPool[typing.Any], factor: float
    ) -> ObjectPool[typing.Any]:
        pass

    @staticmethod
    def erodingPool3(pool: ObjectPool[typing.Any]) -> ObjectPool[typing.Any]:
        pass

    @staticmethod
    def erodingPool2(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any], factor: float, perKey: bool
    ) -> KeyedObjectPool[typing.Any, typing.Any]:
        pass

    @staticmethod
    def erodingPool1(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any], factor: float
    ) -> KeyedObjectPool[typing.Any, typing.Any]:
        pass

    @staticmethod
    def erodingPool0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any]
    ) -> KeyedObjectPool[typing.Any, typing.Any]:
        pass

    @staticmethod
    def checkRethrow(t: BaseException) -> None:
        pass

    @staticmethod
    def checkMinIdle2(
        pool: ObjectPool[typing.Any], minIdle: int, periodMillis: int
    ) -> typing.Union[sched.scheduler, threading.Timer]:
        pass

    @staticmethod
    def checkMinIdle1(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        key: typing.Any,
        minIdle: int,
        periodMillis: int,
    ) -> typing.Union[sched.scheduler, threading.Timer]:
        pass

    @staticmethod
    def checkMinIdle0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        keys: typing.Collection[typing.Any],
        minIdle: int,
        periodMillis: int,
    ) -> typing.Dict[typing.Any, typing.Union[sched.scheduler, threading.Timer]]:
        pass

    @staticmethod
    def __getMinIdleTimer() -> Timer:
        pass

    # Class Methods End
