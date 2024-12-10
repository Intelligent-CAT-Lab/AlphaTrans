from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.internal.MingwSupport import *
from src.main.org.fusesource.jansi.internal.Kernel32 import *
from src.main.org.fusesource.jansi.internal.JansiLoader import *
from src.main.org.fusesource.jansi.internal.CLibrary import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.AnsiPrintStream import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiConsole import *
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.Ansi import *
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class AnsiMain:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __closeQuietly(c: Closeable) -> None:
        pass

    @staticmethod
    def __writeFileContent(f: pathlib.Path) -> None:
        pass

    @staticmethod
    def __printJansiLogoDemo() -> None:
        pass

    @staticmethod
    def __getPomPropertiesVersion(path: str) -> str:
        pass

    @staticmethod
    def __testAnsi(stderr: bool) -> None:
        pass

    @staticmethod
    def __diagnoseTty(stderr: bool) -> None:
        pass

    @staticmethod
    def __getJansiVersion() -> str:
        pass

    # Class Methods End
