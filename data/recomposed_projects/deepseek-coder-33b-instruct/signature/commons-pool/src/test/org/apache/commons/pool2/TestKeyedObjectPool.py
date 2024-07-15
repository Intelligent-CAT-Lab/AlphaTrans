from __future__ import annotations
import re
import os
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.test.org.apache.commons.pool2.MethodCall import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.PrivateException import *


class FailingKeyedPooledObjectFactory:

    __destroyObjectFail: bool = False

    __passivateObjectFail: bool = False

    __validateObjectFail: bool = False

    __activateObjectFail: bool = False

    __makeObjectFail: bool = False

    __count: int = 0

    __methodCalls: typing.List[MethodCall] = []

    def validateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> bool:

        call = MethodCall.MethodCall0("validateObject", key, obj.getObject())
        self.__methodCalls.append(call)

        if self.__validateObjectFail:
            raise PrivateException("validateObject")

        r = True
        call.returned(bool(r))

        return r

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        self.__validateObjectFail = validateObjectFail

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        self.__passivateObjectFail = passivateObjectFail

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        self.__makeObjectFail = makeObjectFail

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        self.__destroyObjectFail = destroyObjectFail

    def setCurrentCount(self, count: int) -> None:
        self.__count = count

    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        self.__activateObjectFail = activateObjectFail

    def reset(self) -> None:
        self.__count = 0
        self.getMethodCalls().clear()
        self.setMakeObjectFail(False)
        self.setActivateObjectFail(False)
        self.setValidateObjectFail(False)
        self.setPassivateObjectFail(False)
        self.setDestroyObjectFail(False)

    def passivateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:

        self.__methodCalls.append(
            MethodCall.MethodCall0("passivateObject", key, obj.getObject())
        )

        if self.__passivateObjectFail:
            raise PrivateException("passivateObject")

    def isValidateObjectFail(self) -> bool:
        return self.__validateObjectFail

    def isPassivateObjectFail(self) -> bool:
        return self.__passivateObjectFail

    def isMakeObjectFail(self) -> bool:
        return self.__makeObjectFail

    def isDestroyObjectFail(self) -> bool:
        return self.__destroyObjectFail

    def isActivateObjectFail(self) -> bool:
        return self.__activateObjectFail

    def getMethodCalls(self) -> typing.List[MethodCall]:
        return self.__methodCalls

    def getCurrentCount(self) -> int:
        return self.__count

    def destroyObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        self.__methodCalls.append(
            MethodCall.MethodCall0("destroyObject", key, obj.getObject())
        )
        if self.__destroyObjectFail:
            raise PrivateException("destroyObject")

    def activateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        self.__methodCalls.append(
            MethodCall.MethodCall0("activateObject", key, obj.getObject())
        )
        if self.__activateObjectFail:
            raise PrivateException("activateObject")

    def __init__(self) -> None:
        pass


