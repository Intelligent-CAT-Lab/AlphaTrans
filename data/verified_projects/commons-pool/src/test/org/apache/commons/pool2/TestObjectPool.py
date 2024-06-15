import pytest

from abc import ABC, abstractmethod
from src.test.org.apache.commons.pool2.MethodCallPoolableObjectFactory import *
from src.test.org.apache.commons.pool2.MethodCall import *
import unittest

class TestObjectPool(unittest.TestCase, ABC):

    _ZERO = 0
    _ONE = 1

    
    @classmethod
    def setUpClass(cls):
        if cls == TestObjectPool:
            "Tests shall only be executed in child classes"
            raise unittest.SkipTest
    

    def __init__(self, methodName='runTest') -> None:
        self.setUpClass()
        super().__init__(methodName)

    
    @staticmethod
    def __clear(factory, expectedMethods) -> None:
        factory.getMethodCalls().clear()
        expectedMethods.clear()

    
    @staticmethod
    def removeDestroyObjectCall(calls) -> None:
        i = 0
        while i < len(calls):
            if calls[i].getName() == "destroyObject":
                del calls[i]
            else:
                i += 1

    
    @staticmethod
    def __reset(pool, factory, expectedMethods) -> None:
        pool.clear()
        TestObjectPool.__clear(factory, expectedMethods)
        factory.reset()

    
    @abstractmethod
    def makeEmptyPool(self, factory) -> Any:
        pass
