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
        pass

    def getData(self) -> str:
        pass


class TestObjectImpl(TestObject):

    __data: str = ""

    def setData(self, data: str) -> None:
        self.__data = data

    def getData(self) -> str:
        return self.__data


class BaseTestProxiedObjectPool(ABC, unittest.TestCase):

    __log: io.StringIO = None

    __pool: typing.List[TestObject] = None
    __ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)
    __DATA1: str = "data1"

    @staticmethod
    def initialize_fields() -> None:
        BaseTestProxiedObjectPool.__pool: typing.List[TestObject] = None

    def testUsageTracking(self) -> None:

        obj = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)

        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )

        self.__pool.borrowObject()

        logOutput = self.__log.getvalue()

        assert "Pooled object created" in logOutput
        assert "The last code to use this object was" in logOutput

    def testPassThroughMethods02(self) -> None:

        self.__pool.close()

        with pytest.raises(RuntimeError):
            self.__pool.addObject()

    def testPassThroughMethods01(self) -> None:

        self.assertEqual(0, len(self.__pool))
        self.assertEqual(0, len([obj for obj in self.__pool if obj.isActive()]))

        self.__pool.append(TestObject())

        self.assertEqual(0, len(self.__pool))
        self.assertEqual(1, len([obj for obj in self.__pool if not obj.isActive()]))

        self.__pool.clear()

        self.assertEqual(0, len(self.__pool))
        self.assertEqual(0, len([obj for obj in self.__pool if obj.isActive()]))

    def testBorrowObject(self) -> None:

        obj = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert self.__DATA1 == obj.getData()

        self.__pool.returnObject(obj)

    def testAccessAfterReturn(self) -> None:

        obj = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.returnObject(obj)

        assert obj is not None

        with pytest.raises(RuntimeError):
            obj.getData()

    def testAccessAfterInvalidate(self) -> None:

        obj = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.invalidateObject0(obj)

        assert obj is not None

        with pytest.raises(RuntimeError):
            obj.getData()

    def _getproxySource(self) -> ProxySource[TestObject]:
        pass


BaseTestProxiedObjectPool.initialize_fields()
