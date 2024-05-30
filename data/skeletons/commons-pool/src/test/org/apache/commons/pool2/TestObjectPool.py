from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.test.org.apache.commons.pool2.MethodCall import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class TestObjectPool(ABC):

    # Class Fields Begin
    __ZERO: int = None
    __ONE: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def removeDestroyObjectCall(calls: typing.List[MethodCall]) -> None:
        pass

    @staticmethod
    def __reset(
        pool: ObjectPool[object],
        factory: MethodCallPoolableObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pass

    @staticmethod
    def __clear(
        factory: MethodCallPoolableObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pass

    def _makeEmptyPool(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        pass

    # Class Methods End
