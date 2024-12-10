from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.io.ColorsAnsiProcessor import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiColors import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
from abc import ABC

# Imports End


class IoRunnable(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    # Class Methods End


class WidthSupplier(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getTerminalWidth(self) -> int:
        pass

    # Class Methods End


class ZeroWidthSupplier:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getTerminalWidth(self) -> int:
        pass

    # Class Methods End


class AnsiOutputStream:

    # Class Fields Begin
    RESET_CODE: typing.List[int] = None
    __LOOKING_FOR_FIRST_ESC_CHAR: int = None
    __LOOKING_FOR_SECOND_ESC_CHAR: int = None
    __LOOKING_FOR_NEXT_ARG: int = None
    __LOOKING_FOR_STR_ARG_END: int = None
    __LOOKING_FOR_INT_ARG_END: int = None
    __LOOKING_FOR_OSC_COMMAND: int = None
    __LOOKING_FOR_OSC_COMMAND_END: int = None
    __LOOKING_FOR_OSC_PARAM: int = None
    __LOOKING_FOR_ST: int = None
    __LOOKING_FOR_CHARSET: int = None
    __FIRST_ESC_CHAR: int = None
    __SECOND_ESC_CHAR: int = None
    __SECOND_OSC_CHAR: int = None
    __BEL: int = None
    __SECOND_ST_CHAR: int = None
    __SECOND_CHARSET0_CHAR: int = None
    __SECOND_CHARSET1_CHAR: int = None
    __ap: AnsiProcessor = None
    __MAX_ESCAPE_SEQUENCE_LENGTH: int = None
    __buffer: typing.List[int] = None
    __pos: int = None
    __startOfValue: int = None
    __options: typing.List[typing.Any] = None
    __state: int = None
    __cs: str = None
    __width: AnsiOutputStream.WidthSupplier = None
    __processor: AnsiProcessor = None
    __type: AnsiType = None
    __colors: AnsiColors = None
    __installer: AnsiOutputStream.IoRunnable = None
    __uninstaller: AnsiOutputStream.IoRunnable = None
    __mode: AnsiMode = None
    __resetAtUninstall: bool = None
    # Class Fields End

    # Class Methods Begin
    def close(self) -> None:
        pass

    def write(self, data: int) -> None:
        pass

    def uninstall(self) -> None:
        pass

    def install(self) -> None:
        pass

    def setResetAtUninstall(self, resetAtUninstall: bool) -> None:
        pass

    def isResetAtUninstall(self) -> bool:
        pass

    def setMode(self, mode: AnsiMode) -> None:
        pass

    def getMode(self) -> AnsiMode:
        pass

    def getColors(self) -> AnsiColors:
        pass

    def getType(self) -> AnsiType:
        pass

    def getTerminalWidth(self) -> int:
        pass

    def __init__(
        self,
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        width: AnsiOutputStream.WidthSupplier,
        mode: AnsiMode,
        processor: AnsiProcessor,
        type_: AnsiType,
        colors: AnsiColors,
        cs: str,
        installer: AnsiOutputStream.IoRunnable,
        uninstaller: AnsiOutputStream.IoRunnable,
        resetAtUninstall: bool,
    ) -> None:
        pass

    def __reset(self, skipBuffer: bool) -> None:
        pass

    def __processEscapeCommand(self, data: int) -> None:
        pass

    def __processOperatingSystemCommand(self) -> None:
        pass

    def __processCharsetSelect(self) -> None:
        pass

    # Class Methods End
