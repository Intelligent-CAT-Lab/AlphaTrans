from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.pool2.Waiter import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from typing import *
import io

# Imports End


class WaiterFactory:

    # Class Fields Begin
    __activateLatency: int = None
    __destroyLatency: int = None
    __makeLatency: int = None
    __passivateLatency: int = None
    __validateLatency: int = None
    __waiterLatency: int = None
    __passivateInvalidationProbability: float = None
    __activeCount: int = None
    __activeCounts: typing.Dict[typing.Any, int] = None
    __maxActive: int = None
    __maxActivePerKey: int = None
    # Class Fields End

    # Class Methods Begin
    def validateObject1(self, obj: PooledObject[Waiter]) -> bool:
        pass

    def validateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> bool:
        pass

    def reset(self) -> None:
        pass

    def passivateObject1(self, obj: PooledObject[Waiter]) -> None:
        pass

    def passivateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:
        pass

    def getMaxActive(self) -> int:
        pass

    def _doWait(self, latency: int) -> None:
        pass

    def destroyObject1(self, obj: PooledObject[Waiter]) -> None:
        pass

    def destroyObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:
        pass

    def activateObject1(self, obj: PooledObject[Waiter]) -> None:
        pass

    def activateObject0(self, key: typing.Any, obj: PooledObject[Waiter]) -> None:
        pass

    @staticmethod
    def WaiterFactory2(
        activateLatency: int,
        destroyLatency: int,
        makeLatency: int,
        passivateLatency: int,
        validateLatency: int,
        waiterLatency: int,
    ) -> WaiterFactory[typing.Any]:
        pass

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
        pass

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
        pass

    # Class Methods End
