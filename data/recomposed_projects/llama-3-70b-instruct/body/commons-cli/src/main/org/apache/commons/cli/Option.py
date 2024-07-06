from __future__ import annotations
import time
import copy
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.OptionValidator import *


class Builder:

    __valueSeparator: str = "\u0000"

    __type: typing.Type[typing.Any] = str
    __argCount: int = 0
    __optionalArg: bool = False

    __required: bool = False

    __argName: str = ""

    __longOption: str = ""

    __description: str = ""

    __option: str = ""

    def valueSeparator1(self, sep: str) -> Builder:
        self.__valueSeparator = sep
        return self

    def valueSeparator0(self) -> Builder:
        return self.valueSeparator1("=")

    def type(self, type: typing.Type[typing.Any]) -> Builder:
        self.__type = type
        return self

    def required1(self, required: bool) -> Builder:
        self.__required = required
        return self

    def required0(self) -> Builder:
        return self.required1(True)

    def optionalArg(self, isOptional: bool) -> Builder:
        self.__optionalArg = isOptional
        return self

    def option(self, option: str) -> Builder:
        self.__option = OptionValidator.validate(option)
        return self

    def numberOfArgs(self, numberOfArgs: int) -> Builder:
        self.__argCount = numberOfArgs
        return self

    def longOpt(self, longOpt: str) -> Builder:
        self.__longOption = longOpt
        return self

    def hasArgs(self) -> Builder:
        self.__argCount = Option.UNLIMITED_VALUES
        return self

    def hasArg1(self, hasArg: bool) -> Builder:
        self.__argCount = 1 if hasArg else Option.UNINITIALIZED
        return self

    def hasArg0(self) -> Builder:
        return self.hasArg1(True)

    def desc(self, description: str) -> Builder:
        self.__description = description
        return self

    def build(self) -> Option:
        if self.__option is None and self.__longOption is None:
            raise ValueError("Either opt or longOpt must be specified")
        return Option(3, None, None, None, False, self)

    def argName(self, argName: str) -> Builder:
        self.__argName = argName
        return self

    def __init__(self, option: str) -> None:
        self.option(option)


