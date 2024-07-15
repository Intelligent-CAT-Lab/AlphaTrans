from __future__ import annotations
import copy
import re
import os
import io
import enum
import typing
from typing import *
import urllib
from src.main.org.joda.convert.StringConvert import *


class RenameHandler:

    INSTANCE: RenameHandler = None
    __enumRenames: typing.Dict[typing.Type[typing.Any], typing.Dict[str, enum.Enum]] = (
        {}
    )
    __typeRenames: typing.Dict[str, typing.Type[typing.Any]] = {}
    __locked: bool = False

    __LOG: bool = StringConvert.LOG

    @staticmethod
    def initialize_fields() -> None:
        RenameHandler.INSTANCE: RenameHandler = RenameHandler.__createInstance()

    def toString(self) -> str:
        return (
            "RenamedTypes"
            + self.__typeRenames
            + ",RenamedEnumConstants"
            + self.__enumRenames
        )

    def lock(self) -> None:
        self.__checkNotLocked()
        self.__locked = True

    def lookupEnum(self, type: typing.Type[typing.Any], name: str) -> typing.Any:
        if type is None:
            raise ValueError("type must not be null")
        if name is None:
            raise ValueError("name must not be null")
        map: typing.Dict[str, enum.Enum] = self.getEnumRenames(type)
        value: enum.Enum = map.get(name)
        if value is not None:
            return type.cast(value)
        return Enum.valueOf(type, name)

    def getEnumRenames(
        self, type: typing.Type[typing.Any]
    ) -> typing.Dict[str, enum.Enum]:
        if type is None:
            raise ValueError("type must not be null")
        map: typing.Dict[str, enum.Enum] = self.__enumRenames.get(type)
        if map is None:
            return {}
        return map.copy()

    def getEnumTypesWithRenames(self) -> typing.Set[typing.Type[typing.Any]]:
        return set(self.__enumRenames.keys())

    def renamedEnum(self, oldName: str, currentValue: enum.Enum) -> None:

        pass  # LLM could not translate this method

    def lookupType(self, name: str) -> typing.Type[typing.Any]:
        if name is None:
            raise ValueError("name must not be null")
        type: typing.Type[typing.Any] = self.__typeRenames.get(name)
        if type is None:
            type = StringConvert.loadType(name)
        return type

    def getTypeRenames(self) -> typing.Dict[str, typing.Type[typing.Any]]:
        return dict(self.__typeRenames)

    def renamedType(self, oldName: str, currentValue: typing.Type[typing.Any]) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def create1(loadFromClasspath: bool) -> RenameHandler:
        handler = RenameHandler()
        if loadFromClasspath:
            handler.__loadFromClasspath()
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
        types: bool = False
        enums: bool = False
        for line in lines:
            try:
                if line == "[types]":
                    types = True
                    enums = False
                elif line == "[enums]":
                    types = False
                    enums = True
                elif types:
                    equalsPos: int = line.index("=")
                    if equalsPos < 0:
                        raise ValueError(
                            "Renamed.ini type line must be formatted as 'oldClassName = newClassName'"
                        )
                    oldName: str = line[0:equalsPos].strip()
                    newName: str = line[equalsPos + 1 :].strip()
                    newClass: typing.Type[typing.Any] = None
                    try:
                        newClass = StringConvert.loadType(newName)
                    except Exception as ex:
                        if self.__LOG:
                            ex.printStackTrace(System.err)
                        raise ValueError(
                            "Class.forName(" + newName + ") failed: " + ex.getMessage()
                        )
                    self.renamedType(oldName, newClass)
                elif enums:
                    equalsPos: int = line.index("=")
                    lastDotPos: int = line.rindex(".")
                    if equalsPos < 0 or lastDotPos < 0 or lastDotPos < equalsPos:
                        raise ValueError(
                            "Renamed.ini enum line must be formatted as 'oldEnumConstantName = enumClassName.newEnumConstantName'"
                        )
                    oldName: str = line[0:equalsPos].strip()
                    enumClassName: str = line[equalsPos + 1 : lastDotPos].strip()
                    enumConstantName: str = line[lastDotPos + 1 :].strip()
                    enumClass: typing.Type[enum.Enum] = Class.forName(
                        enumClassName
                    ).asSubclass(enum.Enum)
                    newEnum: enum.Enum = Enum.valueOf(enumClass, enumConstantName)
                    self.renamedEnum(oldName, newEnum)
                else:
                    raise ValueError("Renamed.ini must start with [types] or [enums]")
            except Exception as ex:
                System.err.println(
                    "ERROR: Invalid Renamed.ini: " + url + ": " + ex.getMessage()
                )

    def __loadRenameFile(
        self,
        url: typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ],
    ) -> typing.List[str]:
        lines: typing.List[str] = []
        with io.BufferedReader(
            io.InputStreamReader(url.openStream(), charset="UTF-8")
        ) as reader:
            line: str
            while (line := reader.readLine()) is not None:
                trimmed: str = line.trim()
                if not trimmed.isEmpty() and not trimmed.startsWith("#"):
                    lines.add(trimmed)
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
            instance.__loadFromClasspath()
        except RuntimeError as ex:
            print("ERROR: " + ex.getMessage())
            ex.printStackTrace()
        except Exception as ex:
            print("ERROR: Failed to load Renamed.ini files: " + ex.getMessage())
            ex.printStackTrace()
        return instance


RenameHandler.initialize_fields()
