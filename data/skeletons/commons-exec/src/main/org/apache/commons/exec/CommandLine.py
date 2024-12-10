from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.util.StringUtils import *
import typing
from typing import *
import io
import pathlib

# Imports End


class Argument:

    # Class Fields Begin
    __value: str = None
    __handleQuoting: bool = None
    # Class Fields End

    # Class Methods Begin
    def __isHandleQuoting(self) -> bool:
        pass

    def __getValue(self) -> str:
        pass

    def __init__(self, value: str, handleQuoting: bool) -> None:
        pass

    # Class Methods End


class CommandLine:

    # Class Fields Begin
    __arguments: typing.List[Argument] = None
    __executable: str = None
    __substitutionMap: typing.Dict[str, typing.Any] = None
    __isFile: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def toStrings(self) -> typing.List[typing.List[str]]:
        pass

    def setSubstitutionMap(self, substitutionMap: typing.Dict[str, typing.Any]) -> None:
        pass

    def isFile(self) -> bool:
        pass

    def getSubstitutionMap(self) -> typing.Dict[str, typing.Any]:
        pass

    def getExecutable(self) -> str:
        pass

    def getArguments(self) -> typing.List[typing.List[str]]:
        pass

    def addArguments3(
        self, addArguments: typing.List[typing.List[str]], handleQuoting: bool
    ) -> CommandLine:
        pass

    def addArguments2(self, addArguments: typing.List[typing.List[str]]) -> CommandLine:
        pass

    def addArguments1(self, addArguments: str, handleQuoting: bool) -> CommandLine:
        pass

    def addArguments0(self, addArguments: str) -> CommandLine:
        pass

    def addArgument1(self, argument: str, handleQuoting: bool) -> CommandLine:
        pass

    def addArgument0(self, argument: str) -> CommandLine:
        pass

    def __init__(
        self,
        constructorId: int,
        other: CommandLine,
        executable: pathlib.Path,
        executableString: str,
    ) -> None:
        pass

    @staticmethod
    def parse1(line: str, substitutionMap: typing.Dict[str, typing.Any]) -> CommandLine:
        pass

    @staticmethod
    def parse0(line: str) -> CommandLine:
        pass

    def __toCleanExecutable(self, dirtyExecutable: str) -> str:
        pass

    def __expandArgument(self, argument: str) -> str:
        pass

    @staticmethod
    def __translateCommandline(toProcess: str) -> typing.List[typing.List[str]]:
        pass

    # Class Methods End
