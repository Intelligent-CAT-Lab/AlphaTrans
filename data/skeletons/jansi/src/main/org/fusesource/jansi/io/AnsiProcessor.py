from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class AnsiProcessor:

    # Class Fields Begin
    _ERASE_SCREEN_TO_END: int = None
    _ERASE_SCREEN_TO_BEGINING: int = None
    _ERASE_SCREEN: int = None
    _ERASE_LINE_TO_END: int = None
    _ERASE_LINE_TO_BEGINING: int = None
    _ERASE_LINE: int = None
    _ATTRIBUTE_INTENSITY_BOLD: int = None
    _ATTRIBUTE_INTENSITY_FAINT: int = None
    _ATTRIBUTE_ITALIC: int = None
    _ATTRIBUTE_UNDERLINE: int = None
    _ATTRIBUTE_BLINK_SLOW: int = None
    _ATTRIBUTE_BLINK_FAST: int = None
    _ATTRIBUTE_NEGATIVE_ON: int = None
    _ATTRIBUTE_CONCEAL_ON: int = None
    _ATTRIBUTE_UNDERLINE_DOUBLE: int = None
    _ATTRIBUTE_INTENSITY_NORMAL: int = None
    _ATTRIBUTE_UNDERLINE_OFF: int = None
    _ATTRIBUTE_BLINK_OFF: int = None
    _ATTRIBUTE_NEGATIVE_OFF: int = None
    _ATTRIBUTE_CONCEAL_OFF: int = None
    _os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None
    _BLACK: int = None
    _RED: int = None
    _GREEN: int = None
    _YELLOW: int = None
    _BLUE: int = None
    _MAGENTA: int = None
    _CYAN: int = None
    _WHITE: int = None
    # Class Fields End

    # Class Methods Begin
    def _processCharsetSelect1(self, set_: int, seq: str) -> None:
        pass

    def _processUnknownOperatingSystemCommand(self, command: int, param: str) -> None:
        pass

    def _processChangeWindowTitle(self, label: str) -> None:
        pass

    def _processChangeIconName(self, label: str) -> None:
        pass

    def _processChangeIconNameAndWindowTitle(self, label: str) -> None:
        pass

    def _processUnknownExtension(
        self, options: typing.List[typing.Any], command: int
    ) -> None:
        pass

    def _processCursorUp(self, count: int) -> None:
        pass

    def _processCursorDown(self, count: int) -> None:
        pass

    def _processCursorRight(self, count: int) -> None:
        pass

    def _processCursorLeft(self, count: int) -> None:
        pass

    def _processCursorDownLine(self, count: int) -> None:
        pass

    def _processCursorUpLine(self, count: int) -> None:
        pass

    def _processCursorToColumn(self, x: int) -> None:
        pass

    def _processCursorTo(self, row: int, col: int) -> None:
        pass

    def _processAttributeReset(self) -> None:
        pass

    def _processDefaultBackgroundColor(self) -> None:
        pass

    def _processDefaultTextColor(self) -> None:
        pass

    def _processSetBackgroundColorExt1(self, r: int, g: int, b: int) -> None:
        pass

    def _processSetBackgroundColorExt0(self, paletteIndex: int) -> None:
        pass

    def _processSetBackgroundColor1(self, color: int, bright: bool) -> None:
        pass

    def _processSetBackgroundColor0(self, color: int) -> None:
        pass

    def _processSetForegroundColorExt1(self, r: int, g: int, b: int) -> None:
        pass

    def _processSetForegroundColorExt0(self, paletteIndex: int) -> None:
        pass

    def _processSetForegroundColor1(self, color: int, bright: bool) -> None:
        pass

    def _processSetForegroundColor0(self, color: int) -> None:
        pass

    def _processSetAttribute(self, attribute: int) -> None:
        pass

    def _processEraseLine(self, eraseOption: int) -> None:
        pass

    def _processEraseScreen(self, eraseOption: int) -> None:
        pass

    def _processScrollUp(self, optionInt: int) -> None:
        pass

    def _processScrollDown(self, optionInt: int) -> None:
        pass

    def _processDeleteLine(self, optionInt: int) -> None:
        pass

    def _processInsertLine(self, optionInt: int) -> None:
        pass

    def _processSaveCursorPosition(self) -> None:
        pass

    def _processRestoreCursorPosition(self) -> None:
        pass

    def _processCharsetSelect0(self, options: typing.List[typing.Any]) -> bool:
        pass

    def _processOperatingSystemCommand(self, options: typing.List[typing.Any]) -> bool:
        pass

    def _processEscapeCommand(
        self, options: typing.List[typing.Any], command: int
    ) -> bool:
        pass

    def _getNextOptionInt(self, optionsIterator: typing.Iterator[typing.Any]) -> int:
        pass

    def __init__(
        self, os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        pass

    def __optionInt1(
        self, options: typing.List[typing.Any], index: int, defaultValue: int
    ) -> int:
        pass

    def __optionInt0(self, options: typing.List[typing.Any], index: int) -> int:
        pass

    # Class Methods End
