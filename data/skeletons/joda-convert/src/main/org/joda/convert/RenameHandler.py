from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.StringConvert import *
import typing
from typing import *
import enum
import io

# Imports End


class RenameHandler:

    # Class Fields Begin
    __enumRenames: typing.Dict[typing.Type[typing.Any], typing.Dict[str, enum.Enum]] = (
        None
    )
    __LOG: bool = None
    INSTANCE: RenameHandler = None
    __locked: bool = None
    __typeRenames: typing.Dict[str, typing.Type[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def lock(self) -> None:
        pass

    def lookupEnum(self, type: typing.Type[typing.Any], name: str) -> typing.Any:
        pass

    def getEnumRenames(
        self, type: typing.Type[typing.Any]
    ) -> typing.Dict[str, enum.Enum]:
        pass

    def getEnumTypesWithRenames(self) -> typing.Set[typing.Type[typing.Any]]:
        pass

    def renamedEnum(self, oldName: str, currentValue: enum.Enum) -> None:
        pass

    def lookupType(self, name: str) -> typing.Type[typing.Any]:
        pass

    def getTypeRenames(self) -> typing.Dict[str, typing.Type[typing.Any]]:
        pass

    def renamedType(self, oldName: str, currentValue: typing.Type[typing.Any]) -> None:
        pass

    @staticmethod
    def create1(loadFromClasspath: bool) -> RenameHandler:
        pass

    @staticmethod
    def create0() -> RenameHandler:
        pass

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
        pass

    def __loadRenameFile(
        self,
        url: typing.Union[
            urllib.parse.ParseResult,
            urllib.parse.SplitResult,
            urllib.parse.DefragResult,
            str,
        ],
    ) -> typing.List[str]:
        pass

    def __loadFromClasspath(self) -> None:
        pass

    def __checkNotLocked(self) -> None:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __createInstance() -> RenameHandler:
        pass

    # Class Methods End
