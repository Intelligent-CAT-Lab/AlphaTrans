from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Waiter:

    # Class Fields Begin
    __instanceCount: int = None
    __active: bool = None
    __valid: bool = None
    __latency: int = None
    __lastPassivatedMillis: int = None
    __lastIdleTimeMillis: int = None
    __passivationCount: int = None
    __validationCount: int = None
    __id: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    @staticmethod
    def sleepQuietly(millis: int) -> None:
        pass

    def setValid(self, valid: bool) -> None:
        pass

    def setLatency(self, latency: int) -> None:
        pass

    def setActive(self, active: bool) -> None:
        pass

    def isValid(self) -> bool:
        pass

    def isActive(self) -> bool:
        pass

    def getValidationCount(self) -> int:
        pass

    def getPassivationCount(self) -> int:
        pass

    def getLatency(self) -> int:
        pass

    def getLastPassivatedMillis(self) -> int:
        pass

    def getLastIdleTimeMillis(self) -> int:
        pass

    def doWait(self) -> None:
        pass

    def __init__(self, active: bool, valid: bool, latency: int) -> None:
        pass

    # Class Methods End
