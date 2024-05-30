from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.BaseObjectPool import *
from src.test.org.apache.commons.pool2.TestObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.test.org.apache.commons.pool2.MethodCall import *
import os
import typing
from typing import *
import io

# Imports End


class TestObjectPool(BaseObjectPool):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    # Class Methods End


class TestBaseObjectPool(TestObjectPool):

    # Class Fields Begin
    __pool: ObjectPool[str] = None
    # Class Fields End

    # Class Methods Begin
    def testUnsupportedOperations(self) -> None:
        pass

    def testClose(self) -> None:
        pass

    def testBaseNumActiveNumIdle(self) -> None:
        pass

    def testBaseInvalidateObject(self) -> None:
        pass

    def testBaseClosePool(self) -> None:
        pass

    def testBaseClear(self) -> None:
        pass

    def testBaseBorrowReturn(self) -> None:
        pass

    def testBaseBorrow(self) -> None:
        pass

    def testBaseAddObject(self) -> None:
        pass

    def _makeEmptyPool(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        pass

    def _makeEmptyPool1(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        pass

    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:
        pass

    def _isLifo(self) -> bool:
        pass

    def _isFifo(self) -> bool:
        pass

    def _getNthObject(self, n: int) -> typing.Any:
        pass

    # Class Methods End
