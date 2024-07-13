from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.util.ValidatorUtils import *
from src.main.org.apache.commons.validator.ValidatorException import *
from src.main.org.apache.commons.validator.Arg import *
import os
import typing
from typing import *
import io

# Imports End


class Field:

    # Class Fields Begin
    _args: typing.List[typing.Dict[str, Arg]] = None
    __serialVersionUID: int = None
    __DEFAULT_ARG: str = None
    TOKEN_INDEXED: str = None
    _TOKEN_START: str = None
    _TOKEN_END: str = None
    _TOKEN_VAR: str = None
    _property: str = None
    _indexedProperty: str = None
    _indexedListProperty: str = None
    _key: str = None
    _depends: str = None
    _page: int = None
    _clientValidation: bool = None
    _fieldOrder: int = None
    __dependencyList: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def getDependencyList(self) -> typing.List[str]:
        pass

    def isDependency(self, validatorName: str) -> bool:
        pass

    def generateKey(self) -> None:
        pass

    def isIndexed(self) -> bool:
        pass

    def setKey(self, key: str) -> None:
        pass

    def getKey(self) -> str:
        pass

    def getArgs(self, key: str) -> typing.List[Arg]:
        pass

    def getArg1(self, key: str, position: int) -> Arg:
        pass

    def getArg0(self, position: int) -> Arg:
        pass

    def addArg(self, arg: Arg) -> None:
        pass

    def setClientValidation(self, clientValidation: bool) -> None:
        pass

    def isClientValidation(self) -> bool:
        pass

    def setDepends(self, depends: str) -> None:
        pass

    def getDepends(self) -> str:
        pass

    def setIndexedListProperty(self, indexedListProperty: str) -> None:
        pass

    def getIndexedListProperty(self) -> str:
        pass

    def setIndexedProperty(self, indexedProperty: str) -> None:
        pass

    def getIndexedProperty(self) -> str:
        pass

    def setProperty(self, property_: str) -> None:
        pass

    def getProperty(self) -> str:
        pass

    def setFieldOrder(self, fieldOrder: int) -> None:
        pass

    def getFieldOrder(self) -> int:
        pass

    def setPage(self, page: int) -> None:
        pass

    def getPage(self) -> int:
        pass

    def __handleMissingAction(self, name: str) -> None:
        pass

    def __processArg(self, key: str, replaceValue: str) -> None:
        pass

    def __ensureArgsCapacity(self, arg: Arg) -> None:
        pass

    def __determineArgPosition(self, arg: Arg) -> None:
        pass

    # Class Methods End
