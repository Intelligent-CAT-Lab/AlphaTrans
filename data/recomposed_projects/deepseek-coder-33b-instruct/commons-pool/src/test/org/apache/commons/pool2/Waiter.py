from __future__ import annotations
import io
import typing
from typing import *


class Waiter:

    __id: int = None  # LLM could not translate this field
    __validationCount: int = None
    __passivationCount: int = None
    __lastIdleTimeMillis: int = None
    __lastPassivatedMillis: int = None
    __latency: int = None
    __valid: bool = None
    __active: bool = None

    __instanceCount: int = 0

    def toString(self) -> str:

        buff = io.StringIO()
        buff.write("ID = " + str(self.__id) + "\n")
        buff.write("valid = " + str(self.__valid) + "\n")
        buff.write("active = " + str(self.__active) + "\n")
        buff.write("lastPassivated = " + str(self.__lastPassivatedMillis) + "\n")
        buff.write("lastIdleTimeMs = " + str(self.__lastIdleTimeMillis) + "\n")
        buff.write("latency = " + str(self.__latency) + "\n")
        return buff.getvalue()

    def hashCode(self) -> int:

        return self.__id

    def equals(self, obj: typing.Any) -> bool:

        if not isinstance(obj, Waiter):
            return False
        return hash(obj) == self.__id

    @staticmethod
    def sleepQuietly(millis: int) -> None:

        try:
            time.sleep(millis / 1000)
        except InterruptedError:
            pass

    def setValid(self, valid: bool) -> None:

        self.__valid = valid

    def setLatency(self, latency: int) -> None:

        self.__latency = latency

    def setActive(self, active: bool) -> None:

        activeState = self.__active
        if activeState == active:
            return
        self.__active = active
        currentTimeMillis = int(time.time() * 1000)
        if active:  # activating
            self.__lastIdleTimeMillis = currentTimeMillis - self.__lastPassivatedMillis
        else:  # passivating
            self.__lastPassivatedMillis = currentTimeMillis
            self.__passivationCount += 1

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
