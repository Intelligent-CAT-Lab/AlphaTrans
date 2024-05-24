from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.MethodCall import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class FailingKeyedPooledObjectFactory:

    # Class Fields Begin
    __methodCalls: typing.List[MethodCall] = None
    __count: int = None
    __makeObjectFail: bool = None
    __activateObjectFail: bool = None
    __validateObjectFail: bool = None
    __passivateObjectFail: bool = None
    __destroyObjectFail: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> bool:
        pass

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        pass

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        pass

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        pass

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        pass

    def setCurrentCount(self, count: int) -> None:
        pass

    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        pass

    def reset(self) -> None:
        pass

    def passivateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        pass

    def isValidateObjectFail(self) -> bool:
        pass

    def isPassivateObjectFail(self) -> bool:
        pass

    def isMakeObjectFail(self) -> bool:
        pass

    def isDestroyObjectFail(self) -> bool:
        pass

    def isActivateObjectFail(self) -> bool:
        pass

    def getMethodCalls(self) -> typing.List[MethodCall]:
        pass

    def getCurrentCount(self) -> int:
        pass

    def destroyObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class TestKeyedObjectPool(ABC):

    # Class Fields Begin
    _KEY: str = None
    __pool: KeyedObjectPool[object, typing.Any] = None
    __ZERO: int = None
    __ONE: int = None
    # Class Fields End

    # Class Methods Begin
    def testBaseNumActiveNumIdle2(self) -> None:
        pass

    def testBaseNumActiveNumIdle(self) -> None:
        pass

    def testBaseInvalidateObject(self) -> None:
        pass

    def testBaseClear(self) -> None:
        pass

    def testBaseBorrowReturn(self) -> None:
        pass

    def testBaseBorrow(self) -> None:
        pass

    def testBaseAddObject(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def __reset(
        self,
        pool: KeyedObjectPool[object, typing.Any],
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pass

    def __clear(
        self,
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pass

    def _makeKey(self, n: int) -> typing.Any:
        pass

    def _makeEmptyPool1(
        self, factory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedObjectPool[object, typing.Any]:
        pass

    def _makeEmptyPool0(self, minCapacity: int) -> KeyedObjectPool[object, typing.Any]:
        pass

    def _isLifo(self) -> bool:
        pass

    def _isFifo(self) -> bool:
        pass

    def _getNthObject(self, key: typing.Any, n: int) -> typing.Any:
        pass

    # Class Methods End
