from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.pool2.MethodCall import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.test.org.apache.commons.pool2.TestObjectPool import *
from src.main.org.apache.commons.pool2.BaseObjectPool import *


class TestObjectPool(BaseObjectPool):

    def returnObject(self, obj: typing.Any) -> None:

        # Your code here
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:

        # Your code here
        pass

    def borrowObject(self) -> typing.Any:
        return None


class TestBaseObjectPool(TestObjectPool, unittest.TestCase):

    __pool: ObjectPool[str] = None

    def testUnsupportedOperations(self) -> None:

        if not isinstance(self, TestBaseObjectPool):
            return  # skip redundant tests

        try:
            pool = TestObjectPool()

            self.assertTrue(pool.getNumIdle() < 0, "Negative expected.")
            self.assertTrue(pool.getNumActive() < 0, "Negative expected.")

            with self.assertRaises(NotImplementedError):
                pool.clear()
            with self.assertRaises(NotImplementedError):
                pool.addObject()

        finally:
            pool.close()

    def testClose(self) -> None:

        # Create an instance of TestObjectPool
        pool = TestObjectPool()

        # Call the close method
        pool.close()

        # Call the close method again
        pool.close()  # should not error as of Pool 2.0.

    def testBaseNumActiveNumIdle(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj1 = self.__pool.borrowObject()
        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

        self.__pool.returnObject(obj0)
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.close()

    def testBaseInvalidateObject(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj0)
        self.assertEqual(1, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.invalidateObject0(obj1)
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.close()

    def testBaseClosePool(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj = self.__pool.borrowObject()
        self.__pool.returnObject(obj)

        self.__pool.close()
        with pytest.raises(RuntimeError):
            self.__pool.borrowObject()

    def testBaseClear(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj0 = self.__pool.borrowObject()
        obj1 = self.__pool.borrowObject()

        self.assertEqual(2, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.returnObject(obj1)
        self.__pool.returnObject(obj0)

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(2, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        obj2 = self.__pool.borrowObject()

        self.assertEqual(self._getNthObject(2), obj2)

        self.__pool.close()

    def testBaseBorrowReturn(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        obj0 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(0), obj0)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)
        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(2), obj2)
        self.__pool.returnObject(obj1)
        obj1 = self.__pool.borrowObject()
        self.assertEqual(self._getNthObject(1), obj1)
        self.__pool.returnObject(obj0)
        self.__pool.returnObject(obj2)
        obj2 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(2), obj2)
        if self._isFifo():
            self.assertEqual(self._getNthObject(0), obj2)

        obj0 = self.__pool.borrowObject()
        if self._isLifo():
            self.assertEqual(self._getNthObject(0), obj0)
        if self._isFifo():
            self.assertEqual(self._getNthObject(2), obj0)
        self.__pool.close()

    def testBaseBorrow(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
        self.assertEqual(self._getNthObject(1), self.__pool.borrowObject())
        self.assertEqual(self._getNthObject(2), self.__pool.borrowObject())
        self.__pool.close()

    def testBaseAddObject(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        try:
            self.assertEqual(0, self.__pool.getNumIdle())
            self.assertEqual(0, self.__pool.getNumActive())
            self.__pool.addObject()
            self.assertEqual(1, self.__pool.getNumIdle())
            self.assertEqual(0, self.__pool.getNumActive())
            obj = self.__pool.borrowObject()
            self.assertEqual(self._getNthObject(0), obj)
            self.assertEqual(0, self.__pool.getNumIdle())
            self.assertEqual(1, self.__pool.getNumActive())
            self.__pool.returnObject(obj)
            self.assertEqual(1, self.__pool.getNumIdle())
            self.assertEqual(0, self.__pool.getNumActive())
        except NotImplementedError:
            return  # skip this test if one of those calls is unsupported
        finally:
            self.__pool.close()

    def _makeEmptyPool(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        return self._makeEmptyPool1(factory)

    def _makeEmptyPool1(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:

        if type(self) != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:

        if type(self) != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    def _isLifo(self) -> bool:
        if type(self) != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        return False

    def _isFifo(self) -> bool:
        if type(self) != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        return False

    def _getNthObject(self, n: int) -> typing.Any:
        if self.__class__ != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")
