from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PoolUtils import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.opentest4j.AssertionFailedError import *
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


class TestPoolUtils:

    __CHECK_SLEEP_PERIOD: int = CHECK_PERIOD * (CHECK_COUNT - 1) + CHECK_PERIOD / 2

    __CHECK_COUNT: int = 4

    __CHECK_PERIOD: int = 300

    def testTimerHolder(self) -> None:

        h = PoolUtils.TimerHolder()
        assert h is not None
        assert PoolUtils.TimerHolder.MIN_IDLE_TIMER is not None

    def testSynchronizedPoolObjectPool(self) -> None:

        # Testing if PoolUtils.synchronizedPool(ObjectPool) allows a null pool.
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(ObjectPool) must not allow a null pool.",
        ):
            PoolUtils.synchronizedPool1(None)

        # Testing if PoolUtils.synchronizedPool(ObjectPool) works correctly.
        called_methods = []
        try:
            op = self.__createProxy1(ObjectPool, called_methods)
            sop = PoolUtils.synchronizedPool1(op)
            expected_methods = self.__invokeEveryMethod2(sop)
            self.assertEqual(expected_methods, called_methods)
        finally:
            if sop is not None:
                sop.close()

    def testSynchronizedPoolKeyedObjectPool(self) -> None:

        # Testing if PoolUtils.synchronizedPool(KeyedObjectPool) allows a null pool.
        with self.assertRaises(
            ValueError,
            msg="PoolUtils.synchronizedPool(KeyedObjectPool) must not allow a null pool.",
        ):
            PoolUtils.synchronizedPool0(None)

        # Creating a list to store the called methods.
        called_methods = []

        # Creating a proxy for the KeyedObjectPool class.
        kop = self.__createProxy1(KeyedObjectPool, called_methods)

        # Creating a synchronized pool from the KeyedObjectPool.
        skop = PoolUtils.synchronizedPool0(kop)

        # Invoking every method of the synchronized pool.
        expected_methods = self.__invokeEveryMethod0(skop)

        # Asserting that the expected methods were called.
        self.assertEqual(expected_methods, called_methods)

    def testPrefillObjectPool(self) -> None:

        with self.assertRaises(
            ValueError,
            msg="PoolUtils.prefill(ObjectPool,int) must not allow null pool.",
        ):
            PoolUtils.prefill2(None, 1)

        called_methods = []
        try:
            pool = self.__createProxy1(ObjectPool, called_methods)

            PoolUtils.prefill2(pool, 0)
            expected_methods = ["addObjects"]
            self.assertEqual(expected_methods, called_methods)

            called_methods.clear()
            PoolUtils.prefill2(pool, 3)
            self.assertEqual(expected_methods, called_methods)
        finally:
            pool.close()

    def testPrefillKeyedObjectPoolCollection(self) -> None:

        try:
            pool: KeyedObjectPool[str, str] = self.__createProxy1(KeyedObjectPool, None)
            with self.assertRaises(
                ValueError,
                msg="PoolUtils.prefill(KeyedObjectPool,Collection,int) must not accept null keys.",
            ):
                PoolUtils.prefill0(pool, None, 1)
        finally:
            pool.close()

        called_methods: List[str] = []
        try:
            pool: KeyedObjectPool[str, object] = self.__createProxy1(
                KeyedObjectPool, called_methods
            )

            keys: Set[str] = set()
            PoolUtils.prefill0(pool, keys, 0)
            expected_methods: List[str] = ["addObjects0"]
            self.assertEqual(expected_methods, called_methods)

            called_methods.clear()
            keys.update(["one", "two", "three"])
            count: int = 3
            PoolUtils.prefill0(pool, keys, count)
            self.assertEqual(expected_methods, called_methods)
        finally:
            pool.close()

    def testJavaBeanInstantiation(self) -> None:

        # The PoolUtils class is not defined in the provided partial Python translation.
        # If it's a class from a different module, you need to import it.
        # If it's a class from the same module, you need to make sure it's defined before this method.
        # Here, I'm assuming it's a class from the same module.

        assert PoolUtils() is not None

    def testErodingPoolKeyedObjectPoolDefaultFactor(self) -> None:

        class MockKeyedObjectPool(KeyedObjectPool):
            def borrowObject(self, key: typing.Any) -> PooledObject:
                pass

            def returnObject(self, key: typing.Any, obj: PooledObject) -> None:
                pass

            def invalidateObject(self, key: typing.Any, obj: PooledObject) -> None:
                pass

            def addObject(self, key: typing.Any) -> None:
                pass

            def getNumIdle(self, key: typing.Any) -> int:
                pass

            def getNumActive(self, key: typing.Any) -> int:
                pass

            def clear(self) -> None:
                pass

            def close(self) -> None:
                pass

        internalPool = MockKeyedObjectPool()
        pool = PoolUtils.erodingPool0(internalPool)

        expectedToString = (
            "ErodingKeyedObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1},"
            + " keyedPool="
            + str(internalPool)
            + "}"
        )
        assert expectedToString == pool.toString()

    def testErodingObjectPoolDefaultFactor(self) -> None:

        class MockObjectPool(ObjectPool):
            def __init__(self, handler):
                self.handler = handler

            def borrowObject(self, arg0=None, arg1=None, arg2=None):
                return self.handler(arg0, arg1, arg2)

            def returnObject(self, obj):
                pass

            def invalidateObject(self, key, obj):
                pass

            def addObject(self):
                pass

            def close(self):
                pass

        internal_pool = MockObjectPool(lambda arg0, arg1, arg2: None)
        pool = PoolUtils.erodingPool3(internal_pool)

        expected_to_string = (
            "ErodingObjectPool{factor=ErodingFactor{factor=1.0, idleHighWaterMark=1}, pool="
            + str(internal_pool)
            + "}"
        )
        assert expected_to_string == pool.toString()

    def testCheckRethrow(self) -> None:

        try:
            PoolUtils.checkRethrow(Exception())
        except Throwable as t:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

        try:
            PoolUtils.checkRethrow(ThreadDeath())
            self.fail("PoolUtils.checkRethrow(Throwable) must rethrow ThreadDeath.")
        except ThreadDeath as td:
            pass
        except Throwable as t:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

        try:
            PoolUtils.checkRethrow(
                InternalError()
            )  # InternalError extends VirtualMachineError
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow VirtualMachineError."
            )
        except VirtualMachineError as td:
            pass
        except Throwable as t:
            self.fail(
                "PoolUtils.checkRethrow(Throwable) must rethrow only ThreadDeath and"
                + " VirtualMachineError."
            )

    def testCheckMinIdleKeyedObjectPoolKeysNulls(self) -> None:

        try:
            pool = self.__createProxy1(KeyedObjectPool, None)
            try:
                PoolUtils.checkMinIdle1(pool, None, 1, 1)
                raise AssertionFailedError(
                    "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must not accept null keys."
                )
            except ValueError:
                pass
        finally:
            pool.close()

        try:
            pool = self.__createProxy1(KeyedObjectPool, None)
            PoolUtils.checkMinIdle1(pool, [], 1, 1)
        except ValueError:
            raise AssertionFailedError(
                "PoolUtils.checkMinIdle(KeyedObjectPool,Collection,int,long) must accept empty lists."
            )
        finally:
            pool.close()

    def testCheckMinIdleKeyedObjectPoolKeys(self) -> None:

        afe = None
        triesLeft = 3
        CHECK_SLEEP_PERIOD = self.__CHECK_SLEEP_PERIOD
        CHECK_COUNT = self.__CHECK_COUNT
        CHECK_PERIOD = self.__CHECK_PERIOD

        while triesLeft > 0:
            afe = None
            calledMethods = []
            try:
                pool = self.__createProxy1(KeyedObjectPool, calledMethods)
                keys = ["one", "two"]
                tasks = PoolUtils.checkMinIdle0(pool, keys, 1, CHECK_PERIOD)

                time.sleep(CHECK_SLEEP_PERIOD)
                for task in tasks.values():
                    task.cancel()

                expectedMethods = []
                for i in range(CHECK_COUNT * len(keys)):
                    expectedMethods.append("getNumIdle1")
                    expectedMethods.append("addObject")
                assert expectedMethods == calledMethods
            except AssertionFailedError as e:
                afe = e
            triesLeft -= 1

        if afe is not None:
            raise afe

    @staticmethod
    def __createProxy0(
        clazz: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:

        return typing.cast(
            typing.Any, Proxy.newProxyInstance(clazz.getClassLoader(), [clazz], handler)
        )

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
        op.invalidateObject(object())
        op.returnObject(object())
        op.toString()

        return [
            "addObject",
            "borrowObject",
            "clear",
            "close",
            "getNumActive",
            "getNumIdle",
            "invalidateObject",
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
