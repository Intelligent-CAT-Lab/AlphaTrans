# Imports Begin
from src.main.org.apache.commons.pool2.VisitTracker import *
from src.main.org.apache.commons.pool2.PooledObject import *
import unittest
import typing
from typing import *

# Imports End


class VisitTrackerFactory(unittest.TestCase):

    # Class Fields Begin
    __nextId: int = None
    # Class Fields End

    # Class Methods Begin
    def validateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> bool:

        return ref.getObject().validate()

    def validateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> bool:

        return ref.getObject().validate()

    def resetId(self) -> None:

        self.__nextId = 0

    def passivateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:

        pass  # LLM could not translate method body

    def passivateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:

        pass  # LLM could not translate method body

    def destroyObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:

        ref.getObject().destroy()

    def destroyObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:

        ref.getObject().destroy()

    def activateObject1(self, ref: PooledObject[VisitTracker[typing.Any]]) -> None:

        ref.getObject().activate()

    def activateObject0(
        self, key: typing.Any, ref: PooledObject[VisitTracker[typing.Any]]
    ) -> None:

        ref.getObject().activate()

    def __init__(self) -> None:

        pass

    # Class Methods End
