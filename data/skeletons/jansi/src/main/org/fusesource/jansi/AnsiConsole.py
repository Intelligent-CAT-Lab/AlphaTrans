from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.io.WindowsAnsiProcessor import *
from src.main.org.fusesource.jansi.io.FastBufferedOutputStream import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.io.AnsiOutputStream import *
from src.main.org.fusesource.jansi.internal.MingwSupport import *
from src.main.org.fusesource.jansi.internal.Kernel32 import *
from src.main.org.fusesource.jansi.internal.CLibrary import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.AnsiPrintStream import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiColors import *
import typing
import sys
import io

# Imports End


class AnsiConsole:

    # Class Fields Begin
    JANSI_OUT_COLORS: str = None
    JANSI_ERR_COLORS: str = None
    JANSI_COLORS_16: str = None
    JANSI_COLORS_256: str = None
    JANSI_COLORS_TRUECOLOR: str = None
    JANSI_PASSTHROUGH: str = None
    JANSI_STRIP: str = None
    JANSI_FORCE: str = None
    JANSI_EAGER: str = None
    JANSI_NORESET: str = None
    JANSI_GRACEFUL: str = None
    system_out: typing.IO = None
    out: typing.IO = None
    system_err: typing.IO = None
    err: typing.IO = None
    IS_WINDOWS: bool = None
    IS_CYGWIN: bool = None
    IS_MSYSTEM: bool = None
    IS_CONEMU: bool = None
    ENABLE_VIRTUAL_TERMINAL_PROCESSING: int = None
    STDOUT_FILENO: int = None
    STDERR_FILENO: int = None
    __initialized: bool = None
    __installed: int = None
    __virtualProcessing: int = None
    JANSI_MODE: str = None
    JANSI_OUT_MODE: str = None
    JANSI_ERR_MODE: str = None
    JANSI_MODE_STRIP: str = None
    JANSI_MODE_FORCE: str = None
    JANSI_MODE_DEFAULT: str = None
    JANSI_COLORS: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def initStreams() -> None:
        pass

    @staticmethod
    def systemUninstall() -> None:
        pass

    @staticmethod
    def isInstalled() -> bool:
        pass

    @staticmethod
    def systemInstall() -> None:
        pass

    @staticmethod
    def sysErr() -> typing.IO:
        pass

    @staticmethod
    def err() -> AnsiPrintStream:
        pass

    @staticmethod
    def sysOut() -> typing.IO:
        pass

    @staticmethod
    def out() -> AnsiPrintStream:
        pass

    @staticmethod
    def getBoolean(name: str) -> bool:
        pass

    @staticmethod
    def getTerminalWidth() -> int:
        pass

    @staticmethod
    def __newPrintStream(out: AnsiOutputStream, enc: str) -> AnsiPrintStream:
        pass

    @staticmethod
    def __ansiStream(stdout: bool) -> AnsiPrintStream:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
