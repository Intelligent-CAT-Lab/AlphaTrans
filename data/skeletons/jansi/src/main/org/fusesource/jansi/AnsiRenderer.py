from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.Ansi import *
import typing
from typing import *
import enum
import io
from io import IOBase

# Imports End


class Code:

    # Class Fields Begin
    BLACK: Code = None
    RED: Code = None
    GREEN: Code = None
    YELLOW: Code = None
    BLUE: Code = None
    MAGENTA: Code = None
    CYAN: Code = None
    WHITE: Code = None
    DEFAULT: Code = None
    FG_BLACK: Code = None
    FG_RED: Code = None
    FG_GREEN: Code = None
    FG_YELLOW: Code = None
    FG_BLUE: Code = None
    FG_MAGENTA: Code = None
    FG_CYAN: Code = None
    FG_WHITE: Code = None
    FG_DEFAULT: Code = None
    BG_BLACK: Code = None
    BG_RED: Code = None
    BG_GREEN: Code = None
    BG_YELLOW: Code = None
    BG_BLUE: Code = None
    BG_MAGENTA: Code = None
    BG_CYAN: Code = None
    BG_WHITE: Code = None
    BG_DEFAULT: Code = None
    RESET: Code = None
    INTENSITY_BOLD: Code = None
    INTENSITY_FAINT: Code = None
    ITALIC: Code = None
    UNDERLINE: Code = None
    BLINK_SLOW: Code = None
    BLINK_FAST: Code = None
    BLINK_OFF: Code = None
    NEGATIVE_ON: Code = None
    NEGATIVE_OFF: Code = None
    CONCEAL_ON: Code = None
    CONCEAL_OFF: Code = None
    UNDERLINE_DOUBLE: Code = None
    UNDERLINE_OFF: Code = None
    BOLD: Code = None
    FAINT: Code = None
    __n: enum.Enum = None
    __background: bool = None
    # Class Fields End

    # Class Methods Begin
    def isBackground(self) -> bool:
        pass

    def getAttribute(self) -> Attribute:
        pass

    def isAttribute(self) -> bool:
        pass

    def getColor(self) -> Ansi.Color:
        pass

    def isColor(self) -> bool:
        pass

    def __init__(self, n: enum.Enum, background: bool) -> None:
        pass

    # Class Methods End


class AnsiRenderer:

    # Class Fields Begin
    BEGIN_TOKEN: str = None
    END_TOKEN: str = None
    CODE_TEXT_SEPARATOR: str = None
    CODE_LIST_SEPARATOR: str = None
    __BEGIN_TOKEN_LEN: int = None
    __END_TOKEN_LEN: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def test(text: str) -> bool:
        pass

    @staticmethod
    def renderCodes1(codes: str) -> str:
        pass

    @staticmethod
    def renderCodes0(codes: typing.List[typing.List[str]]) -> str:
        pass

    @staticmethod
    def render2(text: str, codes: typing.List[typing.List[str]]) -> str:
        pass

    @staticmethod
    def render1(
        input_: str, target: typing.Union[typing.List, io.TextIOBase]
    ) -> typing.Union[typing.List, io.TextIOBase]:
        pass

    @staticmethod
    def render0(input_: str) -> str:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __render3(ansi: Ansi, names: typing.List[typing.List[str]]) -> Ansi:
        pass

    # Class Methods End
