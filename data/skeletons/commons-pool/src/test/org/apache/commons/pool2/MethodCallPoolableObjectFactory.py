from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.MethodCall import *
import typing
from typing import *
import io

# Imports End


class MethodCallPoolableObjectFactory:

    # Class Fields Begin
    __methodCalls: typing.List[MethodCall] = None
    __count: int = None
    __valid: bool = None
    __makeObjectFail: bool = None
    __activateObjectFail: bool = None
    __validateObjectFail: bool = None
    __passivateObjectFail: bool = None
    __destroyObjectFail: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, obj: PooledObject[typing.Any]) -> bool:
        pass

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        pass

    def setValid(self, valid: bool) -> None:
        pass

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        pass

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        pass

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        pass

    def setCurrentCount(self, count: int) -> None:
        pass

    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        pass

    def reset(self) -> None:
        pass

    def passivateObject(self, obj: PooledObject[typing.Any]) -> None:
        pass

    def isValidateObjectFail(self) -> bool:
        pass

    def isValid(self) -> bool:
        pass

    def isPassivateObjectFail(self) -> bool:
        pass

    def isMakeObjectFail(self) -> bool:
        pass

    def isDestroyObjectFail(self) -> bool:
        pass

    def isActivateObjectFail(self) -> bool:
        pass

    def getMethodCalls(self) -> typing.List[MethodCall]:
        pass

    def getCurrentCount(self) -> int:
        pass

    def destroyObject(self, obj: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, obj: PooledObject[typing.Any]) -> None:
        pass

    # Class Methods End
