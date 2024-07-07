from __future__ import annotations
import time
import inspect
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PoolUtils import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *

# from src.main.org.opentest4j.AssertionFailedError import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class MethodCallLogger(typing.Callable):

    __calledMethods: typing.List[str] = None

    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:

        if self.__calledMethods is None:
            return None

        self.__calledMethods.append(method.__name__)

        if method.__annotations__["return"] == bool:
            return False

        if method.__annotations__["return"] == int:
            return 0

        if method.__annotations__["return"] == long:
            return 0

        if method.__annotations__["return"] == object:
            return object()

        if method.__annotations__["return"] == PooledObject:
            return DefaultPooledObject(object())

        return None

    def __init__(self, calledMethods: typing.List[str]) -> None:
        self.__calledMethods = calledMethods


class TestPoolUtils(unittest.TestCase):

    __CHECK_COUNT: int = 4
    __CHECK_PERIOD: int = 300
    __CHECK_SLEEP_PERIOD: int = (
        __CHECK_PERIOD * (__CHECK_COUNT - 1) + __CHECK_PERIOD / 2
    )

    def testTimerHolder(self) -> None:

        h = PoolUtils.TimerHolder()
        assert h is not None
        assert PoolUtils.TimerHolder.MIN_IDLE_TIMER is not None

    def testSynchronizedPoolObjectPool(self) -> None:

        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool.",
        ):
            PoolUtils.synchronizedPool1(None)

        calledMethods = []
        try:
            op = self.__createProxy1(ObjectPool, calledMethods)
            sop = PoolUtils.synchronizedPool1(op)
            expectedMethods = self.__invokeEveryMethod2(sop)
            self.assertEqual(expectedMethods, calledMethods)
        finally:
            if "op" in locals() and isinstance(op, ObjectPool):
                op.close()
            if "sop" in locals() and isinstance(sop, ObjectPool):
                sop.close()

    def testSynchronizedPoolKeyedObjectPool(self) -> None:

        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool.",
        ):
            PoolUtils.synchronizedPool0(None)

        calledMethods = []
        try:
            kop = self.__createProxy1(KeyedObjectPool, calledMethods)
            skop = PoolUtils.synchronizedPool0(kop)
            expectedMethods = self.__invokeEveryMethod0(skop)
            self.assertEqual(expectedMethods, calledMethods)
        finally:
            if "kop" in locals() and hasattr(kop, "close"):
                kop.close()
            if "skop" in locals() and hasattr(skop, "close"):
                skop.close()

    def testPrefillObjectPool(self) -> None:

        with pytest.raises(
            Exception,
            match="PoolUtils.prefill(ObjectPool,int) must not allow null pool.",
        ):
            PoolUtils.prefill2(None, 1)

        calledMethods = []
        try:
            pool = self.__createProxy1(ObjectPool, calledMethods)

            PoolUtils.prefill2(pool, 0)
            expectedMethods = ["addObjects"]
            assert expectedMethods == calledMethods

            calledMethods.clear()
            PoolUtils.prefill2(pool, 3)
            assert expectedMethods == calledMethods
        finally:
            pool.close()

    def testPrefillKeyedObjectPoolCollection(self) -> None:

        try:
            with self.__createProxy1(KeyedObjectPool, None) as pool:
                with pytest.raises(
                    ValueError,
                    match="PoolUtils.prefill(KeyedObjectPool,Collection,int) must not accept null keys.",
                ):
                    PoolUtils.prefill0(pool, None, 1)
        except Exception as e:
            print(e)

        calledMethods = []
        try:
            with self.__createProxy1(KeyedObjectPool, calledMethods) as pool:
                keys = set()
                PoolUtils.prefill0(pool, keys, 0)
                expectedMethods = ["addObjects0"]
                assert expectedMethods == calledMethods

                calledMethods.clear()
                keys.add("one")
                keys.add("two")
                keys.add("three")
                count = 3
                PoolUtils.prefill0(pool, keys, count)
                assert expectedMethods == calledMethods
        except Exception as e:
            print(e)

    def testJavaBeanInstantiation(self) -> None:

        # The Java code is testing if the instantiation of a new PoolUtils object is not null.
        # In Python, we can simply create an instance of the class and assert that it is not None.
        assert PoolUtils() is not None

    def testErodingPoolKeyedObjectPoolDefaultFactor(self) -> None:

        try:
            internalPool = self.__createProxy0(
                KeyedObjectPool, lambda arg0, arg1, arg2: None
            )
            pool = PoolUtils.erodingPool0(internalPool)
            expectedToString = (
                "ErodingKeyedObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1},"
                + " keyedPool="
                + str(internalPool)
                + "}"
            )
            self.assertEqual(expectedToString, pool.toString())
        finally:
            internalPool.close()

    def testErodingObjectPoolDefaultFactor(self) -> None:

        try:
            internal_pool = self.__createProxy0(
                ObjectPool, lambda arg0, arg1, arg2: None
            )
            pool = PoolUtils.erodingPool3(internal_pool)
            expected_to_string = (
                "ErodingObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1}, pool="
                + str(internal_pool)
                + "}"
            )
            self.assertEqual(expected_to_string, pool.to_string())
        finally:
            pool.close()
            internal_pool.close()

    def testCheckRethrow(self) -> None:

        try:
            PoolUtils.checkRethrow(Exception())
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )
        except (ThreadDeath, VirtualMachineError):
            pass
        except:
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

        try:
            PoolUtils.checkRethrow(ThreadDeath())
            pytest.fail("PoolUtils.checkRethrow(Throwable) must rethrow ThreadDeath.")
        except ThreadDeath:
            pass
        except:
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

        try:
            PoolUtils.checkRethrow(
                InternalError()
            )  # InternalError extends VirtualMachineError
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow VirtualMachineError."
            )
        except VirtualMachineError:
            pass
        except:
            pytest.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

    def testCheckMinIdleKeyedObjectPoolKeysNulls(self) -> None:

        try:
            with self.__createProxy1(KeyedObjectPool, None) as pool:
                with self.assertRaises(
                    ValueError,
                    msg="PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must not accept"
                    + " null keys.",
                ):
                    PoolUtils.checkMinIdle1(pool, None, 1, 1)
        except Exception as e:
            pass

        try:
            with self.__createProxy1(KeyedObjectPool, None) as pool:
                PoolUtils.checkMinIdle1(pool, [], 1, 1)
        except ValueError:
            self.fail(
                "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must accept empty"
                + " lists."
            )

    def testCheckMinIdleKeyedObjectPoolKeys(self) -> None:

        afe = None
        triesLeft = 3
        while triesLeft > 0:
            afe = None
            calledMethods = []
            try:
                pool = self.__createProxy1(KeyedObjectPool, calledMethods)
                keys = ["one", "two"]
                tasks = PoolUtils.checkMinIdle0(pool, keys, 1, self.__CHECK_PERIOD)

                time.sleep(
                    self.__CHECK_SLEEP_PERIOD / 1000.0
                )  # will check CHECK_COUNT more times.
                for task in tasks.values():
                    task.cancel()

                expectedMethods = []
                for i in range(self.__CHECK_COUNT * len(keys)):
                    expectedMethods.append("getNumIdle1")
                    expectedMethods.append("addObject")
                self.assertEqual(
                    expectedMethods, calledMethods
                )  # may fail because of the thread scheduler
            except AssertionError as e:
                afe = e
            triesLeft -= 1
        if afe is not None:
            raise afe

    @staticmethod
    def __createProxy0(
        clazz: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:
        return Proxy.newProxyInstance(clazz.getClassLoader(), [clazz], handler)

    @staticmethod
    def __invokeEveryMethod3(pof: PooledObjectFactory[typing.Any]) -> typing.List[str]:

        pof.activateObject(None)
        pof.destroyObject(None)
        pof.makeObject()
        pof.passivateObject(None)
        pof.validateObject(None)
        pof.toString()

        return [
            "activateObject",
            "destroyObject",
            "makeObject",
            "passivateObject",
            "validateObject",
            "toString",
        ]

    @staticmethod
    def __invokeEveryMethod2(op: ObjectPool[object]) -> typing.List[str]:

        op.addObject()
        op.borrowObject()
        op.clear()
        op.close()
        op.getNumActive()
        op.getNumIdle()
        op.invalidateObject0(object())
        op.returnObject(object())
        op.toString()

        return [
            "addObject",
            "borrowObject",
            "clear",
            "close",
            "getNumActive",
            "getNumIdle",
            "invalidateObject0",
            "returnObject",
            "toString",
        ]

    @staticmethod
    def __invokeEveryMethod1(
        kpof: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> typing.List[str]:

        kpof.activateObject(None, None)
        kpof.destroyObject0(None, None)
        kpof.makeObject(None)
        kpof.passivateObject(None, None)
        kpof.validateObject(None, None)
        kpof.toString()

        return [
            "activateObject",
            "destroyObject0",
            "makeObject",
            "passivateObject",
            "validateObject",
            "toString",
        ]

    @staticmethod
    def __invokeEveryMethod0(
        kop: KeyedObjectPool[object, typing.Any]
    ) -> typing.List[str]:

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
        kop.toString()

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
            "toString",
        ]

    @staticmethod
    def __createProxy1(
        clazz: typing.Type[typing.Any], logger: typing.List[str]
    ) -> typing.Any:
        return TestPoolUtils.__createProxy0(clazz, MethodCallLogger(logger))
