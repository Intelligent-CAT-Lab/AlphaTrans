from __future__ import annotations
import re
import sys
import os
import io
import enum
import typing
from typing import *
import urllib
from src.main.org.joda.convert.StringConvert import *


class RenameHandler:

    INSTANCE: RenameHandler = None
    from typing import Dict, Type, Any


class RenameHandler:
    __enumRenames: Dict[Type[Any], Dict[str, enum.Enum]] = ConcurrentHashMap(
        16, 0.75, 2
    )
    __typeRenames: Dict[str, Type[Any]] = ConcurrentHashMap(16, 0.75, 2)
    __locked: bool = False

    __LOG: bool = StringConvert.LOG

    @staticmethod
    def initialize_fields() -> None:
        RenameHandler.INSTANCE: RenameHandler = RenameHandler.__createInstance()

    def toString(self) -> str:
        return (
            "RenamedTypes"
            + str(self.__typeRenames)
            + ",RenamedEnumConstants"
            + str(self.__enumRenames)
        )

    def lock(self) -> None:
        self.__checkNotLocked()
        self.__locked = True

    def lookupEnum(self, type: typing.Type[typing.Any], name: str) -> typing.Any:

        if type is None:
            raise ValueError("type must not be null")
        if name is None:
            raise ValueError("name must not be null")

        map = self.getEnumRenames(type)
        value = map.get(name)
        if value is not None:
            return value
        return type[name]

    def getEnumRenames(
        self, type: typing.Type[typing.Any]
    ) -> typing.Dict[str, enum.Enum]:

        if type is None:
            raise ValueError("type must not be null")

        map = self.__enumRenames.get(type)

        if map is None:
            return {}

        return dict(map)

    def getEnumTypesWithRenames(self) -> typing.Set[typing.Type[typing.Any]]:
        return set(self.__enumRenames.keys())

    def renamedEnum(self, oldName: str, currentValue: enum.Enum) -> None:

        if oldName is None:
            raise ValueError("oldName must not be null")
        if currentValue is None:
            raise ValueError("currentValue must not be null")

        self.__checkNotLocked()

        enumType = type(currentValue)

        if enumType not in self.__enumRenames:
            self.__enumRenames[enumType] = {}

        self.__enumRenames[enumType][oldName] = currentValue

    def lookupType(self, name: str) -> typing.Type[typing.Any]:

        if name is None:
            raise ValueError("name must not be null")

        type = self.__typeRenames.get(name)

        if type is None:
            type = StringConvert.loadType(name)

        return type

    def getTypeRenames(self) -> typing.Dict[str, typing.Type[typing.Any]]:
        return dict(self.__typeRenames)

    def renamedType(self, oldName: str, currentValue: typing.Type[typing.Any]) -> None:

        if oldName is None:
            raise ValueError("oldName must not be null")
        if currentValue is None:
            raise ValueError("currentValue must not be null")
        if (
            oldName.startswith("java.")
            or oldName.startswith("javax.")
            or oldName.startswith("org.joda.")
        ):
            raise ValueError("oldName must not be a java.*, javax.* or org.joda.* type")

        self.__checkNotLocked()
        self.__typeRenames[oldName] = currentValue

    @staticmethod
    def create1(loadFromClasspath: bool) -> RenameHandler:
        handler = RenameHandler()
        if loadFromClasspath:
            handler._RenameHandler__loadFromClasspath()
        return handler

    @staticmethod
    def create0() -> RenameHandler:
        return RenameHandler()

    def __parseRenameFile(
        self,
        lines: typing.List[str],
        url: typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ],
    ) -> None:

        types = False
        enums = False
        for line in lines:
            try:
                if line.strip() == "[types]":
                    types = True
                    enums = False
                elif line.strip() == "[enums]":
                    types = False
                    enums = True
                elif types:
                    equalsPos = line.find("=")
                    if equalsPos < 0:
                        raise ValueError(
                            "Renamed.ini type line must be formatted as 'oldClassName = newClassName'"
                        )
                    oldName = line[:equalsPos].strip()
                    newName = line[equalsPos + 1 :].strip()
                    newClass = None
                    try:
                        newClass = StringConvert.loadType(newName)
                    except Exception as ex:
                        if self.__LOG:
                            print(ex, file=sys.stderr)
                        raise ValueError(f"Class.forName({newName}) failed: {str(ex)}")
                    self.renamedType(oldName, newClass)
                elif enums:
                    equalsPos = line.find("=")
                    lastDotPos = line.rfind(".")
                    if equalsPos < 0 or lastDotPos < 0 or lastDotPos < equalsPos:
                        raise ValueError(
                            "Renamed.ini enum line must be formatted as 'oldEnumConstantName = enumClassName.newEnumConstantName'"
                        )
                    oldName = line[:equalsPos].strip()
                    enumClassName = line[equalsPos + 1 : lastDotPos].strip()
                    enumConstantName = line[lastDotPos + 1 :].strip()
                    enumClass = typing.cast(
                        typing.Type[enum.Enum], Class.forName(enumClassName)
                    )
                    newEnum = enumClass[enumConstantName]
                    self.renamedEnum(oldName, newEnum)
                else:
                    raise ValueError("Renamed.ini must start with [types] or [enums]")
            except Exception as ex:
                print(f"ERROR: Invalid Renamed.ini: {url}: {str(ex)}", file=sys.stderr)

    def __loadRenameFile(
        self,
        url: typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ],
    ) -> typing.List[str]:

        lines = []
        with urllib.request.urlopen(url) as response:
            reader = io.TextIOWrapper(response, encoding="utf-8")
            for line in reader:
                trimmed = line.strip()
                if trimmed and not trimmed.startswith("#"):
                    lines.append(trimmed)
        return lines

    def __loadFromClasspath(self) -> None:

        pass  # LLM could not translate this method

    def __checkNotLocked(self) -> None:
        if self.__locked:
            raise RuntimeError(
                "RenameHandler has been locked and it cannot now be changed"
            )

    def __init__(self) -> None:
        pass

    @staticmethod
    def __createInstance() -> RenameHandler:

        instance = RenameHandler.create1(False)
        try:
            instance._RenameHandler__loadFromClasspath()

        except RuntimeError as ex:
            print("ERROR: " + str(ex))

        except Exception as ex:
            print("ERROR: Failed to load Renamed.ini files: " + str(ex))

        return instance


RenameHandler.initialize_fields()
