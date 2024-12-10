from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.internal.JansiLoader import *
import os
import typing
from typing import *
import numbers
import io

# Imports End


class CHAR_INFO:

    # Class Fields Begin
    SIZEOF: int = None
    attributes: int = None
    unicodeChar: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class CONSOLE_SCREEN_BUFFER_INFO:

    # Class Fields Begin
    SIZEOF: int = None
    size: COORD = None
    cursorPosition: COORD = None
    attributes: int = None
    window: SMALL_RECT = None
    maximumWindowSize: COORD = None
    # Class Fields End

    # Class Methods Begin
    def windowHeight(self) -> int:
        pass

    def windowWidth(self) -> int:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class COORD:

    # Class Fields Begin
    SIZEOF: int = None
    x: int = None
    y: int = None
    # Class Fields End

    # Class Methods Begin
    def copy(self) -> COORD:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class SMALL_RECT:

    # Class Fields Begin
    SIZEOF: int = None
    left: int = None
    top: int = None
    right: int = None
    bottom: int = None
    # Class Fields End

    # Class Methods Begin
    def copy(self) -> SMALL_RECT:
        pass

    def height(self) -> int:
        pass

    def width(self) -> int:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class FOCUS_EVENT_RECORD:

    # Class Fields Begin
    SIZEOF: int = None
    setFocus: bool = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class INPUT_RECORD:

    # Class Fields Begin
    SIZEOF: int = None
    KEY_EVENT: int = None
    MOUSE_EVENT: int = None
    WINDOW_BUFFER_SIZE_EVENT: int = None
    FOCUS_EVENT: int = None
    MENU_EVENT: int = None
    eventType: int = None
    keyEvent: KEY_EVENT_RECORD = None
    mouseEvent: MOUSE_EVENT_RECORD = None
    windowBufferSizeEvent: WINDOW_BUFFER_SIZE_RECORD = None
    menuEvent: MENU_EVENT_RECORD = None
    focusEvent: FOCUS_EVENT_RECORD = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def memmove() -> None:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class MENU_EVENT_RECORD:

    # Class Fields Begin
    SIZEOF: int = None
    commandId: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class WINDOW_BUFFER_SIZE_RECORD:

    # Class Fields Begin
    SIZEOF: int = None
    size: COORD = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class MOUSE_EVENT_RECORD:

    # Class Fields Begin
    SIZEOF: int = None
    FROM_LEFT_1ST_BUTTON_PRESSED: int = None
    FROM_LEFT_2ND_BUTTON_PRESSED: int = None
    FROM_LEFT_3RD_BUTTON_PRESSED: int = None
    FROM_LEFT_4TH_BUTTON_PRESSED: int = None
    RIGHTMOST_BUTTON_PRESSED: int = None
    CAPSLOCK_ON: int = None
    NUMLOCK_ON: int = None
    SCROLLLOCK_ON: int = None
    ENHANCED_KEY: int = None
    LEFT_ALT_PRESSED: int = None
    LEFT_CTRL_PRESSED: int = None
    RIGHT_ALT_PRESSED: int = None
    RIGHT_CTRL_PRESSED: int = None
    SHIFT_PRESSED: int = None
    DOUBLE_CLICK: int = None
    MOUSE_HWHEELED: int = None
    MOUSE_MOVED: int = None
    MOUSE_WHEELED: int = None
    mousePosition: COORD = None
    buttonState: int = None
    controlKeyState: int = None
    eventFlags: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class KEY_EVENT_RECORD:

    # Class Fields Begin
    SIZEOF: int = None
    CAPSLOCK_ON: int = None
    NUMLOCK_ON: int = None
    SCROLLLOCK_ON: int = None
    ENHANCED_KEY: int = None
    LEFT_ALT_PRESSED: int = None
    LEFT_CTRL_PRESSED: int = None
    RIGHT_ALT_PRESSED: int = None
    RIGHT_CTRL_PRESSED: int = None
    SHIFT_PRESSED: int = None
    keyDown: bool = None
    repeatCount: int = None
    keyCode: int = None
    scanCode: int = None
    uchar: str = None
    controlKeyState: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class Kernel32:

    # Class Fields Begin
    FOREGROUND_BLUE: int = None
    FOREGROUND_GREEN: int = None
    FOREGROUND_RED: int = None
    FOREGROUND_INTENSITY: int = None
    BACKGROUND_BLUE: int = None
    BACKGROUND_GREEN: int = None
    BACKGROUND_RED: int = None
    BACKGROUND_INTENSITY: int = None
    COMMON_LVB_LEADING_BYTE: int = None
    COMMON_LVB_TRAILING_BYTE: int = None
    COMMON_LVB_GRID_HORIZONTAL: int = None
    COMMON_LVB_GRID_LVERTICAL: int = None
    COMMON_LVB_GRID_RVERTICAL: int = None
    COMMON_LVB_REVERSE_VIDEO: int = None
    COMMON_LVB_UNDERSCORE: int = None
    FORMAT_MESSAGE_FROM_SYSTEM: int = None
    STD_INPUT_HANDLE: int = None
    STD_OUTPUT_HANDLE: int = None
    STD_ERROR_HANDLE: int = None
    INVALID_HANDLE_VALUE: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getErrorMessage(errorCode: int) -> str:
        pass

    @staticmethod
    def getLastErrorMessage() -> str:
        pass

    @staticmethod
    def readConsoleKeyInput(
        handle: int, count: int, peek: bool
    ) -> typing.List[INPUT_RECORD]:
        pass

    @staticmethod
    def readConsoleInputHelper(
        handle: int, count: int, peek: bool
    ) -> typing.List[INPUT_RECORD]:
        pass

    @staticmethod
    def FlushConsoleInputBuffer() -> int:
        pass

    @staticmethod
    def GetNumberOfConsoleInputEvents() -> int:
        pass

    @staticmethod
    def ScrollConsoleScreenBuffer() -> int:
        pass

    @staticmethod
    def SetConsoleOutputCP() -> int:
        pass

    @staticmethod
    def GetConsoleOutputCP() -> int:
        pass

    @staticmethod
    def SetConsoleTitle() -> int:
        pass

    @staticmethod
    def _getch() -> int:
        pass

    @staticmethod
    def SetConsoleMode() -> int:
        pass

    @staticmethod
    def GetConsoleMode() -> int:
        pass

    @staticmethod
    def WriteConsoleW() -> int:
        pass

    @staticmethod
    def FillConsoleOutputAttribute() -> int:
        pass

    @staticmethod
    def FillConsoleOutputCharacterW() -> int:
        pass

    @staticmethod
    def SetConsoleCursorPosition() -> int:
        pass

    @staticmethod
    def GetStdHandle() -> int:
        pass

    @staticmethod
    def GetConsoleScreenBufferInfo() -> int:
        pass

    @staticmethod
    def FormatMessageW() -> int:
        pass

    @staticmethod
    def GetLastError() -> int:
        pass

    @staticmethod
    def CloseHandle() -> int:
        pass

    @staticmethod
    def WaitForSingleObject() -> int:
        pass

    @staticmethod
    def SetConsoleTextAttribute() -> int:
        pass

    @staticmethod
    def free() -> None:
        pass

    @staticmethod
    def malloc() -> int:
        pass

    @staticmethod
    def __PeekConsoleInputW() -> int:
        pass

    @staticmethod
    def __ReadConsoleInputW() -> int:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End
