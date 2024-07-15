import pytest

import random
import threading
import typing
import sys
from src.test.org.apache.commons.pool2.Waiter import *
from src.main.org.apache.commons.pool2.PooledObject import *

K = typing.TypeVar('K')

class WaiterFactory(typing.Generic[K]):

    def __init__(self, 
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        passivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
        maxActive: int,
        maxActivePerKey: int,
        passivateInvalidationProbability: float) -> None:

        self.__activateLatency = activateLatency
        self.__destroyLatency = destroyLatency
        self.__makeLatency = makeLatency
        self.__passivateLatency = passivateLatency
        self.__validateLatency = validateLatency
        self.__waiterLatency = waiterLatency
        self.__maxActive = maxActive
        self.__maxActivePerKey = maxActivePerKey
        self.__passivateInvalidationProbability = passivateInvalidationProbability
        self.__activeCount = 0
        self.__activeCounts = {}

    
    @classmethod
    def WaiterFactory1( 
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        passivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
        maxActive: int) -> 'WaiterFactory':

        return WaiterFactory(
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency,
            maxActive,
            sys.maxsize,
            0.0
        )

    
    @classmethod
    def WaiterFactory2(
            activateLatency: int,
            destroyLatency: int,
            makeLatency: int,
            passivateLatency: int,
            validateLatency: int,
            waiterLatency: int) -> 'WaiterFactory':
        return WaiterFactory(
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency,
            sys.maxsize,
            sys.maxsize,
            0.0
        )

    
    def activateObject0(self, key: K, obj: PooledObject) -> None:
        try:
            self.activateObject1(obj)
        except Exception as e:
            raise e

    
    def activateObject1(self, obj: PooledObject) -> None:
        try:
            self._doWait(self.__activateLatency)
            obj.getObject().setActive(True)
        except Exception as e:
            raise e

    
    def destroyObject0(self, key: K, obj: PooledObject) -> None:
        try:
            self.destroyObject1(obj)
            with threading.Lock():
                self.__activeCounts[key] -= 1
        except Exception as e:
            raise e

    
    def destroyObject1(self, obj: PooledObject) -> None:
        try:
            self._doWait(self.__destroyLatency)
            obj.getObject().setValid(False)
            obj.getObject().setActive(False)
            with threading.Lock():
                self.__activeCount -= 1
        except Exception as e:
            raise e

    
    def _doWait(self, latency: int) -> None:
        if latency == 0:
            return
        Waiter.sleepQuietly(latency)

    
    def getMaxActive(self) -> int:
        with threading.Lock():
            return self.__maxActive

    
    def passivateObject0(self, key: K, obj: PooledObject) -> None:
        try:
            self.passivateObject1(obj)
        except Exception as e:
            raise e

    
    def passivateObject1(self, obj: PooledObject) -> None:
        try:
            obj.getObject().setActive(False)
            self._doWait(self.__passivateLatency)
            if random.random() < self.__passivateInvalidationProbability:
                obj.getObject().setValid(False)
        except Exception as e:
            raise e

    
    def reset(self) -> None:
        with threading.Lock():
            self.__activeCount = 0
            if not self.__activeCounts:
                return
            for key in self.__activeCounts:
                self.__activeCounts[key] = 0

    
    def validateObject0(self, key: K, obj: PooledObject) -> bool:
        return self.validateObject1(obj)

    
    def validateObject1(self, obj: PooledObject) -> bool:
        self._doWait(self.__validateLatency)
        return obj.getObject().isValid()
