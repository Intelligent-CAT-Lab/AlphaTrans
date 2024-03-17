# Imports Begin
import unittest
import typing
from typing import *

# Imports End


class Waiter(unittest.TestCase):

    # Class Fields Begin
    __instanceCount: int = 0
    __active: bool = None
    __valid: bool = None
    __latency: int = None
    __lastPassivatedMillis: int = None
    __lastIdleTimeMillis: int = None
    __passivationCount: int = None
    __validationCount: int = None
    __id: int = instanceCount.getAndIncrement()
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:

        buff = StringBuilder()
        buff.append("ID = " + self.__id + "\n")
        buff.append("valid = " + self.__valid + "\n")
        buff.append("active = " + self.__active + "\n")
        buff.append("lastPassivated = " + self.__lastPassivatedMillis + "\n")
        buff.append("lastIdleTimeMs = " + self.__lastIdleTimeMillis + "\n")
        buff.append("latency = " + self.__latency + "\n")
        return buff.toString()

    def hashCode(self) -> int:

        return self.__id

    def equals(self, obj: typing.Any) -> bool:

        if not isinstance(obj, Waiter):
            return False
        return obj.hashCode() == self.__id

    @staticmethod
    def sleepQuietly(millis: int) -> None:

        pass  # LLM could not translate method body

    def setValid(self, valid: bool) -> None:

        self.__valid = valid

    def setLatency(self, latency: int) -> None:

        self.__latency = latency

    def setActive(self, active: bool) -> None:

        activeState = self.active
        if activeState == active:
            return
        self.active = active
        currentTimeMillis = int(round(time.time() * 1000))
        if active:  # activating
            self.lastIdleTimeMillis = currentTimeMillis - self.lastPassivatedMillis
        else:  # passivating
            self.lastPassivatedMillis = currentTimeMillis
            self.passivationCount += 1

    def isValid(self) -> bool:

        self.__validationCount += 1
        return self.__valid

    def isActive(self) -> bool:

        return self.__active

    def getValidationCount(self) -> int:

        return self.__validationCount

    def getPassivationCount(self) -> int:

        return self.__passivationCount

    def getLatency(self) -> int:

        return self.__latency

    def getLastPassivatedMillis(self) -> int:

        return self.__lastPassivatedMillis

    def getLastIdleTimeMillis(self) -> int:

        return self.__lastIdleTimeMillis

    def doWait(self) -> None:

        self.sleepQuietly(self.__latency)

    def __init__(self, active: bool, valid: bool, latency: int) -> None:

        self.__active = active
        self.__valid = valid
        self.__latency = latency
        self.__lastPassivatedMillis = int(round(time.time() * 1000))

    # Class Methods End
