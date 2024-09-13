from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.Arg import *
from src.main.org.apache.commons.validator.ValidatorException import *
from src.main.org.apache.commons.validator.util.ValidatorUtils import *


class Field:

    _TOKEN_VAR: str = "var:"
    _TOKEN_END: str = "}"
    _TOKEN_START: str = "${"
    TOKEN_INDEXED: str = "[]"

    __DEFAULT_ARG: str = None

    def __init__(self) -> None:
        self._args: typing.List[typing.Dict[str, Arg]] = []
        self._fieldOrder: int = 0
        self._clientValidation: bool = True
        self._page: int = 0
        self._depends: str = None
        self._key: str = None
        self._indexedListProperty: str = None
        self._indexedProperty: str = None
        self._property: str = None
        self.__dependencyList: typing.List[str] = []
        self.__serialVersionUID: int = -8502647722530192185

    
    @staticmethod
    def initialize_fields() -> None:
        Field.__DEFAULT_ARG: str = "org.apache.commons.validator.Field.DEFAULT"

    def getDependencyList(self) -> typing.List[str]:
        return typing.cast(typing.List[str], self.__dependencyList)

    def isDependency(self, validatorName: str) -> bool:
        return validatorName in self.__dependencyList

    def generateKey(self) -> None:
        if self.isIndexed():
            self._key = (
                self._indexedListProperty + self.TOKEN_INDEXED + "." + self._property
            )
        else:
            self._key = self._property

    def isIndexed(self) -> bool:
        return (
            self._indexedListProperty is not None and len(self._indexedListProperty) > 0
        )

    def setKey(self, key: str) -> None:
        self._key = key

    def getKey(self) -> str:
        if self._key is None:
            self.generateKey()
        return self._key

    def getArgs(self, key: str) -> typing.List[Arg]:

        argList = [None] * len(self._args)

        for i in range(len(self._args)):
            argList[i] = self.getArg1(key, i)

        return argList

    def getArg1(self, key: str, position: int) -> Arg:

        if (position >= len(self._args)) or (self._args[position] is None):
            return None

        arg = self._args[position].get(key)

        if (arg is None) and (key == self.__DEFAULT_ARG):
            return None

        return self.getArg0(position) if arg is None else arg

    def getArg0(self, position: int) -> Arg:

        return self.getArg1(self.__DEFAULT_ARG, position)

    def addArg(self, arg: Arg) -> None:

        if arg is None or arg.getKey() is None or len(arg.getKey()) == 0:
            return

        self.__determineArgPosition(arg)
        self.__ensureArgsCapacity(arg)

        argMap = self._args[arg.getPosition()]
        if argMap is None:
            argMap = {}
            self._args[arg.getPosition()] = argMap

        if arg.getName() is None:
            argMap[self.__DEFAULT_ARG] = arg
        else:
            argMap[arg.getName()] = arg

    def setClientValidation(self, clientValidation: bool) -> None:
        self._clientValidation = clientValidation

    def isClientValidation(self) -> bool:
        return self._clientValidation

    def setDepends(self, depends: str) -> None:

        self._depends = depends

        self.__dependencyList.clear()

        st = depends.split(",")
        for depend in st:
            depend = depend.strip()

            if depend and len(depend) > 0:
                self.__dependencyList.append(depend)

    def getDepends(self) -> str:
        return self._depends

    def setIndexedListProperty(self, indexedListProperty: str) -> None:
        self._indexedListProperty = indexedListProperty

    def getIndexedListProperty(self) -> str:
        return self._indexedListProperty

    def setIndexedProperty(self, indexedProperty: str) -> None:
        self._indexedProperty = indexedProperty

    def getIndexedProperty(self) -> str:
        return self._indexedProperty

    def setProperty(self, property_: str) -> None:
        self._property = property_

    def getProperty(self) -> str:
        return self._property

    def setFieldOrder(self, fieldOrder: int) -> None:
        self._fieldOrder = fieldOrder

    def getFieldOrder(self) -> int:
        return self._fieldOrder

    def setPage(self, page: int) -> None:
        self._page = page

    def getPage(self) -> int:
        return self._page

    def __handleMissingAction(self, name: str) -> None:
        raise ValidatorException(
            "No ValidatorAction named "
            + name
            + " found for field "
            + self.getProperty()
        )

    def __processArg(self, key: str, replaceValue: str) -> None:

        for argMap in self._args:
            if argMap is None:
                continue

            for arg in argMap.values():
                if arg is not None:
                    arg.setKey(ValidatorUtils.replace(arg.getKey(), key, replaceValue))

    def __ensureArgsCapacity(self, arg: Arg) -> None:
        if arg.getPosition() >= len(self._args):
            self._args += [{} for _ in range(arg.getPosition() - len(self._args) + 1)]

    def __determineArgPosition(self, arg: Arg) -> None:

        position = arg.getPosition()

        if position >= 0:
            return

        if self._args is None or len(self._args) == 0:
            arg.setPosition(0)
            return

        keyName = arg.getName() if arg.getName() is not None else self.__DEFAULT_ARG
        lastPosition = -1
        lastDefault = -1
        for i in range(len(self._args)):
            if self._args[i] is not None and keyName in self._args[i]:
                lastPosition = i
            if self._args[i] is not None and self.__DEFAULT_ARG in self._args[i]:
                lastDefault = i

        if lastPosition < 0:
            lastPosition = lastDefault

        arg.setPosition(lastPosition + 1)


Field.initialize_fields()
