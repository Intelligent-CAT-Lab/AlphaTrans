from __future__ import annotations
import time
import re
import os
import unittest
import pytest
from abc import ABC
from io import StringIO
import io
import datetime
import unittest
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class TestObject(ABC):

    def setData(self, data: str) -> None:
        self.data = data

    def getData(self) -> str:
        return "test"


class TestObjectImpl(TestObject):

    __data: str = ""

    def setData(self, data: str) -> None:
        self.__data = data

    def getData(self) -> str:
        return self.__data


class BaseTestProxiedKeyedObjectPool(ABC, unittest.TestCase):

    __log: io.StringIO = None

    __pool: KeyedObjectPool[str, TestObject] = None

    ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)
    __DATA1: str = "data1"
    __KEY1: str = "key1"

    def testUsageTracking(self) -> None:
        obj = self.pool.borrowObject(self.KEY1)
        self.assertIsNotNone(obj)

        obj.setData(self.DATA1)

        time.sleep(self.ABANDONED_TIMEOUT_SECS.total_seconds() + 2)

        self.pool.borrowObject(self.KEY1)

        logOutput = self.log.getbuffer().decode()

        self.assertTrue(logOutput.contains("Pooled object created"))
        self.assertTrue(logOutput.contains("The last code to use this object was"))

    def testPassThroughMethods02(self) -> None:
        self.__pool.close()
        with self.assertRaises(RuntimeError):
            self.__pool.addObject(self.__KEY1)

    def testPassThroughMethods01(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

        self.__pool.addObject(self.__KEY1)

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(1, self.__pool.getNumIdle0())

        self.__pool.clear0()

        self.assertEqual(0, self.__pool.getNumActive0())
        self.assertEqual(0, self.__pool.getNumIdle0())

    def testBorrowObject(self) -> None:
        obj = self.pool.borrowObject(self.KEY1)
        self.assertIsNotNone(obj)

        obj.setData(self.DATA1)
        self.assertEqual(self.DATA1, obj.getData())

        self.pool.returnObject(self.KEY1, obj)

    def testAccessAfterReturn(self) -> None:
        obj = self.pool.borrowObject(self.KEY1)
        self.assertIsNotNone(obj)

        obj.setData(self.DATA1)
        self.assertEqual(self.DATA1, obj.getData())

        self.pool.returnObject(self.KEY1, obj)

        self.assertIsNotNone(obj)
        with self.assertRaises(RuntimeError):
            obj.getData()

    def testAccessAfterInvalidate(self) -> None:
        obj = self.pool.borrowObject(self.KEY1)
        self.assertIsNotNone(obj)

        obj.setData(self.DATA1)
        self.assertEqual(self.DATA1, obj.getData())

        self.pool.invalidateObject0(self.KEY1, obj)

        self.assertIsNotNone(obj)

        with self.assertRaises(RuntimeError):
            obj.getData()

    def _getproxySource(self) -> ProxySource[TestObject]:
        return ProxySource(TestObjectImpl)
