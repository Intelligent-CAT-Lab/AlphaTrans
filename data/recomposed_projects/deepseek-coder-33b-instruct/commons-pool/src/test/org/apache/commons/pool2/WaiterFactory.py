from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.Waiter import *


class WaiterFactory:

    __maxActivePerKey: int = None
    __maxActive: int = None

    __activeCounts: Dict[Any, int] = {}
    __activeCount: int = None
    __passivateInvalidationProbability: float = None
    __waiterLatency: int = None
    __validateLatency: int = None
    __passivateLatency: int = None
    __makeLatency: int = None
    __destroyLatency: int = None
    __activateLatency: int = None

    def validateObject1(self, obj: PooledObject[Waiter]) -> bool:

        self._doWait(self.__validateLatency)
        return obj.getObject().isValid()

    def validateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> bool:

        return self.validateObject1(obj)

    def reset(self) -> None:

        self.__activeCount = 0
        if not self.__activeCounts:
            return
        it = iter(self.__activeCounts.keys())
        while True:
            try:
                key = next(it)
            except StopIteration:
                break
            self.__activeCounts[key] = 0

    def ivateObject1(self, obj: PooledObject[Waiter]) -> None:

        obj.getObject().setActive(False)
        self._doWait(self.__passivateLatency)
        if random.random() < self.__passivateInvalidationProbability:
            obj.getObject().setValid(False)

    def ivateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:

        self.passivateObject1(obj)

    def getMaxActive(self) -> int:

        return self.__maxActive

    def _doWait(self, latency: int) -> None:

        if latency == 0:
            return

        Waiter.sleepQuietly(latency)

    def destroyObject1(self, obj: PooledObject[Waiter]) -> None:

        self._doWait(self.__destroyLatency)
        obj.getObject().setValid(False)
        obj.getObject().setActive(False)
        with self:
            self.__activeCount -= 1

    def destroyObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:

        self.destroyObject1(obj)

        with self:
            count = self.__activeCounts.get(key)
            self.__activeCounts[key] = count - 1

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
        ivateLatency: int,
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
            Long.MAX_VALUE,
            Long.MAX_VALUE,
            0,
        )

    @staticmethod
    def WaiterFactory1(
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        ivateLatency: int,
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
            Long.MAX_VALUE,
            0,
        )

    def __init__(
        self,
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        ivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
        maxActive: int,
        maxActivePerKey: int,
        ivateInvalidationProbability: float,
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
