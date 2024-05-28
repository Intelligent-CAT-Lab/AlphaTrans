from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Var:

    # Class Fields Begin
    __serialVersionUID: int = None
    JSTYPE_INT: str = None
    JSTYPE_STRING: str = None
    JSTYPE_REGEXP: str = None
    __name: str = None
    __value: str = None
    __jsType: str = None
    __resource: bool = None
    __bundle: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def clone(self) -> typing.Any:
        pass

    def setJsType(self, jsType: str) -> None:
        pass

    def getJsType(self) -> str:
        pass

    def setBundle(self, bundle: str) -> None:
        pass

    def getBundle(self) -> str:
        pass

    def setResource(self, resource: bool) -> None:
        pass

    def isResource(self) -> bool:
        pass

    def setValue(self, value: str) -> None:
        pass

    def getValue(self) -> str:
        pass

    def setName(self, name: str) -> None:
        pass

    def getName(self) -> str:
        pass

    def __init__(self, constructorId: int, name: str, value: str, jsType: str) -> None:
        pass

    # Class Methods End
