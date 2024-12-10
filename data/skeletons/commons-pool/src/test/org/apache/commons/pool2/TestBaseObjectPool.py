from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.BaseObjectPool import *
from src.test.org.apache.commons.pool2.TestObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.test.org.apache.commons.pool2.MethodCall import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class TestObjectPool(BaseObjectPool):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    # Class Methods End


class TestBaseObjectPool(TestObjectPool, unittest.TestCase):

    # Class Fields Begin
    __pool: ObjectPool[str] = None
    # Class Fields End

    # Class Methods Begin
    def testUnsupportedOperations_test1_decomposed(self) -> None:
        pass

    def testUnsupportedOperations_test0_decomposed(self) -> None:
        pass

    def testClose_test1_decomposed(self) -> None:
        pass

    def testClose_test0_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test15_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test14_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test13_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test12_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test11_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test10_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test9_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test8_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test7_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test6_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test5_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test4_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test3_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test2_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test1_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test0_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test12_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test11_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test10_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test9_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test8_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test7_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test6_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test5_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test4_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test3_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test2_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test1_decomposed(self) -> None:
        pass

    def testBaseInvalidateObject_test0_decomposed(self) -> None:
        pass

    def testBaseClosePool_test4_decomposed(self) -> None:
        pass

    def testBaseClosePool_test3_decomposed(self) -> None:
        pass

    def testBaseClosePool_test2_decomposed(self) -> None:
        pass

    def testBaseClosePool_test1_decomposed(self) -> None:
        pass

    def testBaseClosePool_test0_decomposed(self) -> None:
        pass

    def testBaseClear_test14_decomposed(self) -> None:
        pass

    def testBaseClear_test13_decomposed(self) -> None:
        pass

    def testBaseClear_test12_decomposed(self) -> None:
        pass

    def testBaseClear_test11_decomposed(self) -> None:
        pass

    def testBaseClear_test10_decomposed(self) -> None:
        pass

    def testBaseClear_test9_decomposed(self) -> None:
        pass

    def testBaseClear_test8_decomposed(self) -> None:
        pass

    def testBaseClear_test7_decomposed(self) -> None:
        pass

    def testBaseClear_test6_decomposed(self) -> None:
        pass

    def testBaseClear_test5_decomposed(self) -> None:
        pass

    def testBaseClear_test4_decomposed(self) -> None:
        pass

    def testBaseClear_test3_decomposed(self) -> None:
        pass

    def testBaseClear_test2_decomposed(self) -> None:
        pass

    def testBaseClear_test1_decomposed(self) -> None:
        pass

    def testBaseClear_test0_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test20_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test19_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test18_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test17_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test16_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test15_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test14_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test13_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test12_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test11_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test10_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test9_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test8_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test7_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test6_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test5_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test4_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test3_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test2_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test1_decomposed(self) -> None:
        pass

    def testBaseBorrowReturn_test0_decomposed(self) -> None:
        pass

    def testBaseBorrow_test7_decomposed(self) -> None:
        pass

    def testBaseBorrow_test6_decomposed(self) -> None:
        pass

    def testBaseBorrow_test5_decomposed(self) -> None:
        pass

    def testBaseBorrow_test4_decomposed(self) -> None:
        pass

    def testBaseBorrow_test3_decomposed(self) -> None:
        pass

    def testBaseBorrow_test2_decomposed(self) -> None:
        pass

    def testBaseBorrow_test1_decomposed(self) -> None:
        pass

    def testBaseBorrow_test0_decomposed(self) -> None:
        pass

    def testBaseAddObject_test1_decomposed(self) -> None:
        pass

    def testBaseAddObject_test0_decomposed(self) -> None:
        pass

    def _makeEmptyPool(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        pass

    def _makeEmptyPool1(
        self, factory: PooledObjectFactory[typing.Any]
    ) -> ObjectPool[object]:
        pass

    def _makeEmptyPool0(self, minCapacity: int) -> ObjectPool[str]:
        pass

    def _isLifo(self) -> bool:
        pass

    def _isFifo(self) -> bool:
        pass

    def _getNthObject(self, n: int) -> typing.Any:
        pass

    # Class Methods End
