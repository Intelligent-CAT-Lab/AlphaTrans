import pytest

import unittest
from src.main.org.apache.commons.pool2.BaseObjectPool import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.test.org.apache.commons.pool2.TestObjectPool import *
from typing import Any

class TestBaseObjectPool(TestObjectPool):

    class TestObjectPool(BaseObjectPool):

        def borrowObject(self) -> Any:
            return None

        
        def invalidateObject0(self, obj) -> None:
            pass

        
        def returnObject(self, obj) -> None:
            pass

    
    def __init__(self) -> None:
        self.__pool = None

    
    def _getNthObject(self, n: int) -> Any:
        if self.__class__ != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    
    def _isFifo(self) -> bool:
        if self.__class__ != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        return False

    
    def _isLifo(self):
        if self.__class__ != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        return False

    
    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:
        if self.__class__ != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    
    def _makeEmptyPool(self, factory) -> ObjectPool[str]:
        return self._makeEmptyPool1(factory)

    
    def _makeEmptyPool1(self, factory) -> ObjectPool[str]:
        if self.__class__ != TestBaseObjectPool:
            self.fail("Subclasses of TestBaseObjectPool must reimplement this method.")
        raise NotImplementedError("BaseObjectPool isn't a complete implementation.")

    
    @pytest.mark.test
    def testBaseAddObject(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
            except (RuntimeError, NotImplementedError):
                return  # skip this test if one of those calls is unsupported
            finally:
                self.__pool.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseBorrow(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
                return  # skip this test if unsupported
            self.assertEqual(self._getNthObject(0), self.__pool.borrowObject())
            self.assertEqual(self._getNthObject(1), self.__pool.borrowObject())
            self.assertEqual(self._getNthObject(2), self.__pool.borrowObject())
            self.__pool.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseBorrowReturn(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseClear(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseClosePool(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
                return  # skip this test if unsupported
            obj = self.__pool.borrowObject()
            self.__pool.returnObject(obj)

            self.__pool.close()
            with self.assertRaises(RuntimeError):
                self.__pool.borrowObject()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseInvalidateObject(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseNumActiveNumIdle(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testClose(self) -> None:
        pool = self.TestObjectPool()

        pool.close()
        pool.close()  # should not error as of Pool 2.0

    
    @pytest.mark.test
    def testUnsupportedOperations(self) -> None:
        try:
            if self.__class__ != TestBaseObjectPool:
                return  # skip redundant tests`
            pool = TestBaseObjectPool.TestObjectPool()
            try:
                self.assertTrue(pool.getNumIdle() < 0, "Negative expected.")
                self.assertTrue(pool.getNumActive() < 0, "Negative expected.")
                with self.assertRaises(NotImplementedError):
                    pool.clear()
                with self.assertRaises(NotImplementedError):
                    pool.addObject()
            except Exception as e:
                raise e
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
