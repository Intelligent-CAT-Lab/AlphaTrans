from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.MethodCall import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
import unittest
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class FailingKeyedPooledObjectFactory:

    # Class Fields Begin
    __methodCalls: typing.List[MethodCall] = None
    __count: int = None
    __makeObjectFail: bool = None
    __activateObjectFail: bool = None
    __validateObjectFail: bool = None
    __passivateObjectFail: bool = None
    __destroyObjectFail: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> bool:
        pass

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        pass

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        pass

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        pass

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        pass

    def setCurrentCount(self, count: int) -> None:
        pass

    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        pass

    def reset(self) -> None:
        pass

    def passivateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        pass

    def isValidateObjectFail(self) -> bool:
        pass

    def isPassivateObjectFail(self) -> bool:
        pass

    def isMakeObjectFail(self) -> bool:
        pass

    def isDestroyObjectFail(self) -> bool:
        pass

    def isActivateObjectFail(self) -> bool:
        pass

    def getMethodCalls(self) -> typing.List[MethodCall]:
        pass

    def getCurrentCount(self) -> int:
        pass

    def destroyObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, key: typing.Any, obj: PooledObject[typing.Any]) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class TestKeyedObjectPool(ABC, unittest.TestCase):

    # Class Fields Begin
    _KEY: str = None
    __pool: KeyedObjectPool[object, typing.Any] = None
    __ZERO: int = None
    __ONE: int = None
    # Class Fields End

    # Class Methods Begin
    def testBaseNumActiveNumIdle2_test36_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test35_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test34_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test33_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test32_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test31_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test30_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test29_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test28_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test27_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test26_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test25_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test24_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test23_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test22_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test21_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test20_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test19_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test18_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test17_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test16_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test15_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test14_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test13_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test12_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test11_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test10_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test9_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test8_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test7_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test6_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test5_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test4_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test3_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test2_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test1_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle2_test0_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test18_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test17_decomposed(self) -> None:
        pass

    def testBaseNumActiveNumIdle_test16_decomposed(self) -> None:
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

    def testBaseInvalidateObject_test13_decomposed(self) -> None:
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

    def testBaseClear_test15_decomposed(self) -> None:
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

    def testBaseBorrowReturn_test21_decomposed(self) -> None:
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

    def testBaseBorrow_test14_decomposed(self) -> None:
        pass

    def testBaseBorrow_test13_decomposed(self) -> None:
        pass

    def testBaseBorrow_test12_decomposed(self) -> None:
        pass

    def testBaseBorrow_test11_decomposed(self) -> None:
        pass

    def testBaseBorrow_test10_decomposed(self) -> None:
        pass

    def testBaseBorrow_test9_decomposed(self) -> None:
        pass

    def testBaseBorrow_test8_decomposed(self) -> None:
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

    def testBaseAddObject_test2_decomposed(self) -> None:
        pass

    def testBaseAddObject_test1_decomposed(self) -> None:
        pass

    def testBaseAddObject_test0_decomposed(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def __reset(
        self,
        pool: KeyedObjectPool[object, typing.Any],
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pass

    def __clear(
        self,
        factory: FailingKeyedPooledObjectFactory,
        expectedMethods: typing.List[MethodCall],
    ) -> None:
        pass

    def _makeKey(self, n: int) -> typing.Any:
        pass

    def _makeEmptyPool1(
        self, factory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedObjectPool[object, typing.Any]:
        pass

    def _makeEmptyPool0(self, minCapacity: int) -> KeyedObjectPool[object, typing.Any]:
        pass

    def _isLifo(self) -> bool:
        pass

    def _isFifo(self) -> bool:
        pass

    def _getNthObject(self, key: typing.Any, n: int) -> typing.Any:
        pass

    # Class Methods End