class TestKeyedObjectPool(ABC, unittest.TestCase):

    _KEY: str = "key"
    __ONE: int = 1
    __ZERO: int = 0
    __pool: KeyedObjectPool[object, typing.Any] = None

    def testBaseNumActiveNumIdle2(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(6)
        except NotImplementedError as uoe:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA0 = self.__pool.borrowObject(keya)
        objB0 = self.__pool.borrowObject(keyb)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        objA1 = self.__pool.borrowObject(keya)
        objB1 = self.__pool.borrowObject(keyb)

        self.assertEqual(4, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.assertEqual(2, self.__pool.getNumActive1(keyb))
        self.assertEqual(0, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA0)
        self.__pool.returnObject(keyb, objB0)

        self.assertEqual(2, self.__pool.getNumActive0())
        self.assertEqual(2, self.__pool.getNumIdle0())
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))
        self.assertEqual(1, self.__pool.getNumActive1(keyb))
        self.assertEqual(1, self.__pool.getNumIdle1(keyb))

        self.__pool.returnObject(keya, objA1)
        self.__pool.returnObject(keyb, objB1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(4, self.__pool.getNumIdle0())
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))
        self.assertEqual(0, self.__pool.getNumActive1(keyb))
        self.assertEqual(2, self.__pool.getNumIdle1(keyb))

        self.__pool.close()

    def testBaseNumActiveNumIdle(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError as uoe:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj1)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(1, self.__pool.getNumIdle1(keya))

        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))

        self.assertEqual(0, self.__pool.getNumActive1("xyzzy12345"))
        self.assertEqual(0, self.__pool.getNumIdle1("xyzzy12345"))

        self.__pool.close()

    def testBaseInvalidateObject(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)

        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj0)
        self.assertEqual(1, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.invalidateObject0(keya, obj1)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))

        self.__pool.close()

    def testBaseClear(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError as uoe:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(2, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(2, self.__pool.getNumIdle1(keya))
        self.__pool.clear1(keya)
        self.assertEqual(0, self.__pool.getNumActive1(keya))
        self.assertEqual(0, self.__pool.getNumIdle1(keya))
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)
        self.__pool.close()

    def testBaseBorrowReturn(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError as uoe:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 0), obj0)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 2), obj2)
        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        self.assertEqual(self._getNthObject(keya, 1), obj1)
        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 0), obj2)
        obj0 = self.__pool.borrowObject(keya)
        if self._isLifo():
            self.assertEqual(self._getNthObject(keya, 0), obj0)
        if self._isFifo():
            self.assertEqual(self._getNthObject(keya, 2), obj0)
        self.__pool.close()

    def testBaseBorrow(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError as uoe:
            return  # skip this test if unsupported

        keya = self._makeKey(0)
        keyb = self._makeKey(1)

        assert self._getNthObject(keya, 0) == self.__pool.borrowObject(keya), "1"
        assert self._getNthObject(keyb, 0) == self.__pool.borrowObject(keyb), "2"
        assert self._getNthObject(keyb, 1) == self.__pool.borrowObject(keyb), "3"
        assert self._getNthObject(keya, 1) == self.__pool.borrowObject(keya), "4"
        assert self._getNthObject(keyb, 2) == self.__pool.borrowObject(keyb), "5"
        assert self._getNthObject(keya, 2) == self.__pool.borrowObject(keya), "6"

        self.__pool.close()

    def testBaseAddObject(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        key = self._makeKey(0)

        try:
            self.assertEqual(0, self.__pool.getNumIdle0())
            self.assertEqual(0, self.__pool.getNumActive0())
            self.assertEqual(0, self.__pool.getNumIdle1(key))
            self.assertEqual(0, self.__pool.getNumActive1(key))
            self.__pool.addObject(key)
            self.assertEqual(1, self.__pool.getNumIdle0())
            self.assertEqual(0, self.__pool.getNumActive0())
            self.assertEqual(1, self.__pool.getNumIdle1(key))
            self.assertEqual(0, self.__pool.getNumActive1(key))
            obj = self.__pool.borrowObject(key)
            self.assertEqual(self._getNthObject(key, 0), obj)
            self.assertEqual(0, self.__pool.getNumIdle0())
            self.assertEqual(1, self.__pool.getNumActive0())
            self.assertEqual(0, self.__pool.getNumIdle1(key))
            self.assertEqual(1, self.__pool.getNumActive1(key))
            self.__pool.returnObject(key, obj)
            self.assertEqual(1, self.__pool.getNumIdle0())
            self.assertEqual(0, self.__pool.getNumActive0())
            self.assertEqual(1, self.__pool.getNumIdle1(key))
            self.assertEqual(0, self.__pool.getNumActive1(key))
        except NotImplementedError:
            return  # skip this test if one of those calls is unsupported
        finally:
            self.__pool.close()

    def tearDown(self) -> None:
        self.__pool = None

    def __reset(
        self,
        pool: KeyedObjectPool[object, typing.Any],
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:

        pool.clear0()
        self.__clear(factory, expectedMethods)
        factory.reset()

    def __clear(
        self,
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        factory.getMethodCalls().clear()
        expectedMethods.clear()

    def _makeKey(self, n: int) -> typing.Any:
        pass

    def _makeEmptyPool1(
        self, factory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedObjectPool[object, typing.Any]:

        # Your implementation here
        pass

    def _makeEmptyPool0(self, minCapacity: int) -> KeyedObjectPool[object, typing.Any]:

        # Here you can implement the logic for creating an empty pool.
        # Since the Java method is abstract, you need to provide the implementation.
        # For now, I'll just return None.

        return None

    def _isLifo(self) -> bool:
        pass

    def _isFifo(self) -> bool:
        pass

    def _getNthObject(self, key: typing.Any, n: int) -> typing.Any:
        pass
