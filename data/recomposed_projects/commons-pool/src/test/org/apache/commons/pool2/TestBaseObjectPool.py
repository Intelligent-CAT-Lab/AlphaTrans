# Imports Begin
from src.main.org.apache.commons.pool2.BaseObjectPool import *
from src.main.org.apache.commons.pool2.TestObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.main.org.apache.commons.pool2.MethodCall import *
import unittest
import os
import typing
from typing import *
# Imports End

class TestObjectPool(unittest.TestCase, BaseObjectPool<Object>):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def returnObject(self, obj: typing.Any) -> None:

            pass

    def invalidateObject0(self, obj: typing.Any) -> None:

            pass

    def borrowObject(self) -> typing.Any:

            return None

    # Class Methods End


class TestBaseObjectPool(unittest.TestCase, TestObjectPool):

    # Class Fields Begin
    __pool: ObjectPool[str] = None
    # Class Fields End

    # Class Methods Begin
    def testUnsupportedOperations(self) -> None:

            if self.__class__ != TestBaseObjectPool:
                return  # skip redundant tests
            with TestObjectPool() as pool:
                assert pool.getNumIdle() < 0, "Negative expected."
                assert pool.getNumActive() < 0, "Negative expected."
                self.assertRaises(UnsupportedOperationException, pool.clear)
                self.assertRaises(UnsupportedOperationException, pool.addObject)

    def testClose(self) -> None:

            pool = TestObjectPool()
            pool.close()
            pool.close() # should not error as of Pool 2.0.

    def testBaseNumActiveNumIdle(self) -> None:

            try:
                self.__pool = self._makeEmptyPool0(3)
            except UnsupportedOperationException:
                return
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
            except UnsupportedOperationException:
                return
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
            except UnsupportedOperationException:
                return
            obj = self.__pool.borrowObject()
            self.__pool.returnObject(obj)
            self.__pool.close()
            assertThrows(IllegalStateException, self.__pool.borrowObject)

    def testBaseClear(self) -> None:

            try:
                self.__pool = self._makeEmptyPool0(3)
            except UnsupportedOperationException:
                return
            assert self.__pool.getNumActive() == 0
            assert self.__pool.getNumIdle() == 0
            obj0 = self.__pool.borrowObject()
            obj1 = self.__pool.borrowObject()
            assert self.__pool.getNumActive() == 2
            assert self.__pool.getNumIdle() == 0
            self.__pool.returnObject(obj1)
            self.__pool.returnObject(obj0)
            assert self.__pool.getNumActive() == 0
            assert self.__pool.getNumIdle() == 2
            self.__pool.clear()
            assert self.__pool.getNumActive() == 0
            assert self.__pool.getNumIdle() == 0
            obj2 = self.__pool.borrowObject()
            assert obj2 == self._getNthObject(2)
            self.__pool.close()

    def testBaseBorrowReturn(self) -> None:

            try:
                self.__pool = self._makeEmptyPool0(3)
            except UnsupportedOperationException:
                return
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
            except UnsupportedOperationException:
                return
            assert self._getNthObject(0) == self.__pool.borrowObject()
            assert self._getNthObject(1) == self.__pool.borrowObject()
            assert self._getNthObject(2) == self.__pool.borrowObject()
            self.__pool.close()

    def testBaseAddObject(self) -> None:

            try:
                self.__pool = self._makeEmptyPool0(3)
            except UnsupportedOperationException:
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
            except UnsupportedOperationException:
                return  # skip this test if one of those calls is unsupported
            finally:
                self.__pool.close()

    def _makeEmptyPool(self, factory: PooledObjectFactory[typing.Any]) -> ObjectPool[object]:

            return self._makeEmptyPool1(factory)

    def _makeEmptyPool1(self, factory: PooledObjectFactory[typing.Any]) -> ObjectPool[object]:

            if self.__class__ != TestBaseObjectPool:
                self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
            raise UnsupportedOperationException("BaseObjectPool isn't a complete implementation.")

    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:

            if self.__class__ != TestBaseObjectPool:
                self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
            raise UnsupportedOperationException("BaseObjectPool isn't a complete implementation.")

    def _isLifo(self) -> bool:

            if self.__class__ != TestBaseObjectPool:
                self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
            return False

    def _isFifo(self) -> bool:

            if self.__class__ != TestBaseObjectPool:
                self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
            return False

    def _getNthObject(self, n: int) -> typing.Any:

            if self.__class__ != TestBaseObjectPool:
                raise NotImplementedError("Subclasses of TestBaseObjectPool must reimplement this method.")
            raise UnsupportedOperation("BaseObjectPool isn't a complete implementation.")

    # Class Methods End


class new Executable(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> typing.Any:

        try:
            self.pool.borrowObject()
        except IllegalStateException:
            pass

    def execute(self) -> None:

        with self.assertRaises(UnsupportedOperationException):
            self.pool.clear()

    def execute(self) -> None:

        with self.assertRaises(UnsupportedOperationException):
            self.pool.addObject()

    # Class Methods End


