from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.pool2.VisitTracker import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from typing import *
import io

# Imports End


class VisitTrackerFactory:

    # Class Fields Begin
    __nextId: int = None
    # Class Fields End

    # Class Methods Begin
    def validateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> bool:
        pass

    def validateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> bool:
        pass

    def resetId(self) -> None:
        pass

    def passivateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:
        pass

    def passivateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:
        pass

    def destroyObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:
        pass

    def destroyObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:
        pass

    def activateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:
        pass

    def activateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
