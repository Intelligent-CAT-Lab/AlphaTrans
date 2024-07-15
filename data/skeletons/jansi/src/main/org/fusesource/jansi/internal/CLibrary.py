from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.internal.JansiLoader import *
import os
import typing
from typing import *
import io

# Imports End


class Termios:

    # Class Fields Begin
    SIZEOF: int = None
    c_iflag: int = None
    c_oflag: int = None
    c_cflag: int = None
    c_lflag: int = None
    c_cc: typing.List[int] = None
    c_ispeed: int = None
    c_ospeed: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class WinSize:

    # Class Fields Begin
    SIZEOF: int = None
    ws_row: int = None
    ws_col: int = None
    ws_xpixel: int = None
    ws_ypixel: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, ws_row: int, ws_col: int) -> None:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End


class CLibrary:

    # Class Fields Begin
    LOADED: bool = None
    STDOUT_FILENO: int = None
    STDERR_FILENO: int = None
    HAVE_ISATTY: bool = None
    HAVE_TTYNAME: bool = None
    TCSANOW: int = None
    TCSADRAIN: int = None
    TCSAFLUSH: int = None
    TIOCGETA: int = None
    TIOCSETA: int = None
    TIOCGETD: int = None
    TIOCSETD: int = None
    TIOCGWINSZ: int = None
    TIOCSWINSZ: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def ioctl() -> int:
        pass

    @staticmethod
    def tcsetattr() -> int:
        pass

    @staticmethod
    def tcgetattr() -> int:
        pass

    @staticmethod
    def openpty() -> int:
        pass

    @staticmethod
    def ttyname() -> str:
        pass

    @staticmethod
    def isatty() -> int:
        pass

    @staticmethod
    def __init() -> None:
        pass

    # Class Methods End
