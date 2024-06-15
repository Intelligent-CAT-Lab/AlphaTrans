import pytest

from typing import List, Any

class MethodCall:

    def __init__(
            self,
            constructorId: int,
            param2: Any,
            params: List[Any],
            param1: Any,
            name: str,
            param: Any
        ) -> None:

        if constructorId == 2:

            if name is None:
                raise ValueError("name must not be null.")
            self.__name = name
            if params is not None:
                self.__params = params
            else:
                self.__params = []
        
        else:

            if name is None:
                raise ValueError("name must not be null.")
            self.__name = name
            if params is not None:
                self.__params = params
            else:
                self.__params = []
        
        self.__returned = None


    @staticmethod
    def MethodCall0(name: str, param1: Any, param2: Any) -> 'MethodCall':
        return MethodCall(2, None, [param1, param2], None, name, None)

    
    @staticmethod
    def MethodCall1(name: str, param: Any) -> 'MethodCall':
        return MethodCall(2, None, [param], None, name, None)

    
    @staticmethod
    def MethodCall3(name: str) -> 'MethodCall':
        return MethodCall(2, None, None, None, name, None)

    
    def equals(self, o: Any) -> bool:
        if self is o:
            return True
        if o is None or self.__class__ != o.__class__:
            return False
        
        that = o

        return (self.__name == that.__name and
                self.__params == that.__params and
                self.__returned == that.__returned)

    
    def getName(self) -> str:
        return self.__name

    
    def getParams(self) -> List[Any]:
        return self.__params

    
    def getReturned(self) -> Any:
        return self.__returned

    
    def hashCode(self) -> int:
        result = None
        result = hash(self.__name) if self.__name is not None else 0
        result = 29 * result +\
            (hash(tuple(self.__params)) if self.__params is not None else 0)
        result = 29 * result +\
            (hash(self.__returned) if self.__returned is not None else 0)
        return result

    
    def returned(self, obj: Any) -> 'MethodCall':
        self.setReturned(obj)
        return self

    
    def setReturned(self, returned: Any) -> None:
        self.__returned = returned

    
    def toString(self) -> str:
        sb = []
        sb.append("MethodCall")
        sb.append(f"{{name='{self.__name}'")
        if self.__params:
            sb.append(f", params={self.__params}")
        if self.__returned is not None:
            sb.append(f", returned={self.__returned}")
        sb.append('}')
        return ''.join(sb)
