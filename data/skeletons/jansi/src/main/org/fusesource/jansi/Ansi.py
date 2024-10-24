from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.AnsiRenderer import *
import os
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class Attribute:

    # Class Fields Begin
    ITALIC_OFF: Attribute = None
    UNDERLINE_OFF: Attribute = None
    BLINK_OFF: Attribute = None
    NEGATIVE_OFF: Attribute = None
    CONCEAL_OFF: Attribute = None
    STRIKETHROUGH_OFF: Attribute = None
    __value: int = None
    __name: str = None
    RESET: Attribute = None
    INTENSITY_BOLD: Attribute = None
    INTENSITY_FAINT: Attribute = None
    ITALIC: Attribute = None
    UNDERLINE: Attribute = None
    BLINK_SLOW: Attribute = None
    BLINK_FAST: Attribute = None
    NEGATIVE_ON: Attribute = None
    CONCEAL_ON: Attribute = None
    STRIKETHROUGH_ON: Attribute = None
    UNDERLINE_DOUBLE: Attribute = None
    INTENSITY_BOLD_OFF: Attribute = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def value(self) -> int:
        pass

    def __init__(self, index: int, name: str) -> None:
        pass

    # Class Methods End


class Color:

    # Class Fields Begin
    BLACK: Ansi.Color = None
    RED: Ansi.Color = None
    GREEN: Ansi.Color = None
    YELLOW: Ansi.Color = None
    BLUE: Ansi.Color = None
    MAGENTA: Ansi.Color = None
    CYAN: Ansi.Color = None
    WHITE: Ansi.Color = None
    DEFAULT: Ansi.Color = None
    __value: int = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def bgBright(self) -> int:
        pass

    def fgBright(self) -> int:
        pass

    def bg(self) -> int:
        pass

    def fg(self) -> int:
        pass

    def value(self) -> int:
        pass

    def __init__(self, index: int, name: str) -> None:
        pass

    # Class Methods End


class Erase:

    # Class Fields Begin
    FORWARD: Erase = None
    BACKWARD: Erase = None
    ALL: Erase = None
    __value: int = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def value(self) -> int:
        pass

    def __init__(self, index: int, name: str) -> None:
        pass

    # Class Methods End


