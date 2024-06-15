import unittest
from unittest.mock import create_autospec, MagicMock, Mock
from threading import Timer
from collections import defaultdict
from typing import List, Dict, Set, Callable, Any, TypeVar, Type
from contextlib import contextmanager
import inspect
import time
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.PoolUtils import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *

class TestPoolUtils(unittest.TestCase):

    class MethodCallLogger:
        def __init__(self, calledMethods: List[str]) -> None:
            self.__calledMethods = calledMethods

        def logMethod(self, methodName: str, returnType: type):
            try:
                if self.__calledMethods is None:
                    return None
                self.__calledMethods.append(methodName)
                if returnType == bool:
                    return False
                if returnType == int:
                    return 0
                if returnType == float:
                    return 0.0
                if returnType == object:
                    return object()
                if returnType == PooledObject:
                    return DefaultPooledObject(object())
                return None
            except BaseException as e:
                raise e

    __CHECK_PERIOD = 300
    __CHECK_COUNT = 4
    __CHECK_SLEEP_PERIOD = __CHECK_PERIOD * (__CHECK_COUNT - 1) + __CHECK_PERIOD // 2


    T = TypeVar('T')

    @staticmethod
    def __createProxy0(clazz: Type[T], handler: Callable) -> T:
        proxy = Mock(spec=clazz)
        for methodName, method in inspect.getmembers(clazz, predicate=inspect.isfunction):
            returnType = method.__annotations__.get('return', None)
            if (isinstance(handler, TestPoolUtils.MethodCallLogger)):
              mockMethod = Mock(
                  side_effect=lambda *args,
                  methodName=methodName,
                  returnType=returnType: handler.logMethod(methodName, returnType)
              )
            else:
               mockMethod = Mock(
                  side_effect=handler
              )
            setattr(proxy, methodName, mockMethod)
        if hasattr(clazz, '__str__'):
            returnType = str  # The return type of __str__ is always str
            if isinstance(handler, TestPoolUtils.MethodCallLogger):
                mockMethod = Mock(
                    side_effect=lambda *args,
                    methodName='__str__',
                    returnType=returnType: handler.logMethod(methodName, returnType)
                )
            else:
                mockMethod = Mock(side_effect=handler)
            setattr(proxy, '__str__', mockMethod)
        return proxy

    
    @staticmethod
    def __createProxy1(clazz: Type[T], logger: List[str]) -> T:
        return TestPoolUtils.__createProxy0(clazz, TestPoolUtils.MethodCallLogger(logger))


    @staticmethod
    def __invokeEveryMethod0(kop: KeyedObjectPool) -> List[str]:
        try:
            kop.addObject(None)
            kop.borrowObject(None)
            kop.clear0()
            kop.clear1(None)
            kop.close()
            kop.getNumActive0()
            kop.getNumActive1(None)
            kop.getNumIdle0()
            kop.getNumIdle1(None)
            kop.invalidateObject0(None, object())
            kop.returnObject(None, object())
            kop.__str__()

            return [
                "addObject",
                "borrowObject",
                "clear0",
                "clear1",
                "close",
                "getNumActive0",
                "getNumActive1",
                "getNumIdle0",
                "getNumIdle1",
                "invalidateObject0",
                "returnObject",
                "__str__"
            ]
        except Exception as e:
            raise e

    
    @staticmethod
    def __invokeEveryMethod1(kpof: KeyedPooledObjectFactory) -> List[str]:
        try:
            kpof.activateObject(None, None)
            kpof.destroyObject0(None, None)
            kpof.makeObject(None)
            kpof.passivateObject(None, None)
            kpof.validateObject(None, None)
            kpof.__str__()

            return [
                "activateObject",
                "destroyObject0",
                "makeObject",
                "passivateObject",
                "validateObject",
                "__str__"
            ]
        except Exception as e:
            raise e
    
    
    @staticmethod
    def __invokeEveryMethod2(op: ObjectPool) -> List[str]:
        try:
            op.addObject()
            op.borrowObject()
            op.clear()
            op.close()
            op.getNumActive()
            op.getNumIdle()
            op.invalidateObject0(object())
            op.returnObject(object())
            op.__str__()

            return [
                "addObject",
                "borrowObject",
                "clear",
                "close",
                "getNumActive",
                "getNumIdle",
                "invalidateObject0",
                "returnObject",
                "__str__"
            ]
        except Exception as e:
            raise e
    

    @staticmethod
    def __invokeEveryMethod3(pof: PooledObjectFactory) -> List[str]:
        try:
            pof.activateObject(None)
            pof.destroyObject0(None)
            pof.makeObject()
            pof.passivateObject(None)
            pof.validateObject(None)
            pof.__str__()

            return [
                "activateObject",
                "destroyObject",
                "makeObject",
                "passivateObject",
                "validateObject",
                "__str__"
            ]
        except Exception as e:
            raise e
    

    def testCheckMinIdleKeyedObjectPoolKeys(self) -> None:
        try:
            afe = None
            triesLeft = 3
            while triesLeft > 0:
                afe = None
                calledMethods = []
                try:
                    pool = TestPoolUtils.__createProxy1(KeyedObjectPool, calledMethods)
                    keys = ["one", "two"]
                    tasks = PoolUtils.checkMinIdle0(
                        pool,
                        keys,
                        1,
                        TestPoolUtils.__CHECK_PERIOD
                    )
                    
                    time.sleep(TestPoolUtils.__CHECK_SLEEP_PERIOD / 1000)
                    for task in tasks.values():
                        task.cancel()

                    expectedMethods = []
                    for i in range(TestPoolUtils.__CHECK_COUNT * len(keys)):
                        expectedMethods.append("getNumIdle1")
                        expectedMethods.append("addObject")
                    
                    self.assertEqual(expectedMethods, calledMethods)
                except AssertionError as e:
                    afe = e

                if afe is None:
                    break
                triesLeft -= 1

            if afe is not None:
                raise afe
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testCheckMinIdleKeyedObjectPoolKeysNulls(self) -> None:
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long)" +\
                "must not accept null keys."
        ):
            pool = TestPoolUtils.__createProxy1(KeyedObjectPool, None)
            PoolUtils.checkMinIdle1(pool, None, 1, 1)

        try:
            pool = TestPoolUtils.__createProxy1(KeyedObjectPool, None)
            PoolUtils.checkMinIdle1(pool, [], 1, 1)
        except ValueError as iae:
            self.fail(
                "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long)" +\
                "must accept empty lists."
            )
    

    def testCheckRethrow(self) -> None:
        try:
            PoolUtils.checkRethrow(Exception())
        except BaseException:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only" +\
                "ThreadDeath and VirtualMachineError.")

        try:
            PoolUtils.checkRethrow(SystemExit())
            self.fail("PoolUtils.checkRethrow(Throwable) must rethrow ThreadError.")
        except SystemExit:
            pass
        except BaseException:
            self.fail("PoolUtils.checkRethrow(Throwable) must rethrow only" +\
                "ThreadError and VirtualMachineError.")

        try:
            PoolUtils.checkRethrow(RuntimeError)
            PoolUtils.checkRethrow(SystemError)
            self.fail("PoolUtils.checkRethrow(Throwable) must rethrow VirtualMachineError.")
        except (RuntimeError, SystemError):
            pass
        except BaseException:
            self.fail("PoolUtils.checkRethrow(Throwable) must rethrow only" +\
                "ThreadError and VirtualMachineError.")
    

    def testErodingObjectPoolDefaultFactor(self) -> None:
        try:
            internalPool = TestPoolUtils.__createProxy0(ObjectPool, lambda *args: None)
            pool = PoolUtils.erodingPool3(internalPool)
            
            expectedToString = "ErodingObjectPool{factor=ErodingFactor{factor=1.0, " +\
                "idleHighWaterMark=1}, pool=" +\
                str(internalPool) +\
                "}"
            
            self.assertEqual(expectedToString, pool.toString())
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testErodingPoolKeyedObjectPoolDefaultFactor(self) -> None:
        try:
            internalPool = TestPoolUtils.__createProxy0(KeyedObjectPool, lambda *args: None)
            pool = PoolUtils.erodingPool0(internalPool)
            
            expectedToString = "ErodingKeyedObjectPool{factor=ErodingFactor{factor=1.0, " +\
                "idleHighWaterMark=1}, keyedPool=" +\
                str(internalPool) +\
                "}"
            
            self.assertEqual(expectedToString, pool.toString())
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testJavaBeanInstantiation(self) -> None:
        self.assertIsNotNone(PoolUtils())
    

    def testPrefillKeyedObjectPoolCollection(self) -> None:
        pool = TestPoolUtils.__createProxy1(KeyedObjectPool, None)
        try:
            with self.assertRaises(
                ValueError,
                msg="PoolUtils.prefill(KeyedObjectPool,Collection,int)" +\
                    "must not accept null keys."
            ):
                PoolUtils.prefill0(pool, None, 1)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

        calledMethods = []
        pool = TestPoolUtils.__createProxy1(KeyedObjectPool, calledMethods)

        try:
            keys = set()
            PoolUtils.prefill0(pool, keys, 0)
            expectedMethods = []
            expectedMethods.append("addObjects0")
            self.assertEqual(expectedMethods, calledMethods)

            calledMethods.clear()
            keys.update(["one", "two", "three"])
            count = 3
            PoolUtils.prefill0(pool, keys, count)
            self.assertEqual(expectedMethods, calledMethods)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testPrefillObjectPool(self) -> None:
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.prefill(ObjectPool,int) must not allow null pool."
        ):
            PoolUtils.prefill2(None, 1)

        calledMethods = []
        pool = TestPoolUtils.__createProxy1(ObjectPool, calledMethods)

        try:
            PoolUtils.prefill2(pool, 0)
            expectedMethods = []
            expectedMethods.append("addObjects")
            self.assertEqual(expectedMethods, calledMethods)

            calledMethods.clear()
            PoolUtils.prefill2(pool, 3)
            self.assertEqual(expectedMethods, calledMethods)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testSynchronizedPoolKeyedObjectPool(self) -> None:
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool."
        ):
            PoolUtils.synchronizedPool0(None)

        calledMethods = []
        kop = TestPoolUtils.__createProxy1(KeyedObjectPool, calledMethods)
        try:
            skop = PoolUtils.synchronizedPool0(kop)

            expectedMethods = TestPoolUtils.__invokeEveryMethod0(skop)
            self.assertEqual(expectedMethods, calledMethods)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testSynchronizedPoolObjectPool(self) -> None:
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool."
        ):
            PoolUtils.synchronizedPool1(None)

        calledMethods = []
        op = TestPoolUtils.__createProxy1(ObjectPool, calledMethods)
        sop = PoolUtils.synchronizedPool1(op)

        try:
            expectedMethods = TestPoolUtils.__invokeEveryMethod2(sop)
            self.assertEqual(expectedMethods, calledMethods)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
    

    def testTimerHolder(self) -> None:
        h = PoolUtils.TimerHolder()
        self.assertIsNotNone(h)
        self.assertIsNotNone(PoolUtils.TimerHolder.MIN_IDLE_TIMER)
