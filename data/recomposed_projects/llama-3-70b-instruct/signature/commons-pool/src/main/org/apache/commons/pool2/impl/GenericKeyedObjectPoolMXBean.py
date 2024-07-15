from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.impl.DefaultPooledObjectInfo import *


class GenericKeyedObjectPoolMXBean(ABC):

    def listAllObjects(self) -> typing.Dict[str, typing.List[DefaultPooledObjectInfo]]:
        return self._pool.listAllObjects()

    def isClosed(self) -> bool:
        return self._pool.isClosed()

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        return self._pool.getTimeBetweenEvictionRunsMillis()

    def getTestWhileIdle(self) -> bool:
        return self._pool.getTestWhileIdle()

    def getTestOnReturn(self) -> bool:
        return self._pool.getTestOnReturn()

    def getTestOnCreate(self) -> bool:
        return self._pool.getTestOnCreate()

    def getTestOnBorrow(self) -> bool:
        return self._pool.getTestOnBorrow()

    def getReturnedCount(self) -> int:
        return self.getPool().getReturnedCount()

    def getNumWaitersByKey(self) -> typing.Dict[str, int]:
        return self.pool.getNumWaitersByKey()

    def getNumWaiters(self) -> int:
        return self.pool.getNumWaiters()

    def getNumTestsPerEvictionRun(self) -> int:
        return self.pool.getNumTestsPerEvictionRun()

    def getNumIdle(self) -> int:
        return self.pool.getNumIdle()

    def getNumActivePerKey(self) -> typing.Dict[str, int]:
        return {k: v.getNumActive() for k, v in self.pools.items()}

    def getNumActive(self) -> int:
        return self.pool.getNumActive()

    def getMinIdlePerKey(self) -> int:
        return self.pool.getMinIdlePerKey()

    def getMinEvictableIdleTimeMillis(self) -> int:
        return self._pool.getMinEvictableIdleTimeMillis()

    def getMeanIdleTimeMillis(self) -> int:
        return self._pool.getMeanIdleTimeMillis()

    def getMeanBorrowWaitTimeMillis(self) -> int:
        return self._pool.getMeanBorrowWaitTimeMillis()

    def getMeanActiveTimeMillis(self) -> int:
        return self._pool.getMeanActiveTimeMillis()

    def getMaxWaitMillis(self) -> int:
        return self._maxWaitMillis

    def getMaxTotalPerKey(self) -> int:
        return self.getMaxTotal()

    def getMaxTotal(self) -> int:
        return self.pool.getMaxTotal()

    def getMaxIdlePerKey(self) -> int:
        return self.pool.getMaxIdlePerKey()

    def getMaxBorrowWaitTimeMillis(self) -> int:
        return self._pool.getMaxBorrowWaitTimeMillis()

    def getLifo(self) -> bool:
        return self._lifo

    def getFairness(self) -> bool:
        return self._pool.getFairness()

    def getDestroyedCount(self) -> int:
        return self._pool.getDestroyedCount()

    def getDestroyedByEvictorCount(self) -> int:
        return self.pool.getDestroyedByEvictorCount()

    def getDestroyedByBorrowValidationCount(self) -> int:
        return self._pool.getDestroyedByBorrowValidationCount()

    def getCreationStackTrace(self) -> str:
        return self._pool.getCreationStackTrace()

    def getCreatedCount(self) -> int:
        return self.pool.getCreatedCount()

    def getBorrowedCount(self) -> int:
        return self._borrowedCount

    def getBlockWhenExhausted(self) -> bool:
        return self.getBlockWhenExhausted()

    def isAbandonedConfig(self) -> bool:
        return False

    def getRemoveAbandonedTimeout(self) -> int:
        return 0

    def getRemoveAbandonedOnMaintenance(self) -> bool:
        return False

    def getRemoveAbandonedOnBorrow(self) -> bool:
        return False

    def getLogAbandoned(self) -> bool:
        return False