class Consumer(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def apply(self, ansi: Ansi) -> None:
        pass

    # Class Methods End


class Ansi:

    # Class Fields Begin
    DISABLE: str = None
    __detector: typing.Callable[[], bool] = None
    __holder: contextvars.ContextVar[typing.TypeVar("T", bound=bool)] = None
    __FIRST_ESC_CHAR: str = None
    __SECOND_ESC_CHAR: str = None
    __builder: typing.Union[typing.List[str], io.StringIO] = None
    __attributeOptions: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def append(self, c: str) -> Ansi:
        pass

    def append(self, csq: str, start: int, end: int) -> Ansi:
        pass

    def append(self, csq: str) -> Ansi:
        pass

    def toString(self) -> str:
        pass

    def restorCursorPosition(self) -> Ansi:
        pass

    def append2(self, c: str) -> Ansi:
        pass

    def append1(self, csq: str, start: int, end: int) -> Ansi:
        pass

    def append0(self, csq: str) -> Ansi:
        pass

    def render1(self, text: str, args: typing.List[typing.Any]) -> Ansi:
        pass

    def render0(self, text: str) -> Ansi:
        pass

    def apply(self, fun: Consumer) -> Ansi:
        pass

    def format_(self, pattern: str, args: typing.List[typing.Any]) -> Ansi:
        pass

    def newline(self) -> Ansi:
        pass

    def a13(self, value: io.StringIO) -> Ansi:
        pass

    def a12(self, value: typing.Any) -> Ansi:
        pass

    def a11(self, value: int) -> Ansi:
        pass

    def a10(self, value: int) -> Ansi:
        pass

    def a9(self, value: float) -> Ansi:
        pass

    def a8(self, value: float) -> Ansi:
        pass

    def a7(self, value: str) -> Ansi:
        pass

    def a6(self, value: str, start: int, end: int) -> Ansi:
        pass

    def a5(self, value: typing.List[str]) -> Ansi:
        pass

    def a4(self, value: typing.List[str], offset: int, len_: int) -> Ansi:
        pass

    def a3(self, value: str) -> Ansi:
        pass

    def a2(self, value: bool) -> Ansi:
        pass

    def a1(self, value: str) -> Ansi:
        pass

    def boldOff(self) -> Ansi:
        pass

    def bold(self) -> Ansi:
        pass

    def reset(self) -> Ansi:
        pass

    def restoreCursorPositionDEC(self) -> Ansi:
        pass

    def restoreCursorPositionSCO(self) -> Ansi:
        pass

    def restoreCursorPosition(self) -> Ansi:
        pass

    def saveCursorPositionDEC(self) -> Ansi:
        pass

    def saveCursorPositionSCO(self) -> Ansi:
        pass

    def saveCursorPosition(self) -> Ansi:
        pass

    def scrollDown(self, rows: int) -> Ansi:
        pass

    def scrollUp(self, rows: int) -> Ansi:
        pass

    def eraseLine1(self, kind: Erase) -> Ansi:
        pass

    def eraseLine0(self) -> Ansi:
        pass

    def eraseScreen1(self, kind: Erase) -> Ansi:
        pass

    def eraseScreen0(self) -> Ansi:
        pass

    def cursorUpLine1(self, n: int) -> Ansi:
        pass

    def cursorUpLine0(self) -> Ansi:
        pass

    def cursorDownLine1(self, n: int) -> Ansi:
        pass

    def cursorDownLine0(self) -> Ansi:
        pass

    def cursorMove(self, x: int, y: int) -> Ansi:
        pass

    def cursorLeft(self, x: int) -> Ansi:
        pass

    def cursorRight(self, x: int) -> Ansi:
        pass

    def cursorDown(self, y: int) -> Ansi:
        pass

    def cursorUp(self, y: int) -> Ansi:
        pass

    def cursorToColumn(self, x: int) -> Ansi:
        pass

    def cursor(self, row: int, column: int) -> Ansi:
        pass

    def a0(self, attribute: Attribute) -> Ansi:
        pass

    def bgBrightYellow(self) -> Ansi:
        pass

    def bgBrightRed(self) -> Ansi:
        pass

    def bgBrightMagenta(self) -> Ansi:
        pass

    def bgBrightGreen(self) -> Ansi:
        pass

    def bgBrightDefault(self) -> Ansi:
        pass

    def bgBrightCyan(self) -> Ansi:
        pass

    def bgBright(self, color: Ansi.Color) -> Ansi:
        pass

    def fgBrightYellow(self) -> Ansi:
        pass

    def fgBrightRed(self) -> Ansi:
        pass

    def fgBrightMagenta(self) -> Ansi:
        pass

    def fgBrightGreen(self) -> Ansi:
        pass

    def fgBrightDefault(self) -> Ansi:
        pass

    def fgBrightCyan(self) -> Ansi:
        pass

    def fgBrightBlue(self) -> Ansi:
        pass

    def fgBrightBlack(self) -> Ansi:
        pass

    def fgBright(self, color: Ansi.Color) -> Ansi:
        pass

    def bgYellow(self) -> Ansi:
        pass

    def bgRed(self) -> Ansi:
        pass

    def bgMagenta(self) -> Ansi:
        pass

    def bgGreen(self) -> Ansi:
        pass

    def bgDefault(self) -> Ansi:
        pass

    def bgCyan(self) -> Ansi:
        pass

    def bgRgb1(self, r: int, g: int, b: int) -> Ansi:
        pass

    def bgRgb0(self, color: int) -> Ansi:
        pass

    def bg1(self, color: int) -> Ansi:
        pass

    def bg0(self, color: Ansi.Color) -> Ansi:
        pass

    def fgYellow(self) -> Ansi:
        pass

    def fgRed(self) -> Ansi:
        pass

    def fgMagenta(self) -> Ansi:
        pass

    def fgGreen(self) -> Ansi:
        pass

    def fgDefault(self) -> Ansi:
        pass

    def fgCyan(self) -> Ansi:
        pass

    def fgBlue(self) -> Ansi:
        pass

    def fgBlack(self) -> Ansi:
        pass

    def fgRgb1(self, r: int, g: int, b: int) -> Ansi:
        pass

    def fgRgb0(self, color: int) -> Ansi:
        pass

    def fg1(self, color: int) -> Ansi:
        pass

    def fg0(self, color: Ansi.Color) -> Ansi:
        pass

    def __init__(
        self,
        constructorId: int,
        builder: typing.Union[typing.List[str], io.StringIO],
        parent: Ansi,
    ) -> None:
        pass

    @staticmethod
    def Ansi2(size: int) -> Ansi:
        pass

    @staticmethod
    def Ansi1(parent: Ansi) -> Ansi:
        pass

    @staticmethod
    def Ansi0() -> Ansi:
        pass

    @staticmethod
    def ansi2(size: int) -> Ansi:
        pass

    @staticmethod
    def ansi1(builder: typing.Union[typing.List[str], io.StringIO]) -> Ansi:
        pass

    @staticmethod
    def ansi0() -> Ansi:
        pass

    @staticmethod
    def isEnabled() -> bool:
        pass

    @staticmethod
    def setEnabled(flag: bool) -> None:
        pass

    @staticmethod
    def isDetected() -> bool:
        pass

    @staticmethod
    def setDetector(detector: typing.Callable[[], bool]) -> None:
        pass

    def ___appendEscapeSequence(
        self, command: str, options: typing.List[typing.Any]
    ) -> Ansi:
        pass

    def __flushAttributes(self) -> None:
        pass

    def __appendEscapeSequence2(
        self, command: str, options: typing.List[typing.Any]
    ) -> Ansi:
        pass

    def __appendEscapeSequence1(self, command: str, option: int) -> Ansi:
        pass

    def __appendEscapeSequence0(self, command: str) -> Ansi:
        pass

    # Class Methods End


class NoAnsi(Ansi):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def reset(self) -> Ansi:
        pass

    def restoreCursorPosition(self) -> Ansi:
        pass

    def restorCursorPosition(self) -> Ansi:
        pass

    def saveCursorPosition(self) -> Ansi:
        pass

    def scrollDown(self, rows: int) -> Ansi:
        pass

    def scrollUp(self, rows: int) -> Ansi:
        pass

    def cursorLeft(self, x: int) -> Ansi:
        pass

    def cursorDown(self, y: int) -> Ansi:
        pass

    def cursorRight(self, x: int) -> Ansi:
        pass

    def cursorUp(self, y: int) -> Ansi:
        pass

    def cursorToColumn(self, x: int) -> Ansi:
        pass

    def cursor(self, row: int, column: int) -> Ansi:
        pass

    def a0(self, attribute: Attribute) -> Ansi:
        pass

    def bgRgb1(self, r: int, g: int, b: int) -> Ansi:
        pass

    def fgRgb1(self, r: int, g: int, b: int) -> Ansi:
        pass

    def bgBright(self, color: Ansi.Color) -> Ansi:
        pass

    def fgBright(self, color: Ansi.Color) -> Ansi:
        pass

    def eraseLine1(self, kind: Erase) -> Ansi:
        pass

    def eraseLine0(self) -> Ansi:
        pass

    def eraseScreen1(self, kind: Erase) -> Ansi:
        pass

    def eraseScreen0(self) -> Ansi:
        pass

    def cursorUpLine1(self, n: int) -> Ansi:
        pass

    def cursorUpLine0(self) -> Ansi:
        pass

    def cursorDownLine1(self, n: int) -> Ansi:
        pass

    def cursorDownLine0(self) -> Ansi:
        pass

    def bg1(self, color: int) -> Ansi:
        pass

    def fg1(self, color: int) -> Ansi:
        pass

    def bg0(self, color: Ansi.Color) -> Ansi:
        pass

    def fg0(self, color: Ansi.Color) -> Ansi:
        pass

    def __init__(self, args: typing.Any) -> None:
        pass

    @staticmethod
    def __determineStringBuilder(
        args: typing.Any,
    ) -> typing.Union[typing.List[str], io.StringIO]:
        pass

    # Class Methods End
