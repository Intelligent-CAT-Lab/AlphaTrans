from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.VisitTracker import *


class VisitTrackerFactory:

    __nextId: int = None

    def validateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> bool:

        return ref.getObject().validate()

    def validateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> bool:

        return ref.getObject().validate()

    def resetId(self) -> None:

        self.__nextId = 0

    def ivateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:

        ref.getObject().passivate()

    def ivateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:

        ref.getObject().passivate()

    def destroyObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:

        ref.getObject().destroy()

    def destroyObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:

        ref.getObject().destroy()

    def activateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:

        try:
            ref.getObject().activate()
        except Exception as e:
            raise e

    def activateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:

        ref.getObject().activate()

    def __init__(self) -> None:

        pass
