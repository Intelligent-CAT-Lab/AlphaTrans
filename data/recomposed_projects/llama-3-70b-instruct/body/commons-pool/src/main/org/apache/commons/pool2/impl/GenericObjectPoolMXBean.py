from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.impl.DefaultPooledObjectInfo import *


class GenericObjectPoolMXBean(ABC):

    def listAllObjects(self) -> typing.Set[DefaultPooledObjectInfo]:
        return self.pool.listAllObjects()

    def isClosed(self) -> bool:
        return self._pool.isClosed()

    def isAbandonedConfig(self) -> bool:
        return self._abandonedConfig

    def getTimeBetweenEvictionRunsMillis(self) -> int:
        return self._evictionConfig.getTimeBetweenEvictionRunsMillis()

    def getTestWhileIdle(self) -> bool:
        return self._pool.getTestWhileIdle()

    def getTestOnReturn(self) -> bool:
        return self._pool.getTestOnReturn()

    def getTestOnCreate(self) -> bool:
        return self.pool.getTestOnCreate()

    def getTestOnBorrow(self) -> bool:
        return self._pool.getTestOnBorrow()

    def getReturnedCount(self) -> int:
        return self.returnedCount

    def getRemoveAbandonedTimeout(self) -> int:
        return self._pool.getRemoveAbandonedTimeout()

    def getRemoveAbandonedOnMaintenance(self) -> bool:
        return self._pool.getRemoveAbandonedOnMaintenance()

    def getRemoveAbandonedOnBorrow(self) -> bool:
        return self._pool.getRemoveAbandonedOnBorrow()

    def getNumWaiters(self) -> int:
        return self._pool.getNumWaiters()

    def getNumTestsPerEvictionRun(self) -> int:
        return self._pool.getNumTestsPerEvictionRun()

    def getNumIdle(self) -> int:
        return self.pool.getNumIdle()

    def getNumActive(self) -> int:
        return self.pool.getNumActive()

    def getMinIdle(self) -> int:
        return self.pool.getMinIdle()

    def getMinEvictableIdleTimeMillis(self) -> int:
        return self._evictor.getMinEvictableIdleTimeMillis()

    def getMeanIdleTimeMillis(self) -> int:
        return self._pool.getMeanIdleTimeMillis()

    def getMeanBorrowWaitTimeMillis(self) -> int:
        return self._borrowedCount.getMean()

    def getMeanActiveTimeMillis(self) -> int:
        return self._pool.getMeanActiveTimeMillis()

    def getMaxWaitMillis(self) -> int:
        return self._maxWaitMillis

    def getMaxTotal(self) -> int:
        return self._maxTotal

    def getMaxIdle(self) -> int:
        return self._maxIdle

    def getMaxBorrowWaitTimeMillis(self) -> int:
        return self._maxBorrowWaitTimeMillis

    def getLogAbandoned(self) -> bool:
        return self._pool.getLogAbandoned()

    def getLifo(self) -> bool:
        return self._lifo

    def getFairness(self) -> bool:
        return self.pool.getFairness()

    def getFactoryType(self) -> str:
        return self.factory.getFactoryType()

    def getDestroyedCount(self) -> int:
        return self._pool.getDestroyedCount()

    def getDestroyedByEvictorCount(self) -> int:
        return self.pool.getDestroyedByEvictorCount()

    def getDestroyedByBorrowValidationCount(self) -> int:
        return self.pool.getDestroyedByBorrowValidationCount()

    def getCreationStackTrace(self) -> str:
        return self._pool.getCreationStackTrace()

    def getCreatedCount(self) -> int:
        return self._pool.getCreatedCount()

    def getBorrowedCount(self) -> int:
        return self._borrowedCount

    def getBlockWhenExhausted(self) -> bool:
        return self._pool.getBlockWhenExhausted()
