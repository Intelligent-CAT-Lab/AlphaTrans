import pytest

import unittest
from abc import ABC, abstractmethod
from src.test.org.apache.commons.pool2.MethodCall import *
from src.test.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from typing import List, Any

class TestKeyedObjectPool(unittest.TestCase, ABC):

    class FailingKeyedPooledObjectFactory:

        def __init__(self) -> None:
            self.__methodCalls = []
            self.__count = 0
            self.__makeObjectFail = False
            self.__activateObjectFail = False
            self.__validateObjectFail = False
            self.__passivateObjectFail = False
            self.__destroyObjectFail = False

        
        def activateObject(self, key, obj) -> None:
            try:
                self.__methodCalls.append(
                    MethodCall.MethodCall0("activateObject", key, obj.getObject())
                )
                if self.__activateObjectFail:
                    raise PrivateException("activateObject")
            except Exception as e:
                raise e

        
        def destroyObject(self, key, obj) -> None:
            try:
                self.__methodCalls.append(
                    MethodCall.MethodCall0("destroyObject", key, obj.getObject())
                )
                if self.__destroyObjectFail:
                    raise PrivateException("destroyObject")
            except Exception as e:
                raise e

        
        def getCurrentCount(self) -> int:
            return self.__count

        
        def getMethodCalls(self) -> List[MethodCall]:
            return self.__methodCalls

        
        def isActivateObjectFail(self) -> bool:
            return self.__activateObjectFail

        
        def isDestroyObjectFail(self) -> bool:
            return self.__destroyObjectFail

        
        def isMakeObjectFail(self) -> bool:
            return self.__makeObjectFail

        
        def isPassivateObjectFail(self) -> bool:
            return self.__passivateObjectFail

        
        def isValidateObjectFail(self) -> bool:
            return self.__validateObjectFail

        
        def passivateObject(self, key, obj) -> None:
            self.__methodCalls.append(
                MethodCall.MethodCall0("passivateObject", key, obj.getObject())
            )
            if self.__passivateObjectFail:
                raise PrivateException("passivateObject")

        
        def reset(self) -> None:
            self.__count = 0
            self.__methodCalls.clear()
            self.setMakeObjectFail(False)
            self.setActivateObjectFail(False)
            self.setValidateObjectFail(False)
            self.setPassivateObjectFail(False)
            self.setDestroyObjectFail(False)

        
        def setActivateObjectFail(self, activateObjectFail) -> None:
            self.__activateObjectFail = activateObjectFail

        
        def setCurrentCount(self, count) -> None:
            self.__count = count

        
        def setDestroyObjectFail(self, destroyObjectFail) -> None:
            self.__destroyObjectFail = destroyObjectFail

        
        def setMakeObjectFail(self, makeObjectFail) -> None:
            self.__makeObjectFail = makeObjectFail

        
        def setPassivateObjectFail(self, passivateObjectFail) -> None:
            self.__passivateObjectFail = passivateObjectFail

        
        def setValidateObjectFail(self, validateObjectFail) -> None:
            self.__validateObjectFail = validateObjectFail

        
        def validateObject(self, key, obj) -> bool:
            call = MethodCall.MethodCall0("validateObject", key, obj.getObject())
            self.__methodCalls.append(call)
            if self.__validateObjectFail:
                raise PrivateException("validateObject")
            r = True
            call.returned(bool(r))
            return r

    
    _KEY = "key"

    
    __test__ = False

    
    __pool = None

    __ZERO = int(0)

    __ONE = int(1)

    
    def __clear(self, factory, expectedMethods) -> None:
        factory.getMethodCalls().clear()
        expectedMethods.clear()
    

    @abstractmethod
    def _getNthObject(self, key, n) -> Any:
        pass

    
    @abstractmethod
    def _isFifo(self) -> bool:
        pass

    
    @abstractmethod
    def _isLifo(self) -> bool:
        pass

    
    @abstractmethod
    def _makeEmptyPool0(self, minCapacity) -> KeyedObjectPool:
        pass

    
    @abstractmethod
    def _makeEmptyPool1(self, factory) -> KeyedObjectPool:
        pass

    
    @abstractmethod
    def _makeKey(self, n) -> Any:
        pass

    
    def __reset(self, pool, factory, expectedMethods) -> None:
        try:
            pool.clear0()
            self.__clear(factory, expectedMethods)
            factory.reset()
        except Exception as e:
                raise e
    
    
    def tearDown(self) -> None:
        self.__pool = None

    @pytest.mark.test
    def testBaseAddObject(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
                return

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
            except (RuntimeError, NotImplementedError):
                return
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
                return
            
            keya = self._makeKey(0)
            keyb = self._makeKey(1)
            self.assertEqual(
                self._getNthObject(keya, 0),
                self.__pool.borrowObject(keya),
                "1"
            )
            self.assertEqual(
                self._getNthObject(keyb, 0),
                self.__pool.borrowObject(keyb),
                "2"
            )
            self.assertEqual(
                self._getNthObject(keyb, 1),
                self.__pool.borrowObject(keyb),
                "3"
            )
            self.assertEqual(
                self._getNthObject(keya, 1),
                self.__pool.borrowObject(keya),
                "4"
            )
            self.assertEqual(
                self._getNthObject(keyb, 2),
                self.__pool.borrowObject(keyb),
                "5"
            )
            self.assertEqual(
                self._getNthObject(keya, 2),
                self.__pool.borrowObject(keya),
                "6"
            )
            self.__pool.close()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseBorrowReturn(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
                return

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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseClear(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
                return

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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseInvalidateObject(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseNumActiveNumIdle(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(3)
            except (RuntimeError, NotImplementedError):
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
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    @pytest.mark.test
    def testBaseNumActiveNumIdle2(self) -> None:
        try:
            try:
                self.__pool = self._makeEmptyPool0(6)
            except (RuntimeError, NotImplementedError):
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

        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
