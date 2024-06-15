import typing
from src.test.org.apache.commons.pool2.VisitTracker import *
from src.main.org.apache.commons.pool2.PooledObject import *

K = typing.TypeVar('K')

class VisitTrackerFactory(typing.Generic[K]):

    def __init__(self) -> None:
        self.__nextId = 0

    
    def activateObject0(self, key: K, ref: PooledObject) -> None:
        try:
            ref.getObject().activate()
        except Exception as e:
            raise e

    
    def activateObject1(self, ref: PooledObject) -> None:
        try:
            ref.getObject().activate()
        except Exception as e:
            raise e

    
    def destroyObject0(self, key: K, ref: PooledObject) -> None:
        ref.getObject().destroy()

    
    def destroyObject1(self, ref: PooledObject) -> None:
        ref.getObject().destroy()

    
    def passivateObject0(self, key: K, ref: PooledObject) -> None:
        try:
            ref.getObject().passivate()
        except Exception as e:
            raise e

    
    def passivateObject1(self, ref: PooledObject) -> None:
        try:
            ref.getObject().passivate()
        except Exception as e:
            raise e

    
    def resetId(self) -> None:
        self.__nextId = 0

    
    def validateObject0(self, key: K, ref: PooledObject) -> bool:
        return ref.getObject().validate()

    
    def validateObject1(self, ref: PooledObject) -> bool:
        return ref.getObject().validate()
