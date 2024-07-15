from __future__ import annotations
import time
import re
import os
import unittest
import pytest
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
import unittest
from src.main.org.apache.commons.pool2.ObjectPool import *
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


class BaseTestProxiedObjectPool(ABC, unittest.TestCase):

    __log: io.StringIO = None

    __pool: typing.List[TestObject] = None

    ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)
    __DATA1: str = "data1"

    def testUsageTracking(self) -> None:
        obj = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)

        time.sleep(self.__ABANDONED_TIMEOUT_SECS.total_seconds() + 2)

        self.__pool.borrowObject()

        logOutput = self.__log.getvalue()

        assert "Pooled object created" in logOutput
        assert "The last code to use this object was" in logOutput

    def testPassThroughMethods02(self) -> None:
        self.pool.close()

        with self.assertRaises(RuntimeError):
            self.pool.addObject()

    def testPassThroughMethods01(self) -> None:
        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

        self.__pool.addObject()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(1, self.__pool.getNumIdle())

        self.__pool.clear()

        self.assertEqual(0, self.__pool.getNumActive())
        self.assertEqual(0, self.__pool.getNumIdle())

    def testBorrowObject(self) -> None:
        obj: TestObject = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert self.__DATA1 == obj.getData()

        self.__pool.returnObject(obj)

    def testAccessAfterReturn(self) -> None:
        obj: TestObject = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.returnObject(obj)

        assert obj is not None

        with pytest.raises(RuntimeError):
            obj.getData()

    def testAccessAfterInvalidate(self) -> None:
        obj: TestObject = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.invalidateObject0(obj)

        assert obj is not None

        with pytest.raises(RuntimeError):
            obj.getData()

    def _getproxySource(self) -> ProxySource[TestObject]:
        return ProxySource(TestObjectImpl)
