# Imports Begin
from src.main.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.MethodCall import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
import unittest
import os
import typing
from typing import *
from abc import ABC

# Imports End


class TestKeyedObjectPool(unittest.TestCase, ABC):

    # Class Fields Begin
    _KEY: str = ""  # LLM could not translate field
    __pool: KeyedObjectPool[object, typing.Any] = None
    __ZERO: int = 0
    __ONE: int = 1
    # Class Fields End

    # Class Methods Begin
    def testBaseNumActiveNumIdle2(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(6)
        except UnsupportedOperationException:
            return
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
        except UnsupportedOperationException:
            return
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
        except UnsupportedOperationException:
            return
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
        except UnsupportedOperationException:
            return
        keya = self._makeKey(0)
        assert self.__pool.getNumActive1(keya) == 0
        assert self.__pool.getNumIdle1(keya) == 0
        obj0 = self.__pool.borrowObject(keya)
        obj1 = self.__pool.borrowObject(keya)
        assert self.__pool.getNumActive1(keya) == 2
        assert self.__pool.getNumIdle1(keya) == 0
        self.__pool.returnObject(keya, obj1)
        self.__pool.returnObject(keya, obj0)
        assert self.__pool.getNumActive1(keya) == 0
        assert self.__pool.getNumIdle1(keya) == 2
        self.__pool.clear1(keya)
        assert self.__pool.getNumActive1(keya) == 0
        assert self.__pool.getNumIdle1(keya) == 0
        obj2 = self.__pool.borrowObject(keya)
        assert self._getNthObject(keya, 2) == obj2
        self.__pool.close()

    def testBaseBorrowReturn(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except UnsupportedOperationException:
            return
        keya = self._makeKey(0)
        obj0 = self.__pool.borrowObject(keya)
        assert self._getNthObject(keya, 0) == obj0
        obj1 = self.__pool.borrowObject(keya)
        assert self._getNthObject(keya, 1) == obj1
        obj2 = self.__pool.borrowObject(keya)
        assert self._getNthObject(keya, 2) == obj2
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        assert self._getNthObject(keya, 2) == obj2
        self.__pool.returnObject(keya, obj1)
        obj1 = self.__pool.borrowObject(keya)
        assert self._getNthObject(keya, 1) == obj1
        self.__pool.returnObject(keya, obj0)
        self.__pool.returnObject(keya, obj2)
        obj2 = self.__pool.borrowObject(keya)
        if self._isLifo():
            assert self._getNthObject(keya, 2) == obj2
        if self._isFifo():
            assert self._getNthObject(keya, 0) == obj2
        obj0 = self.__pool.borrowObject(keya)
        if self._isLifo():
            assert self._getNthObject(keya, 0) == obj0
        if self._isFifo():
            assert self._getNthObject(keya, 2) == obj0
        self.__pool.close()

    def testBaseBorrow(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except UnsupportedOperationException as uoe:
            return  # skip this test if unsupported
        keya = self._makeKey(0)
        keyb = self._makeKey(1)
        self.assertEqual(
            self._getNthObject(keya, 0), self.__pool.borrowObject(keya), "1"
        )
        self.assertEqual(
            self._getNthObject(keyb, 0), self.__pool.borrowObject(keyb), "2"
        )
        self.assertEqual(
            self._getNthObject(keyb, 1), self.__pool.borrowObject(keyb), "3"
        )
        self.assertEqual(
            self._getNthObject(keya, 1), self.__pool.borrowObject(keya), "4"
        )
        self.assertEqual(
            self._getNthObject(keyb, 2), self.__pool.borrowObject(keyb), "5"
        )
        self.assertEqual(
            self._getNthObject(keya, 2), self.__pool.borrowObject(keya), "6"
        )
        self.__pool.close()

    def testBaseAddObject(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except UnsupportedOperationException:
            return None
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
        except UnsupportedOperationException:
            return None
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

        pass  # LLM could not translate method body

    def _makeKey(self, n: int) -> typing.Any:

        return n

    def _makeEmptyPool1(
        self, factory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedObjectPool[object, typing.Any]:

        return {}

    def _makeEmptyPool0(self, minCapacity: int) -> KeyedObjectPool[object, typing.Any]:

        return {}

    def _isLifo(self) -> bool:

        pass  # LLM could not translate method body

    def _isFifo(self) -> bool:

        pass  # LLM could not translate method body

    def _getNthObject(self, key: typing.Any, n: int) -> typing.Any:

        return self._getNthObject(key, n)

    # Class Methods End


class FailingKeyedPooledObjectFactory(unittest.TestCase):

    # Class Fields Begin
    __methodCalls: List[MethodCall] = []
    __count: int = None
    __makeObjectFail: bool = None
    __activateObjectFail: bool = None
    __validateObjectFail: bool = None
    __passivateObjectFail: bool = None
    __destroyObjectFail: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> bool:

        call = MethodCall.MethodCall0("validateObject", key, obj.getObject())
        self.__methodCalls.add(call)
        if self.__validateObjectFail:
            raise PrivateException("validateObject")
        r = True
        call.returned(Boolean.valueOf(r))
        return r

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:

        self.validateObjectFail = validateObjectFail

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:

        pass  # LLM could not translate method body

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

        pass  # LLM could not translate method body

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

        self.__methodCalls.add(self.MethodCall0("destroyObject", key, obj.getObject()))
        if self.__destroyObjectFail:
            raise PrivateException("destroyObject")

    def activateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:

        self.__methodCalls.append(
            self.MethodCall0("activateObject", key, obj.getObject())
        )
        if self.__activateObjectFail:
            raise PrivateException("activateObject")

    def __init__(self) -> None:

        pass

    # Class Methods End
