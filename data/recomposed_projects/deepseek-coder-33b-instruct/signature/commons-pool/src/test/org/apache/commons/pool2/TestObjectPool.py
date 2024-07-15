from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
from src.test.org.apache.commons.pool2.MethodCall import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *


class TestObjectPool(ABC):

    __ONE: int = 1
    __ZERO: int = 0

    @staticmethod
    def removeDestroyObjectCall(calls: typing.List[MethodCall]) -> None:
        calls[:] = [call for call in calls if call.getName() != "destroyObject"]

    @staticmethod
    def __reset(
        pool: ObjectPool[object],
        factory: MethodCallPoolableObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:

        pool.clear()
        TestObjectPool.__clear(factory, expectedMethods)
        factory.reset()

    @staticmethod
    def __clear(
        factory: MethodCallPoolableObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        factory.getMethodCalls().clear()
        expectedMethods.clear()

    def _makeEmptyPool(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        raise NotImplementedError("This method is not supported in Python.")
