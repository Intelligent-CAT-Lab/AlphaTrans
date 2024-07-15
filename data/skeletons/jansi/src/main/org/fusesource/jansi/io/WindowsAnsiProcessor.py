from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.io.Colors import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.internal.Kernel32 import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class WindowsAnsiProcessor(AnsiProcessor):

    # Class Fields Begin
    __console: int = None
    __FOREGROUND_BLACK: int = None
    __FOREGROUND_YELLOW: int = None
    __FOREGROUND_MAGENTA: int = None
    __FOREGROUND_CYAN: int = None
    __FOREGROUND_WHITE: int = None
    __BACKGROUND_BLACK: int = None
    __BACKGROUND_YELLOW: int = None
    __BACKGROUND_MAGENTA: int = None
    __BACKGROUND_CYAN: int = None
    __BACKGROUND_WHITE: int = None
    __ANSI_FOREGROUND_COLOR_MAP: typing.List[int] = None
    __ANSI_BACKGROUND_COLOR_MAP: typing.List[int] = None
    __info: Kernel32.CONSOLE_SCREEN_BUFFER_INFO = None
    __originalColors: int = None
    __negative: bool = None
    __savedX: int = None
    __savedY: int = None
    # Class Fields End

    # Class Methods Begin
    def _processChangeWindowTitle(self, label: str) -> None:
        pass

    def _processDeleteLine(self, optionInt: int) -> None:
        pass

    def _processInsertLine(self, optionInt: int) -> None:
        pass

    def _processRestoreCursorPosition(self) -> None:
        pass

    def _processSaveCursorPosition(self) -> None:
        pass

    def _processSetAttribute(self, attribute: int) -> None:
        pass

    def _processAttributeReset(self) -> None:
        pass

    def _processDefaultBackgroundColor(self) -> None:
        pass

    def _processDefaultTextColor(self) -> None:
        pass

    def _processSetBackgroundColor1(self, color: int, bright: bool) -> None:
        pass

    def _processSetForegroundColor1(self, color: int, bright: bool) -> None:
        pass

    def _processCursorDownLine(self, count: int) -> None:
        pass

    def _processCursorUpLine(self, count: int) -> None:
        pass

    def _processCursorToColumn(self, x: int) -> None:
        pass

    def _processCursorTo(self, row: int, col: int) -> None:
        pass

    def _processCursorUp(self, count: int) -> None:
        pass

    def _processCursorDown(self, count: int) -> None:
        pass

    def _processCursorRight(self, count: int) -> None:
        pass

    def _processCursorLeft(self, count: int) -> None:
        pass

    def _processEraseLine(self, eraseOption: int) -> None:
        pass

    def _processEraseScreen(self, eraseOption: int) -> None:
        pass

    def _processSetBackgroundColorExt1(self, r: int, g: int, b: int) -> None:
        pass

    def _processSetBackgroundColorExt0(self, paletteIndex: int) -> None:
        pass

    def _processSetForegroundColorExt1(self, r: int, g: int, b: int) -> None:
        pass

    def _processSetForegroundColorExt0(self, paletteIndex: int) -> None:
        pass

    def WindowsAnsiProcessor1(
        self, ps: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> WindowsAnsiProcessor:
        pass

    def WindowsAnsiProcessor0(
        self, ps: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], stdout: bool
    ) -> WindowsAnsiProcessor:
        pass

    def __init__(
        self, ps: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], console: int
    ) -> None:
        pass

    def __applyCursorPosition(self) -> None:
        pass

    def __invertAttributeColors(self, attributes: int) -> int:
        pass

    def __applyAttribute(self) -> None:
        pass

    def __getConsoleInfo(self) -> None:
        pass

    # Class Methods End
