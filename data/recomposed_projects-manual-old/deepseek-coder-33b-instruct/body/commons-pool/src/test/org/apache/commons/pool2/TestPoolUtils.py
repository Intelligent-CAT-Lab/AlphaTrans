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
        self.assertIsNotNone(h)
        self.assertIsNotNone(PoolUtils.TimerHolder.MIN_IDLE_TIMER)

    def testSynchronizedPoolObjectPool(self) -> None:

        with pytest.raises(
            ValueError,
            match="PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool.",
        ):
            PoolUtils.synchronizedPool1(None)

        calledMethods = []
        try:
            op = self.__createProxy1(ObjectPool, calledMethods)
            sop = PoolUtils.synchronizedPool1(op)
            expectedMethods = self.__invokeEveryMethod2(sop)
            assert expectedMethods == calledMethods
        finally:
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
            if hasattr(kop, "close"):
                kop.close()

    def testPrefillObjectPool(self) -> None:

        with pytest.raises(
            ValueError,
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
            raise e

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
            raise e

    def testJavaBeanInstantiation(self) -> None:

        assert self.assertIsNotNone(PoolUtils())

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
            self.assertEqual(expectedToString, pool.__str__())
        except Exception as e:
            self.fail(
                f"testErodingPoolKeyedObjectPoolDefaultFactor failed with exception: {str(e)}"
            )

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
            self.assertEqual(expected_to_string, str(pool))
        finally:
            if isinstance(pool, ObjectPool):
                pool.close()

    def testCheckRethrow(self) -> None:

        try:
            PoolUtils.checkRethrow(Exception())
        except Exception as t:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

        try:
            PoolUtils.checkRethrow(ThreadDeath())
            self.fail("PoolUtils.checkRethrow(Throwable) must rethrow ThreadDeath.")
        except ThreadDeath:
            pass
        except Exception as t:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

        try:
            PoolUtils.checkRethrow(InternalError())
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow VirtualMachineError."
            )
        except VirtualMachineError:
            pass
        except Exception as t:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

    def testCheckMinIdleKeyedObjectPoolKeysNulls(self) -> None:

        try:
            pool = self.__createProxy1(KeyedObjectPool, None)
            with self.assertRaises(
                ValueError,
                msg="PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must not accept null keys.",
            ):
                PoolUtils.checkMinIdle1(pool, None, 1, 1)
        except Exception as e:
            self.fail("Unexpected exception: " + str(e))

        try:
            pool = self.__createProxy1(KeyedObjectPool, None)
            PoolUtils.checkMinIdle1(pool, [], 1, 1)
        except ValueError:
            self.fail(
                "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must accept empty lists."
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

                time.sleep(self.__CHECK_SLEEP_PERIOD)
                for task in tasks.values():
                    task.cancel()

                expectedMethods = []
                for i in range(self.__CHECK_COUNT * len(keys)):
                    expectedMethods.append("getNumIdle1")
                    expectedMethods.append("addObject")
                self.assertEqual(expectedMethods, calledMethods)
            except AssertionFailedError as e:
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
        kpof.__str__()

        return [
            "activateObject",
            "destroyObject0",
            "makeObject",
            "passivateObject",
            "validateObject",
            "__str__",
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
