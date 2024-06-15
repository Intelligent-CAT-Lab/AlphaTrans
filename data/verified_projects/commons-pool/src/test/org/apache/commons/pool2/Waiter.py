import time
import asyncio
from typing import Any
from itertools import count

class Waiter:

    __instanceCount = count()

    
    def __init__(self, active: bool, valid: bool, latency: int) -> None:
        self.__active = active
        self.__valid = valid
        self.__latency = latency
        self.__lastPassivatedMillis = int(time.time() * 1000)
        self.__lastIdleTimeMillis = 0
        self.__passivationCount = 0
        self.__validationCount = 0
        self.__id = next(Waiter.__instanceCount)

    
    def doWait(self) -> None:
        Waiter.sleepQuietly(self.__latency)

    
    def equals(self, obj: Any) -> bool:
        if not isinstance(obj, Waiter):
            return False
        return obj.hashCode() == self.__id

    
    def getLastIdleTimeMillis(self) -> int:
        return self.__lastIdleTimeMillis

    
    def getLastPassivatedMillis(self) -> int:
        return self.__lastPassivatedMillis

    
    def getLatency(self) -> int:
        return self.__latency

    
    def getPassivationCount(self) -> int:
        return self.__passivationCount

    
    def getValidationCount(self) -> int:
        return self.__validationCount

    
    def hashCode(self) -> int:
        return self.__id

    
    def isActive(self) -> bool:
        return self.__active

    
    def isValid(self) -> bool:
        self.__validationCount += 1
        return self.__valid

    
    def setActive(self, active: bool) -> None:
        activeState = self.__active
        if activeState == active:
            return
        self.__active = active
        currentTimeMillis = int(time.time() * 1000)
        if active:
            self.__lastIdleTimeMillis = currentTimeMillis - self.__lastPassivatedMillis
        else:
            self.__lastPassivatedMillis = currentTimeMillis
            self.__passivationCount += 1

    
    def setLatency(self, latency: int) -> None:
        self.__latency = latency

    
    def setValid(self, valid: bool) -> None:
        self.__valid = valid

    
    def toString(self) -> str:
        buff = []
        buff.append("ID = " + str(self.__id) + '\n')
        buff.append("valid = " + str(self.__valid) + '\n')
        buff.append("active = " + str(self.__active) + '\n')
        buff.append("lastPassivated = " + str(self.__lastPassivatedMillis) + '\n')
        buff.append("lastIdleTimeMs = " + str(self.__lastIdleTimeMillis) + '\n')
        buff.append("latency = " + str(self.__latency) + '\n')
        return ''.join(buff)

    
    @staticmethod
    def sleepQuietly(millis: int) -> None:
        try:
            time.sleep(millis / 1000)
        except (InterruptedError, KeyboardInterrupt, asyncio.CancelledError, BlockingIOError):
            pass
