from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *

# from src.main.org.opentest4j.AssertionFailedError import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PoolUtils import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class MethodCallLogger:

    # Class Fields Begin
    __calledMethods: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        pass

    def __init__(self, calledMethods: typing.List[str]) -> None:
        pass

    # Class Methods End


class TestPoolUtils(unittest.TestCase):

    # Class Fields Begin
    __CHECK_PERIOD: int = None
    __CHECK_COUNT: int = None
    __CHECK_SLEEP_PERIOD: int = None
    # Class Fields End

    # Class Methods Begin
    def testTimerHolder_test1_decomposed(self) -> None:
        pass

    def testTimerHolder_test0_decomposed(self) -> None:
        pass

    def testSynchronizedPoolObjectPool_test1_decomposed(self) -> None:
        pass

    def testSynchronizedPoolObjectPool_test0_decomposed(self) -> None:
        pass

    def testSynchronizedPoolKeyedObjectPool_test1_decomposed(self) -> None:
        pass

    def testSynchronizedPoolKeyedObjectPool_test0_decomposed(self) -> None:
        pass

    def testPrefillObjectPool_test1_decomposed(self) -> None:
        pass

    def testPrefillObjectPool_test0_decomposed(self) -> None:
        pass

    def testPrefillKeyedObjectPoolCollection_test1_decomposed(self) -> None:
        pass

    def testPrefillKeyedObjectPoolCollection_test0_decomposed(self) -> None:
        pass

    def testJavaBeanInstantiation_test0_decomposed(self) -> None:
        pass

    def testErodingPoolKeyedObjectPoolDefaultFactor_test0_decomposed(self) -> None:
        pass

    def testErodingObjectPoolDefaultFactor_test0_decomposed(self) -> None:
        pass

    def testCheckRethrow_test0_decomposed(self) -> None:
        pass

    def testCheckMinIdleKeyedObjectPoolKeysNulls_test1_decomposed(self) -> None:
        pass

    def testCheckMinIdleKeyedObjectPoolKeysNulls_test0_decomposed(self) -> None:
        pass

    def testCheckMinIdleKeyedObjectPoolKeys_test1_decomposed(self) -> None:
        pass

    def testCheckMinIdleKeyedObjectPoolKeys_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __createProxy0(
        clazz: typing.Type[typing.Any], handler: typing.Callable
    ) -> typing.Any:
        pass

    @staticmethod
    def __invokeEveryMethod3(pof: PooledObjectFactory[typing.Any]) -> typing.List[str]:
        pass

    @staticmethod
    def __invokeEveryMethod2(op: ObjectPool[object]) -> typing.List[str]:
        pass

    @staticmethod
    def __invokeEveryMethod1(
        kpof: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> typing.List[str]:
        pass

    @staticmethod
    def __invokeEveryMethod0(
        kop: KeyedObjectPool[object, typing.Any]
    ) -> typing.List[str]:
        pass

    @staticmethod
    def __createProxy1(
        clazz: typing.Type[typing.Any], logger: typing.List[str]
    ) -> typing.Any:
        pass

    # Class Methods End
