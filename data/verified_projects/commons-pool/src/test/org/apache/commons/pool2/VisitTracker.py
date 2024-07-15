import pytest

import typing

K = typing.TypeVar('K')

class VisitTracker(typing.Generic[K]):

    def __init__(self, constructorId: int, key: K, id: int) -> None:
        self.__validateCount = 0
        self.__activateCount = 0
        self.__passivateCount = 0
        self.__destroyed = False
        self.__id = 0
        self.__key = None

        if constructorId == 0:
            self.__id = id
            self.__key = key
            self.reset()
        elif constructorId == 1:
            self.__id = id
            self.reset()
        else:
            self.reset()

    
    def activate(self) -> None:
        if self.__destroyed:
            self.__fail("attempted to activate a destroyed object")
        self.__activateCount += 1

    
    def destroy(self) -> None:
        self.__destroyed = True

    
    def __fail(self, message: str) -> None:
        raise RuntimeError(message)

    
    def getActivateCount(self) -> int:
        return self.__activateCount

    
    def getId(self) -> int:
        return self.__id

    
    def getKey(self) -> K:
        return self.__key

    
    def getPassivateCount(self) -> int:
        return self.__passivateCount

    
    def getValidateCount(self) -> int:
        return self.__validateCount

    
    def isDestroyed(self) -> bool:
        return self.__destroyed

    
    def passivate(self) -> None:
        if self.__destroyed:
            self.__fail("attempted to passivate a destroyed object")
        self.__passivateCount += 1

    
    def reset(self) -> None:
        self.__validateCount = 0
        self.__activateCount = 0
        self.__passivateCount = 0
        self.__destroyed = False

    
    def toString(self) -> str:
        return "Key: " + str(self.__key) + " id: " + id

    
    def validate(self) -> bool:
        if self.__destroyed:
            self.__fail("attempted to validate a destroyed object")
        self.__validateCount += 1
        return True
