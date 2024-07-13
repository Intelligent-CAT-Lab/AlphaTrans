from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.OptionValidator import *
import typing
from typing import *
import io

# Imports End


class Builder:

    # Class Fields Begin
    __option: str = None
    __description: str = None
    __longOption: str = None
    __argName: str = None
    __required: bool = None
    __optionalArg: bool = None
    __argCount: int = None
    __type: typing.Type[typing.Any] = None
    __valueSeparator: str = None
    # Class Fields End

    # Class Methods Begin
    def valueSeparator1(self, sep: str) -> Builder:
        pass

    def valueSeparator0(self) -> Builder:
        pass

    def type_(self, type_: typing.Type[typing.Any]) -> Builder:
        pass

    def required1(self, required: bool) -> Builder:
        pass

    def required0(self) -> Builder:
        pass

    def optionalArg(self, isOptional: bool) -> Builder:
        pass

    def option(self, option: str) -> Builder:
        pass

    def numberOfArgs(self, numberOfArgs: int) -> Builder:
        pass

    def longOpt(self, longOpt: str) -> Builder:
        pass

    def hasArgs(self) -> Builder:
        pass

    def hasArg1(self, hasArg: bool) -> Builder:
        pass

    def hasArg0(self) -> Builder:
        pass

    def desc(self, description: str) -> Builder:
        pass

    def build(self) -> Option:
        pass

    def argName(self, argName: str) -> Builder:
        pass

    def __init__(self, option: str) -> None:
        pass

    # Class Methods End


class Option:

    # Class Fields Begin
    UNINITIALIZED: int = None
    UNLIMITED_VALUES: int = None
    __serialVersionUID: int = None
    __option: str = None
    __longOption: str = None
    __argName: str = None
    __description: str = None
    __required: bool = None
    __optionalArg: bool = None
    __argCount: int = None
    __type: typing.Type[typing.Any] = None
    __values: typing.List[str] = None
    __valuesep: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def setType1(self, type_: typing.Any) -> None:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def clone(self) -> typing.Any:
        pass

    def addValue(self, value: str) -> bool:
        pass

    def setValueSeparator(self, sep: str) -> None:
        pass

    def setType0(self, type_: typing.Type[typing.Any]) -> None:
        pass

    def setRequired(self, required: bool) -> None:
        pass

    def setOptionalArg(self, optionalArg: bool) -> None:
        pass

    def setLongOpt(self, longOpt: str) -> None:
        pass

    def setDescription(self, description: str) -> None:
        pass

    def setArgs(self, num: int) -> None:
        pass

    def setArgName(self, argName: str) -> None:
        pass

    def isRequired(self) -> bool:
        pass

    def hasValueSeparator(self) -> bool:
        pass

    def hasOptionalArg(self) -> bool:
        pass

    def hasLongOpt(self) -> bool:
        pass

    def hasArgs(self) -> bool:
        pass

    def hasArgName(self) -> bool:
        pass

    def hasArg(self) -> bool:
        pass

    def getValuesList(self) -> typing.List[str]:
        pass

    def getValueSeparator(self) -> str:
        pass

    def getValues(self) -> typing.List[typing.List[str]]:
        pass

    def getValue2(self, defaultValue: str) -> str:
        pass

    def getValue1(self, index: int) -> str:
        pass

    def getValue0(self) -> str:
        pass

    def getType(self) -> typing.Any:
        pass

    def getOpt(self) -> str:
        pass

    def getLongOpt(self) -> str:
        pass

    def getId(self) -> int:
        pass

    def getDescription(self) -> str:
        pass

    def getArgs(self) -> int:
        pass

    def getArgName(self) -> str:
        pass

    @staticmethod
    def Option2(option: str, hasArg: bool, description: str) -> Option:
        pass

    @staticmethod
    def Option1(option: str, description: str) -> Option:
        pass

    def __init__(
        self,
        constructorId: int,
        option: str,
        longOption: str,
        description: str,
        hasArg: bool,
        builder: Builder,
    ) -> None:
        pass

    @staticmethod
    def builder1(option: str) -> Builder:
        pass

    @staticmethod
    def builder0() -> Builder:
        pass

    def __processValue(self, value: str) -> None:
        pass

    def __hasNoValues(self) -> bool:
        pass

    def __add(self, value: str) -> None:
        pass

    def requiresArg(self) -> bool:
        pass

    def getKey(self) -> str:
        pass

    def clearValues(self) -> None:
        pass

    def addValueForProcessing(self, value: str) -> None:
        pass

    def acceptsArg(self) -> bool:
        pass

    # Class Methods End
