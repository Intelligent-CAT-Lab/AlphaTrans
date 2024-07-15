import pytest

from src.test.org.apache.commons.pool2.PrivateException import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.MethodCall import *

class MethodCallPoolableObjectFactory:

    def __init__(self) -> None:
        self.__methodCalls = []
        self.__count = 0
        self.__valid = True
        self.__makeObjectFail = False
        self.__activateObjectFail = False
        self.__validateObjectFail = False
        self.__passivateObjectFail = False
        self.__destroyObjectFail = False

    
    def activateObject(self, obj: PooledObject) -> None:
        try:
            self.__methodCalls.append(
                MethodCall.MethodCall1("activateObject", obj.getObject())
            )
            if self.__activateObjectFail:
                raise PrivateException("activateObject")
        except Exception as e:
            raise e

    
    def destroyObject(self, obj: PooledObject) -> None:
        try:
            self.__methodCalls.append(MethodCall.MethodCall1("destroyObject", obj.getObject()))
            if self.__destroyObjectFail:
                raise PrivateException("destroyObject")
        except Exception as e:
            raise e

    
    def getCurrentCount(self) -> int:
        return self.__count

    
    def getMethodCalls(self) -> List[MethodCall]:
        return self.__methodCalls

    
    def isActivateObjectFail(self) -> bool:
        return self.__activateObjectFail

    
    def isDestroyObjectFail(self) -> bool:
        return self.__destroyObjectFail

    
    def isMakeObjectFail(self) -> bool:
        return self.__makeObjectFail

    
    def isPassivateObjectFail(self) -> bool:
        return self.__passivateObjectFail

    
    def isValid(self) -> bool:
        return self.__valid

    
    def isValidateObjectFail(self) -> bool:
        return self.__validateObjectFail

    
    def passivateObject(self, obj: PooledObject) -> None:
        try:
            self.__methodCalls.append(
                MethodCall.MethodCall1("passivateObject", obj.getObject())
            )
            if self.__passivateObjectFail:
                raise PrivateException("passivateObject")
        except Exception as e:
            raise e

    
    def reset(self) -> None:
        self.__count = 0
        self.getMethodCalls().clear()
        self.setMakeObjectFail(False)
        self.setActivateObjectFail(False)
        self.setValid(True)
        self.setValidateObjectFail(False)
        self.setPassivateObjectFail(False)
        self.setDestroyObjectFail(False)

    
    def setActivateObjectFail(self, activateObjectFail: bool) -> None:
        self.__activateObjectFail = activateObjectFail

    
    def setCurrentCount(self, count: int) -> None:
        self.__count = count

    
    def setDestroyObjectFail(self, destroyObjectFail: bool) -> None:
        self.__destroyObjectFail = destroyObjectFail

    
    def setMakeObjectFail(self, makeObjectFail: bool) -> None:
        self.__makeObjectFail = makeObjectFail

    
    def setPassivateObjectFail(self, passivateObjectFail: bool) -> None:
        self.__passivateObjectFail = passivateObjectFail

    
    def setValid(self, valid: bool) -> None:
        self.__valid = valid

    
    def setValidateObjectFail(self, validateObjectFail: bool) -> None:
        self.__validateObjectFail = validateObjectFail

    
    def validateObject(self, obj: PooledObject) -> bool:
        call = MethodCall.MethodCall1("validateObject", obj.getObject())
        self.__methodCalls.append(call)
        if self.__validateObjectFail:
            raise PrivateException("validateObject")
        r = self.__valid
        call.returned(bool(r))
        return r

