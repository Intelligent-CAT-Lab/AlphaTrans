from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
import pathlib

# Imports End


class OSInfo:

    # Class Fields Begin
    X86: str = None
    X86_64: str = None
    IA64_32: str = None
    IA64: str = None
    PPC: str = None
    PPC64: str = None
    ARM64: str = None
    __archMapping: typing.Dict[str, str] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def translateArchNameToFolderName(archName: str) -> str:
        pass

    @staticmethod
    def translateOSNameToFolderName(osName: str) -> str:
        pass

    @staticmethod
    def getArchName() -> str:
        pass

    @staticmethod
    def resolveArmArchType() -> str:
        pass

    @staticmethod
    def getHardwareName() -> str:
        pass

    @staticmethod
    def isAlpine() -> bool:
        pass

    @staticmethod
    def isAndroid() -> bool:
        pass

    @staticmethod
    def getOSName() -> str:
        pass

    @staticmethod
    def getNativeLibFolderPathForCurrentOS() -> str:
        pass

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __readFully(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> str:
        pass

    # Class Methods End
