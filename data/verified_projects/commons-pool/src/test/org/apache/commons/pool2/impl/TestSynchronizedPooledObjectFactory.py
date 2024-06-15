from threading import Lock
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *

class TestSynchronizedPooledObjectFactory(PooledObjectFactory):

    def __init__(self, factory):
        try:
            if factory is None:
                raise ValueError("factory must not be null.")
            self.__writelock = Lock()
            self.__factory = factory
        except ValueError as e:
            raise e

    
    def activateObject(self, p) -> None:
        try:
            with self.__writelock:
                self.__factory.activateObject(p)
        except Exception as e:
            raise e

    
    def destroyObject0(self, p) -> None:
        try:
            with self.__writelock:
                self.__factory.destroyObject0(p)
        except Exception as e:
            raise e

    
    def makeObject(self) -> PooledObject:
        try:
            with self.__writelock:
                return self.__factory.makeObject()
        except Exception as e:
            raise e

    
    def passivateObject(self, p) -> None:
        try:
            with self.__writelock:
                self.__factory.passivateObject(p)
        except Exception as e:
            raise e

    
    def toString(self) -> str:
        return f"SynchronizedPoolableObjectFactory{{factory={self.__factory}}}"
    
    
    def validateObject(self, p) -> bool:
        with self.__writelock:
            return self.__factory.validateObject(p)
