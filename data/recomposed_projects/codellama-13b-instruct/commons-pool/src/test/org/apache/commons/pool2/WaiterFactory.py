# Imports Begin
from src.main.org.apache.commons.pool2.Waiter import *
from src.main.org.apache.commons.pool2.PooledObject import *
import unittest
import typing
from typing import *

# Imports End


class WaiterFactory(unittest.TestCase):

    # Class Fields Begin
    __activateLatency: int = None
    __destroyLatency: int = None
    __makeLatency: int = None
    __passivateLatency: int = None
    __validateLatency: int = None
    __waiterLatency: int = None
    __passivateInvalidationProbability: float = None
    __activeCount: int = None
    __activeCounts: typing.Dict[typing.Any, int] = ""  # LLM could not translate field
    __maxActive: int = None
    __maxActivePerKey: int = None
    # Class Fields End

    # Class Methods Begin
    def validateObject1(self, obj: PooledObject[Waiter]) -> bool:

        self._doWait(self.__validateLatency)
        return obj.getObject().isValid()

    def validateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> bool:

        return self.validateObject1(obj)

    def reset(self) -> None:

        pass  # LLM could not translate method body

    def passivateObject1(self, obj: PooledObject[Waiter]) -> None:

        pass  # LLM could not translate method body

    def passivateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:

        pass  # LLM could not translate method body

    def getMaxActive(self) -> int:

        return self.__maxActive

    def _doWait(self, latency: int) -> None:

        if latency == 0:
            return
        self.sleepQuietly(latency)

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
            self.__activeCounts.put(key, int(count) - 1)

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

        pass  # LLM could not translate method body

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

        pass  # LLM could not translate method body

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

        pass  # LLM could not translate method body

    # Class Methods End
