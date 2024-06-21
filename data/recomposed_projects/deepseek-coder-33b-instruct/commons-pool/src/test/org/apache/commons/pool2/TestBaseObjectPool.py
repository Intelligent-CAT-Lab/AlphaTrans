from __future__ import annotations
import io
import typing
from typing import *
import os
from src.test.org.apache.commons.pool2.MethodCall import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.test.org.apache.commons.pool2.TestObjectPool import *
from src.main.org.apache.commons.pool2.BaseObjectPool import *


class TestObjectPool(BaseObjectPool):

    def returnObject(self, obj: typing.Any) -> None:

        pass  # LLM could not translate this method

    def invalidateObject0(self, obj: typing.Any) -> None:

        pass

    def borrowObject(self) -> typing.Any:

        return None


class TestBaseObjectPool(TestObjectPool):

    __pool: ObjectPool[str] = None

    def testUnsupportedOperations(self) -> None:

        if not isinstance(self, TestBaseObjectPool):
            return  # skip redundant tests

        with TestObjectPool() as pool:

            assert pool.getNumIdle() < 0, "Negative expected."
            assert pool.getNumActive() < 0, "Negative expected."

            try:
                pool.clear()
                assert False, "Expected NotImplementedError"
            except NotImplementedError:
                pass

            try:
                pool.addObject()
                assert False, "Expected NotImplementedError"
            except NotImplementedError:
                pass

    def testClose(self) -> None:

        self.__pool = TestObjectPool()

        self.__pool.close()
        self.__pool.close()  # should not error as of Pool 2.0.

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
        try:
            self.__pool.borrowObject()
        except IllegalStateException:
            pass
        else:
            raise AssertionError("Expected IllegalStateException")

    def testBaseClear(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

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

        assert self._getNthObject(2) == obj2

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

        assert self._getNthObject(0) == self.__pool.borrowObject()
        assert self._getNthObject(1) == self.__pool.borrowObject()
        assert self._getNthObject(2) == self.__pool.borrowObject()
        self.__pool.close()

    def testBaseAddObject(self) -> None:

        try:
            self.__pool = self._makeEmptyPool0(3)
        except NotImplementedError:
            return  # skip this test if unsupported

        try:
            assert self.__pool.getNumIdle() == 0
            assert self.__pool.getNumActive() == 0
            self.__pool.addObject()
            assert self.__pool.getNumIdle() == 1
            assert self.__pool.getNumActive() == 0
            obj = self.__pool.borrowObject()
            assert self._getNthObject(0) == obj
            assert self.__pool.getNumIdle() == 0
            assert self.__pool.getNumActive() == 1
            self.__pool.returnObject(obj)
            assert self.__pool.getNumIdle() == 1
            assert self.__pool.getNumActive() == 0
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
            raise Exception(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        else:
            raise Exception("BaseObjectPool isn't a complete implementation.")

    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:

        if type(self) != TestBaseObjectPool:
            raise Exception(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        else:
            raise Exception("BaseObjectPool isn't a complete implementation.")

    def _isLifo(self) -> bool:

        if type(self) != TestBaseObjectPool:
            raise Exception(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        return False

    def _isFifo(self) -> bool:

        if type(self) != TestBaseObjectPool:
            raise Exception(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        return False

    def _getNthObject(self, n: int) -> typing.Any:

        if type(self) != TestBaseObjectPool:
            raise Exception(
                "Subclasses of TestBaseObjectPool must reimplement this method."
            )
        else:
            raise Exception("BaseObjectPool isn't a complete implementation.")
