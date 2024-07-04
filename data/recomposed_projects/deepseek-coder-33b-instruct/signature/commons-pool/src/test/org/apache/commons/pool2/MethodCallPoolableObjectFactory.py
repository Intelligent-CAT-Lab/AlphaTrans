from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.pool2.MethodCall import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.PrivateException import *


class MethodCallPoolableObjectFactory:

    __destroyObjectFail: bool = False

    __passivateObjectFail: bool = False

    __validateObjectFail: bool = False

    __activateObjectFail: bool = False

    __makeObjectFail: bool = False

    __valid: bool = True
    __count: int = 0

    __methodCalls: typing.List[MethodCall] = []

    def validateObject(self, obj: PooledObject[typing.Any]) -> bool:

        call = MethodCall.MethodCall1("validateObject", obj.getObject())
        self.__methodCalls.append(call)

        if self.__validateObjectFail:
            raise PrivateException("validateObject")

        r = self.__valid
        call.returned(bool(r))

        return r

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        self.__validateObjectFail = validateObjectFail

    def setValid(self, valid: bool) -> None:
        self.__valid = valid

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        self.__passivateObjectFail = passivateObjectFail

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        self.__makeObjectFail = makeObjectFail

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        self.__destroyObjectFail = destroyObjectFail

    def setCurrentCount(self, count: int) -> None:
        self.__count = count

    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        self.__activateObjectFail = activateObjectFail

    def reset(self) -> None:

        self.__count = 0
        self.getMethodCalls().clear()
        self.setMakeObjectFail(False)
        self.setActivateObjectFail(False)
        self.setValid(True)
        self.setValidateObjectFail(False)
        self.setPassivateObjectFail(False)
        self.setDestroyObjectFail(False)

    def passivateObject(self, obj: PooledObject[typing.Any]) -> None:

        self.__methodCalls.append(
            MethodCall.MethodCall1("passivateObject", obj.getObject())
        )
        if self.__passivateObjectFail:
            raise PrivateException("passivateObject")

    def isValidateObjectFail(self) -> bool:
        return self.__validateObjectFail

    def isValid(self) -> bool:
        return self.__valid

    def isPassivateObjectFail(self) -> bool:
        return self.__passivateObjectFail

    def isMakeObjectFail(self) -> bool:
        return self.__makeObjectFail

    def isDestroyObjectFail(self) -> bool:
        return self.__destroyObjectFail

    def isActivateObjectFail(self) -> bool:
        return self.__activateObjectFail

    def getMethodCalls(self) -> typing.List[MethodCall]:
        return self.__methodCalls

    def getCurrentCount(self) -> int:
        return self.__count

    def destroyObject(self, obj: PooledObject[typing.Any]) -> None:

        self.__methodCalls.append(
            MethodCall.MethodCall1("destroyObject", obj.getObject())
        )
        if self.__destroyObjectFail:
            raise PrivateException("destroyObject")

    def activateObject(self, obj: PooledObject[typing.Any]) -> None:

        self.__methodCalls.append(
            MethodCall.MethodCall1("activateObject", obj.getObject())
        )
        if self.__activateObjectFail:
            raise PrivateException("activateObject")
