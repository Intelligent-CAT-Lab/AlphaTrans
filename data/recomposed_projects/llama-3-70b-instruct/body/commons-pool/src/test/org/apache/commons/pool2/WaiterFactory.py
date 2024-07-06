from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.Waiter import *


class WaiterFactory:

    __maxActivePerKey: int = 0

    __maxActive: int = 0

    __activeCounts: typing.Dict[typing.Any, int] = {}

    __activeCount: int = 0

    __passivateInvalidationProbability: float = 0.0

    __waiterLatency: int = 0

    __validateLatency: int = 0

    __passivateLatency: int = 0

    __makeLatency: int = 0

    __destroyLatency: int = 0

    __activateLatency: int = 0

    def validateObject1(self, obj: PooledObject[Waiter]) -> bool:
        self._doWait(self.__validateLatency)
        return obj.getObject().isValid()

    def validateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> bool:
        return self.validateObject1(obj)

    def reset(self) -> None:
        self.__activeCount = 0
        if not self.__activeCounts:
            return
        for key in self.__activeCounts:
            self.__activeCounts[key] = 0

    def passivateObject1(self, obj: PooledObject[Waiter]) -> None:
        obj.getObject().setActive(False)
        self._doWait(self.__passivateLatency)
        if Math.random() < self.__passivateInvalidationProbability:
            obj.getObject().setValid(False)

    def passivateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:
        self.passivateObject1(obj)

    def getMaxActive(self) -> int:
        return self.__maxActive

    def _doWait(self, latency: int) -> None:
        if latency == 0:
            return
        Waiter.sleepQuietly(latency)

    def destroyObject1(self, obj: PooledObject[Waiter]) -> None:

        pass  # LLM could not translate this method

    def destroyObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:
        self.destroyObject1(obj)
        with self:
            count = self.__activeCounts.get(key)
            self.__activeCounts.put(key, count - 1)

    def activateObject1(self, obj: PooledObject[Waiter]) -> None:
        self._doWait(self.__activateLatency)
        obj.getObject().setActive(True)

    def activateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:
        self.activateObject1(obj)

    @staticmethod
    def WaiterFactory2(
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        passivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
    ) -> WaiterFactory[typing.Any]:
        return WaiterFactory(
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency,
            9223372036854775807,
            9223372036854775807,
            0,
        )

    @staticmethod
    def WaiterFactory1(
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        passivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
        maxActive: int,
    ) -> WaiterFactory[typing.Any]:
        return WaiterFactory(
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency,
            maxActive,
            9223372036854775807,
            0,
        )

    def __init__(
        self,
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        passivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
        maxActive: int,
        maxActivePerKey: int,
        passivateInvalidationProbability: float,
    ) -> None:
        self.__activateLatency = activateLatency
        self.__destroyLatency = destroyLatency
        self.__makeLatency = makeLatency
        self.__passivateLatency = passivateLatency
        self.__validateLatency = validateLatency
        self.__waiterLatency = waiterLatency
        self.__maxActive = maxActive
        self.__maxActivePerKey = maxActivePerKey
        self.__passivateInvalidationProbability = passivateInvalidationProbability
