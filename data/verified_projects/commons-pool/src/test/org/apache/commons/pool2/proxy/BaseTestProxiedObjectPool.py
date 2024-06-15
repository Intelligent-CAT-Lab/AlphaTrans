import unittest
from src.main.org.apache.commons.pool2.proxy.ProxySource import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from time import sleep
from datetime import timedelta
from abc import ABC, abstractmethod

class BaseTestProxiedObjectPool(unittest.TestCase, ABC):

    class TestObject(ABC):
        
        @abstractmethod
        def getData(self) -> str:
            pass

        
        @abstractmethod
        def setData(self, data: str) -> None:
            pass

    
    class TestObjectImpl(TestObject):

        def __init__(self):
            self.__data = None
        

        def getData(self) -> str:
            return self.__data


        def setData(self, data: str) -> None:
            self.__data = data

    
    __DATA1 = "data1"
    __ABANDONED_TIMEOUT_SECS = timedelta(seconds=3)


    @classmethod
    def setUpClass(cls):
        if cls == BaseTestProxiedObjectPool:
            "Tests shall only be executed in child classes."
            raise unittest.SkipTest

    
    def __init__(self, methodName='runTest') -> None:
        self.setUpClass()
        super().__init__(methodName)
        self.__pool = None
        self.__log = None

    
    def setUp(self, pool, log) -> None:
        self.__pool = pool
        self.__log = log


    @abstractmethod
    def _getproxySource(self) -> ProxySource[TestObject]:
        pass

    
    def testAccessAfterInvalidate(self) -> None:
        try:
            obj = self.__pool.borrowObject()
            self.assertIsNotNone(obj)

            obj.setData(BaseTestProxiedObjectPool.__DATA1)
            self.assertEqual(BaseTestProxiedObjectPool.__DATA1, obj.getData())

            self.__pool.invalidateObject0(obj)

            self.assertIsNotNone(obj)

            with self.assertRaises(RuntimeError):
                obj.getData()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    def testAccessAfterReturn(self) -> None:
        try:
            obj = self.__pool.borrowObject()
            self.assertIsNotNone(obj)

            obj.setData(BaseTestProxiedObjectPool.__DATA1)
            self.assertEqual(BaseTestProxiedObjectPool.__DATA1, obj.getData())

            self.__pool.returnObject(obj)

            self.assertIsNotNone(obj)
            with self.assertRaises(RuntimeError):
                obj.getData()
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    def testBorrowObject(self) -> None:
        try:
            obj = self.__pool.borrowObject()
            self.assertIsNotNone(obj)

            obj.setData(BaseTestProxiedObjectPool.__DATA1)
            self.assertEqual(BaseTestProxiedObjectPool.__DATA1, obj.getData())

            self.__pool.returnObject(obj)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    def testPassThroughMethods01(self) -> None:
        try:
            self.assertEqual(0, self.__pool.getNumActive())
            self.assertEqual(0, self.__pool.getNumIdle())

            self.__pool.addObject()

            self.assertEqual(0, self.__pool.getNumActive())
            self.assertEqual(1, self.__pool.getNumIdle())

            self.__pool.clear()

            self.assertEqual(0, self.__pool.getNumActive())
            self.assertEqual(0, self.__pool.getNumIdle())
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")

    
    def testPassThroughMethods02(self) -> None:
        self.__pool.close()

        with self.assertRaises(RuntimeError):
            self.__pool.addObject()

    
    def testUsageTracking(self) -> None:
        try:
            obj = self.__pool.borrowObject()
            self.assertIsNotNone(obj)

            obj.setData(BaseTestProxiedObjectPool.__DATA1)

            sleep(BaseTestProxiedObjectPool.__ABANDONED_TIMEOUT_SECS.total_seconds() + 2)

            self.__pool.borrowObject()

            logOutput = self.__log.getvalue()

            self.assertIn("Pooled object created", logOutput)
            self.assertIn("The last code to use this object was", logOutput)
        except Exception as e:
            self.fail(f"An unexpected exception occurred: {e}")
