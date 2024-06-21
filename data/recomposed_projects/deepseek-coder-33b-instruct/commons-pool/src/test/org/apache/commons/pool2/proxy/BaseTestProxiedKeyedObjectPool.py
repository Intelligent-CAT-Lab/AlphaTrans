from __future__ import annotations
from abc import ABC
from io import StringIO
import io
import datetime
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class TestObject(ABC):

    def setData(self, data: str) -> None:

        # Your code here
        pass

    def getData(self) -> str:

        # Your code here
        pass


class TestObjectImpl(TestObject):

    __data: str = None

    def setData(self, data: str) -> None:

        self.__data = data

    def getData(self) -> str:

        return self.__data


class BaseTestProxiedKeyedObjectPool(ABC):

    __log: io.StringIO = None
    __pool: KeyedObjectPool[str, TestObject] = None

    __ABANDONED_TIMEOUT_SECS: datetime.timedelta = datetime.timedelta(seconds=3)

    __DATA1: str = "data1"

    __KEY1: str = "key1"

    def testUsageTracking(self) -> None:

        obj = self.__pool.borrowObject(self.__KEY1)
        assert obj is not None

        obj.setData(self.__DATA1)

        time.sleep(
            (
                self.__ABANDONED_TIMEOUT_SECS + datetime.timedelta(seconds=2)
            ).total_seconds()
        )

        self.__pool.borrowObject(self.__KEY1)

        logOutput = self.__log.getvalue()

        assert "Pooled object created" in logOutput
        assert "The last code to use this object was" in logOutput

    def testPassThroughMethods02(self) -> None:

        self.__pool.close()

        with self.assertRaises(IllegalStateException):
            self.__pool.addObject(self.__KEY1)

    def testPassThroughMethods01(self) -> None:

        assert self.__pool.getNumActive0() == 0
        assert self.__pool.getNumIdle0() == 0

        self.__pool.addObject(self.__KEY1)

        assert self.__pool.getNumActive0() == 0
        assert self.__pool.getNumIdle0() == 1

        self.__pool.clear0()

        assert self.__pool.getNumActive0() == 0
        assert self.__pool.getNumIdle0() == 0

    def testBorrowObject(self) -> None:

        obj = self.__pool.borrowObject(self.__KEY1)
        assert obj is not None

        obj.setData(self.__DATA1)
        assert self.__DATA1 == obj.getData()

        self.__pool.returnObject(self.__KEY1, obj)

    def testAccessAfterReturn(self) -> None:

        obj = self.__pool.borrowObject(self.__KEY1)
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.returnObject(self.__KEY1, obj)

        assert obj is not None
        try:
            obj.getData()
            assert False
        except IllegalStateException:
            assert True

    def testAccessAfterInvalidate(self) -> None:

        obj = self.__pool.borrowObject(self.__KEY1)
        assert obj is not None

        obj.setData(self.__DATA1)
        assert obj.getData() == self.__DATA1

        self.__pool.invalidateObject0(self.__KEY1, obj)

        assert obj is not None

        try:
            obj.getData()
            assert False, "Expected IllegalStateException"
        except IllegalStateException:
            pass

    def _getproxySource(self) -> ProxySource[TestObject]:

        pass
