from __future__ import annotations
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class TestObject(ABC):

    def setData(self, data: str) -> None:

        pass

    def getData(self) -> str:

        pass


class TestObjectImpl(TestObject):

    __data: str = None

    def setData(self, data: str) -> None:

        self.__data = data

    def getData(self) -> str:

        return self.__data


class BaseTestProxiedObjectPool(ABC):

    __log: io.StringIO = None
    __pool: typing.List[TestObject] = None

    __ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)

    __DATA1: str = "data1"

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

        with self.assertRaises(IllegalStateException):
            self.__pool.addObject()

    def testPassThroughMethods01(self) -> None:

        assert 0 == self.__pool.getNumActive()
        assert 0 == self.__pool.getNumIdle()

        self.__pool.addObject()

        assert 0 == self.__pool.getNumActive()
        assert 1 == self.__pool.getNumIdle()

        self.__pool.clear()

        assert 0 == self.__pool.getNumActive()
        assert 0 == self.__pool.getNumIdle()

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

        try:
            obj.getData()
            assert False, "Expected IllegalStateException"
        except IllegalStateException:
            pass

    def testAccessAfterInvalidate(self) -> None:

        obj = self.__pool.borrowObject()
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.invalidateObject0(obj)

        assert obj is not None

        try:
            obj.getData()
            assert False, "Expected IllegalStateException"
        except IllegalStateException:
            pass

    def _getproxySource(self) -> ProxySource[TestObject]:

        pass