class Option:

    UNLIMITED_VALUES: int = -2
    UNINITIALIZED: int = -1
    __valuesep: str = "\u0000"

    __values: typing.List[str] = []

    __type: typing.Type[typing.Any] = str
    __argCount: int = UNINITIALIZED
    __optionalArg: bool = False

    __required: bool = False

    __description: str = ""

    __argName: str = ""

    __longOption: str = ""

    __option: str = ""

    __serialVersionUID: int = 1

    def toString(self) -> str:
        buf = io.StringIO()
        buf.write("[ option: ")
        buf.write(self.__option)

        if self.__longOption != None:
            buf.write(" ")
            buf.write(self.__longOption)

        buf.write(" ")

        if self.hasArgs():
            buf.write("[ARG...]")
        elif self.hasArg():
            buf.write(" [ARG]")

        buf.write(" :: ")
        buf.write(self.__description)

        if self.__type != None:
            buf.write(" :: ")
            buf.write(self.__type)

        buf.write(" ]")

        return buf.getvalue()

    def setType1(self, type: typing.Any) -> None:
        self.setType0(type.__class__)

    def hashCode(self) -> int:
        return Objects.hash(self.__longOption, self.__option)

    def equals(self, obj: typing.Any) -> bool:
        if self == obj:
            return True
        if not isinstance(obj, Option):
            return False
        other = obj
        return Objects.equals(self.longOption, other.longOption) and Objects.equals(
            self.option, other.option
        )

    def clone(self) -> typing.Any:
        try:
            option = super().clone()
            option.values = self.values.copy()
            return option
        except CloneNotSupportedException as cnse:
            raise RuntimeError(
                "A CloneNotSupportedException was thrown: " + cnse.getMessage()
            )

    def addValue(self, value: str) -> bool:
        return self.addValueForProcessing(value)

    def setValueSeparator(self, sep: str) -> None:
        self.__valuesep = sep

    def setType0(self, type: typing.Type[typing.Any]) -> None:
        self.__type = type

    def setRequired(self, required: bool) -> None:
        self.__required = required

    def setOptionalArg(self, optionalArg: bool) -> None:
        self.__optionalArg = optionalArg

    def setLongOpt(self, longOpt: str) -> None:
        self.__longOption = longOpt

    def setDescription(self, description: str) -> None:
        self.__description = description

    def setArgs(self, num: int) -> None:
        self.__argCount = num

    def setArgName(self, argName: str) -> None:
        self.__argName = argName

    def isRequired(self) -> bool:
        return self.__required

    def hasValueSeparator(self) -> bool:
        return self.__valuesep > 0

    def hasOptionalArg(self) -> bool:
        return self.__optionalArg

    def hasLongOpt(self) -> bool:
        return self.__longOption != None

    def hasArgs(self) -> bool:
        return self.__argCount > 1 or self.__argCount == Option.UNLIMITED_VALUES

    def hasArgName(self) -> bool:
        return self.__argName != None and not self.__argName.isEmpty()

    def hasArg(self) -> bool:
        return self.__argCount > 0 or self.__argCount == Option.UNLIMITED_VALUES

    def getValuesList(self) -> typing.List[str]:
        return self.__values

    def getValueSeparator(self) -> str:
        return self.__valuesep

    def getValues(self) -> typing.List[str]:
        return self.__values if not self.__hasNoValues() else None

    def getValue2(self, defaultValue: str) -> str:
        value = self.getValue0()
        return value if value is not None else defaultValue

    def getValue1(self, index: int) -> str:
        return self.__values[index] if not self.__hasNoValues() else None

    def getValue0(self) -> str:
        return self.__values[0] if not self.__hasNoValues() else None

    def getType(self) -> typing.Any:
        return self.__type

    def getOpt(self) -> str:
        return self.__option

    def getLongOpt(self) -> str:
        return self.__longOption

    def getId(self) -> int:
        return self.getKey().charAt(0)

    def getDescription(self) -> str:
        return self.__description

    def getArgs(self) -> int:
        return self.__argCount

    def getArgName(self) -> str:
        return self.__argName

    @staticmethod
    def Option2(option: str, hasArg: bool, description: str) -> Option:
        if hasArg:
            return Option(0, option, None, description, True, None)
        else:
            return Option(0, option, None, description, False, None)

    @staticmethod
    def Option1(option: str, description: str) -> Option:
        return Option(0, option, None, description, False, None)

    def __init__(
        self,
        constructorId: int,
        option: str,
        longOption: str,
        description: str,
        hasArg: bool,
        builder: Builder,
    ) -> None:
        if constructorId == -1:
            self.__argName = None
            self.__description = ""
            self.__longOption = None
            self.__argCount = 1
            self.__option = None
            self.__optionalArg = False
            self.__required = False
            self.__type = None
            self.__valuesep = "0"
        elif constructorId == 0:

            self.__option = OptionValidator.validate(option)
            self.__longOption = longOption

            if hasArg:
                self.__argCount = 1

            self.__description = description
        else:

            self.__argName = builder.__argName
            self.__description = builder.__description
            self.__longOption = builder.__longOption
            self.__argCount = builder.__argCount
            self.__option = builder.__option
            self.__optionalArg = builder.__optionalArg
            self.__required = builder.__required
            self.__type = builder.__type
            self.__valuesep = builder.__valueSeparator

    @staticmethod
    def builder1(option: str) -> Builder:
        return Builder(option)

    @staticmethod
    def builder0() -> Builder:
        return Option.builder1(None)

    def __processValue(self, value: str) -> None:
        if self.hasValueSeparator():
            sep = self.getValueSeparator()

            index = value.find(sep)

            while index != -1:
                if len(self.__values) == self.__argCount - 1:
                    break

                self.__add(value[0:index])

                value = value[index + 1 :]

                index = value.find(sep)

        self.__add(value)

    def __hasNoValues(self) -> bool:
        return len(self.__values) == 0

    def __add(self, value: str) -> None:
        if not self.acceptsArg():
            raise Exception("Cannot add value, list full.")

        self.__values.append(value)

    def requiresArg(self) -> bool:
        return not self.__optionalArg and (
            self.__argCount == Option.UNLIMITED_VALUES
            and len(self.__values) == 0
            or self.acceptsArg()
        )

    def getKey(self) -> str:
        return self.__option if self.__option is not None else self.__longOption

    def clearValues(self) -> None:
        self.__values.clear()

    def addValueForProcessing(self, value: str) -> None:
        if self.__argCount == Option.UNINITIALIZED:
            raise RuntimeError("NO_ARGS_ALLOWED")
        self.__processValue(value)

    def acceptsArg(self) -> bool:
        return (self.hasArg() or self.hasArgs() or self.hasOptionalArg()) and (
            self.__argCount <= 0 or len(self.__values) < self.__argCount
        )
