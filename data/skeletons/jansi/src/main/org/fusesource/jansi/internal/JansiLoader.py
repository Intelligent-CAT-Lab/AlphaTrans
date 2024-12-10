from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.internal.OSInfo import *
from src.main.org.fusesource.jansi.AnsiConsole import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
import pathlib

# Imports End


class JansiLoader:

    # Class Fields Begin
    __loaded: bool = None
    __nativeLibraryPath: str = None
    __nativeLibrarySourceUrl: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getVersion() -> str:
        pass

    @staticmethod
    def getMinorVersion() -> int:
        pass

    @staticmethod
    def getMajorVersion() -> int:
        pass

    @staticmethod
    def cleanup() -> None:
        pass

    @staticmethod
    def getNativeLibrarySourceUrl() -> str:
        pass

    @staticmethod
    def getNativeLibraryPath() -> str:
        pass

    @staticmethod
    def initialize() -> bool:
        pass

    @staticmethod
    def __hasResource(path: str) -> bool:
        pass

    @staticmethod
    def __loadJansiNativeLibrary() -> None:
        pass

    @staticmethod
    def __loadNativeLibrary(libPath: pathlib.Path) -> bool:
        pass

    @staticmethod
    def __randomUUID() -> str:
        pass

    @staticmethod
    def __extractAndLoadLibraryFile(
        libFolderForCurrentOS: str, libraryFileName: str, targetFolder: str
    ) -> bool:
        pass

    @staticmethod
    def __contentsEquals(
        in1: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        in2: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> str:
        pass

    @staticmethod
    def __readNBytes(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        b: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __getTempDir() -> pathlib.Path:
        pass

    # Class Methods End
