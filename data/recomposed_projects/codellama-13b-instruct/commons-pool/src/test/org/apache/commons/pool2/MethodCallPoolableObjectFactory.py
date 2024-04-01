# Imports Begin
from src.main.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.MethodCall import *
import unittest
import typing
from typing import *

# Imports End


class MethodCallPoolableObjectFactory(unittest.TestCase):

    # Class Fields Begin
    __methodCalls: typing.List[MethodCall] = ""  # LLM could not translate field
    __count: int = None
    __valid: bool = ""  # LLM could not translate field
    __makeObjectFail: bool = None
    __activateObjectFail: bool = None
    __validateObjectFail: bool = None
    __passivateObjectFail: bool = None
    __destroyObjectFail: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, obj: PooledObject[typing.Any]) -> bool:

        call = MethodCall.MethodCall1("validateObject", obj.getObject())
        self.__methodCalls.add(call)
        if self.__validateObjectFail:
            raise PrivateException("validateObject")
        r = self.__valid
        call.returned(Boolean.valueOf(r))
        return r

    def setValidateObjectFail(self, validateObjectFail: bool) -> None:

        self.validateObjectFail = validateObjectFail

    def setValid(self, valid: bool) -> None:

        self.__valid = valid

    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:

        pass  # LLM could not translate method body

    def setMakeObjectFail(self, makeObjectFail: bool) -> None:

        self.__makeObjectFail = makeObjectFail

    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:

        self.destroyObjectFail = destroyObjectFail

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

        pass  # LLM could not translate method body

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

        self.__methodCalls.add(MethodCall.MethodCall1("destroyObject", obj.getObject()))
        if self.__destroyObjectFail:
            raise PrivateException("destroyObject")

    def activateObject(self, obj: PooledObject[typing.Any]) -> None:

        self.__methodCalls.append(self.MethodCall1("activateObject", obj.getObject()))
        if self.__activateObjectFail:
            raise PrivateException("activateObject")

    # Class Methods End
